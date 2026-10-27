.. c:function:: int PyErr_CheckSignals()

   .. index::
      pair: module; signal
      single: SIGINT (C macro)
      single: KeyboardInterrupt (built-in exception)

   Handle external interruptions, such as signals or activating a debugger,
   whose processing has been delayed until it is safe
   to run Python code and/or raise exceptions.

   For example, pressing :kbd:`Ctrl-C` causes a terminal to send the
   :py:data:`signal.SIGINT` signal.
   This function executes the corresponding Python signal handler, which,
   by default, raises the :exc:`KeyboardInterrupt` exception.

   :c:func:`!PyErr_CheckSignals` should be called by long-running C code
   frequently enough so that the response appears immediate to humans.

   Handlers invoked by this function currently include:

   - Signal handlers, including Python functions registered using
     the :mod:`signal` module.

     Signal handlers are only run in the main thread of the main interpreter.

     (This is where the function got the name: originally, signals
     were the only way to interrupt the interpreter.)

   - Running the garbage collector, if necessary.

   - Executing a pending :ref:`remote debugger <remote-debugging>` script.

   - Raise the exception set by :c:func:`PyThreadState_SetAsyncExc`.

   If any handler raises an exception, immediately return ``-1`` with that
   exception set.
   Any remaining interruptions are left to be processed on the next
   :c:func:`PyErr_CheckSignals()` invocation, if appropriate.

   If all handlers finish successfully, or there are no handlers to run,
   return ``0``.

   .. versionchanged:: 3.12
      This function may now invoke the garbage collector.

   .. versionchanged:: 3.14
      This function may now execute a remote debugger script, if remote
      debugging is enabled.

   .. versionchanged:: 3.15
      The exception set by :c:func:`PyThreadState_SetAsyncExc` is now raised.



----

.. c:macro:: PyException_HEAD

   This is a macro including the base fields for an
   exception object.

   This was included in Python's C API by mistake and is not designed for use
   in extensions. For creating custom exception objects, use
   :c:func:`PyErr_NewException` or otherwise create a class inheriting from
   :c:data:`PyExc_BaseException`.

   .. soft-deprecated:: 3.15


Exception Objects
=================

.. c:function:: int PyExceptionInstance_Check(PyObject *op)

   Return true if *op* is an instance of :class:`BaseException`, false
   otherwise. This function always succeeds.


.. c:macro:: PyExceptionInstance_Class(op)

   Equivalent to :c:func:`Py_TYPE(op) <Py_TYPE>`.


.. c:function:: PyObject* PyException_GetTraceback(PyObject *ex)

   Return the traceback associated with the exception as a new reference, as
   accessible from Python through the :attr:`~BaseException.__traceback__`
   attribute. If there is no
   traceback associated, this returns ``NULL``.


.. c:function:: int PyException_SetTraceback(PyObject *ex, PyObject *tb)

   Set the traceback associated with the exception to *tb*.  Use ``Py_None`` to
   clear it.


.. c:function:: PyObject* PyException_GetContext(PyObject *ex)

   Return the context (another exception instance during whose handling *ex* was
   raised) associated with the exception as a new reference, as accessible from
   Python through the :attr:`~BaseException.__context__` attribute.
   If there is no context associated, this returns ``NULL``.


.. c:function:: void PyException_SetContext(PyObject *ex, PyObject *ctx)

   Set the context associated with the exception to *ctx*.  Use ``NULL`` to clear
   it.  There is no type check to make sure that *ctx* is an exception instance.
   This ":term:`steals <steal>`" a reference to *ctx*.


.. c:function:: PyObject* PyException_GetCause(PyObject *ex)

   Return the cause (either an exception instance, or ``None``,
   set by ``raise ... from ...``) associated with the exception as a new
   reference, as accessible from Python through the
   :attr:`~BaseException.__cause__` attribute.


.. c:function:: void PyException_SetCause(PyObject *ex, PyObject *cause)

   Set the cause associated with the exception to *cause*.  Use ``NULL`` to clear
   it.  There is no type check to make sure that *cause* is either an exception
   instance or ``None``.
   This ":term:`steals <steal>`" a reference to *cause*.

   The :attr:`~BaseException.__suppress_context__` attribute is implicitly set
   to ``True`` by this function.


.. c:function:: PyObject* PyException_GetArgs(PyObject *ex)

   Return :attr:`~BaseException.args` of exception *ex*.


