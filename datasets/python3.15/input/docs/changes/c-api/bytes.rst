.. c:function:: PyObject* PyBytes_FromStringAndSize(const char *v, Py_ssize_t len)

   Return a new bytes object with a copy of the string *v* as value and length
   *len* on success, and ``NULL`` on failure.  If *v* is ``NULL``, the contents of
   the bytes object are uninitialized.

   .. soft-deprecated:: 3.15
      Use the :c:type:`PyBytesWriter` API instead of
      ``PyBytes_FromStringAndSize(NULL, len)``.



----

.. c:function:: int _PyBytes_Resize(PyObject **bytes, Py_ssize_t newsize)

   Resize a bytes object. *newsize* will be the new length of the bytes object.
   You can think of it as creating a new bytes object and destroying the old
   one, only more efficiently.
   Pass the address of an
   existing bytes object as an lvalue (it may be written into), and the new size
   desired.  On success, *\*bytes* holds the resized bytes object and ``0`` is
   returned; the address in *\*bytes* may differ from its input value.  If the
   reallocation fails, the original bytes object at *\*bytes* is deallocated,
   *\*bytes* is set to ``NULL``, :exc:`MemoryError` is set, and ``-1`` is
   returned.

   .. soft-deprecated:: 3.15
      Use the :c:type:`PyBytesWriter` API instead.



----

PyBytesWriter
-------------

The :c:type:`PyBytesWriter` API can be used to create a Python :class:`bytes`
object.

.. versionadded:: 3.15

.. c:type:: PyBytesWriter

   A bytes writer instance.

   The API is **not thread safe**. To share a writer with multiple threads, a
   critical section or a lock is needed.

   The instance must be destroyed by :c:func:`PyBytesWriter_Finish` on
   success, or :c:func:`PyBytesWriter_Discard` on error.


Create, Finish, Discard
^^^^^^^^^^^^^^^^^^^^^^^

.. c:function:: PyBytesWriter* PyBytesWriter_Create(Py_ssize_t size)

   Create a :c:type:`PyBytesWriter` to write *size* bytes.

   If *size* is greater than zero, allocate *size* bytes, and set the
   writer size to *size*. The caller is responsible to write *size*
   bytes using :c:func:`PyBytesWriter_GetData`.
   This function does not overallocate.

   On error, set an exception and return ``NULL``.

   *size* must be positive or zero.

.. c:function:: PyObject* PyBytesWriter_Finish(PyBytesWriter *writer)

   Finish a :c:type:`PyBytesWriter` created by
   :c:func:`PyBytesWriter_Create`.

   On success, return a Python :class:`bytes` object.
   On error, set an exception and return ``NULL``.

   The writer instance is invalid after the call in any case.
   No API can be called on the writer after :c:func:`PyBytesWriter_Finish`.

.. c:function:: PyObject* PyBytesWriter_FinishWithSize(PyBytesWriter *writer, Py_ssize_t size)

   Similar to :c:func:`PyBytesWriter_Finish`, but resize the writer
   to *size* bytes before creating the :class:`bytes` object.

.. c:function:: PyObject* PyBytesWriter_FinishWithPointer(PyBytesWriter *writer, void *buf)

   Similar to :c:func:`PyBytesWriter_Finish`, but resize the writer
   using *buf* pointer before creating the :class:`bytes` object.

   Set an exception and return ``NULL`` if *buf* pointer is outside the
   internal buffer bounds.

   Function pseudo-code::

       Py_ssize_t size = (char*)buf - (char*)PyBytesWriter_GetData(writer);
       return PyBytesWriter_FinishWithSize(writer, size);

.. c:function:: void PyBytesWriter_Discard(PyBytesWriter *writer)

   Discard a :c:type:`PyBytesWriter` created by :c:func:`PyBytesWriter_Create`.

   Do nothing if *writer* is ``NULL``.

   The writer instance is invalid after the call.
   No API can be called on the writer after :c:func:`PyBytesWriter_Discard`.

High-level API
^^^^^^^^^^^^^^

.. c:function:: int PyBytesWriter_WriteBytes(PyBytesWriter *writer, const void *bytes, Py_ssize_t size)

   Grow the *writer* internal buffer by *size* bytes,
   write *size* bytes of *bytes* at the *writer* end,
   and add *size* to the *writer* size.

   If *size* is equal to ``-1``, call ``strlen(bytes)`` to get the
   string length.

   On success, return ``0``.
   On error, set an exception and return ``-1``.

.. c:function:: int PyBytesWriter_Format(PyBytesWriter *writer, const char *format, ...)

   Similar to :c:func:`PyBytes_FromFormat`, but write the output directly at
   the writer end. Grow the writer internal buffer on demand. Then add the
   written size to the writer size.

   On success, return ``0``.
   On error, set an exception and return ``-1``.


Getters
^^^^^^^

.. c:function:: Py_ssize_t PyBytesWriter_GetSize(PyBytesWriter *writer)

   Get the writer size.

   The function does not invalidate pointers returned by
   :c:func:`PyBytesWriter_GetData`.

   The function cannot fail.

