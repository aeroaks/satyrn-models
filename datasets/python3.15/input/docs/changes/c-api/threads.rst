.. c:function:: PyThreadStateToken *PyThreadState_Ensure(PyInterpreterGuard *guard)

   Ensure that the thread has an attached thread state for the
   interpreter protected by *guard*, and thus can safely invoke that
   interpreter.

   It is OK to call this function if the thread already has an
   attached thread state, as long as there is a subsequent call to
   :c:func:`PyThreadState_Release` that matches this one (meaning that "nested"
   calls to this function are permitted).

   The function's effect (if any) will be reversed by the matching call to
   :c:func:`PyThreadState_Release`.

   On error, this function returns ``NULL`` *without* an exception set.
   Do not call :c:func:`!PyThreadState_Release` in this case.

   On success, this function returns a pointer value that must be passed
   to the matching call to :c:func:`!PyThreadState_Release`.

   The conditions in which this function creates a new :term:`thread state` are
   considered unstable and implementation-dependent. If you need to control the
   exact lifetime of a thread state, consider using :c:func:`PyThreadState_New`.
   However, do not avoid this function solely on the basis that the lifetime
   of the thread state may be inconsistent across versions; changes to this
   function will be done with caution and in a backwards-compatible manner.
   In particular, the saving of thread-local variables and similar state will
   be retained across Python versions.

   .. impl-detail::

      The exact behavior of whether this function creates a new thread state is
      described below, but be aware that this may change in the future.

      First, this function checks if an attached thread state is present.
      If there is, this function then checks if the interpreter of that
      thread state matches the interpreter guarded by *guard*. If that is
      the case, this function simply marks the thread state as being used
      by a ``PyThreadState_Ensure`` call and returns.

      If there is no attached thread state, then this function checks if any
      thread state has been used by the current OS thread. (This is
      returned by :c:func:`PyGILState_GetThisThreadState`.)
      If there was, then this function checks if that thread state's interpreter
      matches *guard*. If it does, it is re-attached and marked as used.

      Otherwise, if both of the above cases fail, a new thread state is created
      for *guard*. It is then attached and marked as owned by ``PyThreadState_Ensure``.

   .. versionadded:: 3.15



----

.. c:function:: PyThreadStateToken *PyThreadState_EnsureFromView(PyInterpreterView *view)

   Get an attached thread state for the interpreter referenced by *view*.

   The behavior and return value are the same as for :c:func:`PyThreadState_Ensure`;
   additionally, if the function succeeds, the interpreter referenced by *view* will
   be implicitly guarded. The guard will be released upon the corresponding
   :c:func:`PyThreadState_Release` call.

   .. versionadded:: 3.15



----

.. c:function:: void PyThreadState_Release(PyThreadStateToken *token)

   Undo a :c:func:`PyThreadState_Ensure` or
   :c:func:`PyThreadState_EnsureFromView` call.

   This must be called exactly once for each successful *Ensure* call, with
   *token* set to that call's return value.

   The state that was attached before the corresponding *Ensure* call
   (if any) will be attached when :c:func:`PyThreadState_Release` returns.

   The exact behavior of whether this function deletes a thread state is
   considered unstable and implementation-dependent.

   .. impl-detail::

      Currently, this function will decrement an internal counter on the
      attached thread state. If this counter ever reaches below zero, this
      function emits a fatal error (via :c:func:`Py_FatalError`).

      If the attached thread state is owned by ``PyThreadState_Ensure``, then the
      attached thread state will be deallocated and deleted upon the internal counter
      reaching zero. Otherwise, nothing happens when the counter reaches zero.

   .. versionadded:: 3.15


----

