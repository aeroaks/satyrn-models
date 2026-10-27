.. function:: connect(database, *, timeout=5.0, detect_types=0, \
                      isolation_level="DEFERRED", check_same_thread=True, \
                      factory=sqlite3.Connection, cached_statements=128, \
                      uri=False, \
                      autocommit=sqlite3.LEGACY_TRANSACTION_CONTROL)

   Open a connection to an SQLite database.

   :param database:
       The path to the database file to be opened.
       You can pass ``":memory:"`` to create an `SQLite database existing only
       in memory <https://sqlite.org/inmemorydb.html>`_, and open a connection
       to it.
   :type database: :term:`path-like object`

   :param float timeout:
       How many seconds the connection should wait before raising
       an :exc:`OperationalError` when a table is locked.
       If another connection opens a transaction to modify a table,
       that table will be locked until the transaction is committed.
       Default five seconds.

   :param int detect_types:
       Control whether and how data types not
       :ref:`natively supported by SQLite <sqlite3-types>`
       are looked up to be converted to Python types,
       using the converters registered with :func:`register_converter`.
       Set it to any combination (using ``|``, bitwise or) of
       :const:`PARSE_DECLTYPES` and :const:`PARSE_COLNAMES`
       to enable this.
       Column names take precedence over declared types if both flags are set.
       By default (``0``), type detection is disabled.

   :param isolation_level:
       Control legacy transaction handling behaviour.
       See :attr:`Connection.isolation_level` and
       :ref:`sqlite3-transaction-control-isolation-level` for more information.
       Can be ``"DEFERRED"`` (default), ``"EXCLUSIVE"`` or ``"IMMEDIATE"``;
       or ``None`` to disable opening transactions implicitly.
       Has no effect unless :attr:`Connection.autocommit` is set to
       :const:`~sqlite3.LEGACY_TRANSACTION_CONTROL` (the default).
   :type isolation_level: str | None

   :param bool check_same_thread:
       If ``True`` (default), :exc:`ProgrammingError` will be raised
       if the database connection is used by a thread
       other than the one that created it.
       If ``False``, the connection may be accessed in multiple threads;
       write operations may need to be serialized by the user
       to avoid data corruption.
       See :attr:`threadsafety` for more information.

   :param ~sqlite3.Connection factory:
       A custom subclass of :class:`Connection` to create the connection with,
       if not the default :class:`Connection` class.

   :param int cached_statements:
       The number of statements that :mod:`!sqlite3`
       should internally cache for this connection, to avoid parsing overhead.
       By default, 128 statements.

   :param bool uri:
       If set to ``True``, *database* is interpreted as a
       :abbr:`URI (Uniform Resource Identifier)` with a file path
       and an optional query string.
       The scheme part *must* be ``"file:"``,
       and the path can be relative or absolute.
       The query string allows passing parameters to SQLite,
       enabling various :ref:`sqlite3-uri-tricks`.

   :param autocommit:
       Control :pep:`249` transaction handling behaviour.
       See :attr:`Connection.autocommit` and
       :ref:`sqlite3-transaction-control-autocommit` for more information.
       *autocommit* currently defaults to
       :const:`~sqlite3.LEGACY_TRANSACTION_CONTROL`.
       The default will change to ``False`` in a future Python release.
   :type autocommit: bool

   :rtype: ~sqlite3.Connection

   .. audit-event:: sqlite3.connect database sqlite3.connect
   .. audit-event:: sqlite3.connect/handle connection_handle sqlite3.connect

   .. versionchanged:: 3.4
      Added the *uri* parameter.

   .. versionchanged:: 3.7
      *database* can now also be a :term:`path-like object`, not only a string.

   .. versionchanged:: 3.10
      Added the ``sqlite3.connect/handle`` auditing event.

   .. versionchanged:: 3.12
      Added the *autocommit* parameter.

   .. versionchanged:: 3.15
      All parameters except *database* are now keyword-only.


----

.. data:: SQLITE_KEYWORDS

   A :class:`tuple` containing all SQLite keywords.

   This constant is only available if Python was compiled with SQLite
   3.24.0 or greater.

   .. versionadded:: 3.15


----

   .. method:: create_function(name, narg, func, /, *, deterministic=False)

      Create or remove a user-defined SQL function.

      :param str name:
          The name of the SQL function.

      :param int narg:
          The number of arguments the SQL function can accept.
          If ``-1``, it may take any number of arguments.

      :param func:
          A :term:`callable` that is called when the SQL function is invoked.
          The callable must return :ref:`a type natively supported by SQLite
          <sqlite3-types>`.
          Set to ``None`` to remove an existing SQL function.
      :type func: :term:`callback` | None

      :param bool deterministic:
          If ``True``, the created SQL function is marked as
          `deterministic <https://sqlite.org/deterministic.html>`_,
          which allows SQLite to perform additional optimizations.

      .. versionchanged:: 3.8
         Added the *deterministic* parameter.

      .. versionchanged:: 3.15
         The first three parameters are now positional-only.

      Example:

      .. doctest::

         >>> import hashlib
         >>> def md5sum(t):
         ...     return hashlib.md5(t).hexdigest()
         >>> con = sqlite3.connect(":memory:")
         >>> con.create_function("md5", 1, md5sum)
         >>> for row in con.execute("SELECT md5(?)", (b"foo",)):
         ...     print(row)
         ('acbd18db4cc2f85cedef654fccc4a4d8',)
         >>> con.close()



