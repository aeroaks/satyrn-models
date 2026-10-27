.. class:: mmap(fileno, length, tagname=None, \
                access=ACCESS_DEFAULT, offset=0, *, trackfd=True)

   **(Windows version)** Maps *length* bytes from the file specified by the
   file descriptor *fileno*, and creates a mmap object.  If *length* is larger
   than the current size of the file, the file is extended to contain *length*
   bytes.  If *length* is ``0``, the maximum length of the map is the current
   size of the file, except that if the file is empty Windows raises an
   exception (you cannot create an empty mapping on Windows).

   *tagname*, if specified and not ``None``, is a string giving a tag name for
   the mapping.  Windows allows you to have many different mappings against
   the same file.  If you specify the name of an existing tag, that tag is
   opened, otherwise a new tag of this name is created.  If this parameter is
   omitted or ``None``, the mapping is created without a name.  Avoiding the
   use of the *tagname* parameter will assist in keeping your code portable
   between Unix and Windows.

   *offset* may be specified as a non-negative integer offset. mmap references
   will be relative to the offset from the beginning of the file. *offset*
   defaults to 0.  *offset* must be a multiple of the :const:`ALLOCATIONGRANULARITY`.

   If *trackfd* is ``False``, the file handle corresponding to *fileno* will
   not be duplicated, and the resulting :class:`!mmap` object will not
   be associated with the map's underlying file.
   This means that the :meth:`~mmap.mmap.size` and :meth:`~mmap.mmap.resize`
   methods will fail.
   This mode is useful to limit the number of open file handles.
   The original file can be renamed (but not deleted) after closing *fileno*.

   .. versionchanged:: 3.15
      The *trackfd* parameter was added.

   .. audit-event:: mmap.__new__ fileno,length,access,offset mmap.mmap


----

   .. method:: flush([offset[, size]], *, flags=MS_SYNC)

      Flushes changes made to the in-memory copy of a file back to disk. Without
      use of this call there is no guarantee that changes are written back before
      the object is destroyed.  If *offset* and *size* are specified, only
      changes to the given range of bytes will be flushed to disk; otherwise, the
      whole extent of the mapping is flushed.  *offset* must be a multiple of the
      :const:`PAGESIZE` or :const:`ALLOCATIONGRANULARITY`.

      The *flags* parameter specifies the synchronization behavior.
      *flags* must be one of the :ref:`MS_* constants <ms-constants>` available
      on the system.

      On Windows, the *flags* parameter is ignored.

      ``None`` is returned to indicate success.  An exception is raised when the
      call failed.

      .. versionchanged:: 3.8
         Previously, a nonzero value was returned on success; zero was returned
         on error under Windows.  A zero value was returned on success; an
         exception was raised on error under Unix.

      .. versionchanged:: 3.15
         Allow specifying *offset* without *size*. Previously, both *offset*
         and *size* parameters were required together. Now *offset* can be
         specified alone, and the flush operation will extend from *offset*
         to the end of the mmap.

      .. versionchanged:: 3.15
         Added *flags* parameter to control synchronization behavior.



----

   .. method:: set_name(name, /)

      Annotate the memory mapping with the given *name* for easier identification
      in ``/proc/<pid>/maps`` if the kernel supports the feature and :option:`-X dev <-X>` is passed
      to Python or if Python is built in :ref:`debug mode <debug-build>`.
      The length of *name* must not exceed 67 bytes including the ``'\0'`` terminator.

      .. availability:: Linux >= 5.17 (kernel built with ``CONFIG_ANON_VMA_NAME`` option)

      .. versionadded:: 3.15


----

   .. method:: size()

      Return the length of the file, which can be larger than the size of the
      memory-mapped area.
      For an anonymous mapping, return its size.

      .. versionchanged:: 3.15
         Anonymous mappings are now supported on Unix.



----

.. data:: MS_SYNC
          MS_ASYNC
          MS_INVALIDATE

    These flags control the synchronization behavior for :meth:`mmap.flush`:

    * :data:`MS_SYNC` - Synchronous flush: writes are scheduled and the call
      blocks until they are physically written to storage.
    * :data:`MS_ASYNC` - Asynchronous flush: writes are scheduled but the call
      returns immediately without waiting for completion.
    * :data:`MS_INVALIDATE` - Invalidate cached data: invalidates other mappings
      of the same file so they can see the changes.

    .. versionadded:: 3.15