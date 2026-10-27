Python UTF-8 Mode
-----------------

.. versionadded:: 3.7
   See :pep:`540` for more details.

.. versionchanged:: 3.15

   Python UTF-8 mode is now enabled by default (:pep:`686`).
   It may be disabled by setting :envvar:`PYTHONUTF8=0 <PYTHONUTF8>` as
   an environment variable or by using the :option:`-X utf8=0 <-X>` command line option.

The Python UTF-8 Mode ignores the :term:`locale encoding` and forces the usage
of the UTF-8 encoding:

* Use UTF-8 as the :term:`filesystem encoding <filesystem encoding and error
  handler>`.
* :func:`sys.getfilesystemencoding` returns ``'utf-8'``.
* :func:`locale.getpreferredencoding` returns ``'utf-8'`` (the *do_setlocale*
  argument has no effect).
* :data:`sys.stdin`, :data:`sys.stdout`, and :data:`sys.stderr` all use
  UTF-8 as their text encoding, with the ``surrogateescape``
  :ref:`error handler <error-handlers>` being enabled for :data:`sys.stdin`
  and :data:`sys.stdout` (:data:`sys.stderr` continues to use
  ``backslashreplace`` as it does in the default locale-aware mode)
* On Unix, :func:`os.device_encoding` returns ``'utf-8'`` rather than the
  device encoding.

Note that the standard stream settings in UTF-8 mode can be overridden by
:envvar:`PYTHONIOENCODING` (just as they can be in the default locale-aware
mode).

As a consequence of the changes in those lower level APIs, other higher
level APIs also exhibit different default behaviours:

* Command line arguments, environment variables and filenames are decoded
  to text using the UTF-8 encoding.
* :func:`os.fsdecode` and :func:`os.fsencode` use the UTF-8 encoding.
* :func:`open`, :func:`io.open`, and :func:`codecs.open` use the UTF-8
  encoding by default. However, they still use the strict error handler by
  default so that attempting to open a binary file in text mode is likely
  to raise an exception rather than producing nonsense data.

The :ref:`Python UTF-8 Mode <utf8-mode>` is enabled by default.
It can be disabled using the :option:`-X utf8=0 <-X>` command line
option or the :envvar:`PYTHONUTF8=0 <PYTHONUTF8>` environment variable.
The Python UTF-8 Mode can only be disabled at Python startup. Its value
can be read from :data:`sys.flags.utf8_mode <sys.flags>`.

If the UTF-8 mode is disabled, the interpreter defaults to using
the current locale settings, *unless* the current locale is identified
as a legacy ASCII-based locale (as described for :envvar:`PYTHONCOERCECLOCALE`),
and locale coercion is either disabled or fails.
In such legacy locales, the interpreter will default to enabling UTF-8 mode
unless explicitly instructed not to do so.

See also the :ref:`UTF-8 mode on Windows <win-utf8-mode>`
and the :term:`filesystem encoding and error handler`.


.. _os-procinfo:


----

.. data:: environ

   A :term:`mapping` object where keys and values are strings that represent
   the process environment.  For example, ``environ['HOME']`` is the pathname
   of your home directory (on some platforms), and is equivalent to
   ``getenv("HOME")`` in C.

   This mapping is captured the first time the :mod:`!os` module is imported,
   typically during Python startup as part of processing :file:`site.py`.  Changes
   to the environment made after this time are not reflected in :data:`os.environ`,
   except for changes made by modifying :data:`os.environ` directly.

   This mapping may be used to modify the environment as well as query the
   environment.  :func:`putenv` will be called automatically when the mapping
   is modified.

   On Unix, keys and values use :func:`sys.getfilesystemencoding` and
   ``'surrogateescape'`` error handler. Use :data:`environb` if you would like
   to use a different encoding.

   On Windows, the keys are converted to uppercase. This also applies when
   getting, setting, or deleting an item. For example,
   ``environ['monty'] = 'python'`` maps the key ``'MONTY'`` to the value
   ``'python'``.

   .. note::

      Calling :func:`putenv` directly does not change :data:`os.environ`, so it's better
      to modify :data:`os.environ`.

   .. note::

      On some platforms, including FreeBSD and macOS, setting ``environ`` may
      cause memory leaks.  Refer to the system documentation for
      :c:func:`!putenv`.

   You can delete items in this mapping to unset environment variables.
   :func:`unsetenv` will be called automatically when an item is deleted from
   :data:`os.environ`, and when one of the :meth:`~dict.pop` or
   :meth:`~dict.clear` methods is called.

   If the :manpage:`clearenv(3)` function is available, the :meth:`~dict.clear` method
   uses it and emits a single ``os._clearenv`` audit event. Otherwise, it emits
   an ``os.unsetenv`` event on each deleted variable.

   .. audit-event:: os.unsetenv key os.unsetenv

   .. audit-event:: os._clearenv "" os._clearenv

   .. seealso::

      The :func:`os.reload_environ` function.

   .. versionchanged:: 3.9
      Updated to support :pep:`584`'s merge (``|``) and update (``|=``) operators.

   .. versionchanged:: 3.15
      The :meth:`~dict.clear` method can now emit an ``os._clearenv`` audit
      event.



