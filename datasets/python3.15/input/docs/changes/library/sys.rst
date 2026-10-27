.. data:: abi_info

   .. versionadded:: 3.15

   An object containing information about the ABI of the currently running
   Python interpreter.
   It should include information that affect the CPython ABI in ways that
   require a specific build of the interpreter chosen from variants that can
   co-exist on a single machine.
   For example, it does not encode the base OS (Linux or Windows), but does
   include pointer size since some systems support both 32- and 64-bit builds.
   The available entries are the same on all platforms;
   e.g. *pointer_size* is available even on 64-bit-only architectures.

   The following attributes are available:

   .. attribute:: abi_info.pointer_bits

      The width of pointers in bits, as an integer,
      equivalent to ``8 * sizeof(void *)``.
      Usually, this is  ``32`` or ``64``.

   .. attribute:: abi_info.free_threaded

      A Boolean indicating whether the interpreter was built with
      :term:`free threading` support.
      This reflects either the presence of the :option:`--disable-gil`
      :file:`configure` option (on Unix)
      or setting the ``DisableGil`` property (on Windows).

   .. attribute:: abi_info.debug

      A Boolean indicating whether the interpreter was built in
      :ref:`debug mode <debug-build>`.
      This reflects either the presence of the :option:`--with-pydebug`
      :file:`configure` option (on Unix)
      or the ``Debug`` configuration (on Windows).

   .. attribute:: abi_info.byteorder

      A string indicating the native byte order,
      either ``'big'`` or ``'little'``.
      This is the same as the :data:`byteorder` attribute.



----

.. data:: flags

   The :term:`named tuple` *flags* exposes the status of command line
   flags.  Flags should only be accessed only by name and not by index.  The
   attributes are read only.

   .. list-table::

      * - .. attribute:: flags.debug
        - :option:`-d`

      * - .. attribute:: flags.inspect
        - :option:`-i`

      * - .. attribute:: flags.interactive
        - :option:`-i`

      * - .. attribute:: flags.isolated
        - :option:`-I`

      * - .. attribute:: flags.optimize
        - :option:`-O` or :option:`-OO`

      * - .. attribute:: flags.dont_write_bytecode
        - :option:`-B`

      * - .. attribute:: flags.no_user_site
        - :option:`-s`

      * - .. attribute:: flags.no_site
        - :option:`-S`

      * - .. attribute:: flags.ignore_environment
        - :option:`-E`

      * - .. attribute:: flags.verbose
        - :option:`-v`

      * - .. attribute:: flags.bytes_warning
        - :option:`-b`

      * - .. attribute:: flags.quiet
        - :option:`-q`

      * - .. attribute:: flags.hash_randomization
        - :option:`-R`

      * - .. attribute:: flags.dev_mode
        - :option:`-X dev <-X>` (:ref:`Python Development Mode <devmode>`)

      * - .. attribute:: flags.utf8_mode
        - :option:`-X utf8 <-X>`

      * - .. attribute:: flags.safe_path
        - :option:`-P`

      * - .. attribute:: flags.int_max_str_digits
        - :option:`-X int_max_str_digits <-X>`
          (:ref:`integer string conversion length limitation <int_max_str_digits>`)

      * - .. attribute:: flags.warn_default_encoding
        - :option:`-X warn_default_encoding <-X>`

      * - .. attribute:: flags.gil
        - :option:`-X gil <-X>` and :envvar:`PYTHON_GIL`

      * - .. attribute:: flags.thread_inherit_context
        - :option:`-X thread_inherit_context <-X>` and
          :envvar:`PYTHON_THREAD_INHERIT_CONTEXT`

      * - .. attribute:: flags.context_aware_warnings
        - :option:`-X context_aware_warnings <-X>` and
          :envvar:`PYTHON_CONTEXT_AWARE_WARNINGS`

      * - .. attribute:: flags.lazy_imports
        - :option:`-X lazy_imports <-X>` and :envvar:`PYTHON_LAZY_IMPORTS`
          (``1`` for ``all``, ``-1`` otherwise; not changed by
          :func:`set_lazy_imports`)


   .. versionchanged:: 3.2
      Added ``quiet`` attribute for the new :option:`-q` flag.

   .. versionadded:: 3.2.3
      The ``hash_randomization`` attribute.

   .. versionchanged:: 3.3
      Removed obsolete ``division_warning`` attribute.

   .. versionchanged:: 3.4
      Added ``isolated`` attribute for :option:`-I` ``isolated`` flag.

   .. versionchanged:: 3.7
      Added the ``dev_mode`` attribute for the new :ref:`Python Development
      Mode <devmode>` and the ``utf8_mode`` attribute for the new  :option:`-X`
      ``utf8`` flag.

   .. versionchanged:: 3.10
      Added ``warn_default_encoding`` attribute for :option:`-X` ``warn_default_encoding`` flag.

   .. versionchanged:: 3.11
      Added the ``safe_path`` attribute for :option:`-P` option.

   .. versionchanged:: 3.11
      Added the ``int_max_str_digits`` attribute.

   .. versionchanged:: 3.13
      Added the ``gil`` attribute.

   .. versionchanged:: 3.14
      Added the ``thread_inherit_context`` attribute.

   .. versionchanged:: 3.14
      Added the ``context_aware_warnings`` attribute.

   .. versionchanged:: 3.15
      Added the ``lazy_imports`` attribute.



