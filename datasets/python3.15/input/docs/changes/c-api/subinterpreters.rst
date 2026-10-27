.. c:function:: void _PyInterpreterState_SetEvalFrameAllowSpecialization(PyInterpreterState *interp, int allow_specialization)

   Enables or disables specialization why a custom frame evaluator is in place.

   If *allow_specialization* is non-zero, the adaptive specializer will
   continue to specialize bytecodes even though a custom eval frame function
   is set. When *allow_specialization* is zero, setting a custom eval frame
   disables specialization. The standard interpreter loop will continue to deopt
   while a frame evaluation API is in place - the frame evaluation function needs
   to handle the specialized opcodes to take advantage of this.

   .. versionadded:: 3.15


----

.. c:function:: int _PyInterpreterState_IsSpecializationEnabled(PyInterpreterState *interp)

   Return non-zero if adaptive specialization is enabled for the interpreter.
   Specialization is enabled when no custom eval frame function is set, or
   when one is set with *allow_specialization* enabled.

   .. versionadded:: 3.15


Low-level APIs
--------------

All of the following functions must be called after :c:func:`Py_Initialize`.

.. versionchanged:: 3.7
   :c:func:`Py_Initialize()` now initializes the :term:`GIL`
   and sets an :term:`attached thread state`.


.. c:function:: PyInterpreterState* PyInterpreterState_New()

   Create a new interpreter state object.  An :term:`attached thread state` is not needed,
   but may optionally exist if it is necessary to serialize calls to this
   function.

   .. audit-event:: cpython.PyInterpreterState_New "" c.PyInterpreterState_New


.. c:function:: void PyInterpreterState_Clear(PyInterpreterState *interp)

   Reset all information in an interpreter state object.  There must be
   an :term:`attached thread state` for the interpreter.

   .. audit-event:: cpython.PyInterpreterState_Clear "" c.PyInterpreterState_Clear


.. c:function:: void PyInterpreterState_Delete(PyInterpreterState *interp)

   Destroy an interpreter state object.  There **should not** be an
   :term:`attached thread state` for the target interpreter. The interpreter
   state must have been reset with a previous call to :c:func:`PyInterpreterState_Clear`.


.. _advanced-debugging:

Advanced debugger support
-------------------------

These functions are only intended to be used by advanced debugging tools.


.. c:function:: PyInterpreterState* PyInterpreterState_Head()

   Return the interpreter state object at the head of the list of all such objects.


.. c:function:: PyInterpreterState* PyInterpreterState_Main()

   Return the main interpreter state object.


.. c:function:: PyInterpreterState* PyInterpreterState_Next(PyInterpreterState *interp)

   Return the next interpreter state object after *interp* from the list of all
   such objects.


.. c:function:: PyThreadState * PyInterpreterState_ThreadHead(PyInterpreterState *interp)

   Return the pointer to the first :c:type:`PyThreadState` object in the list of
   threads associated with the interpreter *interp*.


.. c:function:: PyThreadState* PyThreadState_Next(PyThreadState *tstate)

   Return the next thread state object after *tstate* from the list of all such
   objects belonging to the same :c:type:`PyInterpreterState` object.