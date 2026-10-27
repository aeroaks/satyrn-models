.. function:: open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)

   Return a :class:`TarFile` object for the pathname *name*. For detailed
   information on :class:`TarFile` objects and the keyword arguments that are
   allowed, see :ref:`tarfile-objects`.

   *mode* has to be a string of the form ``'filemode[:compression]'``, it defaults
   to ``'r'``. Here is a full list of mode combinations:

   +------------------+---------------------------------------------+
   | mode             | action                                      |
   +==================+=============================================+
   | ``'r'`` or       | Open for reading with transparent           |
   | ``'r:*'``        | compression (recommended).                  |
   +------------------+---------------------------------------------+
   | ``'r:'``         | Open for reading exclusively without        |
   |                  | compression.                                |
   +------------------+---------------------------------------------+
   | ``'r:gz'``       | Open for reading with gzip compression.     |
   +------------------+---------------------------------------------+
   | ``'r:bz2'``      | Open for reading with bzip2 compression.    |
   +------------------+---------------------------------------------+
   | ``'r:xz'``       | Open for reading with lzma compression.     |
   +------------------+---------------------------------------------+
   | ``'r:zst'``      | Open for reading with Zstandard compression.|
   +------------------+---------------------------------------------+
   | ``'x'`` or       | Create a tarfile exclusively without        |
   | ``'x:'``         | compression.                                |
   |                  | Raise a :exc:`FileExistsError` exception    |
   |                  | if it already exists.                       |
   +------------------+---------------------------------------------+
   | ``'x:gz'``       | Create a tarfile with gzip compression.     |
   |                  | Raise a :exc:`FileExistsError` exception    |
   |                  | if it already exists.                       |
   +------------------+---------------------------------------------+
   | ``'x:bz2'``      | Create a tarfile with bzip2 compression.    |
   |                  | Raise a :exc:`FileExistsError` exception    |
   |                  | if it already exists.                       |
   +------------------+---------------------------------------------+
   | ``'x:xz'``       | Create a tarfile with lzma compression.     |
   |                  | Raise a :exc:`FileExistsError` exception    |
   |                  | if it already exists.                       |
   +------------------+---------------------------------------------+
   | ``'x:zst'``      | Create a tarfile with Zstandard compression.|
   |                  | Raise a :exc:`FileExistsError` exception    |
   |                  | if it already exists.                       |
   +------------------+---------------------------------------------+
   | ``'a'`` or       | Open for appending with no compression. The |
   | ``'a:'``         | file is created if it does not exist.       |
   +------------------+---------------------------------------------+
   | ``'w'`` or       | Open for uncompressed writing.              |
   | ``'w:'``         |                                             |
   +------------------+---------------------------------------------+
   | ``'w:gz'``       | Open for gzip compressed writing.           |
   +------------------+---------------------------------------------+
   | ``'w:bz2'``      | Open for bzip2 compressed writing.          |
   +------------------+---------------------------------------------+
   | ``'w:xz'``       | Open for lzma compressed writing.           |
   +------------------+---------------------------------------------+
   | ``'w:zst'``      | Open for Zstandard compressed writing.      |
   +------------------+---------------------------------------------+

   Note that ``'a:gz'``, ``'a:bz2'`` or ``'a:xz'`` is not possible. If *mode*
   is not suitable to open a certain (compressed) file for reading,
   :exc:`ReadError` is raised. Use *mode* ``'r'`` to avoid this.  If a
   compression method is not supported, :exc:`CompressionError` is raised.

   If *fileobj* is specified, it is used as an alternative to a :term:`file object`
   opened in binary mode for *name*. It is supposed to be at position 0.

   For modes ``'w:gz'``, ``'x:gz'``, ``'w|gz'``, ``'w:bz2'``, ``'x:bz2'``,
   ``'w|bz2'``, :func:`tarfile.open` accepts the keyword argument
   *compresslevel* (default ``6``) to specify the compression level of the file.

   For modes ``'w:xz'``, ``'x:xz'`` and ``'w|xz'``, :func:`tarfile.open` accepts the
   keyword argument *preset* to specify the compression level of the file.

   For modes ``'w:zst'``, ``'x:zst'`` and ``'w|zst'``, :func:`tarfile.open`
   accepts the keyword argument *level* to specify the compression level of
   the file. The keyword argument *options* may also be passed, providing
   advanced Zstandard compression parameters described by
   :class:`~compression.zstd.CompressionParameter`. The keyword argument
   *zstd_dict* can be passed to provide a :class:`~compression.zstd.ZstdDict`,
   a Zstandard dictionary used to improve compression of smaller amounts of
   data.

   For modes ``'w:gz'`` and ``'w|gz'``, :func:`tarfile.open` accepts the
   keyword argument *mtime* to create a gzip archive header with that mtime. By
   default, the mtime is set to the time of creation of the archive. Use
   *mtime* ``0`` to generate a compressed stream that does not depend on
   creation time, for reproducible output.

   For special purposes, there is a second format for *mode*:
   ``'filemode|[compression]'``.  :func:`tarfile.open` will return a :class:`TarFile`
   object that processes its data as a stream of blocks.  No random seeking will
   be done on the file. If given, *fileobj* may be any object that has a
   :meth:`~io.RawIOBase.read` or :meth:`~io.RawIOBase.write` method
   (depending on the *mode*) that works with bytes.
   *bufsize* specifies the blocksize and defaults to ``20 * 512`` bytes.
   Use this variant in combination with e.g. ``sys.stdin.buffer``, a socket
   :term:`file object` or a tape device.
   However, such a :class:`TarFile` object is limited in that it does
   not allow random access, see :ref:`tar-examples`.  The currently
   possible modes:

   +-------------+--------------------------------------------+
   | Mode        | Action                                     |
   +=============+============================================+
   | ``'r|*'``   | Open a *stream* of tar blocks for reading  |
   |             | with transparent compression.              |
   +-------------+--------------------------------------------+
   | ``'r|'``    | Open a *stream* of uncompressed tar blocks |
   |             | for reading.                               |
   +-------------+--------------------------------------------+
   | ``'r|gz'``  | Open a gzip compressed *stream* for        |
   |             | reading.                                   |
   +-------------+--------------------------------------------+
   | ``'r|bz2'`` | Open a bzip2 compressed *stream* for       |
   |             | reading.                                   |
   +-------------+--------------------------------------------+
   | ``'r|xz'``  | Open an lzma compressed *stream* for       |
   |             | reading.                                   |
   +-------------+--------------------------------------------+
   | ``'r|zst'`` | Open a Zstandard compressed *stream* for   |
   |             | reading.                                   |
   +-------------+--------------------------------------------+
   | ``'w|'``    | Open an uncompressed *stream* for writing. |
   +-------------+--------------------------------------------+
   | ``'w|gz'``  | Open a gzip compressed *stream* for        |
   |             | writing.                                   |
   +-------------+--------------------------------------------+
   | ``'w|bz2'`` | Open a bzip2 compressed *stream* for       |
   |             | writing.                                   |
   +-------------+--------------------------------------------+
   | ``'w|xz'``  | Open an lzma compressed *stream* for       |
   |             | writing.                                   |
   +-------------+--------------------------------------------+
   | ``'w|zst'`` | Open a Zstandard compressed *stream* for   |
   |             | writing.                                   |
   +-------------+--------------------------------------------+

   .. versionchanged:: 3.5
      The ``'x'`` (exclusive creation) mode was added.

   .. versionchanged:: 3.6
      The *name* parameter accepts a :term:`path-like object`.

   .. versionchanged:: 3.12
      The *compresslevel* keyword argument also works for streams.

   .. versionchanged:: 3.14
      The *preset* keyword argument also works for streams.

   .. versionchanged:: 3.15
      The default compression level was reduced to 6 (down from 9).
      It is the default level used by most compression tools and a better
      tradeoff between speed and performance.