.. c:function:: void PyException_SetArgs(PyObject *ex, PyObject *args)

   Set :attr:`~BaseException.args` of exception *ex* to *args*.

.. c:function:: PyObject* PyUnstable_Exc_PrepReraiseStar(PyObject *orig, PyObject *excs)

   Implement part of the interpreter's implementation of :keyword:`!except*`.
   *orig* is the original exception that was caught, and *excs* is the list of
   the exceptions that need to be raised. This list contains the unhandled
   part of *orig*, if any, as well as the exceptions that were raised from the
   :keyword:`!except*` clauses (so they have a different traceback from *orig*) and
   those that were reraised (and have the same traceback as *orig*).
   Return the :exc:`ExceptionGroup` that needs to be reraised in the end, or
   ``None`` if there is nothing to reraise.

   .. versionadded:: 3.12

.. _unicodeexceptions:

Unicode Exception Objects
=========================

The following functions are used to create and modify Unicode exceptions from C.

.. c:function:: PyObject* PyUnicodeDecodeError_Create(const char *encoding, const char *object, Py_ssize_t length, Py_ssize_t start, Py_ssize_t end, const char *reason)

   Create a :class:`UnicodeDecodeError` object with the attributes *encoding*,
   *object*, *length*, *start*, *end* and *reason*. *encoding* and *reason* are
   UTF-8 encoded strings.

.. c:function:: PyObject* PyUnicodeDecodeError_GetEncoding(PyObject *exc)
                PyObject* PyUnicodeEncodeError_GetEncoding(PyObject *exc)

   Return the *encoding* attribute of the given exception object.

.. c:function:: PyObject* PyUnicodeDecodeError_GetObject(PyObject *exc)
                PyObject* PyUnicodeEncodeError_GetObject(PyObject *exc)
                PyObject* PyUnicodeTranslateError_GetObject(PyObject *exc)

   Return the *object* attribute of the given exception object.

.. c:function:: int PyUnicodeDecodeError_GetStart(PyObject *exc, Py_ssize_t *start)
                int PyUnicodeEncodeError_GetStart(PyObject *exc, Py_ssize_t *start)
                int PyUnicodeTranslateError_GetStart(PyObject *exc, Py_ssize_t *start)

   Get the *start* attribute of the given exception object and place it into
   *\*start*.  *start* must not be ``NULL``.  Return ``0`` on success, ``-1`` on
   failure.

   If the :attr:`UnicodeError.object` is an empty sequence, the resulting
   *start* is ``0``. Otherwise, it is clipped to ``[0, len(object) - 1]``.

   .. seealso:: :attr:`UnicodeError.start`

.. c:function:: int PyUnicodeDecodeError_SetStart(PyObject *exc, Py_ssize_t start)
                int PyUnicodeEncodeError_SetStart(PyObject *exc, Py_ssize_t start)
                int PyUnicodeTranslateError_SetStart(PyObject *exc, Py_ssize_t start)

   Set the *start* attribute of the given exception object to *start*.
   Return ``0`` on success, ``-1`` on failure.

   .. note::

      While passing a negative *start* does not raise an exception,
      the corresponding getters will not consider it as a relative
      offset.

.. c:function:: int PyUnicodeDecodeError_GetEnd(PyObject *exc, Py_ssize_t *end)
                int PyUnicodeEncodeError_GetEnd(PyObject *exc, Py_ssize_t *end)
                int PyUnicodeTranslateError_GetEnd(PyObject *exc, Py_ssize_t *end)

   Get the *end* attribute of the given exception object and place it into
   *\*end*.  *end* must not be ``NULL``.  Return ``0`` on success, ``-1`` on
   failure.

   If the :attr:`UnicodeError.object` is an empty sequence, the resulting
   *end* is ``0``. Otherwise, it is clipped to ``[1, len(object)]``.

.. c:function:: int PyUnicodeDecodeError_SetEnd(PyObject *exc, Py_ssize_t end)
                int PyUnicodeEncodeError_SetEnd(PyObject *exc, Py_ssize_t end)
                int PyUnicodeTranslateError_SetEnd(PyObject *exc, Py_ssize_t end)

   Set the *end* attribute of the given exception object to *end*.  Return ``0``
   on success, ``-1`` on failure.

   .. seealso:: :attr:`UnicodeError.end`

