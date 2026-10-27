.. function:: compile(source, filename, mode, flags=0, \
                      dont_inherit=False, optimize=-1, \
                      *, module=None)

   Compile the *source* into a code or AST object.  Code objects can be executed
   by :func:`exec` or :func:`eval`.  *source* can either be a normal string, a
   byte string, or an AST object.  Refer to the :mod:`ast` module documentation
   for information on how to work with AST objects.

   The *filename* argument should give the file from which the code was read;
   pass some recognizable value if it wasn't read from a file (``'<string>'`` is
   commonly used).

   The *mode* argument specifies what kind of code must be compiled; it can be
   ``'exec'`` if *source* consists of a sequence of statements, ``'eval'`` if it
   consists of a single expression, or ``'single'`` if it consists of a single
   interactive statement (in the latter case, expression statements that
   evaluate to something other than ``None`` will be printed).
   It can also be ``'func_type'`` if *source* consists of a
   function type signature, for example ``(int) -> str``; see
   :func:`ast.parse` for more information. This mode requires passing
   :data:`ast.PyCF_ONLY_AST` in *flags*.

   The optional arguments *flags* and *dont_inherit* control which
   :ref:`compiler options <ast-compiler-flags>` should be activated
   and which :ref:`future features <future>` should be allowed. If neither
   is present (or both are zero) the code is compiled with the same flags that
   affect the code that is calling :func:`compile`. If the *flags*
   argument is given and *dont_inherit* is not (or is zero) then the compiler
   options and the future statements specified by the *flags* argument are used
   in addition to those that would be used anyway. If *dont_inherit* is a
   non-zero integer then the *flags* argument is it -- the flags (future
   features and compiler options) in the surrounding code are ignored.

   Compiler options and future statements are specified by bits which can be
   bitwise ORed together to specify multiple options. The bitfield required to
   specify a given future feature can be found as the
   :attr:`~__future__._Feature.compiler_flag` attribute on the
   :class:`~__future__._Feature` instance in the :mod:`__future__` module.
   :ref:`Compiler flags <ast-compiler-flags>` can be found in :mod:`ast`
   module, with ``PyCF_`` prefix.

   The argument *optimize* specifies the optimization level of the compiler; the
   default value of ``-1`` selects the optimization level of the interpreter as
   given by :option:`-O` options.  Explicit levels are ``0`` (no optimization;
   ``__debug__`` is true), ``1`` (asserts are removed, ``__debug__`` is false)
   or ``2`` (docstrings are removed too).

   The optional argument *module* specifies the module name.
   It is needed to unambiguous :ref:`filter <warning-filter>` syntax warnings
   by module name.

   This function raises :exc:`SyntaxError` if the compiled source is invalid,
   including a *source* containing a null character or that cannot be decoded;
   :exc:`ValueError` if *mode* or *flags* is invalid,
   or if a string *source* contains surrogate characters;
   :exc:`MemoryError` or :exc:`RecursionError` if *source* is too complex
   to parse or compile,
   for example an expression with many thousands of nested operators;
   and :exc:`OverflowError` if *source* is too large.

   If you want to parse Python code into its AST representation, see
   :func:`ast.parse`.

   .. audit-event:: compile source,filename compile

      Raises an :ref:`auditing event <auditing>` ``compile`` with arguments
      ``source`` and ``filename``. This event may also be raised by implicit
      compilation.

   .. note::

      When compiling a string with multi-line code in ``'single'`` or
      ``'eval'`` mode, input must be terminated by at least one newline
      character.  This is to facilitate detection of incomplete and complete
      statements in the :mod:`code` module.

   .. warning::

      It is possible to crash the Python interpreter with a
      sufficiently large/complex string when compiling to an AST
      object due to stack depth limitations in Python's AST compiler.

   .. versionchanged:: 3.2
      Allowed use of Windows and Mac newlines.  Also, input in ``'exec'`` mode
      does not have to end in a newline anymore.  Added the *optimize* parameter.

   .. versionchanged:: 3.5
      Previously, :exc:`TypeError` was raised when null bytes were encountered
      in *source*.

   .. versionchanged:: 3.8
      ``ast.PyCF_ALLOW_TOP_LEVEL_AWAIT`` can now be passed in flags to enable
      support for top-level ``await``, ``async for``, and ``async with``.

   .. versionchanged:: 3.8
      Added support for ``mode='func_type'``.

   .. versionchanged:: 3.12
      :exc:`SyntaxError` is raised instead of :exc:`ValueError` when null bytes
      are encountered in *source*.

   .. versionchanged:: 3.15
      Added the *module* parameter.



