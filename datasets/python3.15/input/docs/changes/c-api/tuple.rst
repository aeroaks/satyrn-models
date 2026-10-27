.. c:function:: PyObject* PyTuple_FromArray(PyObject *const *array, Py_ssize_t size)

   Create a tuple of *size* items and copy references from *array* to the new
   tuple.

   *array* can be NULL if *size* is ``0``.

   On success, return a new reference.
   On error, set an exception and return ``NULL``.

   .. versionadded:: 3.15

