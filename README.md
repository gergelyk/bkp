# bkp
![PyPI - Version](https://img.shields.io/pypi/v/bkp)
![PyPI - License](https://img.shields.io/pypi/l/bkp)
![PyPI - Downloads](https://img.shields.io/pypi/dm/bkp)

Simple utility that makes backups of your files/directories.

![](docs/demo.gif)

## Features

* Work with separate files or entire directories.
* Creates simple copy or TAR archive.
* Optionally append metadata: author, creation time, commit message (applies only to TAR archives).

## Installation

```python
pip install bkp
```

## Compatibility

* This software is expected to work with Python 3.6, 3.7 and compatible.
* It has never been tested under operating systems other than Linux.
* For editing messages interactively (``-M`` switch) you need either have `vi` installed, or set ``EDITOR`` system variable to relevant value.

## Usage

### Creating Backups & Restoring

Provided that we have a file or directory: `foo/bar/baz`

```sh
# Create a copy:   
bkp foo/bar/baz

# Following copy will be created: foo/bar/baz.b01
# Invoking command again will create foo/bar/baz.b02 etc.

# Restore your file or directory:
bkp -r foo/bar/baz.01

# This will create/overwrite original file/directory: foo/bar/baz
```

Note that multiple files can be specified in the command line. Output files are always created in the same directory where corresponding input files are located, no matter what CWD at the time.

### Working With Archives

Alternatively `-a` flag can be used to create tar archive instead of a simple copy. Also `-m` can be used to add comments.

```
# Create an archive
bkp -am "initial version" foo/bar/baz

# Comment and other details can be obtained by invoking:
bkp -i foo/bar/baz.b03
```

For more options and explanations invoke `bkp --help`.


## Development

Preparing environment:

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install -r requirements-dev.txt
python3 -m pip install -e .
```

Modifying dependencies:

```sh
# edit setup.py
# edit requirements*.in
pip-compile
pip-sync
# git add... commit... push...
```

Testing:

```sh
pytest
```

Releasing:

```sh
echo $VERSION > bkp/VERSION
twine upload dist/bkp-$VERSION.tar.gz
git tag $VERSION
git push --tags
```

## Disclaimer

Author doesn't take any responsibility for loss or damage caused by this utility. You are using it on your own risk.