----

.. function:: eval(source, /, globals=None, locals=None)

   :param source:
      A Python expression.
   :type source: :class:`str` | :ref:`code object <code-objects>`

   :param globals:
      The global namespace (default: ``None``).
   :type globals: :class:`dict` | :class:`frozendict` | ``None``

   :param locals:
      The local namespace (default: ``None``).
   :type locals: :term:`mapping` | ``None``

   :returns: The result of the evaluated expression.
   :raises: Syntax errors are reported as exceptions.

   .. warning::

      This function executes arbitrary code. Calling it with
      untrusted user-supplied input will lead to security vulnerabilities.

   The *source* argument is parsed and evaluated as a Python expression
   (technically speaking, an :ref:`expression list <exprlists>`)
   using the *globals* and *locals* mappings as global and local namespace.
   If the *globals* dictionary is present and does not contain a value for the
   key ``__builtins__``, a
   reference to the dictionary of the built-in module :mod:`builtins` is
   inserted under that key before *source* is parsed.
   Overriding ``__builtins__`` can be used to restrict or change the available
   names, but this is **not** a security mechanism: the executed code can
   still access all builtins.
   If the *locals* mapping is omitted it defaults to the
   *globals* dictionary.  If both mappings are omitted, the source is
   executed with the *globals* and *locals* in the environment where
   :func:`eval` is called.  Note, *eval()* will only have access to the
   :term:`nested scopes <nested scope>` (non-locals) in the enclosing
   environment if they are already referenced in the scope that is calling
   :func:`eval` (e.g. via a :keyword:`nonlocal` statement).

   Example:

      >>> x = 1
      >>> eval('x+1')
      2

      >>> eval("1, 2")
      (1, 2)

   This function can also be used to execute arbitrary code objects (such as
   those created by :func:`compile`).  In this case, pass a code object instead
   of a string.  If the code object has been compiled with ``'exec'`` as the
   *mode* argument, :func:`eval`\'s return value will be ``None``.

   Hints: dynamic execution of statements is supported by the :func:`exec`
   function.  The :func:`globals` and :func:`locals` functions
   return the current global and local dictionary, respectively, which may be
   useful to pass around for use by :func:`eval` or :func:`exec`.

   If the given source is a string, then leading and trailing spaces and tabs
   are stripped.

   See :func:`ast.literal_eval` for a function to evaluate strings
   with expressions containing only literals.

   .. audit-event:: exec code_object eval

      Raises an :ref:`auditing event <auditing>` ``exec`` with the code object
      as the argument. Code compilation events may also be raised.

   .. versionchanged:: 3.13

      The *globals* and *locals* arguments can now be passed as keywords.

   .. versionchanged:: 3.13

      The semantics of the default *locals* namespace have been adjusted as
      described for the :func:`locals` builtin.

   .. versionchanged:: 3.15

      *globals* can now be a :class:`frozendict`.


----