----

   .. method:: create_aggregate(name, n_arg, aggregate_class, /)

      Create or remove a user-defined SQL aggregate function.

      :param str name:
          The name of the SQL aggregate function.

      :param int n_arg:
          The number of arguments the SQL aggregate function can accept.
          If ``-1``, it may take any number of arguments.

      :param aggregate_class:
          A class must implement the following methods:

          * ``step()``: Add a row to the aggregate.
          * ``finalize()``: Return the final result of the aggregate as
            :ref:`a type natively supported by SQLite <sqlite3-types>`.

          The number of arguments that the ``step()`` method must accept
          is controlled by *n_arg*.

          Set to ``None`` to remove an existing SQL aggregate function.
      :type aggregate_class: :term:`class` | None

      .. versionchanged:: 3.15
         All three parameters are now positional-only.

      Example:

      .. testcode::

         class MySum:
             def __init__(self):
                 self.count = 0

             def step(self, value):
                 self.count += value

             def finalize(self):
                 return self.count

         con = sqlite3.connect(":memory:")
         con.create_aggregate("mysum", 1, MySum)
         cur = con.execute("CREATE TABLE test(i)")
         cur.execute("INSERT INTO test(i) VALUES(1)")
         cur.execute("INSERT INTO test(i) VALUES(2)")
         cur.execute("SELECT mysum(i) FROM test")
         print(cur.fetchone()[0])

         con.close()

      .. testoutput::
         :hide:

         3



----

   .. method:: set_authorizer(authorizer_callback, /)

      Register :term:`callable` *authorizer_callback* to be invoked
      for each attempt to access a column of a table in the database.
      The callback should return one of :const:`SQLITE_OK`,
      :const:`SQLITE_DENY`, or :const:`SQLITE_IGNORE`
      to signal how access to the column should be handled
      by the underlying SQLite library.

      The first argument to the callback signifies what kind of operation is to be
      authorized. The second and third argument will be arguments or ``None``
      depending on the first argument. The 4th argument is the name of the database
      ("main", "temp", etc.) if applicable. The 5th argument is the name of the
      inner-most trigger or view that is responsible for the access attempt or
      ``None`` if this access attempt is directly from input SQL code.

      Please consult the SQLite documentation about the possible values for the first
      argument and the meaning of the second and third argument depending on the first
      one. All necessary constants are available in the :mod:`!sqlite3` module.

      Passing ``None`` as *authorizer_callback* will disable the authorizer.

      .. versionchanged:: 3.11
         Added support for disabling the authorizer using ``None``.

      .. versionchanged:: 3.15
         The only parameter is now positional-only.



----

   .. method:: set_progress_handler(progress_handler, /, n)

      Register :term:`callable` *progress_handler* to be invoked for every *n*
      instructions of the SQLite virtual machine. This is useful if you want to
      get called from SQLite during long-running operations, for example to update
      a GUI.

      If you want to clear any previously installed progress handler, call the
      method with ``None`` for *progress_handler*.

      Returning a non-zero value from the handler function will terminate the
      currently executing query and cause it to raise a :exc:`DatabaseError`
      exception.

      .. versionchanged:: 3.15
         The first parameter is now positional-only.



----

   .. method:: set_trace_callback(trace_callback, /)

      Register :term:`callable` *trace_callback* to be invoked
      for each SQL statement that is actually executed by the SQLite backend.

      The only argument passed to the callback is the statement (as
      :class:`str`) that is being executed. The return value of the callback is
      ignored. Note that the backend does not only run statements passed to the
      :meth:`Cursor.execute` methods.  Other sources include the
      :ref:`transaction management <sqlite3-controlling-transactions>` of the
      :mod:`!sqlite3` module and the execution of triggers defined in the current
      database.

      Passing ``None`` as *trace_callback* will disable the trace callback.

      .. note::
         Exceptions raised in the trace callback are not propagated. As a
         development and debugging aid, use
         :meth:`~sqlite3.enable_callback_tracebacks` to enable printing
         tracebacks from exceptions raised in the trace callback.

      .. versionadded:: 3.3

      .. versionchanged:: 3.15
         The first parameter is now positional-only.



----

   .. attribute:: row_factory

      The initial :attr:`~Cursor.row_factory`
      for :class:`Cursor` objects created from this connection.
      Assigning to this attribute does not affect the :attr:`!row_factory`
      of existing cursors belonging to this connection, only new ones.
      Is ``None`` by default,
      meaning each row is returned as a :class:`tuple`.

      See :ref:`sqlite3-howto-row-factory` for more details.

      .. versionchanged:: 3.15
         Deleting the ``row_factory`` attribute is no longer allowed.


----

   .. attribute:: text_factory

      A :term:`callable` that accepts a :class:`bytes` parameter
      and returns a text representation of it.
      The callable is invoked for SQLite values with the ``TEXT`` data type.
      By default, this attribute is set to :class:`str`.

      See :ref:`sqlite3-howto-encoding` for more details.

      .. versionchanged:: 3.15
         Deleting the ``text_factory`` attribute is no longer allowed.


----

   .. method:: fetchmany(size=cursor.arraysize)

      Return the next set of rows of a query result as a :class:`list`.
      Return an empty list if no more rows are available.

      The number of rows to fetch per call is specified by the *size* parameter.
      If *size* is not given, :attr:`arraysize` determines the number of rows
      to be fetched.
      If fewer than *size* rows are available,
      as many rows as are available are returned.

      Note there are performance considerations involved with the *size* parameter.
      For optimal performance, it is usually best to use the arraysize attribute.
      If the *size* parameter is used, then it is best for it to retain the same
      value from one :meth:`fetchmany` call to the next.

      .. versionchanged:: 3.15
         Negative *size* values are rejected by raising :exc:`ValueError`.


