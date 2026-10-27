.. staticmethod:: str.maketrans(dict, /)
                  str.maketrans(from, to, remove='', /)

   This static method returns a translation table usable for :meth:`str.translate`.

   If there is only one argument, it must be a dictionary mapping Unicode
   ordinals (integers) or characters (strings of length 1) to Unicode ordinals,
   strings (of arbitrary lengths) or ``None``.  Character keys will then be
   converted to ordinals.

   If there are two arguments, they must be strings of equal length, and in the
   resulting dictionary, each character in *from* will be mapped to the character at
   the same position in *to*.  If there is a third argument, it must be a string,
   whose characters will be mapped to ``None`` in the result.

   .. versionchanged:: 3.15

      *dict* can now be a :class:`frozendict`.



----

   .. method:: take_bytes(n=None, /)

      Remove the first *n* bytes from the bytearray and return them as an immutable
      :class:`bytes`.
      By default (if *n* is ``None``), return all bytes and clear the bytearray.

      If *n* is negative, index from the end and take the first :func:`len`
      plus *n* bytes. If *n* is out of bounds, raise :exc:`IndexError`.

      Taking less than the full length will leave remaining bytes in the
      :class:`bytearray`, which requires a copy. If the remaining bytes should be
      discarded, use :func:`~bytearray.resize` or :keyword:`del` to truncate
      then :func:`~bytearray.take_bytes` without a size.

      .. impl-detail::

         Taking all bytes is a zero-copy operation.

      .. versionadded:: 3.15

         See the :ref:`What's New <whatsnew315-bytearray-take-bytes>` entry for
         common code patterns which can be optimized with
         :meth:`bytearray.take_bytes`.

Since bytearray objects are sequences of integers (akin to a list), for a
bytearray object *b*, ``b[0]`` will be an integer, while ``b[0:1]`` will be
a bytearray object of length 1.  (This contrasts with text strings, where
both indexing and slicing will produce a string of length 1)

The representation of bytearray objects uses the bytes literal format
(``bytearray(b'...')``) since it is often more useful than e.g.
``bytearray([46, 46, 46])``.  You can always convert a bytearray object into
a list of integers using ``list(b)``.

.. seealso::

   For detailed information on thread-safety guarantees for :class:`bytearray`
   objects, see :ref:`thread-safety-bytearray`.


.. _bytes-methods:

Bytes and Bytearray Operations
------------------------------

.. index:: pair: bytes; methods
           pair: bytearray; methods

Both bytes and bytearray objects support the :ref:`common <typesseq-common>`
sequence operations. They interoperate not just with operands of the same
type, but with any :term:`bytes-like object`. Due to this flexibility, they can be
freely mixed in operations without causing errors. However, the return type
of the result may depend on the order of operands.

.. note::

   The methods on bytes and bytearray objects don't accept strings as their
   arguments, just as the methods on strings don't accept bytes as their
   arguments.  For example, you have to write::

      a = "abc"
      b = a.replace("a", "f")

   and::

      a = b"abc"
      b = a.replace(b"a", b"f")

Some bytes and bytearray operations assume the use of ASCII compatible
binary formats, and hence should be avoided when working with arbitrary
binary data. These restrictions are covered below.

.. note::
   Using these ASCII based operations to manipulate binary data that is not
   stored in an ASCII based format may lead to data corruption.

The following methods on bytes and bytearray objects can be used with
arbitrary binary data.

.. method:: bytes.count(sub[, start[, end]])
            bytearray.count(sub[, start[, end]])

   Return the number of non-overlapping occurrences of subsequence *sub* in
   the range [*start*, *end*].  Optional arguments *start* and *end* are
   interpreted as in slice notation.

   The subsequence to search for may be any :term:`bytes-like object` or an
   integer in the range 0 to 255.

   If *sub* is empty, returns the number of empty slices between characters
   which is the length of the bytes object plus one.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.


.. method:: bytes.removeprefix(prefix, /)
            bytearray.removeprefix(prefix, /)

   If the binary data starts with the *prefix* string, return
   ``bytes[len(prefix):]``. Otherwise, return a copy of the original
   binary data::

      >>> b'TestHook'.removeprefix(b'Test')
      b'Hook'
      >>> b'BaseTestCase'.removeprefix(b'Test')
      b'BaseTestCase'

   The *prefix* may be any :term:`bytes-like object`.

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.

   .. versionadded:: 3.9


.. method:: bytes.removesuffix(suffix, /)
            bytearray.removesuffix(suffix, /)

   If the binary data ends with the *suffix* string and that *suffix* is
   not empty, return ``bytes[:-len(suffix)]``.  Otherwise, return a copy of
   the original binary data::

      >>> b'MiscTests'.removesuffix(b'Tests')
      b'Misc'
      >>> b'TmpDirMixin'.removesuffix(b'Tests')
      b'TmpDirMixin'

   The *suffix* may be any :term:`bytes-like object`.

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.

   .. versionadded:: 3.9


.. method:: bytes.decode(encoding="utf-8", errors="strict")
            bytearray.decode(encoding="utf-8", errors="strict")

   Return the bytes decoded to a :class:`str`.

   *encoding* defaults to ``'utf-8'``;
   see :ref:`standard-encodings` for possible values.

   *errors* controls how decoding errors are handled.
   If ``'strict'`` (the default), a :exc:`UnicodeError` exception is raised.
   Other possible values are ``'ignore'``, ``'replace'``,
   and any other name registered via :func:`codecs.register_error`.
   See :ref:`error-handlers` for details.

   For performance reasons, the value of *errors* is not checked for validity
   unless a decoding error actually occurs,
   :ref:`devmode` is enabled or a :ref:`debug build <debug-build>` is used.

   .. note::

      Passing the *encoding* argument to :class:`str` allows decoding any
      :term:`bytes-like object` directly, without needing to make a temporary
      :class:`!bytes` or :class:`!bytearray` object.

   .. versionchanged:: 3.1
      Added support for keyword arguments.

   .. versionchanged:: 3.9
      The value of the *errors* argument is now checked in :ref:`devmode` and
      in :ref:`debug mode <debug-build>`.


.. method:: bytes.endswith(suffix[, start[, end]])
            bytearray.endswith(suffix[, start[, end]])

   Return ``True`` if the binary data ends with the specified *suffix*,
   otherwise return ``False``.  *suffix* can also be a tuple of suffixes to
   look for.  With optional *start*, test beginning at that position.  With
   optional *end*, stop comparing at that position.

   The suffix(es) to search for may be any :term:`bytes-like object`.


.. method:: bytes.find(sub[, start[, end]])
            bytearray.find(sub[, start[, end]])

   Return the lowest index in the data where the subsequence *sub* is found,
   such that *sub* is contained in the slice ``s[start:end]``.  Optional
   arguments *start* and *end* are interpreted as in slice notation.  Return
   ``-1`` if *sub* is not found.

   The subsequence to search for may be any :term:`bytes-like object` or an
   integer in the range 0 to 255.

   .. note::

      The :meth:`~bytes.find` method should be used only if you need to know the
      position of *sub*.  To check if *sub* is a substring or not, use the
      :keyword:`in` operator::

         >>> b'Py' in b'Python'
         True

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.


.. method:: bytes.index(sub[, start[, end]])
            bytearray.index(sub[, start[, end]])

   Like :meth:`~bytes.find`, but raise :exc:`ValueError` when the
   subsequence is not found.

   The subsequence to search for may be any :term:`bytes-like object` or an
   integer in the range 0 to 255.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.


.. method:: bytes.join(iterable, /)
            bytearray.join(iterable, /)

   Return a bytes or bytearray object which is the concatenation of the
   binary data sequences in *iterable*.  A :exc:`TypeError` will be raised
   if there are any values in *iterable* that are not :term:`bytes-like
   objects <bytes-like object>`, including :class:`str` objects.  The
   separator between elements is the contents of the bytes or
   bytearray object providing this method.


.. staticmethod:: bytes.maketrans(from, to, /)
                  bytearray.maketrans(from, to, /)

   This static method returns a translation table usable for
   :meth:`bytes.translate` that will map each character in *from* into the
   character at the same position in *to*; *from* and *to* must both be
   :term:`bytes-like objects <bytes-like object>` and have the same length.

   .. versionadded:: 3.1


.. method:: bytes.partition(sep, /)
            bytearray.partition(sep, /)

   Split the sequence at the first occurrence of *sep*, and return a 3-tuple
   containing the part before the separator, the separator itself or its
   bytearray copy, and the part after the separator.
   If the separator is not found, return a 3-tuple
   containing a copy of the original sequence, followed by two empty bytes or
   bytearray objects.

   The separator to search for may be any :term:`bytes-like object`.


.. method:: bytes.replace(old, new, /, count=-1)
            bytearray.replace(old, new, /, count=-1)

   Return a copy of the sequence with all occurrences of subsequence *old*
   replaced by *new*.  If *count* is given, only the first *count* occurrences
   are replaced.  If *count* is not specified or ``-1``, then all occurrences
   are replaced.

   The subsequence to search for and its replacement may be any
   :term:`bytes-like object`.

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.

   .. versionchanged:: 3.15
      *count* is now supported as a keyword argument.


.. method:: bytes.rfind(sub[, start[, end]])
            bytearray.rfind(sub[, start[, end]])

   Return the highest index in the sequence where the subsequence *sub* is
   found, such that *sub* is contained within ``s[start:end]``.  Optional
   arguments *start* and *end* are interpreted as in slice notation. Return
   ``-1`` on failure.

   The subsequence to search for may be any :term:`bytes-like object` or an
   integer in the range 0 to 255.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.


.. method:: bytes.rindex(sub[, start[, end]])
            bytearray.rindex(sub[, start[, end]])

   Like :meth:`~bytes.rfind` but raises :exc:`ValueError` when the
   subsequence *sub* is not found.

   The subsequence to search for may be any :term:`bytes-like object` or an
   integer in the range 0 to 255.

   .. versionchanged:: 3.3
      Also accept an integer in the range 0 to 255 as the subsequence.


.. method:: bytes.rpartition(sep, /)
            bytearray.rpartition(sep, /)

   Split the sequence at the last occurrence of *sep*, and return a 3-tuple
   containing the part before the separator, the separator itself or its
   bytearray copy, and the part after the separator.
   If the separator is not found, return a 3-tuple
   containing two empty bytes or bytearray objects, followed by a copy of the
   original sequence.

   The separator to search for may be any :term:`bytes-like object`.


.. method:: bytes.startswith(prefix[, start[, end]])
            bytearray.startswith(prefix[, start[, end]])

   Return ``True`` if the binary data starts with the specified *prefix*,
   otherwise return ``False``.  *prefix* can also be a tuple of prefixes to
   look for.  With optional *start*, test beginning at that position.  With
   optional *end*, stop comparing at that position.

   The prefix(es) to search for may be any :term:`bytes-like object`.


.. method:: bytes.translate(table, /, delete=b'')
            bytearray.translate(table, /, delete=b'')

   Return a copy of the bytes or bytearray object where all bytes occurring in
   the optional argument *delete* are removed, and the remaining bytes have
   been mapped through the given translation table, which must be a bytes
   object of length 256.

   You can use the :func:`bytes.maketrans` method to create a translation
   table.

   Set the *table* argument to ``None`` for translations that only delete
   characters::

      >>> b'read this short text'.translate(None, b'aeiou')
      b'rd ths shrt txt'

   .. versionchanged:: 3.6
      *delete* is now supported as a keyword argument.


The following methods on bytes and bytearray objects have default behaviours
that assume the use of ASCII compatible binary formats, but can still be used
with arbitrary binary data by passing appropriate arguments. Note that all of
the bytearray methods in this section do *not* operate in place, and instead
produce new objects.

.. method:: bytes.center(width, fillbyte=b' ', /)
            bytearray.center(width, fillbyte=b' ', /)

   Return a copy of the object centered in a sequence of length *width*.
   Padding is done using the specified *fillbyte* (default is an ASCII
   space). For :class:`bytes` objects, the original sequence is returned if
   *width* is less than or equal to ``len(s)``.

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.


.. method:: bytes.ljust(width, fillbyte=b' ', /)
            bytearray.ljust(width, fillbyte=b' ', /)

   Return a copy of the object left justified in a sequence of length *width*.
   Padding is done using the specified *fillbyte* (default is an ASCII
   space). For :class:`bytes` objects, the original sequence is returned if
   *width* is less than or equal to ``len(s)``.

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.