.. function:: exec(source, /, globals=None, locals=None, *, closure=None)

   .. warning::

      This function executes arbitrary code. Calling it with
      untrusted user-supplied input will lead to security vulnerabilities.

   This function supports dynamic execution of Python code. *source* must be
   either a string or a code object.  If it is a string, the string is parsed as
   a suite of Python statements which is then executed (unless a syntax error
   occurs). [#]_ If it is a code object, it is simply executed.  In all cases,
   the code that's executed is expected to be valid as file input (see the
   section :ref:`file-input` in the Reference Manual). Be aware that the
   :keyword:`nonlocal`, :keyword:`yield`,  and :keyword:`return`
   statements may not be used outside of
   function definitions even within the context of code passed to the
   :func:`exec` function. The return value is ``None``.

   In all cases, if the optional parts are omitted, the code is executed in the
   current scope.  If only *globals* is provided, it must be a dictionary
   (and not a subclass of dictionary), which
   will be used for both the global and the local variables.  If *globals* and
   *locals* are given, they are used for the global and local variables,
   respectively.  If provided, *locals* can be any mapping object.  Remember
   that at the module level, globals and locals are the same dictionary.

   .. note::

      When ``exec`` gets two separate objects as *globals* and *locals*, the
      code will be executed as if it were embedded in a class definition. This
      means functions and classes defined in the executed code will not be able
      to access variables assigned at the top level (as the "top level"
      variables are treated as class variables in a class definition).

   If the *globals* dictionary does not contain a value for the key
   ``__builtins__``, a reference to the dictionary of the built-in module
   :mod:`builtins` is inserted under that key.
   Overriding ``__builtins__`` can be used to restrict or change the available
   names, but this is **not** a security mechanism: the executed code can
   still access all builtins.

   The *closure* argument specifies a closure--a tuple of cellvars.
   It's only valid when the *object* is a code object containing
   :term:`free (closure) variables <closure variable>`.
   The length of the tuple must exactly match the length of the code object's
   :attr:`~codeobject.co_freevars` attribute.

   .. audit-event:: exec code_object exec

      Raises an :ref:`auditing event <auditing>` ``exec`` with the code object
      as the argument. Code compilation events may also be raised.

   .. note::

      The built-in functions :func:`globals` and :func:`locals` return the current
      global and local namespace, respectively, which may be useful to pass around
      for use as the second and third argument to :func:`exec`.

   .. note::

      The default *locals* act as described for function :func:`locals` below.
      Pass an explicit *locals* dictionary if you need to see effects of the
      code on *locals* after function :func:`exec` returns.

   .. versionchanged:: 3.11
      Added the *closure* parameter.

   .. versionchanged:: 3.13

      The *globals* and *locals* arguments can now be passed as keywords.

   .. versionchanged:: 3.13

      The semantics of the default *locals* namespace have been adjusted as
      described for the :func:`locals` builtin.

   .. versionchanged:: 3.15

      *globals* can now be a :class:`frozendict`.



----

.. class:: frozendict(**kwargs)
           frozendict(mapping, /, **kwargs)
           frozendict(iterable, /, **kwargs)
   :noindex:

   Create a new frozen dictionary.  The :class:`frozendict` object is a built-in class.
   See also :ref:`typesmapping` for documentation about this class.

   For other containers see the built-in :class:`dict`, :class:`list`, :class:`set`,
   and :class:`tuple` classes, as well as the :mod:`collections` module.

   .. versionadded:: 3.15



----

