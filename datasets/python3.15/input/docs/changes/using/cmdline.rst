.. option:: -b

   Issue a warning when converting :class:`bytes` or :class:`bytearray` to
   :class:`str` without specifying encoding or comparing :class:`!bytes` or
   :class:`!bytearray` with :class:`!str` or :class:`!bytes` with :class:`int`.
   Issue an error when the option is given twice (:option:`!-bb`).

   .. versionchanged:: 3.5
      Affects also comparisons of :class:`bytes` with :class:`int`.

   .. deprecated:: 3.15

      Deprecate :option:`-b` and :option:`!-bb` command line options
      and schedule them to become no-op in Python 3.17.
      These were primarily helpers for the Python 2 -> 3 transition.
      Starting with Python 3.17, no :exc:`BytesWarning` will be raised
      for these cases; use a type checker instead.



----

.. option:: -W arg

   Warning control. Python's warning machinery by default prints warning
   messages to :data:`sys.stderr`.

   The simplest settings apply a particular action unconditionally to all
   warnings emitted by a process (even those that are otherwise ignored by
   default)::

       -Wdefault  # Warn once per call location
       -Werror    # Convert to exceptions
       -Walways   # Warn every time
       -Wall      # Same as -Walways
       -Wmodule   # Warn once per calling module
       -Wonce     # Warn once per Python process
       -Wignore   # Never warn

   The action names can be abbreviated as desired and the interpreter will
   resolve them to the appropriate action name. For example, ``-Wi`` is the
   same as ``-Wignore``.

   The full form of argument is::

       action:message:category:module:lineno

   Empty fields match all values; trailing empty fields may be omitted. For
   example ``-W ignore::DeprecationWarning`` ignores all DeprecationWarning
   warnings.

   The *action* field is as explained above but only applies to warnings that
   match the remaining fields.

   The *message* field must match the start of the warning message;
   this match is case-insensitive.
   If it starts and ends with a forward slash (``/``), it specifies
   a regular expression, otherwise it specifies a literal string.

   The *category* field matches the warning category
   (ex: ``DeprecationWarning``). This must be a class name; the match test
   whether the actual warning category of the message is a subclass of the
   specified warning category.

   The *module* field matches the (fully qualified) module name; this match is
   case-sensitive.
   If it starts and ends with a forward slash (``/``), it specifies
   a regular expression that the start of the fully qualified module name
   must match, otherwise it specifies a literal string that the fully
   qualified module name must be equal to.

   The *lineno* field matches the line number, where zero matches all line
   numbers and is thus equivalent to an omitted line number.

   Multiple :option:`-W` options can be given; when a warning matches more than
   one option, the action for the last matching option is performed. Invalid
   :option:`-W` options are ignored (though, a warning message is printed about
   invalid options when the first warning is issued).

   Warnings can also be controlled using the :envvar:`PYTHONWARNINGS`
   environment variable and from within a Python program using the
   :mod:`warnings` module. For example, the :func:`warnings.filterwarnings`
   function can be used to use a regular expression on the warning message.

   See :ref:`warning-filter` and :ref:`describing-warning-filters` for more
   details.

   .. versionchanged:: 3.15
      Added regular expression support for *message* and *module*.



----

