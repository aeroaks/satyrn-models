   .. method:: sqlite3.reorganize()

      If you have carried out a lot of deletions and would like to shrink the space
      used on disk, this method will reorganize the database; otherwise, deleted file
      space will be kept and reused as new (key, value) pairs are added.

      .. note::
         While reorganizing, as much as two times the size of the original database is required
         in free disk space. However, be aware that this factor changes for each :mod:`!dbm` submodule.

      .. versionadded:: 3.15


:mod:`!dbm.gnu` --- GNU database manager
----------------------------------------

.. module:: dbm.gnu
   :synopsis: GNU database manager

**Source code:** :source:`Lib/dbm/gnu.py`

--------------

The :mod:`!dbm.gnu` module provides an interface to the :abbr:`GDBM (GNU dbm)`
library, similar to the :mod:`dbm.ndbm` module, but with additional
functionality like crash tolerance.

.. note::

   The file formats created by :mod:`!dbm.gnu` and :mod:`dbm.ndbm` are incompatible
   and can not be used interchangeably.

.. include:: ../includes/wasm-mobile-notavail.rst

.. availability:: Unix.

.. exception:: error

   Raised on :mod:`!dbm.gnu`-specific errors, such as I/O errors. :exc:`KeyError` is
   raised for general mapping errors like specifying an incorrect key.


.. data:: open_flags

   A string of characters the *flag* parameter of :meth:`~dbm.gnu.open` supports.


.. function:: open(filename, flag="r", mode=0o666, /)

   Open a GDBM database and return a :class:`!gdbm` object.

   :param filename:
      The database file to open.
   :type filename: :term:`path-like object`

   :param str flag:
      * ``'r'`` (default): |flag_r|
      * ``'w'``: |flag_w|
      * ``'c'``: |flag_c|
      * ``'n'``: |flag_n|

      The following additional characters may be appended
      to control how the database is opened:

      * ``'f'``: Open the database in fast mode.
        Writes to the database will not be synchronized.
      * ``'s'``: Synchronized mode.
        Changes to the database will be written immediately to the file.
      * ``'u'``: Do not lock database.

      Not all flags are valid for all versions of GDBM.
      See the :data:`open_flags` member for a list of supported flag characters.

   :param int mode:
      |mode_param_doc|

   :raises error:
      If an invalid *flag* argument is passed.

   .. versionchanged:: 3.11
      *filename* accepts a :term:`path-like object`.

   :class:`!gdbm` objects behave similar to mutable :term:`mappings <mapping>`,
   but methods :meth:`!items`, :meth:`!values`, :meth:`!pop`, :meth:`!popitem`,
   and :meth:`!update` are not supported,
   the :meth:`!keys` method returns a list, and
   the :meth:`!setdefault` method requires two arguments.
   It also supports a "closing" context manager via the :keyword:`with` keyword.

   .. versionchanged:: 3.2
      Added the :meth:`!get` and :meth:`!setdefault` methods.

   .. versionchanged:: 3.13
      Added the :meth:`!clear` method.

   The following methods are also provided:

   .. method:: gdbm.close()

      Close the GDBM database.

   .. method:: gdbm.firstkey()

      It's possible to loop over every key in the database using this method  and the
      :meth:`nextkey` method.  The traversal is ordered by GDBM's internal
      hash values, and won't be sorted by the key values.  This method returns
      the starting key.

   .. method:: gdbm.nextkey(key)

      Returns the key that follows *key* in the traversal.  The following code prints
      every key in the database ``db``, without having to create a list in memory that
      contains them all::

         k = db.firstkey()
         while k is not None:
             print(k)
             k = db.nextkey(k)

   .. method:: gdbm.reorganize()

      If you have carried out a lot of deletions and would like to shrink the space
      used by the GDBM file, this routine will reorganize the database.  :class:`!gdbm`
      objects will not shorten the length of a database file except by using this
      reorganization; otherwise, deleted file space will be kept and reused as new
      (key, value) pairs are added.

      .. note::
         While reorganizing, as much as one time the size of the original database is required
         in free disk space. However, be aware that this factor changes for each :mod:`!dbm` submodule.

   .. method:: gdbm.sync()

      When the database has been opened in fast mode, this method forces any
      unwritten data to be written to the disk.


:mod:`!dbm.ndbm` --- New Database Manager
-----------------------------------------

.. module:: dbm.ndbm
   :synopsis: The New Database Manager

**Source code:** :source:`Lib/dbm/ndbm.py`

--------------

The :mod:`!dbm.ndbm` module provides an interface to the
:abbr:`NDBM (New Database Manager)` library.
This module can be used with the "classic" NDBM interface or the
:abbr:`GDBM (GNU dbm)` compatibility interface.

.. note::

   The file formats created by :mod:`dbm.gnu` and :mod:`!dbm.ndbm` are incompatible
   and can not be used interchangeably.

.. warning::

   The NDBM library shipped as part of macOS has an undocumented limitation on the
   size of values, which can result in corrupted database files
   when storing values larger than this limit. Reading such corrupted files can
   result in a hard crash (segmentation fault).

.. include:: ../includes/wasm-mobile-notavail.rst