.. function:: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

   Open *file* and return a corresponding :term:`file object`.  If the file
   cannot be opened, an :exc:`OSError` is raised. See
   :ref:`tut-files` for more examples of how to use this function.

   *file* is a :term:`path-like object` giving the pathname (absolute or
   relative to the current working directory) of the file to be opened or an
   integer file descriptor of the file to be wrapped.  (If a file descriptor is
   given, it is closed when the returned I/O object is closed unless *closefd*
   is set to ``False``.)

   *mode* is an optional string that specifies the mode in which the file is
   opened.  It defaults to ``'r'`` which means open for reading in text mode.
   Other common values are ``'w'`` for writing (truncating the file if it
   already exists), ``'x'`` for exclusive creation, and ``'a'`` for appending
   (which on *some* Unix systems, means that *all* writes append to the end of
   the file regardless of the current seek position).  In text mode, if
   *encoding* is not specified, UTF-8 is used by default; if
   :ref:`Python UTF-8 Mode <utf8-mode>` is disabled,
   :func:`locale.getencoding` is called to get the current locale encoding.
   (For reading and writing raw bytes use binary mode and leave
   *encoding* unspecified.)  The available modes are:

   .. _filemodes:

   .. index::
      pair: file; modes

   ========= ===============================================================
   Character Meaning
   ========= ===============================================================
   ``'r'``   open for reading (default)
   ``'w'``   open for writing, truncating the file first
   ``'x'``   open for exclusive creation, failing if the file already exists
   ``'a'``   open for writing, appending to the end of file if it exists
   ``'b'``   binary mode
   ``'t'``   text mode (default)
   ``'+'``   open for updating (reading and writing)
   ========= ===============================================================

   The default mode is ``'r'`` (open for reading text, a synonym of ``'rt'``).
   Modes ``'w+'`` and ``'w+b'`` open and truncate the file.  Modes ``'r+'``
   and ``'r+b'`` open the file with no truncation.

   As mentioned in the :ref:`io-overview`, Python distinguishes between binary
   and text I/O.  Files opened in binary mode (including ``'b'`` in the *mode*
   argument) return contents as :class:`bytes` objects without any decoding.  In
   text mode (the default, or when ``'t'`` is included in the *mode* argument),
   the contents of the file are returned as :class:`str`, the bytes having been
   first decoded using the default encoding or using the specified
   *encoding* if given.

   .. note::

      Python doesn't depend on the underlying operating system's notion of text
      files; all the processing is done by Python itself, and is therefore
      platform-independent.

   *buffering* is an optional integer used to set the buffering policy.  Pass 0
   to switch buffering off (only allowed in binary mode), 1 to select line
   buffering (only usable when writing in text mode), and an integer > 1 to indicate the size
   in bytes of a fixed-size chunk buffer. Note that specifying a buffer size this
   way applies for binary buffered I/O, but ``TextIOWrapper`` (i.e., files opened
   with ``mode='r+'``) would have another buffering. To disable buffering in
   ``TextIOWrapper``, consider using the ``write_through`` flag for
   :func:`io.TextIOWrapper.reconfigure`. When no *buffering* argument is
   given, the default buffering policy works as follows:

   * Binary files are buffered in fixed-size chunks; the size of the buffer
     is ``max(min(blocksize, 8 MiB), DEFAULT_BUFFER_SIZE)``
     when the device block size is available.
     On most systems, the buffer will typically be 128 kilobytes long.

   * "Interactive" text files (files for which :meth:`~io.IOBase.isatty`
     returns ``True``) use line buffering.  Other text files use the policy
     described above for binary files.

   *encoding* is the name of the encoding used to decode or encode the file.
   This should only be used in text mode.  The default encoding is UTF-8;
   if :ref:`Python UTF-8 Mode <utf8-mode>` is disabled, the default is
   platform-dependent (whatever :func:`locale.getencoding` returns).
   Any :term:`text encoding` supported by Python can be used, and
   ``encoding="locale"`` specifies the current locale encoding explicitly.
   See the :mod:`codecs` module for the list of supported encodings.

   *errors* is an optional string that specifies how encoding and decoding
   errors are to be handled—this cannot be used in binary mode.
   A variety of standard error handlers are available,
   though any error handling name that has been registered with
   :func:`codecs.register_error` is also valid.  The standard names
   can be found in :ref:`error-handlers`.

   .. index::
      single: universal newlines; open() built-in function

   .. _open-newline-parameter:

   *newline* determines how to parse newline characters from the stream.
   It can be ``None``, ``''``, ``'\n'``, ``'\r'``, and
   ``'\r\n'``.  It works as follows:

   * When reading input from the stream, if *newline* is ``None``, universal
     newlines mode is enabled.  Lines in the input can end in ``'\n'``,
     ``'\r'``, or ``'\r\n'``, and these are translated into ``'\n'`` before
     being returned to the caller.  If it is ``''``, universal newlines mode is
     enabled, but line endings are returned to the caller untranslated.  If it
     has any of the other legal values, input lines are only terminated by the
     given string, and the line ending is returned to the caller untranslated.

   * When writing output to the stream, if *newline* is ``None``, any ``'\n'``
     characters written are translated to the system default line separator,
     :data:`os.linesep`.  If *newline* is ``''`` or ``'\n'``, no translation
     takes place.  If *newline* is any of the other legal values, any ``'\n'``
     characters written are translated to the given string.

   If *closefd* is ``False`` and a file descriptor rather than a filename was
   given, the underlying file descriptor will be kept open when the file is
   closed.  If a filename is given *closefd* must be ``True`` (the default);
   otherwise, an error will be raised.

   A custom opener can be used by passing a callable as *opener*. The underlying
   file descriptor for the file object is then obtained by calling *opener* with
   (*file*, *flags*). *opener* must return an open file descriptor (passing
   :mod:`os.open` as *opener* results in functionality similar to passing
   ``None``).

   The newly created file is :ref:`non-inheritable <fd_inheritance>`.

   The following example uses the :ref:`dir_fd <dir_fd>` parameter of the
   :func:`os.open` function to open a file relative to a given directory::

      >>> import os
      >>> dir_fd = os.open('somedir', os.O_RDONLY)
      >>> def opener(path, flags):
      ...     return os.open(path, flags, dir_fd=dir_fd)
      ...
      >>> with open('spamspam.txt', 'w', opener=opener) as f:
      ...     print('This will be written to somedir/spamspam.txt', file=f)
      ...
      >>> os.close(dir_fd)  # don't leak a file descriptor

   The type of :term:`file object` returned by the :func:`open` function
   depends on the mode.  When :func:`open` is used to open a file in a text
   mode (``'w'``, ``'r'``, ``'wt'``, ``'rt'``, etc.), it returns a subclass of
   :class:`io.TextIOBase` (specifically :class:`io.TextIOWrapper`).  When used
   to open a file in a binary mode with buffering, the returned class is a
   subclass of :class:`io.BufferedIOBase`.  The exact class varies: in read
   binary mode, it returns an :class:`io.BufferedReader`; in write binary and
   append binary modes, it returns an :class:`io.BufferedWriter`, and in
   read/write mode, it returns an :class:`io.BufferedRandom`.  When buffering is
   disabled, the raw stream, a subclass of :class:`io.RawIOBase`,
   :class:`io.FileIO`, is returned.

   .. index::
      single: line-buffered I/O
      single: unbuffered I/O
      single: buffer size, I/O
      single: I/O control; buffering
      single: binary mode
      single: text mode
      pair: module; sys

   See also the file handling modules, such as :mod:`fileinput`, :mod:`io`
   (where :func:`open` is declared), :mod:`os`, :mod:`os.path`, :mod:`tempfile`,
   and :mod:`shutil`.

   .. audit-event:: open path,mode,flags open

   The ``mode`` and ``flags`` arguments may have been modified or inferred from
   the original call.

   .. versionchanged:: 3.3

      * The *opener* parameter was added.
      * The ``'x'`` mode was added.
      * :exc:`IOError` used to be raised, it is now an alias of :exc:`OSError`.
      * :exc:`FileExistsError` is now raised if the file opened in exclusive
        creation mode (``'x'``) already exists.

   .. versionchanged:: 3.4

      * The file is now non-inheritable.

   .. versionchanged:: 3.5

      * If the system call is interrupted and the signal handler does not raise an
        exception, the function now retries the system call instead of raising an
        :exc:`InterruptedError` exception (see :pep:`475` for the rationale).
      * The ``'namereplace'`` error handler was added.

   .. versionchanged:: 3.6

      * Support added to accept objects implementing :class:`os.PathLike`.
      * On Windows, opening a console buffer may return a subclass of
        :class:`io.RawIOBase` other than :class:`io.FileIO`.

   .. versionchanged:: 3.11
      The ``'U'`` mode has been removed.

   .. versionchanged:: 3.15
      UTF-8 is now the default encoding, instead of the
      platform-dependent locale encoding (:pep:`686`).


