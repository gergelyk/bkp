import os
import re
import shutil

from bkp.resources import BACKUP_DATA_NAME, BACKUP_INFO_NAME, BACKUP_META_NAME
from bkp.config import cfg
from bkp.timestamp import timestamp


def is_backup(path):
    return bool(re.match(cfg.suffix_regexp, path.suffix))


def copy(src, dst):
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copyfile(src, dst)


def move(src, dst):
    shutil.move(src, dst)


def remove(path):
    if path.is_dir():
        shutil.rmtree(path)
    else:
        os.remove(path)