.. availability:: Unix.

.. exception:: error

   Raised on :mod:`!dbm.ndbm`-specific errors, such as I/O errors. :exc:`KeyError` is raised
   for general mapping errors like specifying an incorrect key.


.. data:: library

   Name of the NDBM implementation library used.


.. function:: open(filename, flag="r", mode=0o666, /)

   Open an NDBM database and return an :class:`!ndbm` object.

   :param filename:
      The basename of the database file
      (without the :file:`.dir` or :file:`.pag` extensions).
   :type filename: :term:`path-like object`

   :param str flag:
      * ``'r'`` (default): |flag_r|
      * ``'w'``: |flag_w|
      * ``'c'``: |flag_c|
      * ``'n'``: |flag_n|

   :param int mode:
      |mode_param_doc|

   .. versionchanged:: 3.11
      Accepts :term:`path-like object` for filename.

   :class:`!ndbm` objects behave similar to mutable :term:`mappings <mapping>`,
   but methods :meth:`!items`, :meth:`!values`, :meth:`!pop`, :meth:`!popitem`,
   and :meth:`!update` are not supported,
   the :meth:`!keys` method returns a list, and
   the :meth:`!setdefault` method requires two arguments.
   It also supports a "closing" context manager via the :keyword:`with` keyword.

   .. versionchanged:: 3.2
      Added the :meth:`!get` and :meth:`!setdefault` methods.

   .. versionchanged:: 3.13
      Added the :meth:`!clear` method.

   The following method is also provided:

   .. method:: ndbm.close()

      Close the NDBM database.


:mod:`!dbm.dumb` --- Portable DBM implementation
------------------------------------------------

.. module:: dbm.dumb
   :synopsis: Portable implementation of the simple DBM interface.

**Source code:** :source:`Lib/dbm/dumb.py`

.. index:: single: databases

.. note::

   The :mod:`!dbm.dumb` module is intended as a last resort fallback for the
   :mod:`!dbm` module when a more robust module is not available. The :mod:`!dbm.dumb`
   module is not written for speed and is not nearly as heavily used as the other
   database modules.

--------------

The :mod:`!dbm.dumb` module provides a persistent :class:`dict`-like
interface which is written entirely in Python.
Unlike other :mod:`!dbm` backends, such as :mod:`dbm.gnu`, no
external library is required.

The :mod:`!dbm.dumb` module defines the following:

.. exception:: error

   Raised on :mod:`!dbm.dumb`-specific errors, such as I/O errors.  :exc:`KeyError` is
   raised for general mapping errors like specifying an incorrect key.


.. function:: open(filename, flag="c", mode=0o666)

   Open a :mod:`!dbm.dumb` database.

   :param filename:
      The basename of the database file (without extensions).
      A new database creates the following files:

      - :file:`{filename}.dat`
      - :file:`{filename}.dir`
   :type database: :term:`path-like object`

   :param str flag:
      * ``'r'``: |flag_r|
      * ``'w'``: |flag_w|
      * ``'c'`` (default): |flag_c|
      * ``'n'``: |flag_n|

   :param int mode:
      |mode_param_doc|

   .. warning::
      It is possible to crash the Python interpreter when loading a database
      with a sufficiently large/complex entry due to stack depth limitations in
      Python's AST compiler.

   .. warning::
      :mod:`!dbm.dumb` does not support concurrent read/write access. (Multiple
      simultaneous read accesses are safe.) When a program has the database open
      for writing, no other program should have it open for reading or writing.

   .. versionchanged:: 3.5
      :func:`~dbm.dumb.open` always creates a new database when *flag* is ``'n'``.

   .. versionchanged:: 3.8
      A database opened read-only if *flag* is ``'r'``.
      A database is not created if it does not exist if *flag* is ``'r'`` or ``'w'``.

   .. versionchanged:: 3.11
      *filename* accepts a :term:`path-like object`.

   The returned database object behaves similar to a mutable :term:`mapping`,
   but the :meth:`!keys` and :meth:`!items` methods return lists, and
   the :meth:`!setdefault` method requires two arguments.
   It also supports a "closing" context manager via the :keyword:`with` keyword.

   The following methods are also provided:

   .. method:: dumbdbm.close()

      Close the database.

   .. method:: dumbdbm.reorganize()

      If you have carried out a lot of deletions and would like to shrink the space
      used on disk, this method will reorganize the database; otherwise, deleted file
      space will not be reused.

      .. note::
         While reorganizing, no additional free disk space is required. However, be aware
         that this factor changes for each :mod:`!dbm` submodule.

      .. versionadded:: 3.15

   .. method:: dumbdbm.sync()

      Synchronize the on-disk directory and data files.  This method is called
      by the :meth:`shelve.Shelf.sync` method.

----

   .. method:: dumbdbm.reorganize()

      If you have carried out a lot of deletions and would like to shrink the space
      used on disk, this method will reorganize the database; otherwise, deleted file
      space will not be reused.

      .. note::
         While reorganizing, no additional free disk space is required. However, be aware
         that this factor changes for each :mod:`!dbm` submodule.

      .. versionadded:: 3.15