.. option:: -X

   Reserved for various implementation-specific options.  CPython currently
   defines the following possible values:

   * ``-X faulthandler`` to enable :mod:`faulthandler`.
     See also :envvar:`PYTHONFAULTHANDLER`.

     .. versionadded:: 3.3

   * ``-X showrefcount`` to output the total reference count and number of used
     memory blocks when the program finishes or after each statement in the
     interactive interpreter. This only works on :ref:`debug builds
     <debug-build>`.

     .. versionadded:: 3.4

   * ``-X tracemalloc`` to start tracing Python memory allocations using the
     :mod:`tracemalloc` module. By default, only the most recent frame is
     stored in a traceback of a trace. Use ``-X tracemalloc=NFRAME`` to start
     tracing with a traceback limit of *NFRAME* frames.
     See :func:`tracemalloc.start` and :envvar:`PYTHONTRACEMALLOC`
     for more information.

     .. versionadded:: 3.4

   * ``-X int_max_str_digits`` configures the :ref:`integer string conversion
     length limitation <int_max_str_digits>`.  See also
     :envvar:`PYTHONINTMAXSTRDIGITS`.

     .. versionadded:: 3.11

   * ``-X importtime`` to show how long each import takes. It shows module
     name, cumulative time (including nested imports) and self time (excluding
     nested imports).  Note that its output may be broken in multi-threaded
     application.  Typical usage is ``python -X importtime -c 'import asyncio'``.

     ``-X importtime=2`` enables additional output that indicates when an
     imported module has already been loaded.  In such cases, the string
     ``cached`` will be printed in both time columns.

     See also :envvar:`PYTHONPROFILEIMPORTTIME`.

     .. versionadded:: 3.7

     .. versionchanged:: 3.14

         Added ``-X importtime=2`` to also trace imports of loaded modules,
         and reserved values other than ``1`` and ``2`` for future use.

   * ``-X dev``: enable :ref:`Python Development Mode <devmode>`, introducing
     additional runtime checks that are too expensive to be enabled by
     default.  See also :envvar:`PYTHONDEVMODE`.

     .. versionadded:: 3.7

   * ``-X utf8`` enables the :ref:`Python UTF-8 Mode <utf8-mode>`.
     ``-X utf8=0`` explicitly disables :ref:`Python UTF-8 Mode <utf8-mode>`
     (even when it would otherwise activate automatically).
     See also :envvar:`PYTHONUTF8`.

     .. versionadded:: 3.7

   * ``-X pycache_prefix=PATH`` enables writing ``.pyc`` files to a parallel
     tree rooted at the given directory instead of to the code tree. See also
     :envvar:`PYTHONPYCACHEPREFIX`.

     .. versionadded:: 3.8

   * ``-X warn_default_encoding`` issues a :class:`EncodingWarning` when the
     locale-specific default encoding is used for opening files.
     See also :envvar:`PYTHONWARNDEFAULTENCODING`.

     .. versionadded:: 3.10

   * ``-X no_debug_ranges`` disables the inclusion of the tables mapping extra
     location information (end line, start column offset and end column offset)
     to every instruction in code objects. This is useful when smaller code
     objects and pyc files are desired as well as suppressing the extra visual
     location indicators when the interpreter displays tracebacks. See also
     :envvar:`PYTHONNODEBUGRANGES`.

     .. versionadded:: 3.11

   * ``-X frozen_modules`` determines whether or not frozen modules are
     ignored by the import machinery.  A value of ``on`` means they get
     imported and ``off`` means they are ignored.  The default is ``on``
     if this is an installed Python (the normal case).  If it's under
     development (running from the source tree) then the default is ``off``.
     Note that the :mod:`!importlib_bootstrap` and
     :mod:`!importlib_bootstrap_external` frozen modules are always used, even
     if this flag is set to ``off``. See also :envvar:`PYTHON_FROZEN_MODULES`.

     .. versionadded:: 3.11

   * ``-X perf`` enables support for the Linux ``perf`` profiler.
     When this option is provided, the ``perf`` profiler will be able to
     report Python calls. This option is only available on some platforms and
     will do nothing if is not supported on the current system. The default value
     is "off". See also :envvar:`PYTHONPERFSUPPORT` and :ref:`perf_profiling`.

     .. versionadded:: 3.12

   * ``-X perf_jit`` enables support for the Linux ``perf`` profiler with DWARF
     support. When this option is provided, the ``perf`` profiler will be able
     to report Python calls using DWARF information. This option is only available on
     some platforms and will do nothing if is not supported on the current
     system. The default value is "off". See also :envvar:`PYTHON_PERF_JIT_SUPPORT`
     and :ref:`perf_profiling`.

     .. versionadded:: 3.13

   * ``-X disable-remote-debug`` disables the remote debugging support as described
     in :pep:`768`.  This includes both the functionality to schedule code for
     execution in another process and the functionality to receive code for
     execution in the current process.

     This option is only available on some platforms and will do nothing
     if is not supported on the current system. See also
     :envvar:`PYTHON_DISABLE_REMOTE_DEBUG` and :pep:`768`.

     .. versionadded:: 3.14

   * :samp:`-X cpu_count={n}` overrides :func:`os.cpu_count`,
     :func:`os.process_cpu_count`, and :func:`multiprocessing.cpu_count`.
     *n* must be greater than or equal to 1.
     This option may be useful for users who need to limit CPU resources of a
     container system. See also :envvar:`PYTHON_CPU_COUNT`.
     If *n* is ``default``, nothing is overridden.

     .. versionadded:: 3.13

   * :samp:`-X presite={module}` or :samp:`-X presite={module:func}` specifies
     an entry point that should be executed before the :mod:`site` module is
     executed and before the
     :mod:`__main__` module exists.  Therefore, the imported module isn't
     :mod:`__main__`. This can be used to execute code early during Python
     initialization. Python needs to be :ref:`built in debug mode <debug-build>`
     for this option to exist.  See also :envvar:`PYTHON_PRESITE`.

     .. versionchanged:: 3.15
        Accept also ``module:func`` entry point format.

     .. versionadded:: 3.13

   * :samp:`-X gil={0,1}` forces the GIL to be disabled or enabled,
     respectively. Setting to ``0`` is only available in builds configured with
     :option:`--disable-gil`. See also :envvar:`PYTHON_GIL` and
     :ref:`whatsnew313-free-threaded-cpython`.

     .. versionadded:: 3.13

   * :samp:`-X thread_inherit_context={0,1}` causes :class:`~threading.Thread`
     to, by default, use a copy of context of the caller of
     ``Thread.start()`` when starting.  Otherwise, threads will start
     with an empty context.  If unset, the value of this option defaults
     to ``1`` on free-threaded builds and to ``0`` otherwise.  See also
     :envvar:`PYTHON_THREAD_INHERIT_CONTEXT`.

     .. versionadded:: 3.14

   * :samp:`-X context_aware_warnings={0,1}` causes the
     :class:`warnings.catch_warnings` context manager to use a
     :class:`~contextvars.ContextVar` to store warnings filter state.  If
     unset, the value of this option defaults to ``1`` on free-threaded builds
     and to ``0`` otherwise.  See also :envvar:`PYTHON_CONTEXT_AWARE_WARNINGS`.

     .. versionadded:: 3.14

   * :samp:`-X pathconfig_warnings={0,1}` if true (``1``) then
     :ref:`sys-path-init` is allowed to log warnings into stderr.
     If false (``0``) suppress these warnings. Set to true by default.
     See also :envvar:`PYTHON_PATHCONFIG_WARNINGS`.

     .. versionadded:: 3.15

   * :samp:`-X tlbc={0,1}` enables (1, the default) or disables (0) thread-local
     bytecode in builds configured with :option:`--disable-gil`.  When disabled,
     this also disables the specializing interpreter.  See also
     :envvar:`PYTHON_TLBC`.

     .. versionadded:: 3.14

   * :samp:`-X lazy_imports={all,normal}` controls lazy import behavior.
     ``all`` makes all imports lazy by default, and ``normal`` (the default)
     respects the ``lazy`` keyword in source code.
     See also :envvar:`PYTHON_LAZY_IMPORTS`.

     .. versionadded:: 3.15

   It also allows passing arbitrary values and retrieving them through the
   :data:`sys._xoptions` dictionary.

   .. versionadded:: 3.2

   .. versionchanged:: 3.9
      Removed the ``-X showalloccount`` option.

   .. versionchanged:: 3.10
      Removed the ``-X oldparser`` option.