.. c:function:: void* PyBytesWriter_GetData(PyBytesWriter *writer)

   Get the writer data: start of the internal buffer.

   The pointer remains valid until a :c:type:`PyBytesWriter` function other
   than :c:func:`PyBytesWriter_GetData` or :c:func:`PyBytesWriter_GetSize` is
   called on *writer*.

   The function cannot fail.


Low-level API
^^^^^^^^^^^^^

.. c:function:: int PyBytesWriter_Resize(PyBytesWriter *writer, Py_ssize_t size)

   Resize the writer to *size* bytes. It can be used to enlarge or to
   shrink the writer.
   This function typically overallocates to achieve amortized performance when
   resizing multiple times.

   Newly allocated bytes are left uninitialized.

   On success, return ``0``.
   On error, set an exception and return ``-1``.

   *size* must be positive or zero.

.. c:function:: int PyBytesWriter_Grow(PyBytesWriter *writer, Py_ssize_t grow)

   Resize the writer by adding *grow* bytes to the current writer size.
   This function typically overallocates to achieve amortized performance when
   resizing multiple times.

   Newly allocated bytes are left uninitialized.

   On success, return ``0``.
   On error, set an exception and return ``-1``.

   *grow* can be negative to shrink the writer.

.. c:function:: void* PyBytesWriter_GrowAndUpdatePointer(PyBytesWriter *writer, Py_ssize_t size, void *buf)

   Similar to :c:func:`PyBytesWriter_Grow`, but update also the *buf*
   pointer.

   The *buf* pointer is moved if the internal buffer is moved in memory.
   The *buf* relative position within the internal buffer is left
   unchanged.

   On error, set an exception and return ``NULL``.

   *buf* must not be ``NULL``.

   Function pseudo-code::

       Py_ssize_t pos = (char*)buf - (char*)PyBytesWriter_GetData(writer);
       if (PyBytesWriter_Grow(writer, size) < 0) {
           return NULL;
       }
       return (char*)PyBytesWriter_GetData(writer) + pos;


Example creating the string ``b'abc'``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example creating the bytes string ``b"abc"``, with a fixed size of 3 bytes::

    PyObject* create_abc(void)
    {
        PyBytesWriter *writer = PyBytesWriter_Create(3);
        if (writer == NULL) {
            return NULL;
        }

        char *str = PyBytesWriter_GetData(writer);
        memcpy(str, "abc", 3);
        return PyBytesWriter_Finish(writer);
    }

Variant using a pointer to compute the final size::

    PyObject* create_abc_ptr(void)
    {
        PyBytesWriter *writer = PyBytesWriter_Create(3);
        if (writer == NULL) {
            return NULL;
        }

        char *str = PyBytesWriter_GetData(writer);
        memcpy(str, "abc", 3);
        str += 1;
        return PyBytesWriter_FinishWithPointer(writer, str);
    }


Update ``PyBytes_FromStringAndSize()`` code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of code using the soft deprecated
``PyBytes_FromStringAndSize(NULL, size)`` API::

    int copy_bytes(char *dest, const char *src, Py_ssize_t num_bytes)
    {
        ...
    }

    PyObject* create_string(const char *start, Py_ssize_t num_bytes)
    {
        PyObject *result = PyBytes_FromStringAndSize(NULL, num_bytes);
        if (result == NULL) {
            return NULL;
        }
        if (copy_bytes(PyBytes_AS_STRING(result), start, num_bytes) < 0) {
            Py_CLEAR(result);
        }
        return result;
    }

It can now be updated to::

    PyObject* create_string(const char *start, Py_ssize_t num_bytes)
    {
        PyBytesWriter *writer = PyBytesWriter_Create(num_bytes);
        if (writer == NULL) {
            return NULL;
        }
        if (copy_bytes(PyBytesWriter_GetData(writer), start, num_bytes) < 0) {
            PyBytesWriter_Discard(writer);
            return NULL;
        }
        return PyBytesWriter_Finish(writer);
    }


Update ``_PyBytes_Resize()`` code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example of code using the soft deprecated ``_PyBytes_Resize()`` API::

    void create_string(Py_ssize_t size)
    {
        PyObject *bytes = PyBytes_FromStringAndSize(NULL, size);
        if (bytes == NULL) {
            return NULL;
        }
        char *str = PyBytes_AS_STRING(bytes);

        // ... write data into str ...

        if (_PyBytes_Resize(&bytes, (str - PyBytes_AS_STRING(bytes)))) {
            return NULL;
        }
        return bytes;
    }

It can now be updated to::

    void create_string(Py_ssize_t size)
    {
        PyBytesWriter *writer = PyBytesWriter_Create(size);
        if (writer == NULL) {
            return NULL;
        }
        char *str = PyBytesWriter_GetData(writer);

        // ... write data into str ...

        return PyBytesWriter_FinishWithPointer(writer, str);
    }