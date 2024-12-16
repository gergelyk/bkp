import importlib.metadata

from pathlib import Path
APP_VERSION = importlib.metadata.version('bkp')
BACKUP_DATA_NAME = 'DATA'
BACKUP_INFO_NAME = 'INFO'
BACKUP_META_NAME = 'META'
