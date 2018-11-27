from setuptools import setup, find_packages
from pathlib import Path
from bkp.VERSION import VERSION

readme_path = Path(__file__).parent / 'README.rst'

with open(readme_path) as fh:
    long_description = fh.read()

setup(
    name = 'bkp',
    version = VERSION,
    description = 'Creates backups of your files and directories.',
    author = 'Grzegorz Krason',
    author_email = 'grzegorz.krason@gmail.com',
    url = 'https://github.com/gergelyk/bkp',
    license = 'MIT',
    packages = find_packages(),
    keywords = 'backup'.split(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    python_requires='~=3.6',
    entry_points = {
        'console_scripts': ['bkp = bkp:main'],
        },
    install_requires = [
        'click',
    ],
    classifiers = [
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
        'Topic :: Office/Business',
        'Topic :: System',
        'Topic :: Utilities',
        'Operating System :: POSIX',
        'Operating System :: Unix',
    ],
)
