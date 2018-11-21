import re
import os
import tempfile
from pathlib import Path
from functools import partial, lru_cache

import bkp.fsop as fsop
import bkp.tarop as tarop
from bkp.config import cfg
from bkp.exceptions import InvalidInput
from bkp.timestamp import timestamp
from bkp.terminal import echo_path, echo_inf, confirm


@lru_cache()
def message_from_editor(initial):
    initial = initial or ""
    with tempfile.NamedTemporaryFile(prefix='message-') as fp:
        fp.write(initial.encode() + b'\n\n# Write your message above.')
        fp.flush()
        editor = os.getenv('EDITOR', 'vi')
        os.system(f'{editor} {fp.name}')
        fp.seek(0)
        text = fp.read().decode()
        lines = text.splitlines()
        content = filter(lambda line: not line.strip().startswith('#'), lines)
        return '\n'.join(content).strip()


def generate_index(path):
    items_all = path.parent.iterdir()
    backups = filter(lambda p: p.with_suffix('').name == path.name, items_all)
    suffixes = map(lambda p: p.suffix, backups)
    suffix_re = re.compile(cfg.suffix_regexp)
    matches = filter(None, map(suffix_re.match, suffixes))
    indices = map(lambda m: int(m.groups()[0]), matches)

    try:
        return max(indices) + 1
    except ValueError:
        return cfg.index_from


def backup_copy(src, dst):
    fsop.copy(src, dst)
    echo_inf(f"Created: {dst}")


def backup_move(src, dst):
    fsop.move(src, dst)
    echo_inf(f'Created: {dst}')
    echo_inf(f'Deleted: {src}')


def backup_tar(src, dst, message):
    tarop.archive(src, dst, message)
    echo_inf(f"Created: {dst}")


def backup_tar_rm(src, dst, message):
    backup_tar(src, dst, message)
    fsop.remove(src)
    echo_inf(f'Deleted: {src}')


def backup(path, delete, yes, archive, message, message_edit):

    if message_edit:
        if not archive:
            raise InvalidInput(f"Option '--message-edit' is allowed only in conjunction with '--archive'")
        message = message_from_editor(message)
    elif message is not None:
        if not archive:
            raise InvalidInput(f"Option '--message' is allowed only in conjunction with '--archive'")

    echo_path(path)

    if not yes and fsop.is_backup(path):
        ans = confirm(f'Are you sure you would like to backup another backup?')
        if not ans:
            echo_inf('Skipping')
            return

    message = message or ""

    backup_tar_p = partial(backup_tar, message=message)
    backup_tar_rm_p = partial(backup_tar_rm, message=message)

    backup_funcs = ((backup_copy, backup_move), (backup_tar_p, backup_tar_rm_p))
    backup_func = backup_funcs[archive][delete]

    index = generate_index(path)
    env = dict(i=index, t=timestamp)
    suffix = cfg.suffix_format.format(**env)

    src = path
    dst = Path(str(path) + suffix)

    backup_func(src, dst)
