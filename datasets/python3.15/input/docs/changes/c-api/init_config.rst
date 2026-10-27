.. c:function:: int PyConfig_Set(const char *name, PyObject *value)

   Set the current runtime value of a configuration option.

   * Raise a :exc:`ValueError` if there is no option *name*.
   * Raise a :exc:`ValueError` if *value* is an invalid value.
   * Raise a :exc:`ValueError` if the option is read-only (cannot be set).
   * Raise a :exc:`TypeError` if *value* has not the proper type.

   The caller must have an :term:`attached thread state`. The function cannot
   be called before Python initialization nor after Python finalization.

   .. audit-event:: cpython.PyConfig_Set name,value c.PyConfig_Set

   .. versionadded:: 3.14

   .. versionchanged:: 3.15
      The function now replaces :data:`sys.flags` (create a new object),
      instead of modifying :data:`sys.flags` in-place.



----

   .. c:member:: int bytes_warning

      If equals to ``1``, issue a warning when comparing :class:`bytes` or
      :class:`bytearray` with :class:`str`, or comparing :class:`bytes` with
      :class:`int`.

      If equal or greater to ``2``, raise a :exc:`BytesWarning` exception in these
      cases.

      Incremented by the :option:`-b` command line option.

      Default: ``0``.

      .. deprecated-removed:: 3.15 3.17

         The :option:`-b` and :option:`!-bb` options will become no-op in 3.17.
         :c:member:`~PyConfig.bytes_warning` member will be removed in 3.17.


----

Python Path Configuration
-------------------------

:c:type:`PyConfig` contains multiple fields for the path configuration:

* Path configuration inputs:

  * :c:member:`PyConfig.home`
  * :c:member:`PyConfig.platlibdir`
  * :c:member:`PyConfig.pathconfig_warnings`
  * :c:member:`PyConfig.program_name`
  * :c:member:`PyConfig.pythonpath_env`
  * current working directory: to get absolute paths
  * ``PATH`` environment variable to get the program full path
    (from :c:member:`PyConfig.program_name`)
  * ``__PYVENV_LAUNCHER__`` environment variable
  * (Windows only) Application paths in the registry under
    "Software\Python\PythonCore\X.Y\PythonPath" of HKEY_CURRENT_USER and
    HKEY_LOCAL_MACHINE (where X.Y is the Python version).

* Path configuration output fields:

  * :c:member:`PyConfig.base_exec_prefix`
  * :c:member:`PyConfig.base_executable`
  * :c:member:`PyConfig.base_prefix`
  * :c:member:`PyConfig.exec_prefix`
  * :c:member:`PyConfig.executable`
  * :c:member:`PyConfig.module_search_paths_set`,
    :c:member:`PyConfig.module_search_paths`
  * :c:member:`PyConfig.prefix`

If at least one "output field" is not set, Python calculates the path
configuration to fill unset fields. If
:c:member:`~PyConfig.module_search_paths_set` is equal to ``0``,
:c:member:`~PyConfig.module_search_paths` is overridden and
:c:member:`~PyConfig.module_search_paths_set` is set to ``1``.

It is possible to completely ignore the function calculating the default
path configuration by setting explicitly all path configuration output
fields listed above. A string is considered as set even if it is non-empty.
``module_search_paths`` is considered as set if
``module_search_paths_set`` is set to ``1``. In this case,
``module_search_paths`` will be used without modification.

Set :c:member:`~PyConfig.pathconfig_warnings` to ``0`` to suppress warnings when
calculating the path configuration (Unix only, Windows does not log any warning).

If :c:member:`~PyConfig.base_prefix` or :c:member:`~PyConfig.base_exec_prefix`
fields are not set, they inherit their value from :c:member:`~PyConfig.prefix`
and :c:member:`~PyConfig.exec_prefix` respectively.

:c:func:`Py_RunMain` and :c:func:`Py_Main` modify :data:`sys.path`:

* If :c:member:`~PyConfig.run_filename` is set and is a directory which contains a
  ``__main__.py`` script, prepend :c:member:`~PyConfig.run_filename` to
  :data:`sys.path`.
* If :c:member:`~PyConfig.isolated` is zero:

  * If :c:member:`~PyConfig.run_module` is set, prepend the current directory
    to :data:`sys.path`. Do nothing if the current directory cannot be read.
  * If :c:member:`~PyConfig.run_filename` is set, prepend the directory of the
    filename to :data:`sys.path`.
  * Otherwise, prepend an empty string to :data:`sys.path`.

If :c:member:`~PyConfig.site_import` is non-zero, :data:`sys.path` can be
modified by the :mod:`site` module. If
:c:member:`~PyConfig.user_site_directory` is non-zero and the user's
site-package directory exists, the :mod:`site` module appends the user's
site-package directory to :data:`sys.path`.

