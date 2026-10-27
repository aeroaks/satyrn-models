.. c:function:: PyObject *PySys_GetAttr(PyObject *name)

   Get the attribute *name* of the :mod:`sys` module.
   Return a :term:`strong reference`.
   Raise :exc:`RuntimeError` and return ``NULL`` if it does not exist or
   if the :mod:`sys` module cannot be found.

   If the non-existing object should not be treated as a failure, you can use
   :c:func:`PySys_GetOptionalAttr` instead.

   .. versionadded:: 3.15


----

.. c:function:: PyObject *PySys_GetAttrString(const char *name)

   This is the same as :c:func:`PySys_GetAttr`, but *name* is
   specified as a :c:expr:`const char*` UTF-8 encoded bytes string,
   rather than a :c:expr:`PyObject*`.

   If the non-existing object should not be treated as a failure, you can use
   :c:func:`PySys_GetOptionalAttrString` instead.

   .. versionadded:: 3.15


----

.. c:function:: int PySys_GetOptionalAttr(PyObject *name, PyObject **result)

   Variant of :c:func:`PySys_GetAttr` which doesn't raise
   exception if the object does not exist.

   * Set *\*result* to a new :term:`strong reference` to the object and
     return ``1`` if the object exists.
   * Set *\*result* to ``NULL`` and return ``0`` without setting an exception
     if the object does not exist.
   * Set an exception, set *\*result* to ``NULL``, and return ``-1``,
     if an error occurred.

   .. versionadded:: 3.15


----

.. c:function:: int PySys_GetOptionalAttrString(const char *name, PyObject **result)

   This is the same as :c:func:`PySys_GetOptionalAttr`, but *name* is
   specified as a :c:expr:`const char*` UTF-8 encoded bytes string,
   rather than a :c:expr:`PyObject*`.

   .. versionadded:: 3.15