----

.. data:: RWF_DONTCACHE

   Use uncached buffered IO.

   .. availability:: Linux >= 6.14

   .. versionadded:: 3.15



----

.. data:: RWF_ATOMIC

   Write data atomically. Requires alignment to the device's atomic write unit.

   .. availability:: Linux >= 6.11

   .. versionadded:: 3.15



----

.. function:: listdir(path='.')

   Return a list containing the names of the entries in the directory given by
   *path*.  The list is in arbitrary order, and does not include the special
   entries ``'.'`` and ``'..'`` even if they are present in the directory.
   If a file is removed from or added to the directory during the call of
   this function, whether a name for that file be included is unspecified.

   *path* may be a :term:`path-like object`.  If *path* is of type ``bytes``
   (directly or indirectly through the :class:`PathLike` interface),
   the filenames returned will also be of type ``bytes``;
   in all other circumstances, they will be of type ``str``.

   This function can also support :ref:`specifying a file descriptor
   <path_fd>`; the file descriptor must refer to a directory.

   .. audit-event:: os.listdir path os.listdir

   .. note::
      To encode ``str`` filenames to ``bytes``, use :func:`~os.fsencode`.

   .. seealso::

      The :func:`scandir` function returns directory entries along with
      file attribute information, giving better performance for many
      common use cases.

   .. versionchanged:: 3.2
      The *path* parameter became optional.

   .. versionchanged:: 3.3
      Added support for specifying *path* as an open file descriptor.

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. versionchanged:: 3.15
      ``os.listdir(-1)`` now fails with ``OSError(errno.EBADF)`` rather than
      listing the current directory.



----

