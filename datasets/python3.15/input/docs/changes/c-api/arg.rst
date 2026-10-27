Numbers
-------

These formats allow representing Python numbers or single characters as C numbers.
Formats that require :class:`int`, :class:`float` or :class:`complex` can
also use the corresponding special methods :meth:`~object.__index__`,
:meth:`~object.__float__` or :meth:`~object.__complex__` to convert
the Python object to the required type.

For signed integer formats, :exc:`OverflowError` is raised if the value
is out of range for the C type.
For unsigned integer formats, the
most significant bits are silently truncated when the receiving field is too
small to receive the value, and :exc:`DeprecationWarning` is emitted when
the value is larger than the maximal value for the C type or less than
the minimal value for the corresponding signed integer type of the same size.

``b`` (:class:`int`) [unsigned char]
   Convert a nonnegative Python integer to an unsigned tiny integer, stored in a C
   :c:expr:`unsigned char`.

``B`` (:class:`int`) [unsigned char]
   Convert a Python integer to a tiny integer without overflow checking, stored in a C
   :c:expr:`unsigned char`.
   Convert a Python integer to a C :c:expr:`unsigned char`.

``h`` (:class:`int`) [short int]
   Convert a Python integer to a C :c:expr:`short int`.

``H`` (:class:`int`) [unsigned short int]
   Convert a Python integer to a C :c:expr:`unsigned short int`.

``i`` (:class:`int`) [int]
   Convert a Python integer to a plain C :c:expr:`int`.

``I`` (:class:`int`) [unsigned int]
   Convert a Python integer to a C :c:expr:`unsigned int`.

``l`` (:class:`int`) [long int]
   Convert a Python integer to a C :c:expr:`long int`.

``k`` (:class:`int`) [unsigned long]
   Convert a Python integer to a C :c:expr:`unsigned long`.

   .. versionchanged:: 3.14
      Use :meth:`~object.__index__` if available.

``L`` (:class:`int`) [long long]
   Convert a Python integer to a C :c:expr:`long long`.

``K`` (:class:`int`) [unsigned long long]
   Convert a Python integer to a C :c:expr:`unsigned long long`.

   .. versionchanged:: 3.14
      Use :meth:`~object.__index__` if available.

``n`` (:class:`int`) [:c:type:`Py_ssize_t`]
   Convert a Python integer to a C :c:type:`Py_ssize_t`.

``c`` (:class:`bytes` or :class:`bytearray` of length 1) [char]
   Convert a Python byte, represented as a :class:`bytes` or
   :class:`bytearray` object of length 1, to a C :c:expr:`char`.

   .. versionchanged:: 3.3
      Allow :class:`bytearray` objects.

``C`` (:class:`str` of length 1) [int]
   Convert a Python character, represented as a :class:`str` object of
   length 1, to a C :c:expr:`int`.

``f`` (:class:`float`) [float]
   Convert a Python floating-point number to a C :c:expr:`float`.

``d`` (:class:`float`) [double]
   Convert a Python floating-point number to a C :c:expr:`double`.

``D`` (:class:`complex`) [Py_complex]
   Convert a Python complex number to a C :c:type:`Py_complex` structure.

.. deprecated:: 3.15

   For unsigned integer formats ``B``, ``H``, ``I``, ``k`` and ``K``,
   :exc:`DeprecationWarning` is emitted when the value is larger than
   the maximal value for the C type or less than the minimal value for
   the corresponding signed integer type of the same size.



----

.. c:function:: int PyArg_ParseArray(PyObject *const *args, Py_ssize_t nargs, const char *format, ...)

   Parse the parameters of a function that takes only array parameters into
   local variables (that is, a function using the :c:macro:`METH_FASTCALL`
   calling convention).
   Returns true on success; on failure, it returns false and raises the
   appropriate exception.

   .. versionadded:: 3.15



----

.. c:function:: int PyArg_ParseArrayAndKeywords(PyObject *const *args, Py_ssize_t nargs, PyObject *kwnames, const char *format, const char * const *kwlist, ...)

   Parse the parameters of a function that takes both array and keyword
   parameters into local variables (that is, a function using the
   :c:macro:`METH_FASTCALL` ``|`` :c:macro:`METH_KEYWORDS` calling convention).
   Returns true on success; on failure, it returns false and raises the
   appropriate exception.

   .. versionadded:: 3.15