----

   .. attribute:: arraysize

      Read/write attribute that controls the number of rows returned by :meth:`fetchmany`.
      The default value is 1 which means a single row would be fetched per call.

      .. versionchanged:: 3.15
         Negative values are rejected by raising :exc:`ValueError`.


----

   .. attribute:: row_factory

      Control how a row fetched from this :class:`!Cursor` is represented.
      If ``None``, a row is represented as a :class:`tuple`.
      Can be set to the included :class:`sqlite3.Row`;
      or a :term:`callable` that accepts two arguments,
      a :class:`Cursor` object and the :class:`!tuple` of row values,
      and returns a custom object representing an SQLite row.

      Defaults to what :attr:`Connection.row_factory` was set to
      when the :class:`!Cursor` was created.
      Assigning to this attribute does not affect
      :attr:`Connection.row_factory` of the parent connection.

      See :ref:`sqlite3-howto-row-factory` for more details.

      .. versionchanged:: 3.15
         Deleting the ``row_factory`` attribute is no longer allowed.


.. The sqlite3.Row example used to be a how-to. It has now been incorporated
   into the Row reference. We keep the anchor here in order not to break
   existing links.

.. _sqlite3-columns-by-name:
.. _sqlite3-row-objects:

Row objects
^^^^^^^^^^^

.. class:: Row

   A :class:`!Row` instance serves as a highly optimized
   :attr:`~Connection.row_factory` for :class:`Connection` objects.
   It supports iteration, equality testing, :func:`len`,
   and :term:`mapping` access by column name and index.

   Two :class:`!Row` objects compare equal
   if they have identical column names and values.

   See :ref:`sqlite3-howto-row-factory` for more details.

   .. method:: keys

      Return a :class:`list` of column names as :class:`strings <str>`.
      Immediately after a query,
      it is the first member of each tuple in :attr:`Cursor.description`.

   .. versionchanged:: 3.5
      Added support of slicing.


.. _sqlite3-blob-objects:

Blob objects
^^^^^^^^^^^^

.. class:: Blob

   .. versionadded:: 3.11

   A :class:`Blob` instance is a :term:`file-like object`
   that can read and write data in an SQLite :abbr:`BLOB (Binary Large OBject)`.
   Call :func:`len(blob) <len>` to get the size (number of bytes) of the blob.
   Use indices and :term:`slices <slice>` for direct access to the blob data.

   Use the :class:`Blob` as a :term:`context manager` to ensure that the blob
   handle is closed after use.

   .. testcode::

      con = sqlite3.connect(":memory:")
      con.execute("CREATE TABLE test(blob_col blob)")
      con.execute("INSERT INTO test(blob_col) VALUES(zeroblob(13))")

      # Write to our blob, using two write operations:
      with con.blobopen("test", "blob_col", 1) as blob:
          blob.write(b"hello, ")
          blob.write(b"world.")
          # Modify the first and last bytes of our blob
          blob[0] = ord("H")
          blob[-1] = ord("!")

      # Read the contents of our blob
      with con.blobopen("test", "blob_col", 1) as blob:
          greeting = blob.read()

      print(greeting)  # outputs "b'Hello, world!'"
      con.close()

   .. testoutput::
      :hide:

      b'Hello, world!'

   .. method:: close()

      Close the blob.

      The blob will be unusable from this point onward.  An
      :class:`~sqlite3.Error` (or subclass) exception will be raised if any
      further operation is attempted with the blob.

   .. method:: read(length=-1, /)

      Read *length* bytes of data from the blob at the current offset position.
      If the end of the blob is reached, the data up to
      :abbr:`EOF (End of File)` will be returned.  When *length* is not
      specified, or is negative, :meth:`~Blob.read` will read until the end of
      the blob.

   .. method:: write(data, /)

      Write *data* to the blob at the current offset.  This function cannot
      change the blob length.  Writing beyond the end of the blob will raise
      :exc:`ValueError`.

   .. method:: tell()

      Return the current access position of the blob.

   .. method:: seek(offset, origin=os.SEEK_SET, /)

      Set the current access position of the blob to *offset*.  The *origin*
      argument defaults to :const:`os.SEEK_SET` (absolute blob positioning).
      Other values for *origin* are :const:`os.SEEK_CUR` (seek relative to the
      current position) and :const:`os.SEEK_END` (seek relative to the blob’s
      end).


PrepareProtocol objects
^^^^^^^^^^^^^^^^^^^^^^^

.. class:: PrepareProtocol

   The PrepareProtocol type's single purpose is to act as a :pep:`246` style
   adaption protocol for objects that can :ref:`adapt themselves
   <sqlite3-conform>` to :ref:`native SQLite types <sqlite3-types>`.


.. _sqlite3-exceptions:

Exceptions
^^^^^^^^^^

The exception hierarchy is defined by the DB-API 2.0 (:pep:`249`).

.. exception:: Warning

   This exception is not currently raised by the :mod:`!sqlite3` module,
   but may be raised by applications using :mod:`!sqlite3`,
   for example if a user-defined function truncates data while inserting.
   ``Warning`` is a subclass of :exc:`Exception`.