.. function:: makedirs(name, mode=0o777, exist_ok=False, *, \
                       parent_mode=None)

   .. index::
      single: directory; creating
      single: UNC paths; and os.makedirs()

   Recursive directory creation function.  Like :func:`mkdir`, but makes all
   intermediate-level directories needed to contain the leaf directory.

   The *mode* parameter is passed to :func:`mkdir` for creating the leaf
   directory; see :ref:`the mkdir() description <mkdir_modebits>` for how it
   is interpreted.  To set the file permission bits of any newly created parent
   directories you can set the umask before invoking :func:`makedirs`.  The
   file permission bits of existing parent directories are not changed.

   If *exist_ok* is ``False`` (the default), a :exc:`FileExistsError` is
   raised if the target directory already exists.

   If *parent_mode* is not ``None``, it is used as the mode for any
   newly-created, intermediate-level directories.  Like *mode*, it is
   combined with the process's umask value; see :ref:`the mkdir()
   description <mkdir_modebits>`.  Otherwise, intermediate directories are
   created with the default mode, which is also subject to the umask.

   .. note::

      :func:`makedirs` will become confused if the path elements to create
      include :data:`pardir` (eg. ".." on UNIX systems).

   This function handles UNC paths correctly.

   .. audit-event:: os.mkdir path,mode,dir_fd os.makedirs

   .. versionchanged:: 3.2
      Added the *exist_ok* parameter.

   .. versionchanged:: 3.4.1

      Before Python 3.4.1, if *exist_ok* was ``True`` and the directory existed,
      :func:`makedirs` would still raise an error if *mode* did not match the
      mode of the existing directory. Since this behavior was impossible to
      implement safely, it was removed in Python 3.4.1. See :issue:`21082`.

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. versionchanged:: 3.7
      The *mode* argument no longer affects the file permission bits of
      newly created intermediate-level directories.

   .. versionadded:: 3.15
      The *parent_mode* parameter. To match the behavior from Python 3.6 and
      earlier (where *mode* was applied to all created directories), pass
      ``parent_mode=mode``.



----

.. data:: NODEV

   Non-existent device.

   .. versionadded:: 3.15



----

.. function:: scandir(path='.')

   Return an iterator of :class:`os.DirEntry` objects corresponding to the
   entries in the directory given by *path*. The entries are yielded in
   arbitrary order, and the special entries ``'.'`` and ``'..'`` are not
   included.  If a file is removed from or added to the directory after
   creating the iterator, whether an entry for that file be included is
   unspecified.

   Using :func:`scandir` instead of :func:`listdir` can significantly
   increase the performance of code that also needs file type or file
   attribute information, because :class:`os.DirEntry` objects expose this
   information if the operating system provides it when scanning a directory.
   All :class:`os.DirEntry` methods may perform a system call, but
   :func:`~os.DirEntry.is_dir` and :func:`~os.DirEntry.is_file` usually only
   require a system call for symbolic links; :func:`os.DirEntry.stat`
   always requires a system call on Unix but only requires one for
   symbolic links on Windows.

   *path* may be a :term:`path-like object`.  If *path* is of type ``bytes``
   (directly or indirectly through the :class:`PathLike` interface),
   the type of the :attr:`~os.DirEntry.name` and :attr:`~os.DirEntry.path`
   attributes of each :class:`os.DirEntry` will be ``bytes``; in all other
   circumstances, they will be of type ``str``.

   This function can also support :ref:`specifying a file descriptor
   <path_fd>`; the file descriptor must refer to a directory.

   .. audit-event:: os.scandir path os.scandir

   Sharing a :func:`scandir` iterator between threads will not corrupt the
   iterator, but it is subject to :term:`race conditions <race condition>`:
   which entries each thread receives is unspecified, and closing the iterator
   while another thread is iterating ends that iteration early.

   The :func:`scandir` iterator supports the :term:`context manager` protocol
   and has the following method:

   .. method:: scandir.close()

      Close the iterator and free acquired resources.

      This is called automatically when the iterator is :term:`exhausted` or garbage
      collected, or when an error happens during iterating.  However it
      is advisable to call it explicitly or use the :keyword:`with`
      statement.

      .. versionadded:: 3.6

   The following example shows a simple use of :func:`scandir` to display all
   the files (excluding directories) in the given *path* that don't start with
   ``'.'``. The ``entry.is_file()`` call will generally not make an additional
   system call::

      with os.scandir(path) as it:
          for entry in it:
              if not entry.name.startswith('.') and entry.is_file():
                  print(entry.name)

   .. note::

      On Unix-based systems, :func:`scandir` uses the system's
      `opendir() <https://pubs.opengroup.org/onlinepubs/009695399/functions/opendir.html>`_
      and
      `readdir() <https://pubs.opengroup.org/onlinepubs/009695399/functions/readdir_r.html>`_
      functions. On Windows, it uses the Win32
      `FindFirstFileW <https://msdn.microsoft.com/en-us/library/windows/desktop/aa364418(v=vs.85).aspx>`_
      and
      `FindNextFileW <https://msdn.microsoft.com/en-us/library/windows/desktop/aa364428(v=vs.85).aspx>`_
      functions.

   .. versionadded:: 3.5

   .. versionchanged:: 3.6
      Added support for the :term:`context manager` protocol and the
      :func:`~scandir.close` method.  If a :func:`scandir` iterator is neither
      exhausted nor explicitly closed a :exc:`ResourceWarning` will be emitted
      in its destructor.

      The function accepts a :term:`path-like object`.

   .. versionchanged:: 3.7
      Added support for :ref:`file descriptors <path_fd>` on Unix.

   .. versionchanged:: 3.15
      ``os.scandir(-1)`` now fails with ``OSError(errno.EBADF)`` rather than
      listing the current directory.