.. method:: bytes.lstrip(bytes=None, /)
            bytearray.lstrip(bytes=None, /)

   Return a copy of the sequence with specified leading bytes removed.  The
   *bytes* argument is a binary sequence specifying the set of byte values to
   be removed.  If omitted or ``None``, the *bytes* argument defaults
   to removing :meth:`ASCII whitespace <bytes.isspace>`.
   The *bytes* argument is not a prefix;
   rather, all combinations of its values are stripped::

      >>> b'   spacious   '.lstrip()
      b'spacious   '
      >>> b'www.example.com'.lstrip(b'cmowz.')
      b'example.com'

   The binary sequence of byte values to remove may be any
   :term:`bytes-like object`. See :meth:`~bytes.removeprefix` for a method
   that will remove a single prefix string rather than all of a set of
   characters.  For example::

      >>> b'Arthur: three!'.lstrip(b'Arthur: ')
      b'ee!'
      >>> b'Arthur: three!'.removeprefix(b'Arthur: ')
      b'three!'

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.


.. method:: bytes.rjust(width, fillbyte=b' ', /)
            bytearray.rjust(width, fillbyte=b' ', /)

   Return a copy of the object right justified in a sequence of length *width*.
   Padding is done using the specified *fillbyte* (default is an ASCII
   space). For :class:`bytes` objects, the original sequence is returned if
   *width* is less than or equal to ``len(s)``.

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.


.. method:: bytes.rsplit(sep=None, maxsplit=-1)
            bytearray.rsplit(sep=None, maxsplit=-1)

   Split the binary sequence into subsequences of the same type, using *sep*
   as the delimiter string. If *maxsplit* is given, at most *maxsplit* splits
   are done, the *rightmost* ones.  If *sep* is not specified or ``None``,
   any subsequence consisting solely of
   :meth:`ASCII whitespace <bytes.isspace>` is a separator.
   Except for splitting from the right, :meth:`rsplit` behaves like
   :meth:`split` which is described in detail below.


.. method:: bytes.rstrip(bytes=None, /)
            bytearray.rstrip(bytes=None, /)

   Return a copy of the sequence with specified trailing bytes removed.  The
   *bytes* argument is a binary sequence specifying the set of byte values to
   be removed.  If omitted or ``None``, the *bytes* argument defaults to
   removing :meth:`ASCII whitespace <bytes.isspace>`.
   The *bytes* argument is not a suffix; rather,
   all combinations of its values are stripped::

      >>> b'   spacious   '.rstrip()
      b'   spacious'
      >>> b'mississippi'.rstrip(b'ipz')
      b'mississ'

   The binary sequence of byte values to remove may be any
   :term:`bytes-like object`. See :meth:`~bytes.removesuffix` for a method
   that will remove a single suffix string rather than all of a set of
   characters.  For example::

      >>> b'Monty Python'.rstrip(b' Python')
      b'M'
      >>> b'Monty Python'.removesuffix(b' Python')
      b'Monty'

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.


.. method:: bytes.split(sep=None, maxsplit=-1)
            bytearray.split(sep=None, maxsplit=-1)

   Split the binary sequence into subsequences of the same type, using *sep*
   as the delimiter string. If *maxsplit* is given and non-negative, at most
   *maxsplit* splits are done (thus, the list will have at most ``maxsplit+1``
   elements).  If *maxsplit* is not specified or is ``-1``, then there is no
   limit on the number of splits (all possible splits are made).

   If *sep* is given, consecutive delimiters are not grouped together and are
   deemed to delimit empty subsequences (for example, ``b'1,,2'.split(b',')``
   returns ``[b'1', b'', b'2']``).  The *sep* argument may consist of a
   multibyte sequence as a single delimiter. Splitting an empty sequence with
   a specified separator returns ``[b'']`` or ``[bytearray(b'')]`` depending
   on the type of object being split.  The *sep* argument may be any
   :term:`bytes-like object`.

   For example::

      >>> b'1,2,3'.split(b',')
      [b'1', b'2', b'3']
      >>> b'1,2,3'.split(b',', maxsplit=1)
      [b'1', b'2,3']
      >>> b'1,2,,3,'.split(b',')
      [b'1', b'2', b'', b'3', b'']
      >>> b'1<>2<>3<4'.split(b'<>')
      [b'1', b'2', b'3<4']

   If *sep* is not specified or is ``None``, a different splitting algorithm
   is applied: runs of consecutive :meth:`ASCII whitespace <bytes.isspace>`
   are regarded as a single
   separator, and the result will contain no empty strings at the start or
   end if the sequence has leading or trailing whitespace.  Consequently,
   splitting an empty sequence or a sequence consisting solely of ASCII
   whitespace without a specified separator returns ``[]``.

   For example::


      >>> b'1 2 3'.split()
      [b'1', b'2', b'3']
      >>> b'1 2 3'.split(maxsplit=1)
      [b'1', b'2 3']
      >>> b'   1   2   3   '.split()
      [b'1', b'2', b'3']


.. method:: bytes.strip(bytes=None, /)
            bytearray.strip(bytes=None, /)

   Return a copy of the sequence with specified leading and trailing bytes
   removed. The *bytes* argument is a binary sequence specifying the set of
   byte values to be removed.  If omitted or ``None``, the *bytes*
   argument defaults to removing :meth:`ASCII whitespace <bytes.isspace>`.
   The *bytes* argument is
   not a prefix or suffix; rather, all combinations of its values are
   stripped::

      >>> b'   spacious   '.strip()
      b'spacious'
      >>> b'www.example.com'.strip(b'cmowz.')
      b'example'

   The binary sequence of byte values to remove may be any
   :term:`bytes-like object`.

   .. note::

      The bytearray version of this method does *not* operate in place -
      it always produces a new object, even if no changes were made.


The following methods on bytes and bytearray objects assume the use of ASCII
compatible binary formats and should not be applied to arbitrary binary data.
Note that all of the bytearray methods in this section do *not* operate in
place, and instead produce new objects.

.. method:: bytes.capitalize()
            bytearray.capitalize()

   Return a copy of the sequence with each byte interpreted as an ASCII
   character, and the first byte capitalized and the rest lowercased.
   Non-ASCII byte values are passed through unchanged.

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.


.. method:: bytes.expandtabs(tabsize=8)
            bytearray.expandtabs(tabsize=8)

   Return a copy of the sequence where all ASCII tab characters are replaced
   by one or more ASCII spaces, depending on the current column and the given
   tab size.  Tab positions occur every *tabsize* bytes (default is 8,
   giving tab positions at columns 0, 8, 16 and so on).  To expand the
   sequence, the current column is set to zero and the sequence is examined
   byte by byte.  If the byte is an ASCII tab character (``b'\t'``), one or
   more space characters are inserted in the result until the current column
   is equal to the next tab position. (The tab character itself is not
   copied.)  If the current byte is an ASCII newline (``b'\n'``) or
   carriage return (``b'\r'``), it is copied and the current column is reset
   to zero.  Any other byte value is copied unchanged and the current column
   is incremented by one regardless of how the byte value is represented when
   printed::

      >>> b'01\t012\t0123\t01234'.expandtabs()
      b'01      012     0123    01234'
      >>> b'01\t012\t0123\t01234'.expandtabs(4)
      b'01  012 0123    01234'

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.


.. method:: bytes.isalnum()
            bytearray.isalnum()

   Return ``True`` if all bytes in the sequence are alphabetical ASCII characters
   or ASCII decimal digits and the sequence is not empty, ``False`` otherwise.
   Alphabetic ASCII characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'``. ASCII decimal
   digits are those byte values in the sequence ``b'0123456789'``.

   For example::

      >>> b'ABCabc1'.isalnum()
      True
      >>> b'ABC abc1'.isalnum()
      False


.. method:: bytes.isalpha()
            bytearray.isalpha()

   Return ``True`` if all bytes in the sequence are alphabetic ASCII characters
   and the sequence is not empty, ``False`` otherwise.  Alphabetic ASCII
   characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

   For example::

      >>> b'ABCabc'.isalpha()
      True
      >>> b'ABCabc1'.isalpha()
      False


.. method:: bytes.isascii()
            bytearray.isascii()

   Return ``True`` if the sequence is empty or all bytes in the sequence are ASCII,
   ``False`` otherwise.
   ASCII bytes are in the range 0-0x7F.

   .. versionadded:: 3.7


.. method:: bytes.isdigit()
            bytearray.isdigit()

   Return ``True`` if all bytes in the sequence are ASCII decimal digits
   and the sequence is not empty, ``False`` otherwise. ASCII decimal digits are
   those byte values in the sequence ``b'0123456789'``.

   For example::

      >>> b'1234'.isdigit()
      True
      >>> b'1.23'.isdigit()
      False


.. method:: bytes.islower()
            bytearray.islower()

   Return ``True`` if there is at least one lowercase ASCII character
   in the sequence and no uppercase ASCII characters, ``False`` otherwise.

   For example::

      >>> b'hello world'.islower()
      True
      >>> b'Hello world'.islower()
      False

   Lowercase ASCII characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
   are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.


.. method:: bytes.isspace()
            bytearray.isspace()

   Return ``True`` if all bytes in the sequence are ASCII whitespace and the
   sequence is not empty, ``False`` otherwise.  ASCII whitespace characters are
   those byte values in the sequence ``b' \t\n\r\x0b\f'`` (space, tab, newline,
   carriage return, vertical tab, form feed).


.. method:: bytes.istitle()
            bytearray.istitle()

   Return ``True`` if the sequence is ASCII titlecase and the sequence is not
   empty, ``False`` otherwise. See :meth:`bytes.title` for more details on the
   definition of "titlecase".

   For example::

      >>> b'Hello World'.istitle()
      True
      >>> b'Hello world'.istitle()
      False


.. method:: bytes.isupper()
            bytearray.isupper()

   Return ``True`` if there is at least one uppercase alphabetic ASCII character
   in the sequence and no lowercase ASCII characters, ``False`` otherwise.

   For example::

      >>> b'HELLO WORLD'.isupper()
      True
      >>> b'Hello world'.isupper()
      False

   Lowercase ASCII characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
   are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.


.. method:: bytes.lower()
            bytearray.lower()

   Return a copy of the sequence with all the uppercase ASCII characters
   converted to their corresponding lowercase counterpart.

   For example::

      >>> b'Hello World'.lower()
      b'hello world'

   Lowercase ASCII characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
   are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.


.. index::
   single: universal newlines; bytes.splitlines method
   single: universal newlines; bytearray.splitlines method

.. method:: bytes.splitlines(keepends=False)
            bytearray.splitlines(keepends=False)

   Return a list of the lines in the binary sequence, breaking at ASCII
   line boundaries. This method uses the :term:`universal newlines` approach
   to splitting lines. Line breaks are not included in the resulting list
   unless *keepends* is given and true.

   For example::

      >>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
      [b'ab c', b'', b'de fg', b'kl']
      >>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
      [b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']

   Unlike :meth:`~bytes.split` when a delimiter string *sep* is given, this
   method returns an empty list for the empty string, and a terminal line
   break does not result in an extra line::

      >>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
      ([b''], [b'Two lines', b''])
      >>> b"".splitlines(), b"One line\n".splitlines()
      ([], [b'One line'])


.. method:: bytes.swapcase()
            bytearray.swapcase()

   Return a copy of the sequence with all the lowercase ASCII characters
   converted to their corresponding uppercase counterpart and vice-versa.

   For example::

      >>> b'Hello World'.swapcase()
      b'hELLO wORLD'

   Lowercase ASCII characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
   are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

   Unlike :func:`str.swapcase`, it is always the case that
   ``bin.swapcase().swapcase() == bin`` for the binary versions. Case
   conversions are symmetrical in ASCII, even though that is not generally
   true for arbitrary Unicode code points.

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.


.. method:: bytes.title()
            bytearray.title()

   Return a titlecased version of the binary sequence where words start with
   an uppercase ASCII character and the remaining characters are lowercase.
   Uncased byte values are left unmodified.

   For example::

      >>> b'Hello world'.title()
      b'Hello World'

   Lowercase ASCII characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
   are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.
   All other byte values are uncased.

   The algorithm uses a simple language-independent definition of a word as
   groups of consecutive letters.  The definition works in many contexts but
   it means that apostrophes in contractions and possessives form word
   boundaries, which may not be the desired result::

        >>> b"they're bill's friends from the UK".title()
        b"They'Re Bill'S Friends From The Uk"

   A workaround for apostrophes can be constructed using regular expressions::

        >>> import re
        >>> def titlecase(s):
        ...     return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
        ...                   lambda mo: mo.group(0)[0:1].upper() +
        ...                              mo.group(0)[1:].lower(),
        ...                   s)
        ...
        >>> titlecase(b"they're bill's friends.")
        b"They're Bill's Friends."

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.