.. c:function:: PyObject* PyUnicodeDecodeError_GetReason(PyObject *exc)
                PyObject* PyUnicodeEncodeError_GetReason(PyObject *exc)
                PyObject* PyUnicodeTranslateError_GetReason(PyObject *exc)

   Return the *reason* attribute of the given exception object.

.. c:function:: int PyUnicodeDecodeError_SetReason(PyObject *exc, const char *reason)
                int PyUnicodeEncodeError_SetReason(PyObject *exc, const char *reason)
                int PyUnicodeTranslateError_SetReason(PyObject *exc, const char *reason)

   Set the *reason* attribute of the given exception object to *reason*.  Return
   ``0`` on success, ``-1`` on failure.


.. _recursion:

Recursion Control
=================

These two functions provide a way to perform safe recursive calls at the C
level, both in the core and in extension modules.  They are needed if the
recursive code does not necessarily invoke Python code (which tracks its
recursion depth automatically).
They are also not needed for *tp_call* implementations
because the :ref:`call protocol <call>` takes care of recursion handling.

.. c:function:: int Py_EnterRecursiveCall(const char *where)

   Marks a point where a recursive C-level call is about to be performed.

   The function then checks if the stack limit is reached.  If this is the
   case, a :exc:`RecursionError` is set and a nonzero value is returned.
   Otherwise, zero is returned.

   The check is based on the remaining C stack space of the current thread,
   not on a count of calls, so it is unaffected by
   :c:func:`Py_SetRecursionLimit` and :func:`sys.setrecursionlimit`.

   *where* should be a UTF-8 encoded string such as ``" in instance check"`` to
   be concatenated to the :exc:`RecursionError` message caused by the recursion
   depth limit.

   .. seealso::
      The :c:func:`PyUnstable_ThreadState_SetStackProtection` function.

   .. versionchanged:: 3.9
      This function is now also available in the :ref:`limited API <limited-c-api>`.

   .. versionchanged:: 3.14
      The check is based on the remaining C stack space.  Previously, a
      separate counter of C-level calls was used.

.. c:function:: void Py_LeaveRecursiveCall(void)

   Ends a :c:func:`Py_EnterRecursiveCall`.  Must be called once for each
   *successful* invocation of :c:func:`Py_EnterRecursiveCall`.

   .. versionchanged:: 3.9
      This function is now also available in the :ref:`limited API <limited-c-api>`.

Properly implementing :c:member:`~PyTypeObject.tp_repr` for container types requires
special recursion handling.  In addition to protecting the stack,
:c:member:`~PyTypeObject.tp_repr` also needs to track objects to prevent cycles.  The
following two functions facilitate this functionality.  Effectively,
these are the C equivalent to :deco:`reprlib.recursive_repr`.

.. c:function:: int Py_ReprEnter(PyObject *object)

   Called at the beginning of the :c:member:`~PyTypeObject.tp_repr` implementation to
   detect cycles.

   If the object has already been processed, the function returns a
   positive integer.  In that case the :c:member:`~PyTypeObject.tp_repr` implementation
   should return a string object indicating a cycle.  As examples,
   :class:`dict` objects return ``{...}`` and :class:`list` objects
   return ``[...]``.

   The function will return a negative integer if the recursion limit
   is reached.  In that case the :c:member:`~PyTypeObject.tp_repr` implementation should
   typically return ``NULL``.

   Otherwise, the function returns zero and the :c:member:`~PyTypeObject.tp_repr`
   implementation can continue normally.

.. c:function:: void Py_ReprLeave(PyObject *object)

   Ends a :c:func:`Py_ReprEnter`.  Must be called once for each
   invocation of :c:func:`Py_ReprEnter` that returns zero.

.. c:function:: int Py_GetRecursionLimit(void)

   Get the recursion limit for the current interpreter. It can be set with
   :c:func:`Py_SetRecursionLimit`. The recursion limit prevents the
   Python interpreter stack from growing infinitely.

   This function cannot fail, and the caller must hold an
   :term:`attached thread state`.

   .. seealso::
      :py:func:`sys.getrecursionlimit`

.. c:function:: void Py_SetRecursionLimit(int new_limit)

   Set the recursion limit for the current interpreter.

   This function cannot fail, and the caller must hold an
   :term:`attached thread state`.

   .. seealso::
      :py:func:`sys.setrecursionlimit`

.. _standardexceptions:

Exception and warning types
===========================

