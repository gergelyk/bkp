import getpass
import tarfile
from pathlib import Path
from io import BytesIO
from bkp.config import cfg
from bkp.timestamp import timestamp
from bkp.exceptions import InvalidFile, AccessDenied
from bkp.resources import BACKUP_META_NAME, BACKUP_DATA_NAME, BACKUP_INFO_NAME

def _process_tar(handler, path, mode, *args, **kwargs):
    try:
        tar_ctx = tarfile.open(name=path, mode=mode)
    except Exception as exc:
        raise InvalidFile('File format not supported')
    else:
        with tar_ctx as tar:
            return handler(tar, *args, **kwargs)

def archive(src, dst, message):

    def handler(tar, src, message):

        def get_info_str(message):
            user = getpass.getuser()
            info = dict(author=user,
                        time=cfg.time_format.format(t=timestamp),
                        message=message)
            return repr(info)

        def get_meta_str():
            meta = dict(file_type="backup", file_version="1.0.0")
            return repr(meta)

        def add_text(tar, text, name):
            buf = BytesIO(text.encode())
            tar_info = tarfile.TarInfo(name)
            tar_info.size = len(buf.getvalue())
            tar.addfile(tar_info, fileobj=buf)

        tar.add(src, arcname=BACKUP_DATA_NAME)
        info_str = get_info_str(message)
        meta_str = get_meta_str()
        add_text(tar, info_str, BACKUP_INFO_NAME)
        add_text(tar, meta_str, BACKUP_META_NAME)

    return _process_tar(handler, dst, 'w:', src, message)


def extract_text(path, name):

    def handler(tar, name):
        try:
            buf = tar.extractfile(name)
        except KeyError:
            raise InvalidFile('File format not supported')
        else:
            return buf.read().decode()

    return _process_tar(handler, path, 'r:', name)


def extract_member(path, name, name_arc):

    def handler(tar, name, name_arc):
        for m in tar.getmembers():
            m_name_arc = Path(m.name)
            if m_name_arc.parts[0] == name_arc:
                m.name = str(Path(name) /  Path(*m_name_arc.parts[1:]))
                tar.extract(m)

    return _process_tar(handler, path, 'r:', name, name_arc)

def is_archive(path):

    try:
        if not path.is_file():
            return False
    except PermissionError:
        # this should be handled by click package anyway
        raise AccessDenied("File not available")

    try:
        meta_str = extract_text(path, BACKUP_META_NAME)
    except InvalidFile:
        return False

    try:
        meta_dict = eval(meta_str)
        if meta_dict['file_type'] != "backup":
            return False
        if meta_dict['file_version'] != "1.0.0":
            return False
    except Exception:
        return False

    return True
