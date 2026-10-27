.. function:: fork()

   Fork. Connect the child's controlling terminal to a pseudo-terminal. Return
   value is ``(pid, fd)``. Note that the child  gets *pid* 0, and the *fd* is
   *invalid*. The parent's return value is the *pid* of the child, and *fd* is a
   file descriptor connected to the child's controlling terminal (and also to the
   child's standard input and output).

   The returned file descriptor *fd* is :ref:`non-inheritable <fd_inheritance>`.

   .. warning:: On macOS the use of this function is unsafe when mixed with using
      higher-level system APIs, and that includes using :mod:`urllib.request`.

   .. versionchanged:: 3.15
      The returned file descriptor is now made non-inheritable.

