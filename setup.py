from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).parent / 'README.rst'

with open(readme_path) as fh:
    long_description = fh.read()

setup(
    name = 'bkp',
    version = '0.1.1',
    description = 'Creates backups of your files and directories.',
    author = 'Grzegorz Krason',
    author_email = 'grzegorz.krason@gmail.com',
    url = 'https://github.com/gergelyk/bkp',
    license = 'MIT',
    packages = find_packages(),
    keywords = 'backup'.split(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    entry_points = {
        'console_scripts': ['bkp = bkp:main'],
        },
    classifiers = [],
    install_requires = [
        'click',
    ],
)