.. method:: bytes.upper()
            bytearray.upper()

   Return a copy of the sequence with all the lowercase ASCII characters
   converted to their corresponding uppercase counterpart.

   For example::

      >>> b'Hello World'.upper()
      b'HELLO WORLD'

   Lowercase ASCII characters are those byte values in the sequence
   ``b'abcdefghijklmnopqrstuvwxyz'``. Uppercase ASCII characters
   are those byte values in the sequence ``b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'``.

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.


.. method:: bytes.zfill(width, /)
            bytearray.zfill(width, /)

   Return a copy of the sequence left filled with ASCII ``b'0'`` digits to
   make a sequence of length *width*. A leading sign prefix (``b'+'``/
   ``b'-'``) is handled by inserting the padding *after* the sign character
   rather than before. For :class:`bytes` objects, the original sequence is
   returned if *width* is less than or equal to ``len(seq)``.

   For example::

      >>> b"42".zfill(5)
      b'00042'
      >>> b"-42".zfill(5)
      b'-0042'

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.


.. _bytes-formatting:

``printf``-style Bytes Formatting
----------------------------------

.. index::
   single: formatting; bytes (%)
   single: formatting; bytearray (%)
   single: interpolation; bytes (%)
   single: interpolation; bytearray (%)
   single: bytes; formatting
   single: bytearray; formatting
   single: bytes; interpolation
   single: bytearray; interpolation
   single: printf-style formatting
   single: sprintf-style formatting
   single: % (percent); printf-style formatting

.. note::

   The formatting operations described here exhibit a variety of quirks that
   lead to a number of common errors (such as failing to display tuples and
   dictionaries correctly).  If the value being printed may be a tuple or
   dictionary, wrap it in a tuple.

Bytes objects (``bytes``/``bytearray``) have one unique built-in operation:
the ``%`` operator (modulo).
This is also known as the bytes *formatting* or *interpolation* operator.
Given ``format % values`` (where *format* is a bytes object), ``%`` conversion
specifications in *format* are replaced with zero or more elements of *values*.
The effect is similar to using the :c:func:`sprintf` function in the C language.

If *format* requires a single argument, *values* may be a single non-tuple
object. [5]_  Otherwise, *values* must be a tuple with exactly the number of
items specified by the format bytes object, or a single mapping object (for
example, a dictionary).

.. index::
   single: () (parentheses); in printf-style formatting
   single: * (asterisk); in printf-style formatting
   single: . (dot); in printf-style formatting

A conversion specifier contains two or more characters and has the following
components, which must occur in this order:

#. The ``'%'`` character, which marks the start of the specifier.

#. Mapping key (optional), consisting of a parenthesised sequence of characters
   (for example, ``(somename)``).

#. Conversion flags (optional), which affect the result of some conversion
   types.

#. Minimum field width (optional).  If specified as an ``'*'`` (asterisk), the
   actual width is read from the next element of the tuple in *values*, and the
   object to convert comes after the minimum field width and optional precision.

#. Precision (optional), given as a ``'.'`` (dot) followed by the precision.  If
   specified as ``'*'`` (an asterisk), the actual precision is read from the next
   element of the tuple in *values*, and the value to convert comes after the
   precision.

#. Length modifier (optional).

#. Conversion type.

When the right argument is a dictionary (or other mapping type), then the
formats in the bytes object *must* include a parenthesised mapping key into that
dictionary inserted immediately after the ``'%'`` character. The mapping key
selects the value to be formatted from the mapping.  For example:

   >>> print(b'%(language)s has %(number)03d quote types.' %
   ...       {b'language': b"Python", b"number": 2})
   b'Python has 002 quote types.'

In this case no ``*`` specifiers may occur in a format (since they require a
sequential parameter list).

The conversion flag characters are:

.. index::
   single: # (hash); in printf-style formatting
   single: - (minus); in printf-style formatting
   single: + (plus); in printf-style formatting
   single: space; in printf-style formatting

+---------+---------------------------------------------------------------------+
| Flag    | Meaning                                                             |
+=========+=====================================================================+
| ``'#'`` | The value conversion will use the "alternate form" (where defined   |
|         | below).                                                             |
+---------+---------------------------------------------------------------------+
| ``'0'`` | The conversion will be zero padded for numeric values.              |
+---------+---------------------------------------------------------------------+
| ``'-'`` | The converted value is left adjusted (overrides the ``'0'``         |
|         | conversion if both are given).                                      |
+---------+---------------------------------------------------------------------+
| ``' '`` | (a space) A blank should be left before a positive number (or empty |
|         | string) produced by a signed conversion.                            |
+---------+---------------------------------------------------------------------+
| ``'+'`` | A sign character (``'+'`` or ``'-'``) will precede the conversion   |
|         | (overrides a "space" flag).                                         |
+---------+---------------------------------------------------------------------+

A length modifier (``h``, ``l``, or ``L``) may be present, but is ignored as it
is not necessary for Python -- so e.g. ``%ld`` is identical to ``%d``.

The conversion types are:

+------------+-----------------------------------------------------+-------+
| Conversion | Meaning                                             | Notes |
+============+=====================================================+=======+
| ``'d'``    | Signed integer decimal.                             |       |
+------------+-----------------------------------------------------+-------+
| ``'i'``    | Signed integer decimal.                             |       |
+------------+-----------------------------------------------------+-------+
| ``'o'``    | Signed octal value.                                 | \(1)  |
+------------+-----------------------------------------------------+-------+
| ``'u'``    | Obsolete type -- it is identical to ``'d'``.        | \(8)  |
+------------+-----------------------------------------------------+-------+
| ``'x'``    | Signed hexadecimal (lowercase).                     | \(2)  |
+------------+-----------------------------------------------------+-------+
| ``'X'``    | Signed hexadecimal (uppercase).                     | \(2)  |
+------------+-----------------------------------------------------+-------+
| ``'e'``    | Floating-point exponential format (lowercase).      | \(3)  |
+------------+-----------------------------------------------------+-------+
| ``'E'``    | Floating-point exponential format (uppercase).      | \(3)  |
+------------+-----------------------------------------------------+-------+
| ``'f'``    | Floating-point decimal format.                      | \(3)  |
+------------+-----------------------------------------------------+-------+
| ``'F'``    | Floating-point decimal format.                      | \(3)  |
+------------+-----------------------------------------------------+-------+
| ``'g'``    | Floating-point format. Uses lowercase exponential   | \(4)  |
|            | format if exponent is less than -4 or not less than |       |
|            | precision, decimal format otherwise.                |       |
+------------+-----------------------------------------------------+-------+
| ``'G'``    | Floating-point format. Uses uppercase exponential   | \(4)  |
|            | format if exponent is less than -4 or not less than |       |
|            | precision, decimal format otherwise.                |       |
+------------+-----------------------------------------------------+-------+
| ``'c'``    | Single byte (accepts integer or single              |       |
|            | byte objects).                                      |       |
+------------+-----------------------------------------------------+-------+
| ``'b'``    | Bytes (any object that follows the                  | \(5)  |
|            | :ref:`buffer protocol <bufferobjects>` or has       |       |
|            | :meth:`~object.__bytes__`).                         |       |
+------------+-----------------------------------------------------+-------+
| ``'s'``    | ``'s'`` is an alias for ``'b'`` and should only     | \(6)  |
|            | be used for Python2/3 code bases.                   |       |
+------------+-----------------------------------------------------+-------+
| ``'a'``    | Bytes (converts any Python object using             | \(5)  |
|            | ``repr(obj).encode('ascii', 'backslashreplace')``). |       |
+------------+-----------------------------------------------------+-------+
| ``'r'``    | ``'r'`` is an alias for ``'a'`` and should only     | \(7)  |
|            | be used for Python2/3 code bases.                   |       |
+------------+-----------------------------------------------------+-------+
| ``'%'``    | No argument is converted, results in a ``'%'``      |       |
|            | character in the result.                            |       |
+------------+-----------------------------------------------------+-------+

Notes:

(1)
   The alternate form causes a leading octal specifier (``'0o'``) to be
   inserted before the first digit.

(2)
   The alternate form causes a leading ``'0x'`` or ``'0X'`` (depending on whether
   the ``'x'`` or ``'X'`` format was used) to be inserted before the first digit.

(3)
   The alternate form causes the result to always contain a decimal point, even if
   no digits follow it.

   The precision determines the number of digits after the decimal point and
   defaults to 6.

(4)
   The alternate form causes the result to always contain a decimal point, and
   trailing zeroes are not removed as they would otherwise be.

   The precision determines the number of significant digits before and after the
   decimal point and defaults to 6.

(5)
   If precision is ``N``, the output is truncated to ``N`` characters.

(6)
   ``b'%s'`` is deprecated, but will not be removed during the 3.x series.

(7)
   ``b'%r'`` is deprecated, but will not be removed during the 3.x series.

(8)
   See :pep:`237`.

.. note::

   The bytearray version of this method does *not* operate in place - it
   always produces a new object, even if no changes were made.

.. seealso::

   :pep:`461` - Adding % formatting to bytes and bytearray

.. versionadded:: 3.5

.. _typememoryview:

Memory Views
------------

:class:`memoryview` objects allow Python code to access the internal data
of an object that supports the :ref:`buffer protocol <bufferobjects>` without
copying.