----

.. class:: sentinel(name, /, *, repr=None)

   Return a new unique sentinel object.  *name* must be a :class:`str`, and is
   used by default as the returned object's representation::

      >>> MISSING = sentinel("MISSING")
      >>> MISSING
      MISSING

   The optional *repr* argument can be used to specify a different representation::

      >>> MISSING = sentinel("MISSING", repr="<MISSING>")
      >>> MISSING
      <MISSING>

   Sentinel objects are truthy and compare equal only to themselves.  They are
   intended to be compared with the :keyword:`is` operator.

   ``sentinel`` does not support subclassing.

   Shallow and deep copies of a sentinel object return the object itself.

   Sentinels are conventionally assigned to a variable with a matching name.
   Sentinels defined in this way can be used in :term:`type hints <type hint>`::

      MISSING = sentinel("MISSING")

      def next_value(default: int | MISSING = MISSING):
          ...

   Sentinel objects support the :ref:`| <bitwise>` operator for use in type expressions.

   :mod:`Pickling <pickle>` is supported for sentinel objects that are
   placed in the global scope of a module under a name matching the sentinel's
   name, and for sentinels placed in class scopes with a name matching the
   :term:`qualified name` of the sentinel. Other sentinels, such as those
   defined in a function scope, are not picklable. The identity of the sentinel is preserved
   after pickling::

      import pickle

      PICKLABLE = sentinel("PICKLABLE")

      assert pickle.loads(pickle.dumps(PICKLABLE)) is PICKLABLE

      class Cls:
          PICKLABLE = sentinel("Cls.PICKLABLE")

      assert pickle.loads(pickle.dumps(Cls.PICKLABLE)) is Cls.PICKLABLE

   Sentinel objects have the following attributes:

   .. attribute:: __name__

      The sentinel's name.

   .. attribute:: __module__

      The name of the module where the sentinel was created. This attribute is writable.

   .. versionadded:: 3.15