.. exception:: Error

   The base class of the other exceptions in this module.
   Use this to catch all errors with one single :keyword:`except` statement.
   ``Error`` is a subclass of :exc:`Exception`.

   If the exception originated from within the SQLite library,
   the following two attributes are added to the exception:

   .. attribute:: sqlite_errorcode

      The numeric error code from the
      `SQLite API <https://sqlite.org/rescode.html>`_

      .. versionadded:: 3.11

   .. attribute:: sqlite_errorname

      The symbolic name of the numeric error code
      from the `SQLite API <https://sqlite.org/rescode.html>`_

      .. versionadded:: 3.11

.. exception:: InterfaceError

   Exception raised for misuse of the low-level SQLite C API.
   In other words, if this exception is raised, it probably indicates a bug in the
   :mod:`!sqlite3` module.
   ``InterfaceError`` is a subclass of :exc:`Error`.

.. exception:: DatabaseError

   Exception raised for errors that are related to the database.
   This serves as the base exception for several types of database errors.
   It is only raised implicitly through the specialised subclasses.
   ``DatabaseError`` is a subclass of :exc:`Error`.

.. exception:: DataError

   Exception raised for errors caused by problems with the processed data,
   like numeric values out of range, and strings which are too long.
   ``DataError`` is a subclass of :exc:`DatabaseError`.

.. exception:: OperationalError

   Exception raised for errors that are related to the database's operation,
   and not necessarily under the control of the programmer.
   For example, the database path is not found,
   or a transaction could not be processed.
   ``OperationalError`` is a subclass of :exc:`DatabaseError`.

.. exception:: IntegrityError

   Exception raised when the relational integrity of the database is affected,
   e.g. a foreign key check fails.  It is a subclass of :exc:`DatabaseError`.

.. exception:: InternalError

   Exception raised when SQLite encounters an internal error.
   If this is raised, it may indicate that there is a problem with the runtime
   SQLite library.
   ``InternalError`` is a subclass of :exc:`DatabaseError`.

.. exception:: ProgrammingError

   Exception raised for :mod:`!sqlite3` API programming errors,
   for example supplying the wrong number of bindings to a query,
   or trying to operate on a closed :class:`Connection`.
   ``ProgrammingError`` is a subclass of :exc:`DatabaseError`.

.. exception:: NotSupportedError

   Exception raised in case a method or database API is not supported by the
   underlying SQLite library. For example, setting *deterministic* to
   ``True`` in :meth:`~Connection.create_function`, if the underlying SQLite library
   does not support deterministic functions.
   ``NotSupportedError`` is a subclass of :exc:`DatabaseError`.


.. _sqlite3-types:

SQLite and Python types
^^^^^^^^^^^^^^^^^^^^^^^

SQLite natively supports the following types: ``NULL``, ``INTEGER``,
``REAL``, ``TEXT``, ``BLOB``.

The following Python types can thus be sent to SQLite without any problem:

+-------------------------------+-------------+
| Python type                   | SQLite type |
+===============================+=============+
| ``None``                      | ``NULL``    |
+-------------------------------+-------------+
| :class:`int`                  | ``INTEGER`` |
+-------------------------------+-------------+
| :class:`float`                | ``REAL``    |
+-------------------------------+-------------+
| :class:`str`                  | ``TEXT``    |
+-------------------------------+-------------+
| :class:`bytes`                | ``BLOB``    |
+-------------------------------+-------------+


This is how SQLite types are converted to Python types by default:

+-------------+----------------------------------------------+
| SQLite type | Python type                                  |
+=============+==============================================+
| ``NULL``    | ``None``                                     |
+-------------+----------------------------------------------+
| ``INTEGER`` | :class:`int`                                 |
+-------------+----------------------------------------------+
| ``REAL``    | :class:`float`                               |
+-------------+----------------------------------------------+
| ``TEXT``    | depends on :attr:`~Connection.text_factory`, |
|             | :class:`str` by default                      |
+-------------+----------------------------------------------+
| ``BLOB``    | :class:`bytes`                               |
+-------------+----------------------------------------------+

The type system of the :mod:`!sqlite3` module is extensible in two ways: you can
store additional Python types in an SQLite database via
:ref:`object adapters <sqlite3-adapters>`,
and you can let the :mod:`!sqlite3` module convert SQLite types to
Python types via :ref:`converters <sqlite3-converters>`.


.. _sqlite3-default-converters:

Default adapters and converters (deprecated)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   The default adapters and converters are deprecated as of Python 3.12.
   Instead, use the :ref:`sqlite3-adapter-converter-recipes`
   and tailor them to your needs.

The deprecated default adapters and converters consist of:

* An adapter for :class:`datetime.date` objects to :class:`strings <str>` in
  `ISO 8601`_ format.
* An adapter for :class:`datetime.datetime` objects to strings in
  ISO 8601 format.
* A converter for :ref:`declared <sqlite3-converters>` "date" types to
  :class:`datetime.date` objects.
* A converter for declared "timestamp" types to
  :class:`datetime.datetime` objects.
  Fractional parts will be truncated to 6 digits (microsecond precision).

.. note::

   The default "timestamp" converter ignores UTC offsets in the database and
   always returns a naive :class:`datetime.datetime` object. To preserve UTC
   offsets in timestamps, either leave converters disabled, or register an
   offset-aware converter with :func:`register_converter`.

.. deprecated:: 3.12

.. _ISO 8601: https://en.wikipedia.org/wiki/ISO_8601


.. _sqlite3-cli:

Command-line interface
^^^^^^^^^^^^^^^^^^^^^^

