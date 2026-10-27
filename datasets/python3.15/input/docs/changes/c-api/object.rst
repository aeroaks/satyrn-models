.. c:function:: void PyObject_Dump(PyObject *op)

   Dump an object *op* to ``stderr``. This should only be used for debugging.

   The output is intended to try dumping objects even after memory corruption:

   * Information is written starting with fields that are the least likely to
     crash when accessed.
   * This function can be called without an :term:`attached thread state`, but
     it's not recommended to do so: it can cause deadlocks.
   * An object that does not belong to the current interpreter may be dumped,
     but this may also cause crashes or unintended behavior.
   * Implement a heuristic to detect if the object memory has been freed. Don't
     display the object contents in this case, only its memory address.
   * The output format may change at any time.

   Example of output:

   .. code-block:: output

       object address  : 0x7f80124702c0
       object refcount : 2
       object type     : 0x9902e0
       object type name: str
       object repr     : 'abcdef'

   .. versionadded:: 3.15



----

.. c:function:: int PyObject_SetAttr(PyObject *o, PyObject *attr_name, PyObject *v)

   Set the value of the attribute named *attr_name*, for object *o*, to the value
   *v*. Raise an exception and return ``-1`` on failure;
   return ``0`` on success.  This is the equivalent of the Python statement
   ``o.attr_name = v``.

   If *v* is ``NULL``, the attribute is deleted. This behaviour is deprecated
   in favour of using :c:func:`PyObject_DelAttr`, but there are currently no
   plans to remove it.

   The function must not be called with a ``NULL`` *v* and an exception set.
   This case can arise from forgetting ``NULL`` checks and would delete the
   attribute.

   .. versionchanged:: 3.15
      Must not be called with NULL value if an exception is set.



----

.. c:function:: int PyObject_SetAttrString(PyObject *o, const char *attr_name, PyObject *v)

   This is the same as :c:func:`PyObject_SetAttr`, but *attr_name* is
   specified as a :c:expr:`const char*` UTF-8 encoded bytes string,
   rather than a :c:expr:`PyObject*`.

   If *v* is ``NULL``, the attribute is deleted, but this feature is
   deprecated in favour of using :c:func:`PyObject_DelAttrString`.

   The function must not be called with a ``NULL`` *v* and an exception set.
   This case can arise from forgetting ``NULL`` checks and would delete the
   attribute.

   The number of different attribute names passed to this function
   should be kept small, usually by using a statically allocated string
   as *attr_name*.
   For attribute names that aren't known at compile time, prefer calling
   :c:func:`PyUnicode_FromString` and :c:func:`PyObject_SetAttr` directly.
   For more details, see :c:func:`PyUnicode_InternFromString`, which may be
   used internally to create a key object.

   .. versionchanged:: 3.15
      Must not be called with NULL value if an exception is set.



----

.. c:function:: int PyUnstable_SetImmortal(PyObject *op)

   Marks the object *op* :term:`immortal`. The argument should be uniquely referenced by
   the calling thread. This is intended to be used for reducing reference counting contention
   in the :term:`free-threaded build` for objects which are shared across threads.

   This is a one-way process: objects can only be made immortal; they cannot be
   made mortal once again. Immortal objects do not participate in reference counting
   and will never be garbage collected. If the object is GC-tracked, it is untracked.

   This function is intended to be used soon after *op* is created, by the code that
   creates it, such as in the object's :c:member:`~PyTypeObject.tp_new` slot.
   Returns 1 if the object was made immortal and returns 0 if it was not.
   This function cannot fail.

   .. versionadded:: 3.15