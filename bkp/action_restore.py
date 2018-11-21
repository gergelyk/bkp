import tarfile
from click import confirm
from bkp.terminal import echo_path, echo_wrn, echo_inf

import bkp.fsop as fsop
import bkp.tarop as tarop
from bkp.exceptions import AccessDenied
from bkp.resources import BACKUP_DATA_NAME


def restore(path, delete, yes):

    echo_path(path)

    try:

        if not fsop.is_backup(path):
            echo_wrn('Not a backup')
            return

        is_archive = tarop.is_archive(path)

    except AccessDenied as exc:
        echo_wrn(exc)

    dst = path.with_suffix('')

    if dst.exists():
        if yes or confirm(f'{dst.name!r} already exists, overwrite?'):
            fsop.remove(dst)
            echo_inf(f'Deleted: {dst}')
        else:
            echo_inf('Skipped')
            return

    src = path
    if is_archive:
        tarop.extract_member(src, dst, BACKUP_DATA_NAME)
        echo_inf(f'Restored: {dst}')
        if delete:
            fsop.remove(src)
            echo_inf(f'Deleted: {src}')
    else:
        if delete:
            fsop.move(src, dst)
            echo_inf(f'Restored: {dst}')
            echo_inf(f'Deleted: {src}')
        else:
            fsop.copy(src, dst)
            echo_inf(f'Restored: {dst}')
