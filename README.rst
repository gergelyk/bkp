bkp
===

Simple utility that makes backups of your files/directories.

.. image:: https://user-images.githubusercontent.com/11185582/48983793-ab82df00-f0f3-11e8-8727-c665b92bdb31.gif


Installation
------------

.. code-block:: bash

    sudo pip install bkp


Compatibility
-------------

* This software is expected to work with Python 3.6, 3.7 and compatible.
* It has never been tested under operating systems other than Linux.
* For editing messages interactively (``-M`` switch) you need either have `vi` installed, or set ``EDITOR`` system variable to relevant value.

Usage
-----

Creating Backups & Restoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provided that we have a file or directory: `foo/bar/baz`

.. code-block:: bash

    # Create a copy:   
    bkp foo/bar/baz

    # Following copy will be created: foo/bar/baz.b01
    # Invoking command again will create foo/bar/baz.b02 etc.

    # Restore your file or directory:
    bkp -r foo/bar/baz.01

    # This will create/overwrite original file/directory: foo/bar/baz

Note that multiple files can be specified in the command line. Output files are always created in the same directory where corresponding input files are located, no matter what CWD at the time.

Working With Archives
^^^^^^^^^^^^^^^^^^^^^

Alternatively ``-a`` flag can be used to create tar archive instead of a simple copy. Also ``-m`` can be used to add comments.

.. code-block:: bash

    # Create an archive
    bkp -am "initial version" foo/bar/baz

    # Comment and other details can be obtained by invoking:
    bkp -i foo/bar/baz.b03

For more options and explanations invoke ``bkp --help``.


Development
-----------

Preparing Environment
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    python3 -m pip install -r requirements-dev.txt
    python3 -m pip install -e .

Modifying Dependencies
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # edit setup.py
    # edit requirements*.in
    pip-compile
    pip-sync
    # git add... commit... push...

Testing
^^^^^^^

.. code-block:: bash

    pytest

Releasing
^^^^^^^^^

.. code-block:: bash

    echo $VERSION > bkp/VERSION
    twine upload dist/bkp-$VERSION.tar.gz
    git tag $VERSION
    git push --tags


Disclaimer
----------

Author doesn't take any responsibility for loss or damage caused by this utility. You are using it on your own risk.


Donations
---------

It is absolutely fine if you use this software for free for commercial or non-commercial purposes. On the other hand, if you would like to repay author's efforts you are welcome to use following button:

.. image:: https://www.paypalobjects.com/en_US/PL/i/btn/btn_donateCC_LG.gif
   :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=D9KUJD9LTKJY8&source=url