.. class:: memoryview(object)

   Create a :class:`memoryview` that references *object*.  *object* must
   support the buffer protocol.  Built-in objects that support the buffer
   protocol include :class:`bytes` and :class:`bytearray`.

   A :class:`memoryview` has the notion of an *element*, which is the
   atomic memory unit handled by the originating *object*.  For many simple
   types such as :class:`bytes` and :class:`bytearray`, an element is a single
   byte, but other types such as :class:`array.array` may have bigger elements.

   :class:`!memoryview`\s are :ref:`generic <generics>` over the type of their
   underlying data.

   ``len(view)`` is equal to the length of :meth:`~memoryview.tolist`, which
   is the nested list representation of the view. If ``view.ndim == 1``,
   this is equal to the number of elements in the view.

   .. versionchanged:: 3.12
      If ``view.ndim == 0``, ``len(view)`` now raises :exc:`TypeError` instead of returning 1.

   The :class:`~memoryview.itemsize` attribute will give you the number of
   bytes in a single element.

   A :class:`memoryview` supports slicing and indexing to expose its data.
   One-dimensional slicing will result in a subview::

    >>> v = memoryview(b'abcefg')
    >>> v[1]
    98
    >>> v[-1]
    103
    >>> v[1:4]
    <memory at 0x7f3ddc9f4350>
    >>> bytes(v[1:4])
    b'bce'

   If :class:`~memoryview.format` is one of the native format specifiers
   from the :mod:`struct` module, indexing with an integer or a tuple of
   integers is also supported and returns a single *element* with
   the correct type.  One-dimensional memoryviews can be indexed
   with an integer or a one-integer tuple.  Multi-dimensional memoryviews
   can be indexed with tuples of exactly *ndim* integers where *ndim* is
   the number of dimensions.  Zero-dimensional memoryviews can be indexed
   with the empty tuple.

   Here is an example with a non-byte format::

      >>> import array
      >>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
      >>> m = memoryview(a)
      >>> m[0]
      -11111111
      >>> m[-1]
      44444444
      >>> m[::2].tolist()
      [-11111111, -33333333]

   If the underlying object is writable, the memoryview supports
   one-dimensional slice assignment. Resizing is not allowed::

      >>> data = bytearray(b'abcefg')
      >>> v = memoryview(data)
      >>> v.readonly
      False
      >>> v[0] = ord(b'z')
      >>> data
      bytearray(b'zbcefg')
      >>> v[1:4] = b'123'
      >>> data
      bytearray(b'z123fg')
      >>> v[2:3] = b'spam'
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
      ValueError: memoryview assignment: lvalue and rvalue have different structures
      >>> v[2:6] = b'spam'
      >>> data
      bytearray(b'z1spam')

   One-dimensional memoryviews of :term:`hashable` (read-only) types with formats
   'B', 'b' or 'c' are also hashable. The hash is defined as
   ``hash(m) == hash(m.tobytes())``::

      >>> v = memoryview(b'abcefg')
      >>> hash(v) == hash(b'abcefg')
      True
      >>> hash(v[2:4]) == hash(b'ce')
      True
      >>> hash(v[::-2]) == hash(b'abcefg'[::-2])
      True

   .. versionchanged:: 3.3
      One-dimensional memoryviews can now be sliced.
      One-dimensional memoryviews with formats 'B', 'b' or 'c' are now :term:`hashable`.

   .. versionchanged:: 3.4
      memoryview is now registered automatically with
      :class:`collections.abc.Sequence`

   .. versionchanged:: 3.5
      memoryviews can now be indexed with a tuple of integers.

   .. versionchanged:: 3.14
      memoryview is now a :term:`generic type`.

   :class:`memoryview` has several methods:

   .. method:: __eq__(exporter)

      A memoryview and a :pep:`3118` exporter are equal if their shapes are
      equivalent and if all corresponding values are equal when the operands'
      respective format codes are interpreted using :mod:`struct` syntax.

      For the subset of :mod:`struct` format strings currently supported by
      :meth:`tolist`, ``v`` and ``w`` are equal if ``v.tolist() == w.tolist()``::

         >>> import array
         >>> a = array.array('I', [1, 2, 3, 4, 5])
         >>> b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
         >>> c = array.array('b', [5, 3, 1])
         >>> x = memoryview(a)
         >>> y = memoryview(b)
         >>> x == a == y == b
         True
         >>> x.tolist() == a.tolist() == y.tolist() == b.tolist()
         True
         >>> z = y[::-2]
         >>> z == c
         True
         >>> z.tolist() == c.tolist()
         True

      If either format string is not supported by the :mod:`struct` module,
      then the objects will always compare as unequal (even if the format
      strings and buffer contents are identical)::

         >>> from ctypes import BigEndianStructure, c_long
         >>> class BEPoint(BigEndianStructure):
         ...     _fields_ = [("x", c_long), ("y", c_long)]
         ...
         >>> point = BEPoint(100, 200)
         >>> a = memoryview(point)
         >>> b = memoryview(point)
         >>> a == point
         False
         >>> a == b
         False

      Note that, as with floating-point numbers, ``v is w`` does *not* imply
      ``v == w`` for memoryview objects.

      .. versionchanged:: 3.3
         Previous versions compared the raw memory disregarding the item format
         and the logical array structure.

   .. method:: tobytes(order='C')

      Return the data in the buffer as a bytestring.  This is equivalent to
      calling the :class:`bytes` constructor on the memoryview. ::

         >>> m = memoryview(b"abc")
         >>> m.tobytes()
         b'abc'
         >>> bytes(m)
         b'abc'

      For non-contiguous arrays the result is equal to the flattened list
      representation with all elements converted to bytes. :meth:`tobytes`
      supports all format strings, including those that are not in
      :mod:`struct` module syntax.

      .. versionadded:: 3.8
         *order* can be {'C', 'F', 'A'}.  When *order* is 'C' or 'F', the data
         of the original array is converted to C or Fortran order. For contiguous
         views, 'A' returns an exact copy of the physical memory. In particular,
         in-memory Fortran order is preserved. For non-contiguous views, the
         data is converted to C first. *order=None* is the same as *order='C'*.

   .. method:: hex(*, bytes_per_sep=1)
               hex(sep, bytes_per_sep=1)

      Return a string object containing two hexadecimal digits for each
      byte in the buffer. ::

         >>> m = memoryview(b"abc")
         >>> m.hex()
         '616263'

      .. versionadded:: 3.5

      .. versionchanged:: 3.8
         Similar to :meth:`bytes.hex`, :meth:`memoryview.hex` now supports
         optional *sep* and *bytes_per_sep* parameters to insert separators
         between bytes in the hex output.

   .. method:: tolist()

      Return the data in the buffer as a list of elements. ::

         >>> memoryview(b'abc').tolist()
         [97, 98, 99]
         >>> import array
         >>> a = array.array('d', [1.1, 2.2, 3.3])
         >>> m = memoryview(a)
         >>> m.tolist()
         [1.1, 2.2, 3.3]

      .. versionchanged:: 3.3
         :meth:`tolist` now supports all single character native formats in
         :mod:`struct` module syntax as well as multi-dimensional
         representations.

   .. method:: toreadonly()

      Return a readonly version of the memoryview object.  The original
      memoryview object is unchanged. ::

         >>> m = memoryview(bytearray(b'abc'))
         >>> mm = m.toreadonly()
         >>> mm.tolist()
         [97, 98, 99]
         >>> mm[0] = 42
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         TypeError: cannot modify read-only memory
         >>> m[0] = 43
         >>> mm.tolist()
         [43, 98, 99]

      .. versionadded:: 3.8

   .. method:: release()

      Release the underlying buffer exposed by the memoryview object.  Many
      objects take special actions when a view is held on them (for example,
      a :class:`bytearray` would temporarily forbid resizing); therefore,
      calling release() is handy to remove these restrictions (and free any
      dangling resources) as soon as possible.

      After this method has been called, any further operation on the view
      raises a :class:`ValueError` (except :meth:`release` itself which can
      be called multiple times)::

         >>> m = memoryview(b'abc')
         >>> m.release()
         >>> m[0]
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         ValueError: operation forbidden on released memoryview object

      The context management protocol can be used for a similar effect,
      using the ``with`` statement::

         >>> with memoryview(b'abc') as m:
         ...     m[0]
         ...
         97
         >>> m[0]
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         ValueError: operation forbidden on released memoryview object

      .. versionadded:: 3.2

   .. method:: cast(format, /)
               cast(format, shape, /)

      Cast a memoryview to a new format or shape. *shape* defaults to
      ``[byte_length//new_itemsize]``, which means that the result view
      will be one-dimensional. The return value is a new memoryview, but
      the buffer itself is not copied. Supported casts are 1D -> C-:term:`contiguous`
      and C-contiguous -> 1D.

      The destination format is restricted to a single element native format in
      :mod:`struct` syntax. One of the formats must be a byte format
      ('B', 'b' or 'c'). The byte length of the result must be the same
      as the original length.
      Note that all byte lengths may depend on the operating system.

      Cast 1D/long to 1D/unsigned bytes::

         >>> import array
         >>> a = array.array('l', [1,2,3])
         >>> x = memoryview(a)
         >>> x.format
         'l'
         >>> x.itemsize
         8
         >>> len(x)
         3
         >>> x.nbytes
         24
         >>> y = x.cast('B')
         >>> y.format
         'B'
         >>> y.itemsize
         1
         >>> len(y)
         24
         >>> y.nbytes
         24

      Cast 1D/unsigned bytes to 1D/char::

         >>> b = bytearray(b'zyz')
         >>> x = memoryview(b)
         >>> x[0] = b'a'
         Traceback (most recent call last):
           ...
         TypeError: memoryview: invalid type for format 'B'
         >>> y = x.cast('c')
         >>> y[0] = b'a'
         >>> b
         bytearray(b'ayz')

      Cast 1D/bytes to 3D/ints to 1D/signed char::

         >>> import struct
         >>> buf = struct.pack("i"*12, *list(range(12)))
         >>> x = memoryview(buf)
         >>> y = x.cast('i', shape=[2,2,3])
         >>> y.tolist()
         [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
         >>> y.format
         'i'
         >>> y.itemsize
         4
         >>> len(y)
         2
         >>> y.nbytes
         48
         >>> z = y.cast('b')
         >>> z.format
         'b'
         >>> z.itemsize
         1
         >>> len(z)
         48
         >>> z.nbytes
         48

      Cast 1D/unsigned long to 2D/unsigned long::

         >>> buf = struct.pack("L"*6, *list(range(6)))
         >>> x = memoryview(buf)
         >>> y = x.cast('L', shape=[2,3])
         >>> len(y)
         2
         >>> y.nbytes
         48
         >>> y.tolist()
         [[0, 1, 2], [3, 4, 5]]

      .. versionadded:: 3.3

      .. versionchanged:: 3.5
         The source format is no longer restricted when casting to a byte view.

   .. method:: count(value, /)

      Count the number of occurrences of *value*.

      .. versionadded:: 3.14

   .. method:: index(value, start=0, stop=sys.maxsize, /)

      Return the index of the first occurrence of *value* (at or after
      index *start* and before index *stop*).

      Raises a :exc:`ValueError` if *value* cannot be found.

      .. versionadded:: 3.14

   There are also several readonly attributes available:

   .. attribute:: obj

      The underlying object of the memoryview::

         >>> b  = bytearray(b'xyz')
         >>> m = memoryview(b)
         >>> m.obj is b
         True

      .. versionadded:: 3.3

   .. attribute:: nbytes

      ``nbytes == product(shape) * itemsize == len(m.tobytes())``. This is
      the amount of space in bytes that the array would use in a contiguous
      representation. It is not necessarily equal to ``len(m)``::

         >>> import array
         >>> a = array.array('i', [1,2,3,4,5])
         >>> m = memoryview(a)
         >>> len(m)
         5
         >>> m.nbytes
         20
         >>> y = m[::2]
         >>> len(y)
         3
         >>> y.nbytes
         12
         >>> len(y.tobytes())
         12

      Multi-dimensional arrays::

         >>> import struct
         >>> buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
         >>> x = memoryview(buf)
         >>> y = x.cast('d', shape=[3,4])
         >>> y.tolist()
         [[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]
         >>> len(y)
         3
         >>> y.nbytes
         96

      .. versionadded:: 3.3

   .. attribute:: readonly

      A bool indicating whether the memory is read only.

   .. attribute:: format

      A string containing the format (in :mod:`struct` module style) for each
      element in the view. A memoryview can be created from exporters with
      arbitrary format strings, but some methods (e.g. :meth:`tolist`) are
      restricted to native single element formats.

      .. versionchanged:: 3.3
         format ``'B'`` is now handled according to the struct module syntax.
         This means that ``memoryview(b'abc')[0] == b'abc'[0] == 97``.

   .. attribute:: itemsize

      The size in bytes of each element of the memoryview::

         >>> import array, struct
         >>> m = memoryview(array.array('H', [32000, 32001, 32002]))
         >>> m.itemsize
         2
         >>> m[0]
         32000
         >>> struct.calcsize('H') == m.itemsize
         True

   .. attribute:: ndim

      An integer indicating how many dimensions of a multi-dimensional array the
      memory represents.

   .. attribute:: shape

      A tuple of integers the length of :attr:`ndim` giving the shape of the
      memory as an N-dimensional array.

      .. versionchanged:: 3.3
         An empty tuple instead of ``None`` when ndim = 0.

   .. attribute:: strides

      A tuple of integers the length of :attr:`ndim` giving the size in bytes to
      access each element for each dimension of the array.

      .. versionchanged:: 3.3
         An empty tuple instead of ``None`` when ndim = 0.

   .. attribute:: suboffsets

      Used internally for PIL-style arrays. The value is informational only.

   .. attribute:: c_contiguous

      A bool indicating whether the memory is C-:term:`contiguous`.

      .. versionadded:: 3.3

   .. attribute:: f_contiguous

      A bool indicating whether the memory is Fortran :term:`contiguous`.

      .. versionadded:: 3.3

   .. attribute:: contiguous

      A bool indicating whether the memory is :term:`contiguous`.

      .. versionadded:: 3.3

For information on the thread safety of :class:`memoryview` objects in
the :term:`free-threaded build`, see :ref:`thread-safety-memoryview`.


.. _types-set:

Set Types --- :class:`set`, :class:`frozenset`
==============================================

.. index:: pair: object; set

A :dfn:`set` object is an unordered collection of distinct :term:`hashable` objects.
Common uses include membership testing, removing duplicates from a sequence, and
computing mathematical operations such as intersection, union, difference, and
symmetric difference.
(For other containers see the built-in :class:`dict`, :class:`list`,
and :class:`tuple` classes, and the :mod:`collections` module.)
See :ref:`time-complexity` for the costs of the various set operations.

Like other collections, sets support ``x in set``, ``len(set)``, and ``for x in
set``.  Being an unordered collection, sets do not record element position or
order of insertion.  Accordingly, sets do not support indexing, slicing, or
other sequence-like behavior.

There are currently two built-in set types, :class:`set` and :class:`frozenset`.
The :class:`set` type is mutable --- the contents can be changed using methods
like :meth:`~set.add` and :meth:`~set.remove`.
Since it is mutable, it has no hash value and cannot be used as
either a dictionary key or as an element of another set.
The :class:`frozenset` type is immutable and :term:`hashable` ---
its contents cannot be altered after it is created;
it can therefore be used as a dictionary key or as an element of another set.

Non-empty sets (not frozensets) can be created by placing a comma-separated list
of elements within braces, for example: ``{'jack', 'sjoerd'}``, in addition to the
:class:`set` constructor.

The constructors for both classes work the same:

.. class:: set(iterable=(), /)
           frozenset(iterable=(), /)

   Return a new set or frozenset object whose elements are taken from
   *iterable*.  The elements of a set must be :term:`hashable`.  To
   represent sets of sets, the inner sets must be :class:`frozenset`
   objects.  If *iterable* is not specified, a new empty set is
   returned.

Sets can be created by several means:

* Use a comma-separated list of elements within braces: ``{'jack', 'sjoerd'}``
* Use a set comprehension: ``{c for c in 'abracadabra' if c not in 'abc'}``
* Use the type constructor: ``set()``, ``set('foobar')``, ``set(['a', 'b', 'foo'])``

Instances of :class:`set` and :class:`frozenset` provide the following
operations:

.. describe:: len(s)

   Return the number of elements in set *s* (cardinality of *s*).

.. describe:: x in s

   Test *x* for membership in *s*.

.. describe:: x not in s

   Test *x* for non-membership in *s*.

.. method:: frozenset.isdisjoint(other, /)
            set.isdisjoint(other, /)

   Return ``True`` if the set has no elements in common with *other*.  Sets are
   disjoint if and only if their intersection is the empty set.

.. method:: frozenset.issubset(other, /)
            set.issubset(other, /)
.. describe:: set <= other

   Test whether every element in the set is in *other*.

.. describe:: set < other

   Test whether the set is a proper subset of *other*, that is,
   ``set <= other and set != other``.

.. method:: frozenset.issuperset(other, /)
            set.issuperset(other, /)
.. describe:: set >= other

   Test whether every element in *other* is in the set.

.. describe:: set > other

   Test whether the set is a proper superset of *other*, that is, ``set >=
   other and set != other``.

.. method:: frozenset.union(*others)
            set.union(*others)
.. describe:: set | other | ...

   Return a new set with elements from the set and all others.

.. method:: frozenset.intersection(*others)
            set.intersection(*others)
.. describe:: set & other & ...

   Return a new set with elements common to the set and all others.

.. method:: frozenset.difference(*others)
            set.difference(*others)
.. describe:: set - other - ...

   Return a new set with elements in the set that are not in the others.

.. method:: frozenset.symmetric_difference(other, /)
            set.symmetric_difference(other, /)
.. describe:: set ^ other

   Return a new set with elements in either the set or *other* but not both.

.. method:: frozenset.copy()
            set.copy()

   Return a shallow copy of the set.


Note, the non-operator versions of :meth:`~frozenset.union`,
:meth:`~frozenset.intersection`, :meth:`~frozenset.difference`, :meth:`~frozenset.symmetric_difference`, :meth:`~frozenset.issubset`, and
:meth:`~frozenset.issuperset` methods will accept any iterable as an argument.  In
contrast, their operator based counterparts require their arguments to be
sets.  This precludes error-prone constructions like ``set('abc') & 'cbs'``
in favor of the more readable ``set('abc').intersection('cbs')``.

Both :class:`set` and :class:`frozenset` support set to set comparisons. Two
sets are equal if and only if every element of each set is contained in the
other (each is a subset of the other). A set is less than another set if and
only if the first set is a proper subset of the second set (is a subset, but
is not equal). A set is greater than another set if and only if the first set
is a proper superset of the second set (is a superset, but is not equal).

Instances of :class:`set` are compared to instances of :class:`frozenset`
based on their members.  For example, ``set('abc') == frozenset('abc')``
returns ``True`` and so does ``set('abc') in set([frozenset('abc')])``.

The subset and equality comparisons do not generalize to a total ordering
function.  For example, any two nonempty disjoint sets are not equal and are not
subsets of each other, so *all* of the following return ``False``: ``a<b``,
``a==b``, or ``a>b``.

Since sets only define partial ordering (subset relationships), the output of
the :meth:`list.sort` method is undefined for lists of sets.

Set elements, like dictionary keys, must be :term:`hashable`.

Binary operations that mix :class:`set` instances with :class:`frozenset`
return the type of the first operand.  For example: ``frozenset('ab') |
set('bc')`` returns an instance of :class:`frozenset`.

The following table lists operations available for :class:`set` that do not
apply to immutable instances of :class:`frozenset`:

.. method:: set.update(*others)
.. describe:: set |= other | ...

   Update the set, adding elements from all others.

.. method:: set.intersection_update(*others)
.. describe:: set &= other & ...

   Update the set, keeping only elements found in it and all others.

.. method:: set.difference_update(*others)
.. describe:: set -= other | ...

   Update the set, removing elements found in others.

.. method:: set.symmetric_difference_update(other, /)
.. describe:: set ^= other

   Update the set, keeping only elements found in either set, but not in both.

.. method:: set.add(elem, /)

   Add element *elem* to the set.

.. method:: set.remove(elem, /)

   Remove element *elem* from the set.  Raises :exc:`KeyError` if *elem* is
   not contained in the set.

.. method:: set.discard(elem, /)

   Remove element *elem* from the set if it is present.

.. method:: set.pop()

   Remove and return an arbitrary element from the set.  Raises
   :exc:`KeyError` if the set is empty.

.. method:: set.clear()

   Remove all elements from the set.


Note, the non-operator versions of the :meth:`~set.update`,
:meth:`~set.intersection_update`, :meth:`~set.difference_update`, and
:meth:`~set.symmetric_difference_update` methods will accept any iterable as an
argument.

Note, the *elem* argument to the :meth:`~object.__contains__`,
:meth:`~set.remove`, and
:meth:`~set.discard` methods may be a set.  To support searching for an equivalent
frozenset, a temporary one is created from *elem*.

Sets and frozensets are :ref:`generic <generics>` over the type of their elements.

.. seealso::

   For detailed information on thread-safety guarantees for :class:`set`
   objects, see :ref:`thread-safety-set`.


.. _typesmapping:

Mapping types --- :class:`!dict`, :class:`!frozendict`
======================================================

.. index::
   pair: object; mapping
   pair: object; dictionary
   triple: operations on; mapping; types
   triple: operations on; dictionary; type
   pair: statement; del
   pair: built-in function; len

A :term:`mapping` object maps :term:`hashable` values to arbitrary objects.
There are currently two standard mapping types, the :dfn:`dictionary` and
:class:`frozendict`.
(For other containers see the built-in
:class:`list`, :class:`set`, and :class:`tuple` classes, and the
:mod:`collections` module.)
See :ref:`time-complexity` for the costs of the various dictionary
operations.

A dictionary's keys are *almost* arbitrary values.  Values that are not
:term:`hashable`, that is, values containing lists, dictionaries or other
mutable types (that are compared by value rather than by object identity) may
not be used as keys.
Values that compare equal (such as ``1``, ``1.0``, and ``True``)
can be used interchangeably to index the same dictionary entry.

.. class:: dict(**kwargs)
           dict(mapping, /, **kwargs)
           dict(iterable, /, **kwargs)

   Return a new dictionary initialized from an optional positional argument
   and a possibly empty set of keyword arguments.

   Dictionaries can be created by several means:

   * Use a comma-separated list of ``key: value`` pairs within braces:
     ``{'jack': 4098, 'sjoerd': 4127}`` or ``{4098: 'jack', 4127: 'sjoerd'}``
   * Use a dict comprehension: ``{}``, ``{x: x ** 2 for x in range(10)}``
   * Use the type constructor: ``dict()``,
     ``dict([('foo', 100), ('bar', 200)])``, ``dict(foo=100, bar=200)``

   If no positional argument is given, an empty dictionary is created.
   If a positional argument is given and it defines a ``keys()`` method, a
   dictionary is created by calling :meth:`~object.__getitem__` on the argument with
   each returned key from the method.  Otherwise, the positional argument must be an
   :term:`iterable` object.  Each item in the iterable must itself be an iterable
   with exactly two elements.  The first element of each item becomes a key in the
   new dictionary, and the second element the corresponding value.  If a key occurs
   more than once, the last value for that key becomes the corresponding value in
   the new dictionary.

   If keyword arguments are given, the keyword arguments and their values are
   added to the dictionary created from the positional argument.  If a key
   being added is already present, the value from the keyword argument
   replaces the value from the positional argument.

   Dictionaries compare equal if and only if they have the same ``(key,
   value)`` pairs (regardless of ordering). Order comparisons ('<', '<=', '>=', '>') raise
   :exc:`TypeError`.  To illustrate dictionary creation and equality,
   the following examples all return a dictionary equal to
   ``{"one": 1, "two": 2, "three": 3}``::

      >>> a = dict(one=1, two=2, three=3)
      >>> b = {'one': 1, 'two': 2, 'three': 3}
      >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
      >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
      >>> e = dict({'three': 3, 'one': 1, 'two': 2})
      >>> f = dict({'one': 1, 'three': 3}, two=2)
      >>> a == b == c == d == e == f
      True

   Providing keyword arguments as in the first example only works for keys that
   are valid Python identifiers.  Otherwise, any valid keys can be used.

   Dictionaries preserve insertion order.  Note that updating a key does not
   affect the order.  Keys added after deletion are inserted at the end. ::

      >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
      >>> d
      {'one': 1, 'two': 2, 'three': 3, 'four': 4}
      >>> list(d)
      ['one', 'two', 'three', 'four']
      >>> list(d.values())
      [1, 2, 3, 4]
      >>> d["one"] = 42
      >>> d
      {'one': 42, 'two': 2, 'three': 3, 'four': 4}
      >>> del d["two"]
      >>> d["two"] = None
      >>> d
      {'one': 42, 'three': 3, 'four': 4, 'two': None}

   .. versionchanged:: 3.7
      Dictionary order is guaranteed to be insertion order.  This behavior was
      an implementation detail of CPython from 3.6.

   Dictionaries are :ref:`generic <generics>` over two types, signifying
   (respectively) the types of the dictionary's keys and values.

   These are the operations that dictionaries support (and therefore, custom
   mapping types should support too):

   .. describe:: list(d)

      Return a list of all the keys used in the dictionary *d*.

   .. describe:: len(d)

      Return the number of items in the dictionary *d*.

   .. describe:: d[key]

      Return the item of *d* with key *key*.  Raises a :exc:`KeyError` if *key* is
      not in the map.

      .. index:: __missing__()

      If a subclass of dict defines a method :meth:`~object.__missing__` and *key*
      is not present, the ``d[key]`` operation calls that method with the key *key*
      as argument.  The ``d[key]`` operation then returns or raises whatever is
      returned or raised by the ``__missing__(key)`` call.
      No other operations or methods invoke :meth:`~object.__missing__`. If
      :meth:`~object.__missing__` is not defined, :exc:`KeyError` is raised.
      :meth:`~object.__missing__` must be a method; it cannot be an instance variable::

          >>> class Counter(dict):
          ...     def __missing__(self, key):
          ...         return 0
          ...
          >>> c = Counter()
          >>> c['red']
          0
          >>> c['red'] += 1
          >>> c['red']
          1

      The example above shows part of the implementation of
      :class:`collections.Counter`.
      A different :meth:`!__missing__` method is used
      by :class:`collections.defaultdict`.

   .. describe:: d[key] = value

      Set ``d[key]`` to *value*.

   .. describe:: del d[key]

      Remove ``d[key]`` from *d*.  Raises a :exc:`KeyError` if *key* is not in the
      map.

   .. describe:: key in d

      Return ``True`` if *d* has a key *key*, else ``False``.

   .. describe:: key not in d

      Equivalent to ``not key in d``.

   .. describe:: iter(d)

      Return an iterator over the keys of the dictionary.  This is a shortcut
      for ``iter(d.keys())``.

   .. method:: clear()

      Remove all items from the dictionary.

   .. method:: copy()

      Return a shallow copy of the dictionary.

   .. classmethod:: fromkeys(iterable, value=None, /)

      Create a new dictionary with keys from *iterable* and values set to *value*.

      :meth:`fromkeys` is a class method that returns a new dictionary. *value*
      defaults to ``None``.  All of the values refer to just a single instance,
      so it generally doesn't make sense for *value* to be a mutable object
      such as an empty list.  To get distinct values, use a :ref:`dict
      comprehension <dict>` instead.

   .. method:: get(key, default=None, /)

      Return the value for *key* if *key* is in the dictionary, else *default*.
      If *default* is not given, it defaults to ``None``, so that this method
      never raises a :exc:`KeyError`.

   .. method:: items()

      Return a new view of the dictionary's items (``(key, value)`` pairs).
      See the :ref:`documentation of view objects <dict-views>`.

   .. method:: keys()

      Return a new view of the dictionary's keys.  See the :ref:`documentation
      of view objects <dict-views>`.

   .. method:: pop(key, /)
               pop(key, default, /)

      If *key* is in the dictionary, remove it and return its value, else return
      *default*.  If *default* is not given and *key* is not in the dictionary,
      a :exc:`KeyError` is raised.

   .. method:: popitem()

      Remove and return a ``(key, value)`` pair from the dictionary.
      Pairs are returned in :abbr:`LIFO (last-in, first-out)` order.

      :meth:`popitem` is useful to destructively iterate over a dictionary, as
      often used in set algorithms.  If the dictionary is empty, calling
      :meth:`popitem` raises a :exc:`KeyError`.

      .. versionchanged:: 3.7
         LIFO order is now guaranteed. In prior versions, :meth:`popitem` would
         return an arbitrary key/value pair.

   .. describe:: reversed(d)

      Return a reverse iterator over the keys of the dictionary. This is a
      shortcut for ``reversed(d.keys())``.

      .. versionadded:: 3.8

   .. method:: setdefault(key, default=None, /)

      If *key* is in the dictionary, return its value.  If not, insert *key*
      with a value of *default* and return *default*.  *default* defaults to
      ``None``.

   .. method:: update(**kwargs)
               update(mapping, /, **kwargs)
               update(iterable, /, **kwargs)

      Update the dictionary with the key/value pairs from *mapping* or *iterable* and *kwargs*, overwriting
      existing keys.  Return ``None``.

      :meth:`update` accepts either another object with a ``keys()`` method (in
      which case :meth:`~object.__getitem__` is called with every key returned from
      the method) or an iterable of key/value pairs (as tuples or other iterables
      of length two). If keyword arguments are specified, the dictionary is then
      updated with those key/value pairs: ``d.update(red=1, blue=2)``.

   .. method:: values()

      Return a new view of the dictionary's values.  See the
      :ref:`documentation of view objects <dict-views>`.

      An equality comparison between one ``dict.values()`` view and another
      will always return ``False``. This also applies when comparing
      ``dict.values()`` to itself::

         >>> d = {'a': 1}
         >>> d.values() == d.values()
         False

   .. describe:: d | other

      Create a new dictionary with the merged keys and values of *d* and
      *other*, which must both be dictionaries. The values of *other* take
      priority when *d* and *other* share keys.

      .. versionadded:: 3.9

   .. describe:: d |= other

      Update the dictionary *d* with keys and values from *other*, which may be
      either a :term:`mapping` or an :term:`iterable` of key/value pairs. The
      values of *other* take priority when *d* and *other* share keys.

      .. versionadded:: 3.9

   Dictionaries and dictionary views are reversible. ::

      >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
      >>> d
      {'one': 1, 'two': 2, 'three': 3, 'four': 4}
      >>> list(reversed(d))
      ['four', 'three', 'two', 'one']
      >>> list(reversed(d.values()))
      [4, 3, 2, 1]
      >>> list(reversed(d.items()))
      [('four', 4), ('three', 3), ('two', 2), ('one', 1)]

   .. versionchanged:: 3.8
      Dictionaries are now reversible.


   .. seealso::
      :class:`frozendict` and :class:`types.MappingProxyType` can be used to
      create a read-only view of a :class:`dict`.

.. seealso::

   For detailed information on thread-safety guarantees for :class:`dict`
   objects, see :ref:`thread-safety-dict`.


.. _dict-views:

Dictionary view objects
-----------------------

The objects returned by :meth:`dict.keys`, :meth:`dict.values` and
:meth:`dict.items` are *view objects*.  They provide a dynamic view on the
dictionary's entries, which means that when the dictionary changes, the view
reflects these changes.

Dictionary views can be iterated over to yield their respective data, and
support membership tests:

.. describe:: len(dictview)

   Return the number of entries in the dictionary.

.. describe:: iter(dictview)

   Return an iterator over the keys, values or items (represented as tuples of
   ``(key, value)``) in the dictionary.

   Keys and values are iterated over in insertion order.
   This allows the creation of ``(value, key)`` pairs
   using :func:`zip`: ``pairs = zip(d.values(), d.keys())``.  Another way to
   create the same list is ``pairs = [(v, k) for (k, v) in d.items()]``.

   Iterating views while adding or deleting entries in the dictionary may raise
   a :exc:`RuntimeError` or fail to iterate over all entries.

   .. versionchanged:: 3.7
      Dictionary order is guaranteed to be insertion order.

.. describe:: x in dictview

   Return ``True`` if *x* is in the underlying dictionary's keys, values or
   items (in the latter case, *x* should be a ``(key, value)`` tuple).

.. describe:: reversed(dictview)

   Return a reverse iterator over the keys, values or items of the dictionary.
   The view will be iterated in reverse order of the insertion.

   .. versionchanged:: 3.8
      Dictionary views are now reversible.

.. describe:: dictview.mapping

   Return a :class:`types.MappingProxyType` that wraps the original
   dictionary to which the view refers.

   .. versionadded:: 3.10

Keys views are set-like since their entries are unique and :term:`hashable`.
Items views also have set-like operations since the (key, value) pairs
are unique and the keys are hashable.
If all values in an items view are hashable as well,
then the items view can interoperate with other sets.
(Values views are not treated as set-like
since the entries are generally not unique.)  For set-like views, all of the
operations defined for the abstract base class :class:`collections.abc.Set` are
available (for example, ``==``, ``<``, or ``^``).  While using set operators,
set-like views accept any iterable as the other operand,
unlike sets which only accept sets as the input.

An example of dictionary view usage::

   >>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
   >>> keys = dishes.keys()
   >>> values = dishes.values()

   >>> # iteration
   >>> n = 0
   >>> for val in values:
   ...     n += val
   ...
   >>> print(n)
   504

   >>> # keys and values are iterated over in the same order (insertion order)
   >>> list(keys)
   ['eggs', 'sausage', 'bacon', 'spam']
   >>> list(values)
   [2, 1, 1, 500]

   >>> # view objects are dynamic and reflect dict changes
   >>> del dishes['eggs']
   >>> del dishes['sausage']
   >>> list(keys)
   ['bacon', 'spam']

   >>> # set operations
   >>> keys & {'eggs', 'bacon', 'salad'}
   {'bacon'}
   >>> keys ^ {'sausage', 'juice'} == {'juice', 'sausage', 'bacon', 'spam'}
   True
   >>> keys | ['juice', 'juice', 'juice'] == {'bacon', 'spam', 'juice'}
   True

   >>> # get back a read-only proxy for the original dictionary
   >>> values.mapping
   mappingproxy({'bacon': 1, 'spam': 500})
   >>> values.mapping['spam']
   500


Frozen dictionaries
-------------------

.. class:: frozendict(**kwargs)
           frozendict(mapping, /, **kwargs)
           frozendict(iterable, /, **kwargs)

   Return a new frozen dictionary initialized from an optional positional
   argument and a possibly empty set of keyword arguments.

   A :class:`!frozendict` has a similar API to the :class:`dict` API, with the
   following differences:

   * :class:`!dict` has more methods than :class:`!frozendict`:

      * :meth:`!__delitem__`
      * :meth:`!__setitem__`
      * :meth:`~dict.clear`
      * :meth:`~dict.pop`
      * :meth:`~dict.popitem`
      * :meth:`~dict.setdefault`
      * :meth:`~dict.update`

   * A :class:`!frozendict` can be hashed with ``hash(frozendict)`` if all keys and
     values can be hashed.

   * ``frozendict |= other`` does not modify the :class:`!frozendict` in-place but
     creates a new frozen dictionary.

   :class:`!frozendict` is not a :class:`!dict` subclass but inherits directly
   from ``object``.

   Like dictionaries, frozendicts are :ref:`generic <generics>` over two types,
   signifying (respectively) the types of the frozendict's keys and values.

   .. classmethod:: fromkeys(iterable, value=None, /)

      Similar to :meth:`dict.fromkeys`, but call again the type constructor
      with an initialized :class:`frozendict` if the type is a
      :class:`frozendict` subclass or if the constructor returned a
      :class:`frozendict`.

   .. versionadded:: 3.15


.. _typecontextmanager:

Context Manager Types
=====================

.. index::
   single: context manager
   single: context management protocol
   single: protocol; context management

Python's :keyword:`with` statement supports the concept of a runtime context
defined by a context manager.  This is implemented using a pair of methods
that allow user-defined classes to define a runtime context that is entered
before the statement body is executed and exited when the statement ends:


.. method:: contextmanager.__enter__()

   Enter the runtime context and return either this object or another object
   related to the runtime context. The value returned by this method is bound to
   the identifier in the :keyword:`!as` clause of :keyword:`with` statements using
   this context manager.

   An example of a context manager that returns itself is a :term:`file object`.
   File objects return themselves from __enter__() to allow :func:`open` to be
   used as the context expression in a :keyword:`with` statement.

   An example of a context manager that returns a related object is the one
   returned by :func:`decimal.localcontext`. These managers set the active
   decimal context to a copy of the original decimal context and then return the
   copy. This allows changes to be made to the current decimal context in the body
   of the :keyword:`with` statement without affecting code outside the
   :keyword:`!with` statement.


.. method:: contextmanager.__exit__(exc_type, exc_val, exc_tb)

   Exit the runtime context and return a Boolean flag indicating if any exception
   that occurred should be suppressed. If an exception occurred while executing the
   body of the :keyword:`with` statement, the arguments contain the exception type,
   value and traceback information. Otherwise, all three arguments are ``None``.

   Returning a true value from this method will cause the :keyword:`with` statement
   to suppress the exception and continue execution with the statement immediately
   following the :keyword:`!with` statement. Otherwise the exception continues
   propagating after this method has finished executing.

   If this method raises an exception while handling an earlier exception from the
   :keyword:`with` block, the new exception is raised, and the original exception
   is stored in its :attr:`~BaseException.__context__` attribute.

   The exception passed in should never be reraised explicitly - instead, this
   method should return a false value to indicate that the method completed
   successfully and does not want to suppress the raised exception. This allows
   context management code to easily detect whether or not an :meth:`~object.__exit__`
   method has actually failed.

Python defines several context managers to support easy thread synchronisation,
prompt closure of files or other objects, and simpler manipulation of the active
decimal arithmetic context. The specific types are not treated specially beyond
their implementation of the context management protocol. See the
:mod:`contextlib` module for some examples.

Python's :term:`generator`\s and the :class:`contextlib.contextmanager` decorator
provide a convenient way to implement these protocols.  If a generator function is
decorated with the :class:`contextlib.contextmanager` decorator, it will return a
context manager implementing the necessary :meth:`~contextmanager.__enter__` and
:meth:`~contextmanager.__exit__` methods, rather than the iterator produced by an
undecorated generator function.

Note that there is no specific slot for any of these methods in the type
structure for Python objects in the Python/C API. Extension types wanting to
define these methods must provide them as a normal Python accessible method.
Compared to the overhead of setting up the runtime context, the overhead of a
single class dictionary lookup is negligible.


Type Annotation Types --- :ref:`Generic Alias <types-genericalias>`, :ref:`Union <types-union>`
===============================================================================================

.. index::
   single: annotation; type annotation; type hint

The core built-in types for :term:`type annotations <annotation>` are
:ref:`Generic Alias <types-genericalias>` and :ref:`Union <types-union>`.


.. _types-genericalias:

Generic Alias Type
------------------

.. index::
   pair: object; GenericAlias
   pair: Generic; Alias

``GenericAlias`` objects are generally created by
:ref:`subscripting <subscriptions>` a class. They are most often used with
:ref:`container classes <sequence-types>`, such as :class:`list` or
:class:`dict`. For example, ``list[int]`` is a ``GenericAlias`` object created
by subscripting the ``list`` class with the argument :class:`int`.
``GenericAlias`` objects are intended primarily for use with
:term:`type annotations <annotation>`.

.. note::

   It is generally only possible to subscript a class if the class implements
   the special method :meth:`~object.__class_getitem__`.

A ``GenericAlias`` object acts as a proxy for a :term:`generic type`,
implementing *parameterized generics*.

For a container class, the
argument(s) supplied to a :ref:`subscription <subscriptions>` of the class may
indicate the type(s) of the elements an object contains. For example,
``set[bytes]`` can be used in type annotations to signify a :class:`set` in
which all the elements are of type :class:`bytes`.

For a class which defines :meth:`~object.__class_getitem__` but is not a
container, the argument(s) supplied to a subscription of the class will often
indicate the return type(s) of one or more methods defined on an object. For
example, :mod:`regular expressions <re>` can be used on both the :class:`str` data
type and the :class:`bytes` data type:

* If ``x = re.search('foo', 'foo')``, ``x`` will be a
  :ref:`re.Match <match-objects>` object where the return values of
  ``x.group(0)`` and ``x[0]`` will both be of type :class:`str`. We can
  represent this kind of object in type annotations with the ``GenericAlias``
  ``re.Match[str]``.

* If ``y = re.search(b'bar', b'bar')``, (note the ``b`` for :class:`bytes`),
  ``y`` will also be an instance of ``re.Match``, but the return
  values of ``y.group(0)`` and ``y[0]`` will both be of type
  :class:`bytes`. In type annotations, we would represent this
  variety of :ref:`re.Match <match-objects>` objects with ``re.Match[bytes]``.

``GenericAlias`` objects are instances of the class
:class:`types.GenericAlias`, which can also be used to create ``GenericAlias``
objects directly. Specializations of user-defined :ref:`generic classes <generic-classes>`
may not be instances of :class:`types.GenericAlias`, but they provide similar functionality.

.. describe:: T[X, Y, ...]

   Creates a ``GenericAlias`` representing a type ``T`` parameterized by types
   *X*, *Y*, and more depending on the ``T`` used.
   For example, a function expecting a :class:`list` containing
   :class:`float` elements::

      def average(values: list[float]) -> float:
          return sum(values) / len(values)

   Another example for :term:`mapping` objects, using a :class:`dict`, which
   is a generic type expecting two type parameters representing the key type
   and the value type.  In this example, the function expects a ``dict`` with
   keys of type :class:`str` and values of type :class:`int`::

      def send_post_request(url: str, body: dict[str, int]) -> None:
          ...

The builtin functions :func:`isinstance` and :func:`issubclass` do not accept
``GenericAlias`` types for their second argument::

   >>> isinstance([1, 2], list[str])
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: isinstance() argument 2 cannot be a parameterized generic

The Python runtime does not enforce :term:`type annotations <annotation>`.
This extends to generic types and their type parameters. When creating
a container object from a ``GenericAlias``, the elements in the container are not checked
against their type. For example, the following code is discouraged, but will
run without errors::

   >>> t = list[str]
   >>> t([1, 2, 3])
   [1, 2, 3]

Furthermore, parameterized generics erase type parameters during object
creation::

   >>> t = list[str]
   >>> type(t)
   <class 'types.GenericAlias'>

   >>> l = t()
   >>> type(l)
   <class 'list'>


Instances of ``GenericAlias`` are not classes at runtime, even though they behave like classes (they can be instantiated and subclassed)::

   >>> import inspect
   >>> inspect.isclass(list[int])
   False

This is true for :ref:`user-defined generics <user-defined-generics>` also.

Calling :func:`repr` or :func:`str` on a generic shows the parameterized type::

   >>> repr(list[int])
   'list[int]'

   >>> str(list[int])
   'list[int]'

The :meth:`~object.__getitem__` method of generic containers will raise an
exception to disallow mistakes like ``dict[str][str]``::

   >>> dict[str][str]
   Traceback (most recent call last):
     ...
   TypeError: dict[str] is not a generic class

However, such expressions are valid when :ref:`type variables <generics>` are
used.  The index must have as many elements as there are type variable items
in the ``GenericAlias`` object's :attr:`~genericalias.__args__`. ::

   >>> from typing import TypeVar
   >>> Y = TypeVar('Y')
   >>> dict[str, Y][int]
   dict[str, int]


Standard Generic Classes
^^^^^^^^^^^^^^^^^^^^^^^^

The following standard library classes support parameterized generics. This
list is non-exhaustive.

* :class:`tuple`
* :class:`list`
* :class:`dict`
* :class:`set`
* :class:`frozendict`
* :class:`frozenset`
* :class:`type`
* :class:`asyncio.Future`
* :class:`asyncio.Task`
* :class:`collections.deque`
* :class:`collections.defaultdict`
* :class:`collections.OrderedDict`
* :class:`collections.Counter`
* :class:`collections.ChainMap`
* :class:`collections.abc.Awaitable`
* :class:`collections.abc.Coroutine`
* :class:`collections.abc.AsyncIterable`
* :class:`collections.abc.AsyncIterator`
* :class:`collections.abc.AsyncGenerator`
* :class:`collections.abc.Iterable`
* :class:`collections.abc.Iterator`
* :class:`collections.abc.Generator`
* :class:`collections.abc.Reversible`
* :class:`collections.abc.Container`
* :class:`collections.abc.Collection`
* :class:`collections.abc.Callable`
* :class:`collections.abc.Set`
* :class:`collections.abc.MutableSet`
* :class:`collections.abc.Mapping`
* :class:`collections.abc.MutableMapping`
* :class:`collections.abc.Sequence`
* :class:`collections.abc.MutableSequence`
* :class:`collections.abc.ByteString`
* :class:`collections.abc.MappingView`
* :class:`collections.abc.KeysView`
* :class:`collections.abc.ItemsView`
* :class:`collections.abc.ValuesView`
* :class:`contextlib.AbstractContextManager`
* :class:`contextlib.AbstractAsyncContextManager`
* :class:`dataclasses.Field`
* :class:`functools.cached_property`
* :class:`functools.partialmethod`
* :class:`os.PathLike`
* :class:`queue.LifoQueue`
* :class:`queue.Queue`
* :class:`queue.PriorityQueue`
* :class:`queue.SimpleQueue`
* :ref:`re.Pattern <re-objects>`
* :ref:`re.Match <match-objects>`
* :class:`shelve.BsdDbShelf`
* :class:`shelve.DbfilenameShelf`
* :class:`shelve.Shelf`
* :class:`types.MappingProxyType`
* :class:`weakref.WeakKeyDictionary`
* :class:`weakref.WeakMethod`
* :class:`weakref.WeakSet`
* :class:`weakref.WeakValueDictionary`



Special Attributes of ``GenericAlias`` objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All parameterized generics implement special read-only attributes.

.. attribute:: genericalias.__origin__

   This attribute points at the non-parameterized generic class::

      >>> list[int].__origin__
      <class 'list'>


.. attribute:: genericalias.__args__

   This attribute is a :class:`tuple` (possibly of length 1) of generic
   types passed to the original :meth:`~object.__class_getitem__` of the
   generic class::

      >>> dict[str, list[int]].__args__
      (<class 'str'>, list[int])


.. attribute:: genericalias.__parameters__

   This attribute is a lazily computed tuple (possibly empty) of unique type
   variables found in ``__args__``::

      >>> from typing import TypeVar

      >>> T = TypeVar('T')
      >>> list[T].__parameters__
      (~T,)


   .. note::
      A ``GenericAlias`` object with :class:`typing.ParamSpec` parameters may not
      have correct ``__parameters__`` after substitution because
      :class:`typing.ParamSpec` is intended primarily for static type checking.


.. attribute:: genericalias.__unpacked__

   A boolean that is true if the alias has been unpacked using the
   ``*`` operator (see :data:`~typing.TypeVarTuple`).

   .. versionadded:: 3.11


.. seealso::

   :pep:`484` - Type Hints
      Introducing Python's framework for type annotations.

   :pep:`585` - Type Hinting Generics In Standard Collections
      Introducing the ability to natively parameterize standard-library
      classes, provided they implement the special class method
      :meth:`~object.__class_getitem__`.

   :ref:`Generics`, :ref:`user-defined generics <user-defined-generics>` and :class:`typing.Generic`
      Documentation on how to implement generic classes that can be
      parameterized at runtime and understood by static type-checkers.

.. versionadded:: 3.9


.. _types-union:

Union Type
----------

.. index::
   pair: object; Union
   pair: union; type

A union object holds the value of the ``|`` (bitwise or) operation on
multiple :ref:`type objects <bltin-type-objects>`.  These types are intended
primarily for :term:`type annotations <annotation>`. The union type expression
enables cleaner type hinting syntax compared to subscripting :class:`typing.Union`.

.. describe:: X | Y | ...

   Defines a union object which holds types *X*, *Y*, and so forth. ``X | Y``
   means either X or Y.  It is equivalent to ``typing.Union[X, Y]``.
   For example, the following function expects an argument of type
   :class:`int` or :class:`float`::

      def square(number: int | float) -> int | float:
          return number ** 2

   .. note::

      The ``|`` operator cannot be used at runtime to define unions where one or
      more members is a forward reference. For example, ``int | "Foo"``, where
      ``"Foo"`` is a reference to a class not yet defined, will fail at
      runtime. For unions which include forward references, present the
      whole expression as a string, e.g. ``"int | Foo"``.

.. describe:: union_object == other

   Union objects can be tested for equality with other union objects.  Details:

   * Unions of unions are flattened::

       (int | str) | float == int | str | float

   * Redundant types are removed::

       int | str | int == int | str

   * When comparing unions, the order is ignored::

      int | str == str | int

   * It creates instances of :class:`typing.Union`::

      int | str == typing.Union[int, str]
      type(int | str) is typing.Union

   * Optional types can be spelled as a union with ``None``::

      str | None == typing.Optional[str]

.. describe:: isinstance(obj, union_object)
.. describe:: issubclass(obj, union_object)

   Calls to :func:`isinstance` and :func:`issubclass` are also supported with a
   union object::

      >>> isinstance("", int | str)
      True

   However, :ref:`parameterized generics <types-genericalias>` in
   union objects cannot be checked::

      >>> isinstance(1, int | list[int])  # short-circuit evaluation
      True
      >>> isinstance([1], int | list[int])
      Traceback (most recent call last):
        ...
      TypeError: isinstance() argument 2 cannot be a parameterized generic

The user-exposed type for the union object can be accessed from
:class:`typing.Union` and used for :func:`isinstance` checks::

   >>> import typing
   >>> isinstance(int | str, typing.Union)
   True
   >>> typing.Union()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: cannot create 'typing.Union' instances

.. note::
   The :meth:`!__or__` method for type objects was added to support the syntax
   ``X | Y``.  If a metaclass implements :meth:`!__or__`, the Union may
   override it:

   .. doctest::

      >>> class M(type):
      ...     def __or__(self, other):
      ...         return "Hello"
      ...
      >>> class C(metaclass=M):
      ...     pass
      ...
      >>> C | int
      'Hello'
      >>> int | C
      int | C

.. seealso::

   :pep:`604` -- PEP proposing the ``X | Y`` syntax and the Union type.

.. versionadded:: 3.10

.. versionchanged:: 3.14

   Union objects are now instances of :class:`typing.Union`. Previously, they were instances
   of :class:`types.UnionType`, which remains an alias for :class:`typing.Union`.


.. _typesother:

Other Built-in Types
====================

The interpreter supports several other kinds of objects. Most of these support
only one or two operations.


.. _typesmodules:

Modules
-------

The only special operation on a module is attribute access: ``m.name``, where
*m* is a module and *name* accesses a name defined in *m*'s symbol table.
Module attributes can be assigned to.  (Note that the :keyword:`import`
statement is not, strictly speaking, an operation on a module object; ``import
foo`` does not require a module object named *foo* to exist, rather it requires
an (external) *definition* for a module named *foo* somewhere.)

A special attribute of every module is :attr:`~object.__dict__`. This is the
dictionary containing the module's symbol table. Modifying this dictionary will
actually change the module's symbol table, but direct assignment to the
:attr:`~object.__dict__` attribute is not possible (you can write
``m.__dict__['a'] = 1``, which defines ``m.a`` to be ``1``, but you can't write
``m.__dict__ = {}``).  Modifying :attr:`~object.__dict__` directly is
not recommended.

Modules built into the interpreter are written like this: ``<module 'sys'
(built-in)>``.  If loaded from a file, they are written as ``<module 'os' from
'/usr/local/lib/pythonX.Y/os.pyc'>``.


.. _typesobjects:

Classes and Class Instances
---------------------------

See :ref:`objects` and :ref:`class` for these.


.. _typesfunctions:

Functions
---------

Function objects are created by function definitions.  The only operation on a
function object is to call it: ``func(argument-list)``.

There are really two flavors of function objects: built-in functions and
user-defined functions.  Both support the same operation (to call the function),
but the implementation is different, hence the different object types.

See :ref:`function` for more information.


.. _typesmethods:

Methods
-------

.. index:: pair: object; method

Methods are functions that are called using the attribute notation.
There are two flavors: :ref:`built-in methods <builtin-methods>`
(such as :meth:`~list.append` on lists)
and :ref:`class instance methods <instance-methods>`.
Built-in methods are described with the types that support them.

If you access a method (a function defined in a class namespace) through an
instance, you get a special object: a :dfn:`bound method` (also called
:ref:`instance method <instance-methods>`) object. When called, it will add
the ``self`` argument
to the argument list.  Bound methods have two special read-only attributes:
:attr:`m.__self__ <method.__self__>` is the object on which the method
operates, and :attr:`m.__func__ <method.__func__>` is
the function implementing the method.  Calling ``m(arg-1, arg-2, ..., arg-n)``
is completely equivalent to calling ``m.__func__(m.__self__, arg-1, arg-2, ...,
arg-n)``.

Like :ref:`function objects <user-defined-funcs>`, bound method objects support
getting arbitrary
attributes.  However, since method attributes are actually stored on the
underlying function object (:attr:`method.__func__`), setting method attributes on
bound methods is disallowed.  Attempting to set an attribute on a method
results in an :exc:`AttributeError` being raised.  In order to set a method
attribute, you need to explicitly set it on the underlying function object:

.. doctest::

   >>> class C:
   ...     def method(self):
   ...         pass
   ...
   >>> c = C()
   >>> c.method.whoami = 'my name is method'  # can't set on the method
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'method' object has no attribute 'whoami'
   >>> c.method.__func__.whoami = 'my name is method'
   >>> c.method.whoami
   'my name is method'

See :ref:`instance-methods` for more information.


.. index:: object; code, code object

.. _bltin-code-objects:

Code Objects
------------

.. index::
   pair: built-in function; compile
   single: __code__ (function object attribute)

Code objects are used by the implementation to represent "pseudo-compiled"
executable Python code such as a function body. They differ from function
objects because they don't contain a reference to their global execution
environment.  Code objects are returned by the built-in :func:`compile` function
and can be extracted from function objects through their
:attr:`~function.__code__` attribute. See also the :mod:`code` module.

Accessing :attr:`~function.__code__` raises an :ref:`auditing event <auditing>`
``object.__getattr__`` with arguments ``obj`` and ``"__code__"``.

.. index::
   pair: built-in function; exec
   pair: built-in function; eval

A code object can be executed or evaluated by passing it (instead of a source
string) to the :func:`exec` or :func:`eval`  built-in functions.

See :ref:`types` for more information.


.. _bltin-type-objects:

Type Objects
------------

.. index::
   pair: built-in function; type
   pair: module; types

Type objects represent the various object types.  An object's type is accessed
by the built-in function :func:`type`.  There are no special operations on
types.  The standard module :mod:`types` defines names for all standard built-in
types.

Types are written like this: ``<class 'int'>``.


.. _bltin-null-object:

The Null Object
---------------

This object is returned by functions that don't explicitly return a value.  It
supports no special operations.  There is exactly one null object, named
``None`` (a built-in name).  ``type(None)()`` produces the same singleton.

It is written as ``None``.


.. index:: single: ...; ellipsis literal
.. _bltin-ellipsis-object:

The Ellipsis Object
-------------------

This object is commonly used to indicate that something is omitted.
It supports no special operations.  There is exactly one ellipsis object, named
:const:`Ellipsis` (a built-in name).  ``type(Ellipsis)()`` produces the
:const:`Ellipsis` singleton.

It is written as ``Ellipsis`` or ``...``.

In typical use, ``...`` as the ``Ellipsis`` object appears in a few different
places, for instance:

- In type annotations, such as :ref:`callable arguments <annotating-callables>`
  or :ref:`tuple elements <annotating-tuples>`.

- As the body of a function instead of a :ref:`pass statement <tut-pass>`.

- In third-party libraries, such as `Numpy's slicing and striding
  <https://numpy.org/doc/stable/user/basics.indexing.html#slicing-and-striding>`_.

Python also uses three dots in ways that are not ``Ellipsis`` objects, for instance:

- Doctest's :const:`ELLIPSIS <doctest.ELLIPSIS>`, as a pattern for missing content.

- The default Python prompt of the :term:`interactive` shell when partial input is incomplete.

Lastly, the Python documentation often uses three dots in conventional English
usage to mean omitted content, even in code examples that also use them as the
``Ellipsis``.


.. _bltin-notimplemented-object:

The NotImplemented Object
-------------------------

This object is returned from comparisons and binary operations when they are
asked to operate on types they don't support. See :ref:`comparisons` for more
information.  There is exactly one :data:`NotImplemented` object.
:code:`type(NotImplemented)()` produces the singleton instance.

It is written as :code:`NotImplemented`.


.. _typesinternal:

Internal Objects
----------------

See :ref:`types` for this information.  It describes
:ref:`stack frame objects <frame-objects>`,
:ref:`traceback objects <traceback-objects>`, and slice objects.


.. _specialattrs:

Special Attributes
==================

The implementation adds a few special read-only attributes to several object
types, where they are relevant.  Some of these are not reported by the
:func:`dir` built-in function.


.. attribute:: definition.__name__

   The name of the class, function, method, descriptor, or
   generator instance.


.. attribute:: definition.__qualname__

   The :term:`qualified name` of the class, function, method, descriptor,
   or generator instance.

   .. versionadded:: 3.3


.. attribute:: definition.__module__

   The name of the module in which a class or function was defined.


.. attribute:: definition.__doc__

   The documentation string of a class or function, or ``None`` if undefined.


.. attribute:: definition.__type_params__

   The :ref:`type parameters <type-params>` of generic classes, functions,
   and :ref:`type aliases <type-aliases>`. For classes and functions that
   are not generic, this will be an empty tuple.

   .. versionadded:: 3.12


.. _int_max_str_digits:

Integer string conversion length limitation
===========================================

CPython has a global limit for converting between :class:`int` and :class:`str`
to mitigate denial of service attacks. This limit *only* applies to decimal or
other non-power-of-two number bases. Hexadecimal, octal, and binary conversions
are unlimited. The limit can be configured.

The :class:`int` type in CPython is an arbitrary length number stored in binary
form (commonly known as a "bignum"). There exists no algorithm that can convert
a string to a binary integer or a binary integer to a string in linear time,
*unless* the base is a power of 2. Even the best known algorithms for base 10
have sub-quadratic complexity. Converting a large value such as ``int('1' *
500_000)`` can take over a second on a fast CPU.

Limiting conversion size offers a practical way to avoid :cve:`2020-10735`.

The limit is applied to the number of digit characters in the input or output
string when a non-linear conversion algorithm would be involved.  Underscores
and the sign are not counted towards the limit.

When an operation would exceed the limit, a :exc:`ValueError` is raised:

.. doctest::

   >>> import sys
   >>> sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
   >>> _ = int('2' * 5432)
   Traceback (most recent call last):
   ...
   ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5432 digits; use sys.set_int_max_str_digits() to increase the limit
   >>> i = int('2' * 4300)
   >>> len(str(i))
   4300
   >>> i_squared = i*i
   >>> len(str(i_squared))
   Traceback (most recent call last):
   ...
   ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
   >>> len(hex(i_squared))
   7144
   >>> assert int(hex(i_squared), base=16) == i*i  # Hexadecimal is unlimited.

The default limit is 4300 digits as provided in
:data:`sys.int_info.default_max_str_digits <sys.int_info>`.
The lowest limit that can be configured is 640 digits as provided in
:data:`sys.int_info.str_digits_check_threshold <sys.int_info>`.

Verification:

.. doctest::

   >>> import sys
   >>> assert sys.int_info.default_max_str_digits == 4300, sys.int_info
   >>> assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
   >>> msg = int('578966293710682886880994035146873798396722250538762761564'
   ...           '9252925514383915483333812743580549779436104706260696366600'
   ...           '571186405732').to_bytes(53, 'big')
   ...

.. versionadded:: 3.11

Affected APIs
-------------

The limitation only applies to potentially slow conversions between :class:`int`
and :class:`str` or :class:`bytes`:

* ``int(string)`` with default base 10.
* ``int(string, base)`` for all bases that are not a power of 2.
* ``str(integer)``.
* ``repr(integer)``.
* any other string conversion to base 10, for example ``f"{integer}"``,
  ``"{}".format(integer)``, or ``b"%d" % integer``.

The limitations do not apply to functions with a linear algorithm:

* ``int(string, base)`` with base 2, 4, 8, 16, or 32.
* :func:`int.from_bytes` and :func:`int.to_bytes`.
* :func:`hex`, :func:`oct`, :func:`bin`.
* :ref:`formatspec` for hex, octal, and binary numbers.
* :class:`str` to :class:`float`.
* :class:`str` to :class:`decimal.Decimal`.

Configuring the limit
---------------------

Before Python starts up you can use an environment variable or an interpreter
command line flag to configure the limit:

* :envvar:`PYTHONINTMAXSTRDIGITS`, e.g.
  ``PYTHONINTMAXSTRDIGITS=640 python3`` to set the limit to 640 or
  ``PYTHONINTMAXSTRDIGITS=0 python3`` to disable the limitation.
* :option:`-X int_max_str_digits <-X>`, e.g.
  ``python3 -X int_max_str_digits=640``
* :data:`sys.flags.int_max_str_digits` contains the value of
  :envvar:`PYTHONINTMAXSTRDIGITS` or :option:`-X int_max_str_digits <-X>`.
  If both the env var and the ``-X`` option are set, the ``-X`` option takes
  precedence. A value of *-1* indicates that both were unset, thus a value of
  :data:`sys.int_info.default_max_str_digits` was used during initialization.

From code, you can inspect the current limit and set a new one using these
:mod:`sys` APIs:

* :func:`sys.get_int_max_str_digits` and :func:`sys.set_int_max_str_digits` are
  a getter and setter for the interpreter-wide limit. Subinterpreters have
  their own limit.

Information about the default and minimum can be found in :data:`sys.int_info`:

* :data:`sys.int_info.default_max_str_digits <sys.int_info>` is the compiled-in
  default limit.
* :data:`sys.int_info.str_digits_check_threshold <sys.int_info>` is the lowest
  accepted value for the limit (other than 0 which disables it).

.. versionadded:: 3.11

.. caution::

   Setting a low limit *can* lead to problems. While rare, code exists that
   contains integer constants in decimal in their source that exceed the
   minimum threshold. A consequence of setting the limit is that Python source
   code containing decimal integer literals longer than the limit will
   encounter an error during parsing, usually at startup time or import time or
   even at installation time - anytime an up to date ``.pyc`` does not already
   exist for the code. A workaround for source that contains such large
   constants is to convert them to ``0x`` hexadecimal form as it has no limit.

   Test your application thoroughly if you use a low limit. Ensure your tests
   run with the limit set early via the environment or flag so that it applies
   during startup and even during any installation step that may invoke Python
   to precompile ``.py`` sources to ``.pyc`` files.

Recommended configuration
-------------------------

The default :data:`sys.int_info.default_max_str_digits` is expected to be
reasonable for most applications. If your application requires a different
limit, set it from your main entry point using Python version agnostic code as
these APIs were added in security patch releases in versions before 3.12.

Example::

   >>> import sys
   >>> if hasattr(sys, "set_int_max_str_digits"):
   ...     upper_bound = 68000
   ...     lower_bound = 4004
   ...     current_limit = sys.get_int_max_str_digits()
   ...     if current_limit == 0 or current_limit > upper_bound:
   ...         sys.set_int_max_str_digits(upper_bound)
   ...     elif current_limit < lower_bound:
   ...         sys.set_int_max_str_digits(lower_bound)

If you need to disable it entirely, set it to ``0``.


.. rubric:: Footnotes

.. [1] Additional information on these special methods may be found in the Python
   Reference Manual (:ref:`customization`).

.. [2] As a consequence, the list ``[1, 2]`` is considered equal to ``[1.0, 2.0]``, and
   similarly for tuples.

.. [3] They must have since the parser can't tell the type of the operands.

.. [4] Cased characters are those with general category property being one of
   "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).

.. [5] To format only a tuple you should therefore provide a singleton tuple whose only
   element is the tuple to be formatted.

----

.. method:: bytes.replace(old, new, /, count=-1)
            bytearray.replace(old, new, /, count=-1)

   Return a copy of the sequence with all occurrences of subsequence *old*
   replaced by *new*.  If *count* is given, only the first *count* occurrences
   are replaced.  If *count* is not specified or ``-1``, then all occurrences
   are replaced.

   The subsequence to search for and its replacement may be any
   :term:`bytes-like object`.

   .. note::

      The bytearray version of this method does *not* operate in place - it
      always produces a new object, even if no changes were made.

   .. versionchanged:: 3.15
      *count* is now supported as a keyword argument.



----

.. class:: frozendict(**kwargs)
           frozendict(mapping, /, **kwargs)
           frozendict(iterable, /, **kwargs)

   Return a new frozen dictionary initialized from an optional positional
   argument and a possibly empty set of keyword arguments.

   A :class:`!frozendict` has a similar API to the :class:`dict` API, with the
   following differences:

   * :class:`!dict` has more methods than :class:`!frozendict`:

      * :meth:`!__delitem__`
      * :meth:`!__setitem__`
      * :meth:`~dict.clear`
      * :meth:`~dict.pop`
      * :meth:`~dict.popitem`
      * :meth:`~dict.setdefault`
      * :meth:`~dict.update`

   * A :class:`!frozendict` can be hashed with ``hash(frozendict)`` if all keys and
     values can be hashed.

   * ``frozendict |= other`` does not modify the :class:`!frozendict` in-place but
     creates a new frozen dictionary.

   :class:`!frozendict` is not a :class:`!dict` subclass but inherits directly
   from ``object``.

   Like dictionaries, frozendicts are :ref:`generic <generics>` over two types,
   signifying (respectively) the types of the frozendict's keys and values.

   .. classmethod:: fromkeys(iterable, value=None, /)

      Similar to :meth:`dict.fromkeys`, but call again the type constructor
      with an initialized :class:`frozendict` if the type is a
      :class:`frozendict` subclass or if the constructor returned a
      :class:`frozendict`.

   .. versionadded:: 3.15