All standard Python exceptions and warning categories are available as global
variables whose names are ``PyExc_`` followed by the Python exception name.
These have the type :c:expr:`PyObject*`; they are all class objects.

For completeness, here are all the variables:

Exception types
---------------

.. stable-abi-note::

   These pointers are part of the :ref:`Stable ABI <stable>` since the
   version in the *S.ABI* column (or since 3.2 when *S.ABI* is empty).
   Exceptions marked N/A are *not* part of the Stable ABI.

.. omit-stable-abi-notes::

   .. list-table::
      :align: left
      :widths: auto
      :header-rows: 1

      * * C name
        * .. stable-abi-note::

             S.ABI
        * Python name
      * * .. c:var:: PyObject *PyExc_BaseException
        *
        * :exc:`BaseException`
      * * .. c:var:: PyObject *PyExc_BaseExceptionGroup
        * 3.11
        * :exc:`BaseExceptionGroup`
      * * .. c:var:: PyObject *PyExc_Exception
        *
        * :exc:`Exception`
      * * .. c:var:: PyObject *PyExc_ArithmeticError
        *
        * :exc:`ArithmeticError`
      * * .. c:var:: PyObject *PyExc_AssertionError
        *
        * :exc:`AssertionError`
      * * .. c:var:: PyObject *PyExc_AttributeError
        *
        * :exc:`AttributeError`
      * * .. c:var:: PyObject *PyExc_BlockingIOError
        * 3.7
        * :exc:`BlockingIOError`
      * * .. c:var:: PyObject *PyExc_BrokenPipeError
        * 3.7
        * :exc:`BrokenPipeError`
      * * .. c:var:: PyObject *PyExc_BufferError
        *
        * :exc:`BufferError`
      * * .. c:var:: PyObject *PyExc_ChildProcessError
        * 3.7
        * :exc:`ChildProcessError`
      * * .. c:var:: PyObject *PyExc_ConnectionAbortedError
        * 3.7
        * :exc:`ConnectionAbortedError`
      * * .. c:var:: PyObject *PyExc_ConnectionError
        * 3.7
        * :exc:`ConnectionError`
      * * .. c:var:: PyObject *PyExc_ConnectionRefusedError
        * 3.7
        * :exc:`ConnectionRefusedError`
      * * .. c:var:: PyObject *PyExc_ConnectionResetError
        * 3.7
        * :exc:`ConnectionResetError`
      * * .. c:var:: PyObject *PyExc_EOFError
        *
        * :exc:`EOFError`
      * * .. c:var:: PyObject *PyExc_FileExistsError
        * 3.7
        * :exc:`FileExistsError`
      * * .. c:var:: PyObject *PyExc_FileNotFoundError
        * 3.7
        * :exc:`FileNotFoundError`
      * * .. c:var:: PyObject *PyExc_FloatingPointError
        *
        * :exc:`FloatingPointError`
      * * .. c:var:: PyObject *PyExc_GeneratorExit
        *
        * :exc:`GeneratorExit`
      * * .. c:var:: PyObject *PyExc_ImportCycleError
        * N/A
        * :exc:`ImportCycleError`
      * * .. c:var:: PyObject *PyExc_ImportError
        *
        * :exc:`ImportError`
      * * .. c:var:: PyObject *PyExc_IndentationError
        *
        * :exc:`IndentationError`
      * * .. c:var:: PyObject *PyExc_IndexError
        *
        * :exc:`IndexError`
      * * .. c:var:: PyObject *PyExc_InterruptedError
        * 3.7
        * :exc:`InterruptedError`
      * * .. c:var:: PyObject *PyExc_IsADirectoryError
        * 3.7
        * :exc:`IsADirectoryError`
      * * .. c:var:: PyObject *PyExc_KeyError
        *
        * :exc:`KeyError`
      * * .. c:var:: PyObject *PyExc_KeyboardInterrupt
        *
        * :exc:`KeyboardInterrupt`
      * * .. c:var:: PyObject *PyExc_LookupError
        *
        * :exc:`LookupError`
      * * .. c:var:: PyObject *PyExc_MemoryError
        *
        * :exc:`MemoryError`
      * * .. c:var:: PyObject *PyExc_ModuleNotFoundError
        * 3.6
        * :exc:`ModuleNotFoundError`
      * * .. c:var:: PyObject *PyExc_NameError
        *
        * :exc:`NameError`
      * * .. c:var:: PyObject *PyExc_NotADirectoryError
        * 3.7
        * :exc:`NotADirectoryError`
      * * .. c:var:: PyObject *PyExc_NotImplementedError
        *
        * :exc:`NotImplementedError`
      * * .. c:var:: PyObject *PyExc_OSError
        *
        * :exc:`OSError`
      * * .. c:var:: PyObject *PyExc_OverflowError
        *
        * :exc:`OverflowError`
      * * .. c:var:: PyObject *PyExc_PermissionError
        * 3.7
        * :exc:`PermissionError`
      * * .. c:var:: PyObject *PyExc_ProcessLookupError
        * 3.7
        * :exc:`ProcessLookupError`
      * * .. c:var:: PyObject *PyExc_PythonFinalizationError
        *
        * :exc:`PythonFinalizationError`
      * * .. c:var:: PyObject *PyExc_RecursionError
        * 3.7
        * :exc:`RecursionError`
      * * .. c:var:: PyObject *PyExc_ReferenceError
        *
        * :exc:`ReferenceError`
      * * .. c:var:: PyObject *PyExc_RuntimeError
        *
        * :exc:`RuntimeError`
      * * .. c:var:: PyObject *PyExc_StopAsyncIteration
        * 3.7
        * :exc:`StopAsyncIteration`
      * * .. c:var:: PyObject *PyExc_StopIteration
        *
        * :exc:`StopIteration`
      * * .. c:var:: PyObject *PyExc_SyntaxError
        *
        * :exc:`SyntaxError`
      * * .. c:var:: PyObject *PyExc_SystemError
        *
        * :exc:`SystemError`
      * * .. c:var:: PyObject *PyExc_SystemExit
        *
        * :exc:`SystemExit`
      * * .. c:var:: PyObject *PyExc_TabError
        *
        * :exc:`TabError`
      * * .. c:var:: PyObject *PyExc_TimeoutError
        * 3.7
        * :exc:`TimeoutError`
      * * .. c:var:: PyObject *PyExc_TypeError
        *
        * :exc:`TypeError`
      * * .. c:var:: PyObject *PyExc_UnboundLocalError
        *
        * :exc:`UnboundLocalError`
      * * .. c:var:: PyObject *PyExc_UnicodeDecodeError
        *
        * :exc:`UnicodeDecodeError`
      * * .. c:var:: PyObject *PyExc_UnicodeEncodeError
        *
        * :exc:`UnicodeEncodeError`
      * * .. c:var:: PyObject *PyExc_UnicodeError
        *
        * :exc:`UnicodeError`
      * * .. c:var:: PyObject *PyExc_UnicodeTranslateError
        *
        * :exc:`UnicodeTranslateError`
      * * .. c:var:: PyObject *PyExc_ValueError
        *
        * :exc:`ValueError`
      * * .. c:var:: PyObject *PyExc_ZeroDivisionError
        *
        * :exc:`ZeroDivisionError`