The :mod:`!sqlite3` module can be invoked as a script,
using the interpreter's :option:`-m` switch,
in order to provide a simple SQLite shell.
The argument signature is as follows::

   python -m sqlite3 [-h] [-v] [filename] [sql]

Type ``.quit`` or CTRL-D to exit the shell.

.. program:: python -m sqlite3 [-h] [-v] [filename] [sql]

.. option:: -h, --help

   Print CLI help.

.. option:: -v, --version

   Print underlying SQLite library version.

.. versionadded:: 3.12


.. _sqlite3-howtos:

How-to guides
-------------

.. _sqlite3-placeholders:

How to use placeholders to bind values in SQL queries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SQL operations usually need to use values from Python variables. However,
beware of using Python's string operations to assemble queries, as they
are vulnerable to `SQL injection attacks`_. For example, an attacker can simply
close the single quote and inject ``OR TRUE`` to select all rows::

   >>> # Never do this -- insecure!
   >>> symbol = input()
   ' OR TRUE; --
   >>> sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol
   >>> print(sql)
   SELECT * FROM stocks WHERE symbol = '' OR TRUE; --'
   >>> cur.execute(sql)

Instead, use the DB-API's parameter substitution. To insert a variable into a
query string, use a placeholder in the string, and substitute the actual values
into the query by providing them as a :class:`tuple` of values to the second
argument of the cursor's :meth:`~Cursor.execute` method.

An SQL statement may use one of two kinds of placeholders:
question marks (qmark style) or named placeholders (named style).
For the qmark style, *parameters* must be a
:term:`sequence` whose length must match the number of placeholders,
or a :exc:`ProgrammingError` is raised.
For the named style, *parameters* must be
an instance of a :class:`dict` (or a subclass),
which must contain keys for all named parameters;
any extra items are ignored.
Here's an example of both styles:

.. testcode::

   con = sqlite3.connect(":memory:")
   cur = con.execute("CREATE TABLE lang(name, first_appeared)")

   # This is the named style used with executemany():
   data = (
       {"name": "C", "year": 1972},
       {"name": "Fortran", "year": 1957},
       {"name": "Python", "year": 1991},
       {"name": "Go", "year": 2009},
   )
   cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

   # This is the qmark style used in a SELECT query:
   params = (1972,)
   cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
   print(cur.fetchall())
   con.close()

.. testoutput::
   :hide:

   [('C', 1972)]

.. note::

   :pep:`249` numeric placeholders are *not* supported.
   If used, they will be interpreted as named placeholders.


.. _sqlite3-adapters:

How to adapt custom Python types to SQLite values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SQLite supports only a limited set of data types natively.
To store custom Python types in SQLite databases, *adapt* them to one of the
:ref:`Python types SQLite natively understands <sqlite3-types>`.

There are two ways to adapt Python objects to SQLite types:
letting your object adapt itself, or using an *adapter callable*.
The latter will take precedence above the former.
For a library that exports a custom type,
it may make sense to enable that type to adapt itself.
As an application developer, it may make more sense to take direct control by
registering custom adapter functions.


.. _sqlite3-conform:

How to write adaptable objects
""""""""""""""""""""""""""""""

Suppose we have a :class:`!Point` class that represents a pair of coordinates,
``x`` and ``y``, in a Cartesian coordinate system.
The coordinate pair will be stored as a text string in the database,
using a semicolon to separate the coordinates.
This can be implemented by adding a ``__conform__(self, protocol)``
method which returns the adapted value.
The object passed to *protocol* will be of type :class:`PrepareProtocol`.

.. testcode::

   class Point:
       def __init__(self, x, y):
           self.x, self.y = x, y

       def __conform__(self, protocol):
           if protocol is sqlite3.PrepareProtocol:
               return f"{self.x};{self.y}"

   con = sqlite3.connect(":memory:")
   cur = con.cursor()

   cur.execute("SELECT ?", (Point(4.0, -3.2),))
   print(cur.fetchone()[0])
   con.close()

.. testoutput::
   :hide:

   4.0;-3.2


