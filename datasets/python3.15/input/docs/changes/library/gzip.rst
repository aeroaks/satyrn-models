.. function:: open(filename, mode='rb', compresslevel=6, encoding=None, errors=None, newline=None)

   Open a gzip-compressed file in binary or text mode, returning a :term:`file
   object`.

   The *filename* argument can be an actual filename (a :class:`str` or
   :class:`bytes` object), or an existing file object to read from or write to.

   The *mode* argument can be any of ``'r'``, ``'rb'``, ``'a'``, ``'ab'``,
   ``'w'``, ``'wb'``, ``'x'`` or ``'xb'`` for binary mode, or ``'rt'``,
   ``'at'``, ``'wt'``, or ``'xt'`` for text mode. The default is ``'rb'``.

   The *compresslevel* argument is an integer from 0 to 9, as for the
   :class:`GzipFile` constructor.

   For binary mode, this function is equivalent to the :class:`GzipFile`
   constructor: ``GzipFile(filename, mode, compresslevel)``. In this case, the
   *encoding*, *errors* and *newline* arguments must not be provided.

   For text mode, a :class:`GzipFile` object is created, and wrapped in an
   :class:`io.TextIOWrapper` instance with the specified encoding, error
   handling behavior, and line ending(s).

   .. versionchanged:: 3.3
      Added support for *filename* being a file object, support for text mode,
      and the *encoding*, *errors* and *newline* arguments.

   .. versionchanged:: 3.4
      Added support for the ``'x'``, ``'xb'`` and ``'xt'`` modes.

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. versionchanged:: 3.15
      The default compression level was reduced to 6 (down from 9).
      It is the default level used by most compression tools and a better
      tradeoff between speed and performance.


----

