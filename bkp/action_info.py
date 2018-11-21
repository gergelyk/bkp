import tarfile
from click import secho

import bkp.fsop as fsop
import bkp.tarop as tarop
from bkp.terminal import echo_path, echo_wrn, echo_inf
from bkp.resources import BACKUP_INFO_NAME, BACKUP_META_NAME
from bkp.exceptions import InvalidFile, AccessDenied


def info(path):
    echo_path(path)

    try:
        if not fsop.is_backup(path):
            echo_wrn('Not a backup')
            return

        if not tarop.is_archive(path):
            echo_wrn('Not an archive')
            return

        info_str = tarop.extract_text(path, BACKUP_INFO_NAME)
        info_dict = eval(info_str)
        max_key_len = max(map(len, info_dict.keys()))
        highlighted = ['message']
        sep = " : "

        def echo_val(text, highlighted):
            lines = text.splitlines()
            first_line = ''.join(lines[:1])
            other_lines = '\n'.join(lines[1:])
            echo_inf(first_line, indent=0, highlight=highlighted)
            if other_lines:
                echo_inf(other_lines, indent=max_key_len + len(sep), highlight=highlighted)

        for key, val in info_dict.items():
            echo_inf(f"{key:<{max_key_len}}" + sep, nl=False)
            echo_val(val, key in highlighted)

    except AccessDenied as exc:
        echo_wrn(exc)