----

.. envvar:: PYTHONWARNINGS

   This is equivalent to the :option:`-W` option. If set to a comma
   separated string, it is equivalent to specifying :option:`-W` multiple
   times, with filters later in the list taking precedence over those earlier
   in the list.

   The simplest settings apply a particular action unconditionally to all
   warnings emitted by a process (even those that are otherwise ignored by
   default)::

       PYTHONWARNINGS=default  # Warn once per call location
       PYTHONWARNINGS=error    # Convert to exceptions
       PYTHONWARNINGS=always   # Warn every time
       PYTHONWARNINGS=all      # Same as PYTHONWARNINGS=always
       PYTHONWARNINGS=module   # Warn once per calling module
       PYTHONWARNINGS=once     # Warn once per Python process
       PYTHONWARNINGS=ignore   # Never warn

   See :ref:`warning-filter` and :ref:`describing-warning-filters` for more
   details.

   .. versionchanged:: 3.15
      Added regular expression support for *message* and *module*.



----

.. envvar:: PYTHON_PYMALLOC_HUGEPAGES

   If set to a non-zero integer, enable huge page support for
   :ref:`pymalloc <pymalloc>` arenas.  Set to ``0`` or unset to disable.
   Python must be compiled with :option:`--with-pymalloc-hugepages` for this
   variable to have any effect.

   When enabled, arena allocation uses ``MAP_HUGETLB`` (Linux) or
   ``MEM_LARGE_PAGES`` (Windows) with automatic fallback to regular pages if
   huge pages are not available.

   .. warning::

      On Linux, if the huge-page pool is exhausted, page faults — including
      copy-on-write faults triggered by :func:`os.fork` — deliver ``SIGBUS``
      and kill the process.  Only enable this in environments where the
      huge-page pool is properly sized and fork-safety is not a concern.

      On Windows you need a special privilege. See the
      `Windows documentation for large pages
      <https://learn.microsoft.com/windows/win32/memory/large-page-support>`_
      for details. Python will fail on startup if the required privilege
      `SeLockMemoryPrivilege
      <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/lock-pages-in-memory>`_
      is not held by the user.

   .. versionadded:: 3.15