How to register adapter callables
"""""""""""""""""""""""""""""""""

The other possibility is to create a function that converts the Python object
to an SQLite-compatible type.
This function can then be registered using :func:`register_adapter`.

.. testcode::

   class Point:
       def __init__(self, x, y):
           self.x, self.y = x, y

   def adapt_point(point):
       return f"{point.x};{point.y}"

   sqlite3.register_adapter(Point, adapt_point)

   con = sqlite3.connect(":memory:")
   cur = con.cursor()

   cur.execute("SELECT ?", (Point(1.0, 2.5),))
   print(cur.fetchone()[0])
   con.close()

.. testoutput::
   :hide:

   1.0;2.5


.. _sqlite3-converters:

How to convert SQLite values to custom Python types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writing an adapter lets you convert *from* custom Python types *to* SQLite
values.
To be able to convert *from* SQLite values *to* custom Python types,
we use *converters*.

Let's go back to the :class:`!Point` class. We stored the x and y coordinates
separated via semicolons as strings in SQLite.

First, we'll define a converter function that accepts the string as a parameter
and constructs a :class:`!Point` object from it.

.. note::

   Converter functions are **always** passed a :class:`bytes` object,
   no matter the underlying SQLite data type.

.. testcode::

   def convert_point(s):
       x, y = map(float, s.split(b";"))
       return Point(x, y)

We now need to tell :mod:`!sqlite3` when it should convert a given SQLite value.
This is done when connecting to a database, using the *detect_types* parameter
of :func:`connect`. There are three options:

* Implicit: set *detect_types* to :const:`PARSE_DECLTYPES`
* Explicit: set *detect_types* to :const:`PARSE_COLNAMES`
* Both: set *detect_types* to
  ``sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES``.
  Column names take precedence over declared types.

The following example illustrates the implicit and explicit approaches:

.. testcode::

   class Point:
       def __init__(self, x, y):
           self.x, self.y = x, y

       def __repr__(self):
           return f"Point({self.x}, {self.y})"

   def adapt_point(point):
       return f"{point.x};{point.y}"

   def convert_point(s):
       x, y = list(map(float, s.split(b";")))
       return Point(x, y)

   # Register the adapter and converter
   sqlite3.register_adapter(Point, adapt_point)
   sqlite3.register_converter("point", convert_point)

   # 1) Parse using declared types
   p = Point(4.0, -3.2)
   con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
   cur = con.execute("CREATE TABLE test(p point)")

   cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
   cur.execute("SELECT p FROM test")
   print("with declared types:", cur.fetchone()[0])
   cur.close()
   con.close()

   # 2) Parse using column names
   con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
   cur = con.execute("CREATE TABLE test(p)")

   cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
   cur.execute('SELECT p AS "p [point]" FROM test')
   print("with column names:", cur.fetchone()[0])
   cur.close()
   con.close()

.. testoutput::
   :hide:

   with declared types: Point(4.0, -3.2)
   with column names: Point(4.0, -3.2)


.. _sqlite3-adapter-converter-recipes:

Adapter and converter recipes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section shows recipes for common adapters and converters.

.. testcode::

   import datetime as dt
   import sqlite3

   def adapt_date_iso(val):
       """Adapt datetime.date to ISO 8601 date."""
       return val.isoformat()

   def adapt_datetime_iso(val):
       """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
       return val.replace(tzinfo=None).isoformat()

   def adapt_datetime_epoch(val):
       """Adapt datetime.datetime to Unix timestamp."""
       return int(val.timestamp())

   sqlite3.register_adapter(dt.date, adapt_date_iso)
   sqlite3.register_adapter(dt.datetime, adapt_datetime_iso)
   sqlite3.register_adapter(dt.datetime, adapt_datetime_epoch)

   def convert_date(val):
       """Convert ISO 8601 date to datetime.date object."""
       return dt.date.fromisoformat(val.decode())

   def convert_datetime(val):
       """Convert ISO 8601 datetime to datetime.datetime object."""
       return dt.datetime.fromisoformat(val.decode())

   def convert_timestamp(val):
       """Convert Unix epoch timestamp to datetime.datetime object."""
       return dt.datetime.fromtimestamp(int(val))

   sqlite3.register_converter("date", convert_date)
   sqlite3.register_converter("datetime", convert_datetime)
   sqlite3.register_converter("timestamp", convert_timestamp)

.. testcode::
   :hide:

   when = dt.datetime(2019, 5, 18, 15, 17, 8, 123456)

   assert adapt_date_iso(when.date()) == "2019-05-18"
   assert convert_date(b"2019-05-18") == when.date()

   assert adapt_datetime_iso(when) == "2019-05-18T15:17:08.123456"
   assert convert_datetime(b"2019-05-18T15:17:08.123456") == when

   # Using current time as fromtimestamp() returns local date/time.
   # Dropping microseconds as adapt_datetime_epoch truncates fractional second part.
   now = dt.datetime.now().replace(microsecond=0)
   current_timestamp = int(now.timestamp())

   assert adapt_datetime_epoch(now) == current_timestamp
   assert convert_timestamp(str(current_timestamp).encode()) == now


.. _sqlite3-connection-shortcuts:

How to use connection shortcut methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the :meth:`~Connection.execute`,
:meth:`~Connection.executemany`, and :meth:`~Connection.executescript`
methods of the :class:`Connection` class, your code can
be written more concisely because you don't have to create the (often
superfluous) :class:`Cursor` objects explicitly. Instead, the :class:`Cursor`
objects are created implicitly and these shortcut methods return the cursor
objects. This way, you can execute a ``SELECT`` statement and iterate over it
directly using only a single call on the :class:`Connection` object.

.. testcode::

   # Create and fill the table.
   con = sqlite3.connect(":memory:")
   con.execute("CREATE TABLE lang(name, first_appeared)")
   data = [
       ("C++", 1985),
       ("Objective-C", 1984),
   ]
   con.executemany("INSERT INTO lang(name, first_appeared) VALUES(?, ?)", data)

   # Print the table contents
   for row in con.execute("SELECT name, first_appeared FROM lang"):
       print(row)

   print("I just deleted", con.execute("DELETE FROM lang").rowcount, "rows")

   # close() is not a shortcut method and it's not called automatically;
   # the connection object should be closed manually
   con.close()

.. testoutput::
   :hide:

   ('C++', 1985)
   ('Objective-C', 1984)
   I just deleted 2 rows


.. _sqlite3-connection-context-manager:

How to use the connection context manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A :class:`Connection` object can be used as a context manager that
automatically commits or rolls back open transactions when leaving the body of
the context manager.
If the body of the :keyword:`with` statement finishes without exceptions,
the transaction is committed.
If this commit fails,
or if the body of the ``with`` statement raises an uncaught exception,
the transaction is rolled back.
If :attr:`~Connection.autocommit` is ``False``,
a new transaction is implicitly opened after committing or rolling back.

If there is no open transaction upon leaving the body of the ``with`` statement,
or if :attr:`~Connection.autocommit` is ``True``,
the context manager does nothing.

