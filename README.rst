bkp
===

Simple utility that makes backups of your files/directories.

Installation
------------

.. code-block:: bash

    sudo pip install bkp


Usage
-----

.. code-block:: bash

    # Given that we have a file or directory: foo/bar/baz
    # Create copy by invoking:

    bkp foo/bar/baz

    # Following copy will be created: foo/bar/baz.b01
    # Invoking command again will create foo/bar/baz.b02 etc.

    # Alternatively '-a' flag can be used to create tar archive instead of
    # simple copy. Also '-m' can be used to add comments:

    bkp -am "initial version" foo/bar/baz

    # Comment and other details can be obtained by invoking:

    bkp -i foo/bar/baz.b03

    # Restore your file or directory by invoking:

    bkp -r foo/bar/baz.01

    # This will create/overwrite original file/directory: foo/bar/baz

    # Note that multiple files can be specified in the command line.
    # Output files are always created in the same directory where corresponding
    # input files are located, no matter what CWD at the time.
    # For more help invoke:

    bkp --help


Disclaimer
----------

    Author doesn't take any responsibility for loss or damage caused by this
    utility. You are using it on your own risk.
