from pathlib import Path
APP_VERSION = open(Path(__file__).parent / 'VERSION').read().strip()
BACKUP_DATA_NAME = 'DATA'
BACKUP_INFO_NAME = 'INFO'
BACKUP_META_NAME = 'META'