.. note::
   The context manager neither implicitly opens a new transaction
   nor closes the connection. If you need a closing context manager, consider
   using :meth:`contextlib.closing`.

.. testcode::

   con = sqlite3.connect(":memory:")
   con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

   # Successful, con.commit() is called automatically afterwards
   with con:
       con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))

   # con.rollback() is called after the with block finishes with an exception,
   # the exception is still raised and must be caught
   try:
       with con:
           con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))
   except sqlite3.IntegrityError:
       print("couldn't add Python twice")

   # Connection object used as context manager only commits or rollbacks transactions,
   # so the connection object should be closed manually
   con.close()

.. testoutput::
   :hide:

   couldn't add Python twice


.. _sqlite3-uri-tricks:

How to work with SQLite URIs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some useful URI tricks include:

* Open a database in read-only mode:

.. doctest::

   >>> con = sqlite3.connect("file:tutorial.db?mode=ro", uri=True)
   >>> con.execute("CREATE TABLE readonly(data)")
   Traceback (most recent call last):
   OperationalError: attempt to write a readonly database
   >>> con.close()

* Do not implicitly create a new database file if it does not already exist;
  will raise :exc:`~sqlite3.OperationalError` if unable to create a new file:

.. doctest::

   >>> con = sqlite3.connect("file:nosuchdb.db?mode=rw", uri=True)
   Traceback (most recent call last):
   OperationalError: unable to open database file


* Create a shared named in-memory database:

.. testcode::

   db = "file:mem1?mode=memory&cache=shared"
   con1 = sqlite3.connect(db, uri=True)
   con2 = sqlite3.connect(db, uri=True)
   with con1:
       con1.execute("CREATE TABLE shared(data)")
       con1.execute("INSERT INTO shared VALUES(28)")
   res = con2.execute("SELECT data FROM shared")
   assert res.fetchone() == (28,)

   con1.close()
   con2.close()

More information about this feature, including a list of parameters,
can be found in the `SQLite URI documentation`_.

.. _SQLite URI documentation: https://www.sqlite.org/uri.html


.. _sqlite3-howto-row-factory:

How to create and use row factories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, :mod:`!sqlite3` represents each row as a :class:`tuple`.
If a :class:`!tuple` does not suit your needs,
you can use the :class:`sqlite3.Row` class
or a custom :attr:`~Cursor.row_factory`.

While :attr:`!row_factory` exists as an attribute both on the
:class:`Cursor` and the :class:`Connection`,
it is recommended to set :class:`Connection.row_factory`,
so all cursors created from the connection will use the same row factory.

:class:`!Row` provides indexed and case-insensitive named access to columns,
with minimal memory overhead and performance impact over a :class:`!tuple`.
To use :class:`!Row` as a row factory,
assign it to the :attr:`!row_factory` attribute:

.. doctest::

   >>> con = sqlite3.connect(":memory:")
   >>> con.row_factory = sqlite3.Row

Queries now return :class:`!Row` objects:

.. doctest::

   >>> res = con.execute("SELECT 'Earth' AS name, 6378 AS radius")
   >>> row = res.fetchone()
   >>> row.keys()
   ['name', 'radius']
   >>> row[0]         # Access by index.
   'Earth'
   >>> row["name"]    # Access by name.
   'Earth'
   >>> row["RADIUS"]  # Column names are case-insensitive.
   6378
   >>> con.close()

.. note::

    The ``FROM`` clause can be omitted in the ``SELECT`` statement, as in the
    above example. In such cases, SQLite returns a single row with columns
    defined by expressions, e.g. literals, with the given aliases
    ``expr AS alias``.

You can create a custom :attr:`~Cursor.row_factory`
that returns each row as a :class:`dict`, with column names mapped to values:

.. testcode::

   def dict_factory(cursor, row):
       fields = [column[0] for column in cursor.description]
       return {key: value for key, value in zip(fields, row)}

Using it, queries now return a :class:`!dict` instead of a :class:`!tuple`:

.. doctest::

   >>> con = sqlite3.connect(":memory:")
   >>> con.row_factory = dict_factory
   >>> for row in con.execute("SELECT 1 AS a, 2 AS b"):
   ...     print(row)
   {'a': 1, 'b': 2}
   >>> con.close()

The following row factory returns a :term:`named tuple`:

.. testcode::

   from collections import namedtuple

   def namedtuple_factory(cursor, row):
       fields = [column[0] for column in cursor.description]
       cls = namedtuple("Row", fields)
       return cls._make(row)

:func:`!namedtuple_factory` can be used as follows:

.. doctest::

   >>> con = sqlite3.connect(":memory:")
   >>> con.row_factory = namedtuple_factory
   >>> cur = con.execute("SELECT 1 AS a, 2 AS b")
   >>> row = cur.fetchone()
   >>> row
   Row(a=1, b=2)
   >>> row[0]  # Indexed access.
   1
   >>> row.b   # Attribute access.
   2
   >>> con.close()

With some adjustments, the above recipe can be adapted to use a
:class:`~dataclasses.dataclass`, or any other custom class,
instead of a :class:`~collections.namedtuple`.


.. _sqlite3-howto-encoding:

How to handle non-UTF-8 text encodings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, :mod:`!sqlite3` uses :class:`str` to adapt SQLite values
with the ``TEXT`` data type.
This works well for UTF-8 encoded text, but it might fail for other encodings
and invalid UTF-8.
You can use a custom :attr:`~Connection.text_factory` to handle such cases.

