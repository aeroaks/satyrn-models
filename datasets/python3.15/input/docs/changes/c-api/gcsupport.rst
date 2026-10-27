.. c:function:: void *PyObject_GetTypeData_DuringGC(PyObject *o, PyTypeObject *cls)
                void *PyObject_GetItemData_DuringGC(PyObject *o)
                void *PyType_GetModuleState_DuringGC(PyTypeObject *type)
                void *PyModule_GetState_DuringGC(PyObject *module)
                int PyModule_GetToken_DuringGC(PyObject *module, void** result)

   See :ref:`duringgc-functions` for common information.

   .. versionadded:: 3.15

   .. seealso::

      :c:func:`PyObject_GetTypeData`,
      :c:func:`PyObject_GetItemData`,
      :c:func:`PyType_GetModuleState`,
      :c:func:`PyModule_GetState`,
      :c:func:`PyModule_GetToken`,
      :c:func:`PyType_GetBaseByToken`


----

.. c:function:: int PyType_GetBaseByToken_DuringGC(PyTypeObject *type, void *tp_token, PyTypeObject **result)

   See :ref:`duringgc-functions` for common information.

   Sets *\*result* to a :term:`borrowed reference` rather than a strong one.
   The reference is valid for the duration
   of the :c:member:`!tp_traverse` handler call.

   .. versionadded:: 3.15

   .. seealso:: :c:func:`PyType_GetBaseByToken`


----

.. c:function:: PyObject* PyType_GetModule_DuringGC(PyTypeObject *type)
                PyObject* PyType_GetModuleByToken_DuringGC(PyTypeObject *type, const void *mod_token)

   See :ref:`duringgc-functions` for common information.

   These functions return a :term:`borrowed reference`, which is
   valid for the duration of the :c:member:`!tp_traverse` handler call.

   .. versionadded:: 3.15

   .. seealso::

      :c:func:`PyType_GetModule`,
      :c:func:`PyType_GetModuleByToken`


Controlling the Garbage Collector State
---------------------------------------

The C-API provides the following functions for controlling
garbage collection runs.

.. c:function:: Py_ssize_t PyGC_Collect(void)

   Perform a full garbage collection, if the garbage collector is enabled.
   (Note that :func:`gc.collect` runs it unconditionally.)

   Returns the number of collected + unreachable objects which cannot
   be collected.
   If the garbage collector is disabled or already collecting,
   returns ``0`` immediately.
   Errors during garbage collection are passed to :data:`sys.unraisablehook`.
   This function does not raise exceptions.


.. c:function:: int PyGC_Enable(void)

   Enable the garbage collector: similar to :func:`gc.enable`.
   Returns the previous state, 0 for disabled and 1 for enabled.

   .. versionadded:: 3.10


.. c:function:: int PyGC_Disable(void)

   Disable the garbage collector: similar to :func:`gc.disable`.
   Returns the previous state, 0 for disabled and 1 for enabled.

   .. versionadded:: 3.10


.. c:function:: int PyGC_IsEnabled(void)

   Query the state of the garbage collector: similar to :func:`gc.isenabled`.
   Returns the current state, 0 for disabled and 1 for enabled.

   .. versionadded:: 3.10


Querying Garbage Collector State
--------------------------------

The C-API provides the following interface for querying information about
the garbage collector.

.. c:function:: void PyUnstable_GC_VisitObjects(gcvisitobjects_t callback, void *arg)

   Run supplied *callback* on all live GC-capable objects. *arg* is passed through to
   all invocations of *callback*.

   .. warning::
      If new objects are (de)allocated by the callback it is undefined if they
      will be visited.

      Garbage collection is disabled during operation. Explicitly running a collection
      in the callback may lead to undefined behaviour e.g. visiting the same objects
      multiple times or not at all.

   .. versionadded:: 3.12

.. c:type:: int (*gcvisitobjects_t)(PyObject *object, void *arg)

   Type of the visitor function to be passed to :c:func:`PyUnstable_GC_VisitObjects`.
   *arg* is the same as the *arg* passed to ``PyUnstable_GC_VisitObjects``.
   Return ``1`` to continue iteration, return ``0`` to stop iteration. Other return
   values are reserved for now so behavior on returning anything else is undefined.

   .. versionadded:: 3.12

