.. c:function:: PyObject* PyImport_ExecCodeModule(const char *name, PyObject *co)

   .. index:: pair: built-in function; compile

   Given a module name (possibly of the form ``package.module``) and a code object
   read from a Python bytecode file or obtained from the built-in function
   :func:`compile`, load the module.  Return a new reference to the module object,
   or ``NULL`` with an exception set if an error occurred.  *name*
   is removed from :data:`sys.modules` in error cases, even if *name* was already
   in :data:`sys.modules` on entry to :c:func:`PyImport_ExecCodeModule`.  Leaving
   incompletely initialized modules in :data:`sys.modules` is dangerous, as imports of
   such modules have no way to know that the module object is an unknown (and
   probably damaged with respect to the module author's intents) state.

   The module's :attr:`~module.__spec__` and :attr:`~module.__loader__` will be
   set, if not set already, with the appropriate values.  The spec's loader
   will be set to the module's :attr:`!__loader__` (if set) and to an instance
   of :class:`~importlib.machinery.SourceFileLoader` otherwise.

   The module's :attr:`~module.__file__` attribute will be set to the code
   object's :attr:`~codeobject.co_filename`.

   This function will reload the module if it was already imported.  See
   :c:func:`PyImport_ReloadModule` for the intended way to reload a module.

   If *name* points to a dotted name of the form ``package.module``, any package
   structures not already created will still not be created.

   See also :c:func:`PyImport_ExecCodeModuleEx` and
   :c:func:`PyImport_ExecCodeModuleWithPathnames`.

   .. versionchanged:: 3.12
      The setting of ``__cached__`` and :attr:`~module.__loader__`
      is deprecated. See :class:`~importlib.machinery.ModuleSpec` for
      alternatives.

   .. versionchanged:: 3.15
      The ``__cached__`` attribute is no longer set.



----

.. c:function:: PyObject* PyImport_ExecCodeModuleObject(PyObject *name, PyObject *co, PyObject *pathname, PyObject *cpathname)

   Like :c:func:`PyImport_ExecCodeModuleEx`, but the path to any compiled file
   via *cpathname* is used appropriately when non-``NULL``.  Of the three
   functions, this is the preferred one to use.

   .. versionadded:: 3.3

   .. versionchanged:: 3.12
      Setting ``__cached__`` is deprecated. See
      :class:`~importlib.machinery.ModuleSpec` for alternatives.

   .. versionchanged:: 3.15
      The ``__cached__`` attribute no longer set.



----

.. c:function:: PyImport_LazyImportsMode PyImport_GetLazyImportsMode()

   Gets the current lazy imports mode.

   .. versionadded:: 3.15


----

.. c:function:: PyObject* PyImport_GetLazyImportsFilter()

   Return a :term:`strong reference` to the current lazy imports filter,
   or ``NULL`` if none exists. This function always succeeds.

   .. versionadded:: 3.15


----

.. c:function:: int PyImport_SetLazyImportsMode(PyImport_LazyImportsMode mode)

   Sets the current lazy imports mode.

   This function always returns ``0``.

   .. versionadded:: 3.15


----

.. c:function:: int PyImport_SetLazyImportsFilter(PyObject *filter)

   Sets the current lazy imports filter. The *filter* should be a callable that
   will receive ``(importing_module_name, imported_module_name, [fromlist])``
   when an import can potentially be lazy. The ``imported_module_name`` value
   is the resolved module name, so ``lazy from .spam import eggs`` passes
   ``package.spam``. The callable must return ``True`` if the import should be
   lazy and ``False`` otherwise.

   Return ``0`` on success and ``-1`` with an exception set otherwise.

   .. versionadded:: 3.15


----

.. c:type:: PyImport_LazyImportsMode

   Enumeration of possible lazy import modes.

   .. c:enumerator:: PyImport_LAZY_NORMAL

      Respect the ``lazy`` keyword in source code. This is the default mode.

   .. c:enumerator:: PyImport_LAZY_ALL

      Make all imports lazy by default.

   .. versionadded:: 3.15


----

.. c:function:: PyObject* PyImport_CreateModuleFromInitfunc(PyObject *spec, PyObject* (*initfunc)(void))

   This function is a building block that enables embedders to implement
   the :py:meth:`~importlib.abc.Loader.create_module` step of custom
   static extension importers (e.g. of statically-linked extensions).

   *spec* must be a :class:`~importlib.machinery.ModuleSpec` object.

   *initfunc* must be an :ref:`initialization function <extension-pyinit>`,
   the same as for :c:func:`PyImport_AppendInittab`.

   On success, create and return a module object.
   This module will not be initialized; call :c:func:`PyModule_Exec`
   to initialize it.
   (Custom importers should do this in their
   :py:meth:`~importlib.abc.Loader.exec_module` method.)

   On error, return NULL with an exception set.

   For modules using :ref:`legacy single-phase initialization <single-phase-initialization>`,
   most of the import process is done in this function, rather than in
   extra steps that importers typically take after
   :py:meth:`~importlib.abc.Loader.create_module`.
   Specifically:

   - The module is added to :data:`sys.modules` under the *spec*'s
     :py:attr:`~importlib.machinery.ModuleSpec.name` as part of initialization.
   - If a single-phase module was previously imported under the
     same :py:attr:`~importlib.machinery.ModuleSpec.name` by this function
     or as a built-in module (for example, one registered with
     :c:func:`PyImport_AppendInittab`), Python may reuse the previous module's
     contents instead of calling *initfunc* again.
   - The module will be fully initialized by *initfunc*.
     Calling :c:func:`PyModule_Exec` on it will have no effect, though it is
     still recommended, in case the module later switches to
     :ref:`multi-phase initialization <multi-phase-initialization>`.
   - Also, if the *spec*'s :py:attr:`!name` contains dots, this name is used
     for prepending a parent package to the new module's
     :attr:`~module.__name__`.

   .. versionadded:: 3.15