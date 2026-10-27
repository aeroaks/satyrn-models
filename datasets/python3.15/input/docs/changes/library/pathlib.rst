.. method:: Path.mkdir(mode=0o777, parents=False, exist_ok=False, *, \
                       parent_mode=None)

   Create a new directory at this given path.  If *mode* is given, it is
   combined with the process's ``umask`` value to determine the file mode
   and access flags.  If the path already exists, :exc:`FileExistsError`
   is raised.

   If *parents* is true, any missing parents of this path are created
   as needed; they are created with the default permissions without taking
   *mode* into account (mimicking the POSIX ``mkdir -p`` command).

   If *parent_mode* is not ``None``, it is used as the mode for any
   newly-created, intermediate-level directories when *parents* is true.
   Like *mode*, it is combined with the process's ``umask`` value.
   Otherwise, intermediate directories are created with the default
   permissions (also subject to the umask).

   If *parents* is false (the default), a missing parent raises
   :exc:`FileNotFoundError`.

   If *exist_ok* is false (the default), :exc:`FileExistsError` is
   raised if the target directory already exists.

   If *exist_ok* is true, :exc:`FileExistsError` will not be raised unless the given
   path already exists in the file system and is not a directory (same
   behavior as the POSIX ``mkdir -p`` command).

   .. versionchanged:: 3.5
      The *exist_ok* parameter was added.

   .. versionadded:: 3.15
      The *parent_mode* parameter.