.. versionadded:: 3.3
   :c:data:`PyExc_BlockingIOError`, :c:data:`PyExc_BrokenPipeError`,
   :c:data:`PyExc_ChildProcessError`, :c:data:`PyExc_ConnectionError`,
   :c:data:`PyExc_ConnectionAbortedError`, :c:data:`PyExc_ConnectionRefusedError`,
   :c:data:`PyExc_ConnectionResetError`, :c:data:`PyExc_FileExistsError`,
   :c:data:`PyExc_FileNotFoundError`, :c:data:`PyExc_InterruptedError`,
   :c:data:`PyExc_IsADirectoryError`, :c:data:`PyExc_NotADirectoryError`,
   :c:data:`PyExc_PermissionError`, :c:data:`PyExc_ProcessLookupError`
   and :c:data:`PyExc_TimeoutError` were introduced following :pep:`3151`.

.. versionadded:: 3.5
   :c:data:`PyExc_StopAsyncIteration` and :c:data:`PyExc_RecursionError`.

.. versionadded:: 3.6
   :c:data:`PyExc_ModuleNotFoundError`.

.. versionadded:: 3.11
   :c:data:`PyExc_BaseExceptionGroup`.


OSError aliases
---------------

The following are a compatibility aliases to :c:data:`PyExc_OSError`.

.. versionchanged:: 3.3
   These aliases used to be separate exception types.

