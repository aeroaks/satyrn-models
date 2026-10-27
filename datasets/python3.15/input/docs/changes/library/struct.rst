Format Characters
^^^^^^^^^^^^^^^^^

Format characters have the following meaning; the conversion between C and
Python values should be obvious given their types.  The 'Standard size' column
refers to the size of the packed value in bytes when using standard size; that
is, when the format string starts with one of ``'<'``, ``'>'``, ``'!'`` or
``'='``.  When using native size, the size of the packed value is
platform-dependent.

+--------+--------------------------+--------------------+----------------+------------+
| Format | C Type                   | Python type        | Standard size  | Notes      |
+========+==========================+====================+================+============+
| ``x``  | pad byte                 | no value           |                | \(7)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``c``  | :c:expr:`char`           | bytes of length 1  | 1              |            |
+--------+--------------------------+--------------------+----------------+------------+
| ``b``  | :c:expr:`signed char`    | int                | 1              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``B``  | :c:expr:`unsigned char`  | int                | 1              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``?``  | :c:expr:`_Bool`          | bool               | 1              | \(1)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``h``  | :c:expr:`short`          | int                | 2              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``H``  | :c:expr:`unsigned short` | int                | 2              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``i``  | :c:expr:`int`            | int                | 4              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``I``  | :c:expr:`unsigned int`   | int                | 4              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``l``  | :c:expr:`long`           | int                | 4              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``L``  | :c:expr:`unsigned long`  | int                | 4              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``q``  | :c:expr:`long long`      | int                | 8              | \(2)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``Q``  | :c:expr:`unsigned long   | int                | 8              | \(2)       |
|        | long`                    |                    |                |            |
+--------+--------------------------+--------------------+----------------+------------+
| ``n``  | :c:type:`ssize_t`        | int                |                | \(2), \(3) |
+--------+--------------------------+--------------------+----------------+------------+
| ``N``  | :c:type:`size_t`         | int                |                | \(2), \(3) |
+--------+--------------------------+--------------------+----------------+------------+
| ``e``  | :c:expr:`_Float16`       | float              | 2              | \(4), \(6) |
+--------+--------------------------+--------------------+----------------+------------+
| ``f``  | :c:expr:`float`          | float              | 4              | \(4)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``d``  | :c:expr:`double`         | float              | 8              | \(4)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``Zf`` | :c:expr:`float complex`  | complex            | 8              | \(10)      |
+--------+--------------------------+--------------------+----------------+------------+
| ``Zd`` | :c:expr:`double complex` | complex            | 16             | \(10)      |
+--------+--------------------------+--------------------+----------------+------------+
| ``s``  | :c:expr:`char[]`         | bytes              |                | \(9)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``p``  | :c:expr:`char[]`         | bytes              |                | \(8)       |
+--------+--------------------------+--------------------+----------------+------------+
| ``P``  | :c:expr:`void \*`        | int                |                | \(2), \(5) |
+--------+--------------------------+--------------------+----------------+------------+

.. versionchanged:: 3.3
   Added support for the ``'n'`` and ``'N'`` formats.

.. versionchanged:: 3.6
   Added support for the ``'e'`` format.

.. versionchanged:: 3.14
   Added support for the ``'F'`` and ``'D'`` formats.

.. versionchanged:: 3.15
   Added support for the ``'Zf'`` and ``'Zd'`` formats.
   ``'F'`` and ``'D'`` formats are :term:`soft deprecated`.

.. seealso::

   The :mod:`array` and :ref:`ctypes <ctypes-fundamental-data-types>` modules,
   as well as third-party modules like `numpy <https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__>`__,
   use similar -- but slightly different -- type codes.


Notes:

(1)
   .. index:: single: ? (question mark); in struct format strings

   The ``'?'`` conversion code corresponds to the :c:expr:`_Bool` type
   defined by C standards since C99.  In standard mode, it is
   represented by one byte.

(2)
   When attempting to pack a non-integer using any of the integer conversion
   codes, if the non-integer has a :meth:`~object.__index__` method then that method is
   called to convert the argument to an integer before packing.

   .. versionchanged:: 3.2
      Added use of the :meth:`~object.__index__` method for non-integers.

(3)
   The ``'n'`` and ``'N'`` conversion codes are only available for the native
   size (selected as the default or with the ``'@'`` byte order character).
   For the standard size, you can use whichever of the other integer formats
   fits your application.