Because of SQLite's `flexible typing`_, it is not uncommon to encounter table
columns with the ``TEXT`` data type containing non-UTF-8 encodings,
or even arbitrary data.
To demonstrate, let's assume we have a database with ISO-8859-2 (Latin-2)
encoded text, for example a table of Czech-English dictionary entries.
Assuming we now have a :class:`Connection` instance :py:data:`!con`
connected to this database,
we can decode the Latin-2 encoded text using this :attr:`~Connection.text_factory`:

.. testcode::

   con.text_factory = lambda data: str(data, encoding="latin2")

For invalid UTF-8 or arbitrary data in stored in ``TEXT`` table columns,
you can use the following technique, borrowed from the :ref:`unicode-howto`:

.. testcode::

   con.text_factory = lambda data: str(data, errors="surrogateescape")

.. note::

   The :mod:`!sqlite3` module API does not support strings
   containing surrogates.

.. seealso::

   :ref:`unicode-howto`


.. _sqlite3-explanation:

Explanation
-----------

.. _sqlite3-transaction-control:
.. _sqlite3-controlling-transactions:

Transaction control
^^^^^^^^^^^^^^^^^^^

:mod:`!sqlite3` offers multiple methods of controlling whether,
when and how database transactions are opened and closed.
:ref:`sqlite3-transaction-control-autocommit` is recommended,
while :ref:`sqlite3-transaction-control-isolation-level`
retains the pre-Python 3.12 behaviour.

.. _sqlite3-transaction-control-autocommit:

Transaction control via the ``autocommit`` attribute
""""""""""""""""""""""""""""""""""""""""""""""""""""

The recommended way of controlling transaction behaviour is through
the :attr:`Connection.autocommit` attribute,
which should preferably be set using the *autocommit* parameter
of :func:`connect`.

It is suggested to set *autocommit* to ``False``,
which implies :pep:`249`-compliant transaction control.
This means:

* :mod:`!sqlite3` ensures that a transaction is always open,
  so :func:`connect`, :meth:`Connection.commit`, and :meth:`Connection.rollback`
  will implicitly open a new transaction
  (immediately after closing the pending one, for the latter two).
  :mod:`!sqlite3` uses ``BEGIN DEFERRED`` statements when opening transactions.
* Transactions should be committed explicitly using :meth:`!commit`.
* Transactions should be rolled back explicitly using :meth:`!rollback`.
* An implicit rollback is performed if the database is
  :meth:`~Connection.close`-ed with pending changes.

Set *autocommit* to ``True`` to enable SQLite's `autocommit mode`_.
In this mode, :meth:`Connection.commit` and :meth:`Connection.rollback`
have no effect.
Note that SQLite's autocommit mode is distinct from
the :pep:`249`-compliant :attr:`Connection.autocommit` attribute;
use :attr:`Connection.in_transaction` to query
the low-level SQLite autocommit mode.

Set *autocommit* to :data:`LEGACY_TRANSACTION_CONTROL`
to leave transaction control behaviour to the
:attr:`Connection.isolation_level` attribute.
See :ref:`sqlite3-transaction-control-isolation-level` for more information.


.. _sqlite3-transaction-control-isolation-level:

Transaction control via the ``isolation_level`` attribute
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. note::

   The recommended way of controlling transactions is via the
   :attr:`~Connection.autocommit` attribute.
   See :ref:`sqlite3-transaction-control-autocommit`.

If :attr:`Connection.autocommit` is set to
:data:`LEGACY_TRANSACTION_CONTROL` (the default),
transaction behaviour is controlled using
the :attr:`Connection.isolation_level` attribute.
Otherwise, :attr:`!isolation_level` has no effect.

If the connection attribute :attr:`~Connection.isolation_level`
is not ``None``,
new transactions are implicitly opened before
:meth:`~Cursor.execute` and :meth:`~Cursor.executemany` executes
``INSERT``, ``UPDATE``, ``DELETE``, or ``REPLACE`` statements;
for other statements, no implicit transaction handling is performed.
Use the :meth:`~Connection.commit` and :meth:`~Connection.rollback` methods
to respectively commit and roll back pending transactions.
You can choose the underlying `SQLite transaction behaviour`_ —
that is, whether and what type of ``BEGIN`` statements :mod:`!sqlite3`
implicitly executes –
via the :attr:`~Connection.isolation_level` attribute.

If :attr:`~Connection.isolation_level` is set to ``None``,
no transactions are implicitly opened at all.
This leaves the underlying SQLite library in `autocommit mode`_,
but also allows the user to perform their own transaction handling
using explicit SQL statements.
The underlying SQLite library autocommit mode can be queried using the
:attr:`~Connection.in_transaction` attribute.

The :meth:`~Cursor.executescript` method implicitly commits
any pending transaction before execution of the given SQL script,
regardless of the value of :attr:`~Connection.isolation_level`.

.. versionchanged:: 3.6
   :mod:`!sqlite3` used to implicitly commit an open transaction before DDL
   statements.  This is no longer the case.

.. versionchanged:: 3.12
   The recommended way of controlling transactions is now via the
   :attr:`~Connection.autocommit` attribute.

.. _autocommit mode:
   https://www.sqlite.org/lang_transaction.html#implicit_versus_explicit_transactions

.. _SQLite transaction behaviour:
   https://www.sqlite.org/lang_transaction.html#deferred_immediate_and_exclusive_transactions

.. testcleanup::

   import os
   os.remove("backup.db")
   os.remove("dump.sql")
   os.remove("example.db")
   os.remove("tutorial.db")