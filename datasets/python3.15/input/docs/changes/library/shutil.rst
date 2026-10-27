.. function:: make_archive(base_name, format, [root_dir, [base_dir, [verbose, [dry_run, [owner, [group, [logger]]]]]]])

   Create an archive file (such as zip or tar) and return its name.

   *base_name* is a string or :term:`path-like object` specifying the name of
   the file to create, including the path, minus any format-specific extension.

   *format* is the archive format: one of
   "zip" (if the :mod:`zlib` module is available), "tar", "gztar" (if the
   :mod:`zlib` module is available), "bztar" (if the :mod:`bz2` module is
   available), "xztar" (if the :mod:`lzma` module is available), or "zstdtar"
   (if the :mod:`compression.zstd` module is available).

   *root_dir* is a string or :term:`path-like object` specifying a directory
   that will be the root directory of the archive, all paths in the archive
   will be relative to it; for example, we typically chdir into *root_dir*
   before creating the archive.

   *base_dir* is a string or :term:`path-like object` specifying a directory
   where we start archiving from; i.e. *base_dir* will be the common prefix of
   all files and directories in the archive.  *base_dir* must be given relative
   to *root_dir*.  See :ref:`shutil-archiving-example-with-basedir` for how to
   use *base_dir* and *root_dir* together.

   *root_dir* and *base_dir* both default to the current directory.

   If *dry_run* is true, no archive is created, but the operations that would be
   executed are logged to *logger*.

   *owner* and *group* are used when creating a tar archive. By default,
   uses the current owner and group.

   *logger* must be an object compatible with :pep:`282`, usually an instance of
   :class:`logging.Logger`.

   The *verbose* argument is unused and deprecated.

   .. audit-event:: shutil.make_archive base_name,format,root_dir,base_dir shutil.make_archive

   .. note::

      This function is not thread-safe when custom archivers registered
      with :func:`register_archive_format` do not support the *root_dir*
      argument.  In this case it
      temporarily changes the current working directory of the process
      to *root_dir* to perform archiving.

   .. versionchanged:: 3.8
      The modern pax (POSIX.1-2001) format is now used instead of
      the legacy GNU format for archives created with ``format="tar"``.

   .. versionchanged:: 3.10.6
      This function is now made thread-safe during creation of standard
      ``.zip`` and tar archives.

   .. versionchanged:: 3.15
      Accepts a :term:`path-like object` for *base_name*, *root_dir* and
      *base_dir*.