----

.. class:: type(object, /)
           type(name, bases, dict, /, **kwargs)

   .. index:: pair: object; type

   With one argument, return the type of an *object*.  The return value is a
   type object and generally the same object as returned by
   :attr:`object.__class__`.

   The :func:`isinstance` built-in function is recommended for testing the type
   of an object, because it takes subclasses into account.

   With three arguments, return a new type object.  This is essentially a
   dynamic form of the :keyword:`class` statement. The *name* string is
   the class name and becomes the :attr:`~type.__name__` attribute.
   The *bases* tuple contains the base classes and becomes the
   :attr:`~type.__bases__` attribute; if empty, :class:`object`, the
   ultimate base of all classes, is added.  The *dict* dictionary contains
   attribute and method definitions for the class body; it may be copied
   or wrapped before becoming the :attr:`~type.__dict__` attribute.
   The following two statements create identical :class:`!type` objects:

      >>> class X:
      ...     a = 1
      ...
      >>> X = type('X', (), dict(a=1))

   See also:

   * :ref:`Documentation on attributes and methods on classes <class-attrs-and-methods>`.
   * :ref:`bltin-type-objects`

   Keyword arguments provided to the three argument form are passed to the
   appropriate metaclass machinery (usually :meth:`~object.__init_subclass__`)
   in the same way that keywords in a class
   definition (besides *metaclass*) would.

   Unlike a :keyword:`class` statement, the three argument form does not
   call the metaclass ``__prepare__`` method (see :ref:`prepare`).  Use
   :func:`types.new_class` to dynamically create a class using the
   appropriate metaclass.

   See also :ref:`class-customization`.

   .. versionchanged:: 3.6
      Subclasses of :class:`!type` which don't override ``type.__new__`` may no
      longer use the one-argument form to get the type of an object.

   .. versionchanged:: 3.15

      *dict* can now be a :class:`frozendict`.
