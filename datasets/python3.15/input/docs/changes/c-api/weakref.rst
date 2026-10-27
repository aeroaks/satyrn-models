.. c:function:: PyObject **PyObject_GET_WEAKREFS_LISTPTR(PyObject *object)

   Return a pointer to an internal linked list of weak references to *object*.
   *object* must support weak references and must not be ``NULL``.

   This function is intended for internal use only. Do not access or modify
   the weak reference list through the returned pointer.

   .. soft-deprecated:: 3.15.2