----

.. envvar:: PYTHON_BASIC_COMPLETER

   If this variable is set to any value, PyREPL will use :mod:`rlcompleter` to
   implement tab completion, instead of the default one which uses colors.

   .. versionadded:: 3.15


----

.. envvar:: PYTHON_PATHCONFIG_WARNINGS

   If true (``1``) then :ref:`sys-path-init` is allowed to log warnings into
   stderr. If false (``0``) suppress these warnings. Set to true by default.
   See also :option:`-X pathconfig_warnings<-X>`.

   .. versionadded:: 3.15


----

.. envvar:: PYTHON_LAZY_IMPORTS

   Controls lazy import behavior. Accepts two values: ``all`` makes all
   imports lazy by default, and ``normal`` (the default) respects the
   ``lazy`` keyword in source code.

   See also the :option:`-X lazy_imports <-X>` command-line option.

   .. versionadded:: 3.15


----

.. envvar:: PYTHON_PRESITE

   If this variable is set to a module, that module will be imported
   early in the interpreter lifecycle, before the :mod:`site` module is
   executed, and before the :mod:`__main__` module is created.
   Therefore, the imported module is not treated as :mod:`__main__`.

   This can be used to execute code early during Python initialization.

   To import a submodule, use ``package.module`` as the value, like in
   an import statement.

   See also the :option:`-X presite <-X>` command-line option,
   which takes precedence over this variable.

   Needs Python configured with the :option:`--with-pydebug` build option.

   .. versionchanged:: 3.15
      Accept also ``module:func`` entry point format.

   .. versionadded:: 3.13