.. c:function:: PyGILState_STATE PyGILState_Ensure()

   Ensure that the current thread is ready to call the Python C API regardless
   of the current state of Python, or of the :term:`attached thread state`. This may
   be called as many times as desired by a thread as long as each call is
   matched with a call to :c:func:`PyGILState_Release`. In general, other
   thread-related APIs may be used between :c:func:`PyGILState_Ensure` and
   :c:func:`PyGILState_Release` calls as long as the thread state is restored to
   its previous state before the Release().  For example, normal usage of the
   :c:macro:`Py_BEGIN_ALLOW_THREADS` and :c:macro:`Py_END_ALLOW_THREADS` macros is
   acceptable.

   The return value is an opaque "handle" to the :term:`attached thread state` when
   :c:func:`PyGILState_Ensure` was called, and must be passed to
   :c:func:`PyGILState_Release` to ensure Python is left in the same state. Even
   though recursive calls are allowed, these handles *cannot* be shared - each
   unique call to :c:func:`PyGILState_Ensure` must save the handle for its call
   to :c:func:`PyGILState_Release`.

   When the function returns, there will be an :term:`attached thread state`
   and the thread will be able to call arbitrary Python code.

   This function has no way to return an error. As such, errors are either fatal
   (that is, they send ``SIGABRT`` and crash the process; see
   :c:func:`Py_FatalError`), or the thread will be permanently blocked (such as
   during interpreter finalization).

   .. warning::
      Calling this function when the interpreter is finalizing will
      infinitely hang the thread, which may cause deadlocks.
      :ref:`cautions-regarding-runtime-finalization` for more details.

      In addition, this function generally does not work with subinterpreters
      when used from foreign threads, because this function has no way of
      knowing which interpreter created the thread (and as such, will implicitly
      pick the main interpreter).

   .. versionchanged:: 3.14
      Hangs the current thread, rather than terminating it, if called while the
      interpreter is finalizing.

   .. soft-deprecated:: 3.15
      Use :c:func:`PyThreadState_Ensure` or
      :c:func:`PyThreadState_EnsureFromView` instead.



----

.. c:function:: void PyGILState_Release(PyGILState_STATE)

   Release any resources previously acquired.  After this call, Python's state will
   be the same as it was prior to the corresponding :c:func:`PyGILState_Ensure` call
   (but generally this state will be unknown to the caller, hence the use of the
   GIL-state API).

   Every call to :c:func:`PyGILState_Ensure` must be matched by a call to
   :c:func:`PyGILState_Release` on the same thread.

   .. soft-deprecated:: 3.15
      Use :c:func:`PyThreadState_Release` instead.



----

.. c:function:: PyThreadState* PyGILState_GetThisThreadState()

   Get the :term:`thread state` that was most recently :term:`attached
   <attached thread state>` for this thread. (If the most recent thread state
   has been deleted, this returns ``NULL``.)

   If the caller has an attached thread state, it is returned.

   In other terms, this function returns the thread state that will be used by
   :c:func:`PyGILState_Ensure`. If this returns ``NULL``, then
   ``PyGILState_Ensure`` will create a new thread state.

   This function cannot fail.

   .. soft-deprecated:: 3.15
      Use :c:func:`PyThreadState_Get` or :c:func:`PyThreadState_GetUnchecked`
      instead.



----

.. c:function:: int PyGILState_Check()

   Return ``1`` if the current thread has an :term:`attached thread state`
   that matches the thread state returned by
   :c:func:`PyGILState_GetThisThreadState`. If the caller has no attached thread
   state or it otherwise doesn't match, then this returns ``0``.

   If the current Python process has ever created a subinterpreter, this
   function will *always* return ``1``.

   This is mainly a helper/diagnostic function.

   .. versionadded:: 3.4

   .. soft-deprecated:: 3.15
      Use ``PyThreadState_GetUnchecked() != NULL`` instead.



----

.. c:function:: int PyUnstable_ThreadState_SetStackProtection(PyThreadState *tstate, void *stack_start_addr, size_t stack_size)

   Set the stack protection start address and stack protection size
   of a Python thread state.

   On success, return ``0``.
   On failure, set an exception and return ``-1``.

   CPython implements :ref:`recursion control <recursion>` for C code by raising
   :py:exc:`RecursionError` when it notices that the machine execution stack is close
   to overflow. See for example the :c:func:`Py_EnterRecursiveCall` function.
   For this, it needs to know the location of the current thread's stack, which it
   normally gets from the operating system.
   When the stack is changed, for example using context switching techniques like the
   Boost library's ``boost::context``, you must call
   :c:func:`~PyUnstable_ThreadState_SetStackProtection` to inform CPython of the change.

   Call :c:func:`~PyUnstable_ThreadState_SetStackProtection` either before
   or after changing the stack.
   Do not call any other Python C API between the call and the stack
   change.

   See :c:func:`PyUnstable_ThreadState_ResetStackProtection` for undoing this operation.

   .. versionadded:: 3.15



----

.. c:function:: void PyUnstable_ThreadState_ResetStackProtection(PyThreadState *tstate)

   Reset the stack protection start address and stack protection size
   of a Python thread state to the operating system defaults.

   See :c:func:`PyUnstable_ThreadState_SetStackProtection` for an explanation.

   .. versionadded:: 3.15

