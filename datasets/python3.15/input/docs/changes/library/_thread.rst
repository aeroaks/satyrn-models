.. function:: get_native_id()

   Return the native integral Thread ID of the current thread assigned by the kernel.
   This is a non-negative integer.
   Its value may be used to uniquely identify this particular thread system-wide
   (until the thread terminates, after which the value may be recycled by the OS).

   .. availability:: Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD, Solaris.

   .. versionadded:: 3.8

   .. versionchanged:: 3.13
      Added support for GNU/kFreeBSD.

   .. versionchanged:: 3.15
      Added support for Solaris.