.. class:: GzipFile(filename=None, mode=None, compresslevel=6, fileobj=None, mtime=None)

   Constructor for the :class:`GzipFile` class, which simulates most of the
   methods of a :term:`file object`, with the exception of the :meth:`~io.IOBase.truncate`
   method.  At least one of *fileobj* and *filename* must be given a non-trivial
   value.

   The new class instance is based on *fileobj*, which can be a regular file, an
   :class:`io.BytesIO` object, or any other object which simulates a file.  It
   defaults to ``None``, in which case *filename* is opened to provide a file
   object.

   When *fileobj* is not ``None``, the *filename* argument is only used to be
   included in the :program:`gzip` file header, which may include the original
   filename of the uncompressed file.  It defaults to the filename of *fileobj*, if
   discernible; otherwise, it defaults to the empty string, and in this case the
   original filename is not included in the header.

   The *mode* argument can be any of ``'r'``, ``'rb'``, ``'a'``, ``'ab'``, ``'w'``,
   ``'wb'``, ``'x'``, or ``'xb'``, depending on whether the file will be read or
   written.  The default is the mode of *fileobj* if discernible; otherwise, the
   default is ``'rb'``.  In future Python releases the mode of *fileobj* will
   not be used.  It is better to always specify *mode* for writing.

   Note that the file is always opened in binary mode. To open a compressed file
   in text mode, use :func:`.open` (or wrap your :class:`GzipFile` with an
   :class:`io.TextIOWrapper`).

   The *compresslevel* argument is an integer from ``0`` to ``9`` controlling
   the level of compression; ``1`` is fastest and produces the least
   compression, and ``9`` is slowest and produces the most compression. ``0``
   is no compression. The default is ``6``.

   The optional *mtime* argument is the timestamp requested by gzip. The time
   is in Unix format, i.e., seconds since 00:00:00 UTC, January 1, 1970. Set
   *mtime* to ``0`` to generate a compressed stream that does not depend on
   creation time. If *mtime* is omitted or ``None``, the current time is used;
   however, if the current time is outside the range 00:00:00 UTC, January 1,
   1970 through 06:28:15 UTC, February 7, 2106, or explicitly passed *mtime*
   argument is outside the range ``0`` to ``2**32-1``, then the value ``0``
   is used instead.

   See below for the :attr:`mtime` attribute that is set when decompressing.

   Calling a :class:`GzipFile` object's :meth:`!close` method does not close
   *fileobj*, since you might wish to append more material after the compressed
   data.  This also allows you to pass an :class:`io.BytesIO` object opened for
   writing as *fileobj*, and retrieve the resulting memory buffer using the
   :class:`io.BytesIO` object's :meth:`~io.BytesIO.getvalue` method.

   :class:`GzipFile` supports the :class:`io.BufferedIOBase` interface,
   including iteration and the :keyword:`with` statement.  Only the
   :meth:`~io.IOBase.truncate` method isn't implemented.

   :class:`GzipFile` also provides the following method and attribute:

   .. method:: peek(n)

      Read *n* uncompressed bytes without advancing the file position.
      The number of bytes returned may be more or less than requested.

      .. note:: While calling :meth:`peek` does not change the file position of
         the :class:`GzipFile`, it may change the position of the underlying
         file object (e.g. if the :class:`GzipFile` was constructed with the
         *fileobj* parameter).

      .. versionadded:: 3.2

   .. attribute:: mode

      ``'rb'`` for reading and ``'wb'`` for writing.

      .. versionchanged:: 3.13
         In previous versions it was an integer ``1`` or ``2``.

   .. attribute:: mtime

      When decompressing, this attribute is set to the last timestamp in the most
      recently read header.  It is an integer, holding the number of seconds
      since the Unix epoch (00:00:00 UTC, January 1, 1970).
      The initial value before reading any headers is ``None``.

   .. attribute:: name

      The path to the gzip file on disk, as a :class:`str` or :class:`bytes`.
      Equivalent to the output of :func:`os.fspath` on the original input path,
      with no other normalization, resolution or expansion.

   .. versionchanged:: 3.1
      Support for the :keyword:`with` statement was added, along with the
      *mtime* constructor argument and :attr:`mtime` attribute.

   .. versionchanged:: 3.2
      Support for zero-padded and unseekable files was added.

   .. versionchanged:: 3.3
      The :meth:`io.BufferedIOBase.read1` method is now implemented.

   .. versionchanged:: 3.4
      Added support for the ``'x'`` and ``'xb'`` modes.

   .. versionchanged:: 3.5
      Added support for writing arbitrary
      :term:`bytes-like objects <bytes-like object>`.
      The :meth:`~io.BufferedIOBase.read` method now accepts an argument of
      ``None``.

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. deprecated:: 3.9
      Opening :class:`GzipFile` for writing without specifying the *mode*
      argument is deprecated.

   .. versionchanged:: 3.12
      Remove the ``filename`` attribute, use the :attr:`~GzipFile.name`
      attribute instead.

   .. versionchanged:: 3.15
      The default compression level was reduced to 6 (down from 9).
      It is the default level used by most compression tools and a better
      tradeoff between speed and performance.



----

.. function:: compress(data, compresslevel=6, *, mtime=0)

   Compress the *data*, returning a :class:`bytes` object containing
   the compressed data.  *compresslevel* and *mtime* have the same meaning as in
   the :class:`GzipFile` constructor above,
   but *mtime* defaults to 0 for reproducible output.

   .. versionadded:: 3.2
   .. versionchanged:: 3.8
      Added the *mtime* parameter for reproducible output.
   .. versionchanged:: 3.11
      Speed is improved by compressing all data at once instead of in a
      streamed fashion. Calls with *mtime* set to ``0`` are delegated to
      :func:`zlib.compress` for better speed. In this situation the
      output may contain a gzip header "OS" byte value other than 255
      "unknown" as supplied by the underlying zlib implementation.

   .. versionchanged:: 3.13
      The gzip header OS byte is guaranteed to be set to 255 when this function
      is used as was the case in 3.10 and earlier.
   .. versionchanged:: 3.14
      The *mtime* parameter now defaults to 0 for reproducible output.
      For the previous behaviour of using the current time,
      pass ``None`` to *mtime*.
   .. versionchanged:: 3.15
      The default compression level was reduced to 6 (down from 9).
      It is the default level used by most compression tools and a better
      tradeoff between speed and performance.
