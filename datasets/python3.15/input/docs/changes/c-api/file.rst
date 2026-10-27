.. c:function:: PyObject *PyFile_NewStdPrinter(int fd)

   Use :c:func:`PyFile_FromFd` with defaults (``fd, NULL, "w", -1, NULL, NULL, NULL, 0``) instead.

   .. soft-deprecated:: 3.15



----

.. c:var:: PyTypeObject PyStdPrinter_Type

   Type of file-like objects used internally at Python startup when :py:mod:`io` is
   not yet available.
   Use Python :py:func:`open` or :c:func:`PyFile_FromFd` to create file objects instead.

   .. soft-deprecated:: 3.15



----

.. c:macro:: PY_STDIOTEXTMODE

   The string literal ``"b"``, used to open files in binary mode.
   Exposed for backwards compatibility only.

   .. soft-deprecated:: 3.15.2