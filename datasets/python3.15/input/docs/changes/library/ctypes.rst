Fundamental data types
^^^^^^^^^^^^^^^^^^^^^^

:mod:`!ctypes` defines a number of primitive C compatible data types:

.. list-table::
   :header-rows: 1

   * - ctypes type
     - C type
     - Python type
     - :py:attr:`~_SimpleCData._type_`
   * - :class:`c_bool`
     - :c:expr:`_Bool`
     - :py:class:`bool`
     - ``'?'``
   * - :class:`c_char`
     - :c:expr:`char`
     - 1-character :py:class:`bytes`
     - ``'c'``
   * - :class:`c_wchar`
     - :c:type:`wchar_t`
     - 1-character :py:class:`str`
     - ``'u'``
   * - :class:`c_byte`
     - :c:expr:`char`
     - :py:class:`int`
     - ``'b'``
   * - :class:`c_ubyte`
     - :c:expr:`unsigned char`
     - :py:class:`int`
     - ``'B'``
   * - :class:`c_short`
     - :c:expr:`short`
     - :py:class:`int`
     - ``'h'``
   * - :class:`c_ushort`
     - :c:expr:`unsigned short`
     - :py:class:`int`
     - ``'H'``
   * - :class:`c_int`
     - :c:expr:`int`
     - :py:class:`int`
     - ``'i'`` \*
   * - :class:`c_int8`
     - :c:type:`int8_t`
     - :py:class:`int`
     - \*
   * - :class:`c_int16`
     - :c:type:`int16_t`
     - :py:class:`int`
     - \*
   * - :class:`c_int32`
     - :c:type:`int32_t`
     - :py:class:`int`
     - \*
   * - :class:`c_int64`
     - :c:type:`int64_t`
     - :py:class:`int`
     - \*
   * - :class:`c_uint`
     - :c:expr:`unsigned int`
     - :py:class:`int`
     - ``'I'`` \*
   * - :class:`c_uint8`
     - :c:type:`uint8_t`
     - :py:class:`int`
     - \*
   * - :class:`c_uint16`
     - :c:type:`uint16_t`
     - :py:class:`int`
     - \*
   * - :class:`c_uint32`
     - :c:type:`uint32_t`
     - :py:class:`int`
     - \*
   * - :class:`c_uint64`
     - :c:type:`uint64_t`
     - :py:class:`int`
     - \*
   * - :class:`c_long`
     - :c:expr:`long`
     - :py:class:`int`
     - ``'l'``
   * - :class:`c_ulong`
     - :c:expr:`unsigned long`
     - :py:class:`int`
     - ``'L'``
   * - :class:`c_longlong`
     - :c:expr:`long long`
     - :py:class:`int`
     - ``'q'`` \*
   * - :class:`c_ulonglong`
     - :c:expr:`unsigned long long`
     - :py:class:`int`
     - ``'Q'`` \*
   * - :class:`c_size_t`
     - :c:type:`size_t`
     - :py:class:`int`
     - \*
   * - :class:`c_ssize_t`
     - :c:type:`Py_ssize_t`
     - :py:class:`int`
     - \*
   * - :class:`c_time_t`
     - :c:type:`time_t`
     - :py:class:`int`
     - \*
   * - :class:`c_float`
     - :c:expr:`float`
     - :py:class:`float`
     - ``'f'``
   * - :class:`c_double`
     - :c:expr:`double`
     - :py:class:`float`
     - ``'d'``
   * - :class:`c_longdouble`
     - :c:expr:`long double`
     - :py:class:`float`
     - ``'g'`` \*
   * - :class:`c_char_p`
     - :c:expr:`char *` (NUL terminated)
     - :py:class:`bytes` or ``None``
     - ``'z'``
   * - :class:`c_wchar_p`
     - :c:expr:`wchar_t *` (NUL terminated)
     - :py:class:`str` or ``None``
     - ``'Z'``
   * - :class:`c_void_p`
     - :c:expr:`void *`
     - :py:class:`int` or ``None``
     - ``'P'``
   * - :class:`py_object`
     - :c:expr:`PyObject *`
     - :py:class:`object`
     - ``'O'``
   * - :ref:`VARIANT_BOOL <ctypes-wintypes>`
     - :c:expr:`short int`
     - :py:class:`bool`
     - ``'v'``

Additionally, if IEC 60559 compatible complex arithmetic (Annex G) is supported
in both C and ``libffi``, the following complex types are available:

.. list-table::
   :header-rows: 1

   * - ctypes type
     - C type
     - Python type
     - :py:attr:`~_SimpleCData._type_`
   * - :class:`c_float_complex`
     - :c:expr:`float complex`
     - :py:class:`complex`
     - ``'Zf'``
   * - :class:`c_double_complex`
     - :c:expr:`double complex`
     - :py:class:`complex`
     - ``'Zd'``
   * - :class:`c_longdouble_complex`
     - :c:expr:`long double complex`
     - :py:class:`complex`
     - ``'Zg'``

.. versionchanged:: 3.15
   The :py:attr:`~_SimpleCData._type_` types ``F``, ``D`` and ``G`` have been
   replaced with ``Zf``, ``Zd`` and ``Zg``.


All these types can be created by calling them with an optional initializer of
the correct type and value::

   >>> c_int()
   c_long(0)
   >>> c_wchar_p("Hello, World")
   c_wchar_p(140018365411392)
   >>> c_ushort(-3)
   c_ushort(65533)
   >>>

The constructors for numeric types will convert input using
:py:meth:`~object.__bool__`,
:py:meth:`~object.__index__` (for ``int``),
:py:meth:`~object.__float__` or :py:meth:`~object.__complex__`.
This means :py:class:`~ctypes.c_bool` accepts any object with a truth value::

   >>> empty_list = []
   >>> c_bool(empty_list)
   c_bool(False)

Since these types are mutable, their value can also be changed afterwards::

   >>> i = c_int(42)
   >>> print(i)
   c_long(42)
   >>> print(i.value)
   42
   >>> i.value = -99
   >>> print(i.value)
   -99
   >>>

Assigning a new value to instances of the pointer types :class:`c_char_p`,
:class:`c_wchar_p`, and :class:`c_void_p` changes the *memory location* they
point to, *not the contents* of the memory block (of course not, because Python
string objects are immutable)::

   >>> s = "Hello, World"
   >>> c_s = c_wchar_p(s)
   >>> print(c_s)
   c_wchar_p(139966785747344)
   >>> print(c_s.value)
   Hello World
   >>> c_s.value = "Hi, there"
   >>> print(c_s)              # the memory location has changed
   c_wchar_p(139966783348904)
   >>> print(c_s.value)
   Hi, there
   >>> print(s)                # first object is unchanged
   Hello, World
   >>>

You should be careful, however, not to pass them to functions expecting pointers
to mutable memory. If you need mutable memory blocks, ctypes has a
:func:`create_string_buffer` function which creates these in various ways.  The
current memory block contents can be accessed (or changed) with the ``raw``
property; if you want to access it as NUL terminated string, use the ``value``
property::

   >>> from ctypes import *
   >>> p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes
   >>> print(sizeof(p), repr(p.raw))
   3 b'\x00\x00\x00'
   >>> p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string
   >>> print(sizeof(p), repr(p.raw))
   6 b'Hello\x00'
   >>> print(repr(p.value))
   b'Hello'
   >>> p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer
   >>> print(sizeof(p), repr(p.raw))
   10 b'Hello\x00\x00\x00\x00\x00'
   >>> p.value = b"Hi"
   >>> print(sizeof(p), repr(p.raw))
   10 b'Hi\x00lo\x00\x00\x00\x00\x00'
   >>>

The :func:`create_string_buffer` function replaces the old :func:`!c_buffer`
function (which is still available as an alias).  To create a mutable memory
block containing unicode characters of the C type :c:type:`wchar_t`, use the
:func:`create_unicode_buffer` function.


.. _ctypes-calling-functions-continued:


----

.. function:: find_library(name)
   :module: ctypes.util

   Try to find a library and return a pathname.

   *name* is the "short" library name without any prefix like ``lib``,
   suffix like ``.so``, ``.dylib`` or version number.
   (This is the form used for the posix linker option :option:`!-l`.)
   The result is in a format suitable for passing to :py:class:`~ctypes.CDLL`.

   If no library can be found, return ``None``.

   The exact functionality is system dependent, and is *not guaranteed*
   to match the behavior of the compiler, linker, and loader used for
   (or by) Python.
   It is recommended to only use this function as a default or fallback,

   .. soft-deprecated:: 3.15

      This function is kept for use in cases where it works, but not expected to
      be updated for additional platforms and configurations.