----

.. function:: statx(path, mask, *, flags=0, dir_fd=None, follow_symlinks=True)

   Get the status of a file or file descriptor by performing a :c:func:`!statx`
   system call on the given path.

   *path* is a :term:`path-like object` or an open file descriptor. *mask* is a
   combination of the module-level :const:`STATX_* <STATX_TYPE>` constants
   specifying the information to retrieve. *flags* is a combination of the
   module-level :const:`AT_STATX_* <AT_STATX_FORCE_SYNC>` constants and/or
   :const:`AT_NO_AUTOMOUNT`. Returns a :class:`statx_result` object whose
   :attr:`~os.statx_result.stx_mask` attribute specifies the information
   actually retrieved (which may differ from *mask*).

   This function supports :ref:`specifying a file descriptor <path_fd>`,
   :ref:`paths relative to directory descriptors <dir_fd>`, and
   :ref:`not following symlinks <follow_symlinks>`.

   .. seealso:: The :manpage:`statx(2)` man page.

   .. availability:: Linux >= 4.11 with glibc >= 2.28.

   .. versionadded:: 3.15



----

.. class:: statx_result

   Information about a file returned by :func:`os.statx`.

   :class:`!statx_result` has the following attributes:

   .. attribute:: stx_atime

      Time of most recent access expressed in seconds.

      Equal to ``None`` if :data:`STATX_ATIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_atime_ns

      Time of most recent access expressed in nanoseconds as an integer.

      Equal to ``None`` if :data:`STATX_ATIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_atomic_write_segments_max

      Maximum iovecs for direct I/O with torn-write protection.

      Equal to ``None`` if :data:`STATX_WRITE_ATOMIC` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.11.

   .. attribute:: stx_atomic_write_unit_max

      Maximum size for direct I/O with torn-write protection.

      Equal to ``None`` if :data:`STATX_WRITE_ATOMIC` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.11.

   .. attribute:: stx_atomic_write_unit_max_opt

      Maximum optimized size for direct I/O with torn-write protection.

      Equal to ``None`` if :data:`STATX_WRITE_ATOMIC` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.16.

   .. attribute:: stx_atomic_write_unit_min

      Minimum size for direct I/O with torn-write protection.

      Equal to ``None`` if :data:`STATX_WRITE_ATOMIC` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.11.

   .. attribute:: stx_attributes

      Bitmask of :const:`STATX_ATTR_* <stat.STATX_ATTR_COMPRESSED>` constants
      specifying the attributes of this file.

   .. attribute:: stx_attributes_mask

      A mask indicating which bits in :attr:`stx_attributes` are supported by
      the VFS and the filesystem.

   .. attribute:: stx_blksize

      "Preferred" blocksize for efficient file system I/O. Writing to a file in
      smaller chunks may cause an inefficient read-modify-rewrite.

   .. attribute:: stx_blocks

      Number of 512-byte blocks allocated for file.
      This may be smaller than :attr:`stx_size`/512 when the file has holes.

      Equal to ``None`` if :data:`STATX_BLOCKS` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_btime

      Time of file creation expressed in seconds.

      Equal to ``None`` if :data:`STATX_BTIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_btime_ns

      Time of file creation expressed in nanoseconds as an integer.

      Equal to ``None`` if :data:`STATX_BTIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_ctime

      Time of most recent metadata change expressed in seconds.

      Equal to ``None`` if :data:`STATX_CTIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_ctime_ns

      Time of most recent metadata change expressed in nanoseconds as an
      integer.

      Equal to ``None`` if :data:`STATX_CTIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_dev

      Identifier of the device on which this file resides.

   .. attribute:: stx_dev_major

      Major number of the device on which this file resides.

   .. attribute:: stx_dev_minor

      Minor number of the device on which this file resides.

   .. attribute:: stx_dio_mem_align

      Direct I/O memory buffer alignment requirement.

      Equal to ``None`` if :data:`STATX_DIOALIGN` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.1.

   .. attribute:: stx_dio_offset_align

      Direct I/O file offset alignment requirement.

      Equal to ``None`` if :data:`STATX_DIOALIGN` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.1.

   .. attribute:: stx_dio_read_offset_align

      Direct I/O file offset alignment requirement for reads.

      Equal to ``None`` if :data:`STATX_DIO_READ_ALIGN` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.14.

   .. attribute:: stx_gid

      Group identifier of the file owner.

      Equal to ``None`` if :data:`STATX_GID` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_ino

      Inode number.

      Equal to ``None`` if :data:`STATX_INO` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_mask

      Bitmask of :const:`STATX_* <STATX_TYPE>` constants specifying the
      information retrieved, which may differ from what was requested.

   .. attribute:: stx_mnt_id

      Mount identifier.

      Equal to ``None`` if :data:`STATX_MNT_ID` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 5.8.

   .. attribute:: stx_mode

      File mode: file type and file mode bits (permissions).

      Equal to ``None`` if :data:`STATX_TYPE | STATX_MODE <STATX_TYPE>`
      is missing from :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_mtime

      Time of most recent content modification expressed in seconds.

      Equal to ``None`` if :data:`STATX_MTIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_mtime_ns

      Time of most recent content modification expressed in nanoseconds as an
      integer.

      Equal to ``None`` if :data:`STATX_MTIME` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_nlink

      Number of hard links.

      Equal to ``None`` if :data:`STATX_NLINK` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_rdev

      Type of device if an inode device.

   .. attribute:: stx_rdev_major

      Major number of the device this file represents.

   .. attribute:: stx_rdev_minor

      Minor number of the device this file represents.

   .. attribute:: stx_size

      Size of the file in bytes, if it is a regular file or a symbolic link.
      The size of a symbolic link is the length of the pathname it contains,
      without a terminating null byte.

      Equal to ``None`` if :data:`STATX_SIZE` is missing from
      :attr:`~statx_result.stx_mask`.

   .. attribute:: stx_subvol

      Subvolume identifier.

      Equal to ``None`` if :data:`STATX_SUBVOL` is missing from
      :attr:`~statx_result.stx_mask`.

      .. availability:: Linux >= 4.11 with glibc >= 2.28 and build-time kernel
         userspace API headers >= 6.10.

   .. attribute:: stx_uid

      User identifier of the file owner.

      Equal to ``None`` if :data:`STATX_UID` is missing from
      :attr:`~statx_result.stx_mask`.

   .. seealso:: The :manpage:`statx(2)` man page.

   .. availability:: Linux >= 4.11 with glibc >= 2.28.

   .. versionadded:: 3.15



----

.. data:: STATX_TYPE
          STATX_MODE
          STATX_NLINK
          STATX_UID
          STATX_GID
          STATX_ATIME
          STATX_MTIME
          STATX_CTIME
          STATX_INO
          STATX_SIZE
          STATX_BLOCKS
          STATX_BASIC_STATS
          STATX_BTIME
          STATX_MNT_ID
          STATX_DIOALIGN
          STATX_MNT_ID_UNIQUE
          STATX_SUBVOL
          STATX_WRITE_ATOMIC
          STATX_DIO_READ_ALIGN

   Bitflags for use in the *mask* parameter to :func:`os.statx`.  Some of these
   flags may be available even when their corresponding members in
   :class:`statx_result` are not available.

   .. availability:: Linux >= 4.11 with glibc >= 2.28.

   .. versionadded:: 3.15


----

.. data:: AT_STATX_FORCE_SYNC

   A flag for the :func:`os.statx` function.  Requests that the kernel return
   up-to-date information even when doing so is expensive (for example,
   requiring a round trip to the server for a file on a network filesystem).

   .. availability:: Linux >= 4.11 with glibc >= 2.28.

   .. versionadded:: 3.15


----

.. data:: AT_STATX_DONT_SYNC

   A flag for the :func:`os.statx` function.  Requests that the kernel return
   cached information if possible.

   .. availability:: Linux >= 4.11 with glibc >= 2.28.

   .. versionadded:: 3.15


----

.. data:: AT_STATX_SYNC_AS_STAT

   A flag for the :func:`os.statx` function.  This flag is defined as ``0``, so
   it has no effect, but it can be used to explicitly indicate neither
   :data:`AT_STATX_FORCE_SYNC` nor :data:`AT_STATX_DONT_SYNC` is being passed.
   In the absence of the other two flags, the kernel will generally return
   information as fresh as :func:`os.stat` would return.

   .. availability:: Linux >= 4.11 with glibc >= 2.28.

   .. versionadded:: 3.15



----

.. data:: AT_NO_AUTOMOUNT

   If the final component of a path is an automount point, operate on the
   automount point instead of performing the automount.  On Linux,
   :func:`os.stat`, :func:`os.fstat` and :func:`os.lstat` always behave this
   way.

   .. availability:: Linux.

   .. versionadded:: 3.15



----

.. function:: utime(path, times=None, *[, ns], dir_fd=None, follow_symlinks=True)

   Set the access and modified times of the file specified by *path*.

   :func:`utime` takes two optional parameters, *times* and *ns*.
   These specify the times set on *path* and are used as follows:

   - If *ns* is specified,
     it must be a 2-tuple of the form ``(atime_ns, mtime_ns)``
     where each member is an int expressing nanoseconds.
   - If *times* is not ``None``,
     it must be a 2-tuple of the form ``(atime, mtime)``
     where each member is a real number expressing seconds,
     rounded down to nanoseconds.
   - If *times* is ``None`` and *ns* is unspecified,
     this is equivalent to specifying ``ns=(atime_ns, mtime_ns)``
     where both times are the current time.

   It is an error to specify tuples for both *times* and *ns*.

   Note that the exact times you set here may not be returned by a subsequent
   :func:`~os.stat` call, depending on the resolution with which your operating
   system records access and modification times; see :func:`~os.stat`. The best
   way to preserve exact times is to use the *st_atime_ns* and *st_mtime_ns*
   fields from the :func:`os.stat` result object with the *ns* parameter to
   :func:`utime`.

   This function can support :ref:`specifying a file descriptor <path_fd>`,
   :ref:`paths relative to directory descriptors <dir_fd>` and :ref:`not
   following symlinks <follow_symlinks>`.

   .. audit-event:: os.utime path,times,ns,dir_fd os.utime

   .. versionchanged:: 3.3
      Added support for specifying *path* as an open file descriptor,
      and the *dir_fd*, *follow_symlinks*, and *ns* parameters.

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. versionchanged:: 3.15
      Accepts any real numbers as *times*, not only integers or floats.



----

.. function:: listxattr(path=None, *, follow_symlinks=True)

   Return a list of the extended filesystem attributes on *path*.  The
   attributes in the list are represented as strings decoded with the filesystem
   encoding.  If *path* is ``None``, :func:`listxattr` will examine the current
   directory.

   This function can support :ref:`specifying a file descriptor <path_fd>` and
   :ref:`not following symlinks <follow_symlinks>`.

   .. audit-event:: os.listxattr path os.listxattr

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. versionchanged:: 3.15
      ``os.listxattr(-1)`` now fails with ``OSError(errno.EBADF)`` rather than
      listing extended attributes of the current directory.



----

.. function:: forkpty()

   Fork a child process, using a new pseudo-terminal as the child's controlling
   terminal. Return a pair of ``(pid, fd)``, where *pid* is ``0`` in the child, the
   new child's process id in the parent, and *fd* is the file descriptor of the
   master end of the pseudo-terminal.  For a more portable approach, use the
   :mod:`pty` module.  If an error occurs :exc:`OSError` is raised.

   The returned file descriptor *fd* is :ref:`non-inheritable <fd_inheritance>`.

   .. audit-event:: os.forkpty "" os.forkpty

   .. warning::

      On macOS the use of this function is unsafe when mixed with using
      higher-level system APIs, and that includes using :mod:`urllib.request`.

   .. versionchanged:: 3.8
      Calling ``forkpty()`` in a subinterpreter is no longer supported
      (:exc:`RuntimeError` is raised).

   .. versionchanged:: 3.12
      If Python is able to detect that your process has multiple
      threads, this now raises a :exc:`DeprecationWarning`. See the
      longer explanation on :func:`os.fork`.

   .. versionchanged:: 3.15
      The returned file descriptor is now made non-inheritable.

   .. availability:: Unix, not WASI, not Android, not iOS.