The following configuration files are used by the path configuration:

* ``pyvenv.cfg``
* ``._pth`` file (ex: ``python._pth``)
* ``pybuilddir.txt`` (Unix only)

If a ``._pth`` file is present:

* Set :c:member:`~PyConfig.isolated` to ``1``.
* Set :c:member:`~PyConfig.use_environment` to ``0``.
* Set :c:member:`~PyConfig.site_import` to ``0``.
* Set :c:member:`~PyConfig.user_site_directory` to ``0`` (since 3.15).
* Set :c:member:`~PyConfig.safe_path` to ``1``.

If :c:member:`~PyConfig.home` is not set and a ``pyvenv.cfg`` file is present in
the same directory as :c:member:`~PyConfig.executable`, or its parent,
:c:member:`~PyConfig.prefix` and :c:member:`~PyConfig.exec_prefix` are set that
location. When this happens, :c:member:`~PyConfig.base_prefix` and
:c:member:`~PyConfig.base_exec_prefix` still keep their value, pointing to the
base installation. See :ref:`sys-path-init-virtual-environments` for more
information.

The ``__PYVENV_LAUNCHER__`` environment variable is used to set
:c:member:`PyConfig.base_executable`.

.. versionchanged:: 3.14

   :c:member:`~PyConfig.prefix`, and :c:member:`~PyConfig.exec_prefix`, are now
   set to the ``pyvenv.cfg`` directory. This was previously done by :mod:`site`,
   therefore affected by :option:`-S`.


.. versionchanged:: 3.15

   :c:member:`~PyConfig.user_site_directory` is now set to ``0`` when a
   ``._pth`` file is present.


Py_GetArgcArgv()
================

.. c:function:: void Py_GetArgcArgv(int *argc, wchar_t ***argv)

   Get the original command line arguments, before Python modified them.

   See also :c:member:`PyConfig.orig_argv` member.


Multi-Phase Initialization Private Provisional API
==================================================

This section is a private provisional API introducing multi-phase
initialization, the core feature of :pep:`432`:

* "Core" initialization phase, "bare minimum Python":

  * Builtin types;
  * Builtin exceptions;
  * Builtin and frozen modules;
  * The :mod:`sys` module is only partially initialized
    (ex: :data:`sys.path` doesn't exist yet).

* "Main" initialization phase, Python is fully initialized:

  * Install and configure :mod:`importlib`;
  * Apply the :ref:`Path Configuration <init-path-config>`;
  * Install signal handlers;
  * Finish :mod:`sys` module initialization (ex: create :data:`sys.stdout`
    and :data:`sys.path`);
  * Enable optional features like :mod:`faulthandler` and :mod:`tracemalloc`;
  * Import the :mod:`site` module;
  * etc.

Private provisional API:

.. c:member:: int PyConfig._init_main

   If set to ``0``, :c:func:`Py_InitializeFromConfig` stops at the "Core"
   initialization phase.

.. c:function:: PyStatus _Py_InitializeMain(void)

   Move to the "Main" initialization phase, finish the Python initialization.

No module is imported during the "Core" phase and the ``importlib`` module is
not configured: the :ref:`Path Configuration <init-path-config>` is only
applied during the "Main" phase. It may allow to customize Python in Python to
override or tune the :ref:`Path Configuration <init-path-config>`, maybe
install a custom :data:`sys.meta_path` importer or an import hook, etc.

It may become possible to calculate the :ref:`Path Configuration
<init-path-config>` in Python, after the Core phase and before the Main phase,
which is one of the :pep:`432` motivation.

The "Core" phase is not properly defined: what should be and what should
not be available at this phase is not specified yet. The API is marked
as private and provisional: the API can be modified or even be removed
anytime until a proper public API is designed.

Example running Python code between "Core" and "Main" initialization
phases::

    void init_python(void)
    {
        PyStatus status;

        PyConfig config;
        PyConfig_InitPythonConfig(&config);
        config._init_main = 0;

        /* ... customize 'config' configuration ... */

        status = Py_InitializeFromConfig(&config);
        PyConfig_Clear(&config);
        if (PyStatus_Exception(status)) {
            Py_ExitStatusException(status);
        }

        /* Use sys.stderr because sys.stdout is only created
           by _Py_InitializeMain() */
        int res = PyRun_SimpleString(
            "import sys; "
            "print('Run Python code before _Py_InitializeMain', "
                   "file=sys.stderr)");
        if (res < 0) {
            exit(1);
        }

        /* ... put more configuration code here ... */

        status = _Py_InitializeMain();
        if (PyStatus_Exception(status)) {
            Py_ExitStatusException(status);
        }
    }