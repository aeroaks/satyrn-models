Command-line usage
------------------

.. versionadded:: 3.3

The :mod:`!tokenize` module can be executed as a script from the command line.
It is as simple as:

.. code-block:: sh

   python -m tokenize [-e] [filename.py]

The following options are accepted:

.. program:: tokenize

.. option:: -h, --help

   show this help message and exit

.. option:: -e, --exact

   display token names using the exact type

If :file:`filename.py` is specified its contents are tokenized to stdout.
Otherwise, tokenization is performed on stdin.

.. versionadded:: 3.15
   Output is in color by default and can be
   :ref:`controlled using environment variables <using-on-controlling-color>`.