----

.. function:: get_lazy_imports()

   Returns the current lazy imports mode as a string.

   * ``"normal"``: Only imports explicitly marked with the ``lazy`` keyword
     are lazy
   * ``"all"``: All top-level imports are potentially lazy

   See also :func:`set_lazy_imports` and :pep:`810`.

   .. versionadded:: 3.15



----

.. function:: get_lazy_imports_filter()

   Returns the current lazy imports filter function, or ``None`` if no
   filter is set.

   The filter function is called for every potentially lazy import to
   determine whether it should actually be lazy. See
   :func:`set_lazy_imports_filter` for details on the filter function
   signature.

   .. versionadded:: 3.15



----

.. data:: lazy_modules

   A :class:`set` of fully qualified module name strings that have been lazily
   imported in the current interpreter but not yet loaded.
   When a lazily imported module is accessed for the first time, its name is
   typically removed from this set.

   The set may contain some additional strings.
   It is intended for debugging and introspection, and consumers are expected
   to verify each entry's status.

   .. impl-detail::

      Currently, :data:`!lazy_modules` may also contain:

      * names of *attributes* (non-modules), such as ``"pathlib.Path"`` after
        running ``lazy from pathlib import Path``, and
      * names of items than have already been accessed.

      In future versions of Python, these may be removed, and/or additional
      extras may be added.

   See also :func:`set_lazy_imports` and :pep:`810`.

   .. versionadded:: 3.15



----

.. function:: set_lazy_imports(mode)

   Sets the global lazy imports mode. The *mode* parameter must be one of
   the following strings:

   * ``"normal"``: Only imports explicitly marked with the ``lazy`` keyword
     are lazy
   * ``"all"``: All top-level imports become potentially lazy

   This function is intended for advanced users who need to control lazy
   imports across their entire application. Library developers should
   generally not use this function as it affects the runtime execution of
   applications.

   In addition to the mode, lazy imports can be controlled via the filter
   provided by :func:`set_lazy_imports_filter`.

   See also :func:`get_lazy_imports` and :pep:`810`.

   .. versionadded:: 3.15



----

.. function:: set_lazy_imports_filter(filter)

   Sets the lazy imports filter callback. The *filter* parameter must be a
   callable or ``None`` to clear the filter.

   The filter function is called for every potentially lazy import to
   determine whether it should actually be lazy. It should have the following
   signature::

      def filter(importing_module: str, imported_module: str,
                 fromlist: tuple[str, ...] | None) -> bool

   The function is called with three positional arguments:

   * *importing_module* is the name of the module doing the import
   * *imported_module* is the resolved name of the module being imported
     (for example, ``lazy from .spam import eggs`` passes
     ``package.spam``)
   * *fromlist* is the tuple of names being imported (for ``from ... import``
     statements), or ``None`` for regular imports

   The filter should return ``True`` to allow the import to be lazy, or
   ``False`` to force an eager import.

   This is an advanced feature intended for specialized users who need
   fine-grained control over lazy import behavior.

   See also :func:`get_lazy_imports_filter` and :pep:`810`.

   .. versionadded:: 3.15



----

.. function:: unraisablehook(unraisable, /)

   Handle an unraisable exception.

   Called when an exception has occurred but there is no way for Python to
   handle it. For example, when a destructor raises an exception or during
   garbage collection (:func:`gc.collect`).

   The *unraisable* argument has the following attributes:

   * :attr:`!exc_type`: Exception type.
   * :attr:`!exc_value`: Exception value, can be ``None``.
   * :attr:`!exc_traceback`: Exception traceback, can be ``None``.
   * :attr:`!err_msg`: Error message, can be ``None``.
   * :attr:`!object`: Object causing the exception, can be ``None``.

   The default hook formats :attr:`!err_msg` and :attr:`!object` as:
   ``f'{err_msg}: {object!r}'``; use "Exception ignored in" error message
   if :attr:`!err_msg` is ``None``. Similar to the :mod:`traceback` module,
   this adds color to exceptions by default. This can be disabled using
   :ref:`environment variables <using-on-controlling-color>`.

   :func:`sys.unraisablehook` can be overridden to control how unraisable
   exceptions are handled.

   .. versionchanged:: 3.15
      Exceptions are now printed with colorful text.

   .. seealso::

      :func:`excepthook` which handles uncaught exceptions.

   .. warning::

      Storing :attr:`!exc_value` using a custom hook can create a reference cycle.
      It should be cleared explicitly to break the reference cycle when the
      exception is no longer needed.

      Storing :attr:`!object` using a custom hook can resurrect it if it is set to an
      object which is being finalized. Avoid storing :attr:`!object` after the custom
      hook completes to avoid resurrecting objects.

   .. audit-event:: sys.unraisablehook hook,unraisable sys.unraisablehook

      Raise an auditing event ``sys.unraisablehook`` with arguments
      *hook*, *unraisable* when an exception that cannot be handled occurs.
      The *unraisable* object is the same as what will be passed to the hook.
      If no hook has been set, *hook* may be ``None``.

   .. versionadded:: 3.8