.. list-table::
   :align: left
   :widths: auto
   :header-rows: 1

   * * C name
     * Python name
     * Notes
   * * .. c:var:: PyObject *PyExc_EnvironmentError
     * :exc:`OSError`
     *
   * * .. c:var:: PyObject *PyExc_IOError
     * :exc:`OSError`
     *
   * * .. c:var:: PyObject *PyExc_WindowsError
     * :exc:`OSError`
     * [win]_

Notes:

.. [win]
   :c:var:`!PyExc_WindowsError` is only defined on Windows; protect code that
   uses this by testing that the preprocessor macro ``MS_WINDOWS`` is defined.


.. _standardwarningcategories:

Warning types
-------------

.. stable-abi-note::

   These pointers are part of the :ref:`Stable ABI <stable>` since the
   version in the *S.ABI* column (or since 3.2 when *S.ABI* is empty).

.. omit-stable-abi-notes::

   .. list-table::
      :align: left
      :widths: auto
      :header-rows: 1

      * * C name
        * .. stable-abi-note::

           S.ABI
        * Python name
      * * .. c:var:: PyObject *PyExc_Warning
        *
        * :exc:`Warning`
      * * .. c:var:: PyObject *PyExc_BytesWarning
        *
        * :exc:`BytesWarning`
      * * .. c:var:: PyObject *PyExc_DeprecationWarning
        *
        * :exc:`DeprecationWarning`
      * * .. c:var:: PyObject *PyExc_EncodingWarning
        * 3.10
        * :exc:`EncodingWarning`
      * * .. c:var:: PyObject *PyExc_FutureWarning
        *
        * :exc:`FutureWarning`
      * * .. c:var:: PyObject *PyExc_ImportWarning
        *
        * :exc:`ImportWarning`
      * * .. c:var:: PyObject *PyExc_PendingDeprecationWarning
        *
        * :exc:`PendingDeprecationWarning`
      * * .. c:var:: PyObject *PyExc_ResourceWarning
        * 3.7
        * :exc:`ResourceWarning`
      * * .. c:var:: PyObject *PyExc_RuntimeWarning
        *
        * :exc:`RuntimeWarning`
      * * .. c:var:: PyObject *PyExc_SyntaxWarning
        *
        * :exc:`SyntaxWarning`
      * * .. c:var:: PyObject *PyExc_UnicodeWarning
        *
        * :exc:`UnicodeWarning`
      * * .. c:var:: PyObject *PyExc_UserWarning
        *
        * :exc:`UserWarning`

.. versionadded:: 3.2
   :c:data:`PyExc_ResourceWarning`.

.. versionadded:: 3.10
   :c:data:`PyExc_EncodingWarning`.


Tracebacks
==========

.. c:var:: PyTypeObject PyTraceBack_Type

   Type object for traceback objects. This is available as
   :class:`types.TracebackType` in the Python layer.


.. c:function:: int PyTraceBack_Check(PyObject *op)

   Return true if *op* is a traceback object, false otherwise. This function
   does not account for subtypes.


.. c:function:: int PyTraceBack_Here(PyFrameObject *f)

   Replace the :attr:`~BaseException.__traceback__` attribute on the current
   exception with a new traceback prepending *f* to the existing chain.

   Calling this function without an exception set is undefined behavior.

   This function returns ``0`` on success, and returns ``-1`` with an
   exception set on failure.


.. c:function:: int PyTraceBack_Print(PyObject *tb, PyObject *f)

   Write the traceback *tb* into the file *f*.

   This function returns ``0`` on success, and returns ``-1`` with an
   exception set on failure.

.. c:function:: const char* PyUnstable_DumpTraceback(int fd, PyThreadState *tstate)

   Write a trace of the Python stack in *tstate* into the file *fd*.  The format
   looks like::

      Traceback (most recent call first):
        File "xxx", line xxx in <xxx>
        File "xxx", line xxx in <xxx>
        ...
        File "xxx", line xxx in <xxx>

   This function is meant to debug situations such as segfaults, fatal errors,
   and similar. The file and function names it outputs are encoded to ASCII with
   backslashreplace and truncated to 500 characters. It writes only the first
   100 frames; further frames are truncated with the line ``...``.

   This function will return ``NULL`` on success, or an error message on error.

   This function is intended for use in crash scenarios such as signal handlers
   for SIGSEGV, where the interpreter may be in an inconsistent state. Given
   that it reads interpreter data structures that may be partially modified, the
   function might produce incomplete output or it may even crash itself.

   The caller does not need to hold an :term:`attached thread state`, nor does
   *tstate* need to be attached.

   .. versionadded:: 3.15