----

.. exception:: LinkFallbackError

   Raised to refuse emulating a link (hard or symbolic) by extracting another
   archive member, when that member would be rejected by the filter location.
   The exception that was raised to reject the replacement member is available
   as :attr:`!BaseException.__context__`.

   .. versionadded:: 3.15



----

.. function:: tar_filter(member, path)

  Implements the ``'tar'`` filter.

  - Strip leading slashes (``/`` and :data:`os.sep`) from filenames.
  - :ref:`Refuse <tarfile-extraction-refuse>` to extract files with absolute
    paths (in case the name is absolute
    even after stripping slashes, e.g. ``C:/foo`` on Windows).
    This raises :class:`~tarfile.AbsolutePathError`.
  - Normalize filenames (:attr:`TarInfo.name`) that contain ``..`` components
    using :func:`os.path.normpath`.
    Note that this removes internal ``..`` components, which may change the
    meaning of the name if it traverses symbolic links.
  - :ref:`Refuse <tarfile-extraction-refuse>` to extract files whose absolute
    path (after following symlinks) would end up outside the destination.
    This raises :class:`~tarfile.OutsideDestinationError`.
  - :ref:`Refuse <tarfile-extraction-refuse>` to extract links (hard or soft)
    whose name refers to the destination directory itself.
    This raises :class:`~tarfile.OutsideDestinationError`.
    Note that such files are refused even on platforms that do not support
    symbolic links.
  - Clear high mode bits (setuid, setgid, sticky) and group/other write bits
    (:const:`~stat.S_IWGRP` | :const:`~stat.S_IWOTH`).

  Return the modified ``TarInfo`` member.

  .. versionchanged:: 3.15

     Filenames containing ``..`` components are now normalized.


----

.. function:: data_filter(member, path)

  Implements the ``'data'`` filter.
  In addition to what ``tar_filter`` does:

  - Normalize link targets (:attr:`TarInfo.linkname`) using
    :func:`os.path.normpath`.
    Note that this removes internal ``..`` components, which may change the
    meaning of the link if the path in :attr:`!TarInfo.linkname` traverses
    symbolic links.

  - :ref:`Refuse <tarfile-extraction-refuse>` to extract links (hard or soft)
    that link to absolute paths, or ones that link outside the destination.

    This raises :class:`~tarfile.AbsoluteLinkError` or
    :class:`~tarfile.LinkOutsideDestinationError`.

    Note that such files are refused even on platforms that do not support
    symbolic links.

  - :ref:`Refuse <tarfile-extraction-refuse>` to extract device files
    (including pipes).
    This raises :class:`~tarfile.SpecialFileError`.

  - For regular files, including hard links:

    - Set the owner read and write permissions
      (:const:`~stat.S_IRUSR` | :const:`~stat.S_IWUSR`).
    - Remove the group & other executable permission
      (:const:`~stat.S_IXGRP` | :const:`~stat.S_IXOTH`)
      if the owner doesn’t have it (:const:`~stat.S_IXUSR`).

  - For other files (directories), set ``mode`` to ``None``, so
    that extraction methods skip applying permission bits.
  - Set user and group info (``uid``, ``gid``, ``uname``, ``gname``)
    to ``None``, so that extraction methods skip setting it.

  Return the modified ``TarInfo`` member.

  Note that this filter does not block *all* dangerous archive features.
  See :ref:`tarfile-further-verification`  for details.

  .. versionchanged:: 3.15

     Link targets are now normalized.