(4)
   For the ``'f'``, ``'d'`` and ``'e'`` conversion codes, the packed
   representation uses the IEEE 754 binary32, binary64 or binary16 format (for
   ``'f'``, ``'d'`` or ``'e'`` respectively), regardless of the floating-point
   format used by the platform.

(5)
   The ``'P'`` format character is only available for the native byte ordering
   (selected as the default or with the ``'@'`` byte order character). The byte
   order character ``'='`` chooses to use little- or big-endian ordering based
   on the host system. The struct module does not interpret this as native
   ordering, so the ``'P'`` format is not available.

(6)
   The IEEE 754 binary16 "half precision" type was introduced in the 2008
   revision of the `IEEE 754 standard <ieee 754 standard_>`_. It has a sign
   bit, a 5-bit exponent and 11-bit precision (with 10 bits explicitly stored),
   and can represent numbers between approximately ``6.1e-05`` and ``6.5e+04``
   at full precision. This type is not widely supported by C compilers:
   it's available as :c:expr:`_Float16` type, if the compiler supports the Annex H
   of the C23 standard.  On a
   typical machine, an unsigned short can be used for storage, but not for math
   operations. See the Wikipedia page on the `half-precision floating-point
   format <half precision format_>`_ for more information.

(7)
   When packing, ``'x'`` inserts one NUL byte.

(8)
   The ``'p'`` format character encodes a "Pascal string", meaning a short
   variable-length string stored in a *fixed number of bytes*, given by the count.
   The first byte stored is the length of the string, or 255, whichever is
   smaller.  The bytes of the string follow.  If the byte string passed in to
   :func:`pack` is too long (longer than the count minus 1), only the leading
   ``count-1`` bytes of the string are stored.  If the byte string is shorter than
   ``count-1``, it is padded with null bytes so that exactly count bytes in all
   are used.  Note that for :func:`unpack`, the ``'p'`` format character consumes
   ``count`` bytes, but that the :class:`!bytes` object returned can never contain more than 255
   bytes.
   When packing, arguments of types :class:`bytes` and :class:`bytearray`
   are accepted.

(9)
   For the ``'s'`` format character, the count is interpreted as the length of the
   byte string, not a repeat count like for the other format characters; for example,
   ``'10s'`` means a single 10-byte string mapping to or from a single
   Python byte string, while ``'10c'`` means 10
   separate one byte character elements (e.g., ``cccccccccc``) mapping
   to or from ten different Python byte objects. (See :ref:`struct-examples`
   for a concrete demonstration of the difference.)
   If a count is not given, it defaults to 1.  For packing, the byte string is
   truncated or padded with null bytes as appropriate to make it fit. For
   unpacking, the resulting :class:`!bytes` object always has exactly the specified number
   of bytes.  As a special case, ``'0s'`` means a single, empty byte string (while
   ``'0c'`` means 0 characters).
   When packing, arguments of types :class:`bytes` and :class:`bytearray`
   are accepted.

(10)
   For the ``'Zf'`` and ``'Zd'`` type codes, the packed representation uses
   the IEEE 754 binary32 and binary64 format for components of the complex
   number, regardless of the floating-point format used by the platform.
   Note that complex types are available unconditionally,
   despite complex types being an optional feature in C.
   As specified in the C11 standard, each complex type is represented by a
   two-element C array containing, respectively, the real and imaginary parts.
   The ``'F'`` and ``'D'`` (for ``'Zf'`` and ``'Zd'``, respectively) format
   characters are supported for compatibility.


A format character may be preceded by an integral repeat count.  For example,
the format string ``'4h'`` means exactly the same as ``'hhhh'``.

Whitespace characters between formats are ignored; a count and its format must
not contain whitespace though.

When packing a value ``x`` using one of the integer formats (``'b'``,
``'B'``, ``'h'``, ``'H'``, ``'i'``, ``'I'``, ``'l'``, ``'L'``,
``'q'``, ``'Q'``), if ``x`` is outside the valid range for that format
then :exc:`struct.error` is raised.

.. versionchanged:: 3.1
   Previously, some of the integer formats wrapped out-of-range values and
   raised :exc:`DeprecationWarning` instead of :exc:`struct.error`.

.. index:: single: ? (question mark); in struct format strings

For the ``'?'`` format character, the return value is either :const:`True` or
:const:`False`. When packing, the truth value of the argument object is used.
Either 0 or 1 in the native or standard bool representation will be packed, and
any non-zero value will be ``True`` when unpacking.



.. _struct-examples:
