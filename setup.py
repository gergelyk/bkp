from setuptools import setup, find_packages

setup(
    name = 'bkp',
    version = '0.1.0',
    description = 'Creates backups of your files and directories.',
    author = 'Grzegorz Krason',
    author_email = 'grzegorz.krason@gmail.com',
    url = 'https://pypi.org/project/bkp/',
    license = 'MIT',
    packages = find_packages(),
    keywords = 'backup'.split(),
    entry_points = {
        'console_scripts': ['bkp = bkp:main'],
        },
    classifiers = [],
    install_requires = [
        'click',
    ],
)
