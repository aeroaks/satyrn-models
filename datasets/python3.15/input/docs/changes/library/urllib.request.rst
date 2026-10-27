.. method:: HTTPPasswordMgr.add_password(realm, uri, user, passwd)

   *uri* can be either a single URI, or a sequence of URIs. *realm*, *user* and
   *passwd* must be strings. This causes ``(user, passwd)`` to be used as
   authentication tokens when authentication for *realm* and a super-URI of any
   of the given URIs is given. If a URI includes a scheme, its credentials only
   match authentication URIs with the same scheme or no scheme. A URI without a
   scheme matches authentication URIs with any scheme.

   .. versionchanged:: 3.15
      Authentication credentials for URIs with a scheme are now scoped by
      that scheme.