.. c:function:: const char* PyUnstable_DumpTracebackThreads(int fd, PyInterpreterState *interp, PyThreadState *current_tstate, Py_ssize_t max_threads)

   Write the traces of all Python threads in *interp* into the file *fd*.

   If *interp* is ``NULL`` then this function will try to identify the current
   interpreter using thread-specific storage. If it cannot, it will return an
   error.

   If *current_tstate* is not ``NULL`` then it will be used to identify what the
   current thread is in the written output. If it is ``NULL`` then this function
   will identify the current thread using thread-specific storage. It is not an
   error if the function is unable to get the current Python thread state.

   This function will return ``NULL`` on success, or an error message on error.

   This function is meant to debug situations such as segfaults, fatal
   errors, and similar. It calls :c:func:`PyUnstable_DumpTraceback` for each
   thread. It only writes the tracebacks of the first *max_threads* threads,
   further output is truncated with the line ``...``. If *max_threads* is 0, the
   function will use a default value of 100 for the argument.

   This function is intended for use in crash scenarios such as signal handlers
   for SIGSEGV, where the interpreter may be in an inconsistent state. Given
   that it reads interpreter data structures that may be partially modified, the
   function might produce incomplete output or it may even crash itself.

   The caller does not need to hold an :term:`attached thread state`, nor does
   *current_tstate* need to be attached.

   .. warning::
      On the :term:`free-threaded build`, this function is not thread-safe. If
      another thread deletes its :term:`thread state` while this function is being
      called, the process will likely crash.

   .. versionadded:: 3.15

----

.. c:function:: const char* PyUnstable_DumpTraceback(int fd, PyThreadState *tstate)

   Write a trace of the Python stack in *tstate* into the file *fd*.  The format
   looks like::

      Traceback (most recent call first):
        File "xxx", line xxx in <xxx>
        File "xxx", line xxx in <xxx>
        ...
        File "xxx", line xxx in <xxx>

   This function is meant to debug situations such as segfaults, fatal errors,
   and similar. The file and function names it outputs are encoded to ASCII with
   backslashreplace and truncated to 500 characters. It writes only the first
   100 frames; further frames are truncated with the line ``...``.

   This function will return ``NULL`` on success, or an error message on error.

   This function is intended for use in crash scenarios such as signal handlers
   for SIGSEGV, where the interpreter may be in an inconsistent state. Given
   that it reads interpreter data structures that may be partially modified, the
   function might produce incomplete output or it may even crash itself.

   The caller does not need to hold an :term:`attached thread state`, nor does
   *tstate* need to be attached.

   .. versionadded:: 3.15


----

.. c:function:: const char* PyUnstable_DumpTracebackThreads(int fd, PyInterpreterState *interp, PyThreadState *current_tstate, Py_ssize_t max_threads)

   Write the traces of all Python threads in *interp* into the file *fd*.

   If *interp* is ``NULL`` then this function will try to identify the current
   interpreter using thread-specific storage. If it cannot, it will return an
   error.

   If *current_tstate* is not ``NULL`` then it will be used to identify what the
   current thread is in the written output. If it is ``NULL`` then this function
   will identify the current thread using thread-specific storage. It is not an
   error if the function is unable to get the current Python thread state.

   This function will return ``NULL`` on success, or an error message on error.

   This function is meant to debug situations such as segfaults, fatal
   errors, and similar. It calls :c:func:`PyUnstable_DumpTraceback` for each
   thread. It only writes the tracebacks of the first *max_threads* threads,
   further output is truncated with the line ``...``. If *max_threads* is 0, the
   function will use a default value of 100 for the argument.

   This function is intended for use in crash scenarios such as signal handlers
   for SIGSEGV, where the interpreter may be in an inconsistent state. Given
   that it reads interpreter data structures that may be partially modified, the
   function might produce incomplete output or it may even crash itself.

   The caller does not need to hold an :term:`attached thread state`, nor does
   *current_tstate* need to be attached.

   .. warning::
      On the :term:`free-threaded build`, this function is not thread-safe. If
      another thread deletes its :term:`thread state` while this function is being
      called, the process will likely crash.

   .. versionadded:: 3.15