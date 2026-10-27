.. method:: loop.create_connection(protocol_factory, \
                 host=None, port=None, *, ssl=None, \
                 family=0, proto=0, flags=0, sock=None, \
                 local_addr=None, server_hostname=None, \
                 ssl_handshake_timeout=None, \
                 ssl_shutdown_timeout=None, \
                 happy_eyeballs_delay=None, interleave=None, \
                 all_errors=False)
   :async:

   Open a streaming transport connection to a given
   address specified by *host* and *port*.

   The socket family can be either :py:const:`~socket.AF_INET` or
   :py:const:`~socket.AF_INET6` depending on *host* (or the *family*
   argument, if provided).

   The socket type will be :py:const:`~socket.SOCK_STREAM`.

   *protocol_factory* must be a callable returning an
   :ref:`asyncio protocol <asyncio-protocol>` implementation.

   This method will try to establish the connection in the background.
   When successful, it returns a ``(transport, protocol)`` pair.

   The chronological synopsis of the underlying operation is as follows:

   #. The connection is established and a :ref:`transport <asyncio-transport>`
      is created for it.

   #. *protocol_factory* is called without arguments and is expected to
      return a :ref:`protocol <asyncio-protocol>` instance.

   #. The protocol instance is coupled with the transport by calling its
      :meth:`~BaseProtocol.connection_made` method.

   #. A ``(transport, protocol)`` tuple is returned on success.

   The created transport is an implementation-dependent bidirectional
   stream.

   Other arguments:

   * *ssl*: if given and not false, a SSL/TLS transport is created
     (by default a plain TCP transport is created).  If *ssl* is
     a :class:`ssl.SSLContext` object, this context is used to create
     the transport; if *ssl* is :const:`True`, a default context returned
     from :func:`ssl.create_default_context` is used.

     .. seealso:: :ref:`SSL/TLS security considerations <ssl-security>`

   * *server_hostname* sets or overrides the hostname that the target
     server's certificate will be matched against.  Should only be passed
     if *ssl* is not ``None``.  By default the value of the *host* argument
     is used.  If *host* is empty, there is no default and you must pass a
     value for *server_hostname*.  If *server_hostname* is an empty
     string, hostname matching is disabled (which is a serious security
     risk, allowing for potential man-in-the-middle attacks).

   * *family*, *proto*, *flags* are the optional address family, protocol
     and flags to be passed through to getaddrinfo() for *host* resolution.
     If given, these should all be integers from the corresponding
     :mod:`socket` module constants.

   * *happy_eyeballs_delay*, if given, enables Happy Eyeballs for this
     connection. It should
     be a floating-point number representing the amount of time in seconds
     to wait for a connection attempt to complete, before starting the next
     attempt in parallel. This is the "Connection Attempt Delay" as defined
     in :rfc:`8305`. A sensible default value recommended by the RFC is ``0.25``
     (250 milliseconds).

   * *interleave* controls address reordering when a host name resolves to
     multiple IP addresses.
     If ``0`` or unspecified, no reordering is done, and addresses are
     tried in the order returned by :meth:`getaddrinfo`. If a positive integer
     is specified, the addresses are interleaved by address family, and the
     given integer is interpreted as "First Address Family Count" as defined
     in :rfc:`8305`. The default is ``0`` if *happy_eyeballs_delay* is not
     specified, and ``1`` if it is.

   * *sock*, if given, should be an existing, already connected
     :class:`socket.socket` object to be used by the transport.
     If *sock* is given, none of *host*, *port*, *family*, *proto*, *flags*,
     *happy_eyeballs_delay*, *interleave*
     and *local_addr* should be specified.

     .. note::

        The *sock* argument transfers ownership of the socket to the
        transport created. To close the socket, call the transport's
        :meth:`~asyncio.BaseTransport.close` method.

   * *local_addr*, if given, is a ``(local_host, local_port)`` tuple used
     to bind the socket locally.  The *local_host* and *local_port*
     are looked up using ``getaddrinfo()``, similarly to *host* and *port*.

   * *ssl_handshake_timeout* is (for a TLS connection) the time in seconds
     to wait for the TLS handshake to complete before aborting the connection.
     ``60.0`` seconds if ``None`` (default).

   * *ssl_shutdown_timeout* is the time in seconds to wait for the SSL shutdown
     to complete before aborting the connection. ``30.0`` seconds if ``None``
     (default).

   * *all_errors* determines what exceptions are raised when a connection cannot
     be created. By default, only a single ``Exception`` is raised: the first
     exception if there is only one or all errors have same message, or a single
     ``OSError`` with the error messages combined. When ``all_errors`` is ``True``,
     an ``ExceptionGroup`` will be raised containing all exceptions (even if there
     is only one).


   .. versionchanged:: 3.5

      Added support for SSL/TLS in :class:`ProactorEventLoop`.

   .. versionchanged:: 3.6

      The socket option :ref:`socket.TCP_NODELAY <socket-unix-constants>` is set by default
      for all TCP connections.

   .. versionchanged:: 3.7

      Added the *ssl_handshake_timeout* parameter.

   .. versionchanged:: 3.8

      Added the *happy_eyeballs_delay* and *interleave* parameters.

      Happy Eyeballs Algorithm: Success with Dual-Stack Hosts.
      When a server's IPv4 path and protocol are working, but the server's
      IPv6 path and protocol are not working, a dual-stack client
      application experiences significant connection delay compared to an
      IPv4-only client.  This is undesirable because it causes the
      dual-stack client to have a worse user experience.  This document
      specifies requirements for algorithms that reduce this user-visible
      delay and provides an algorithm.

      For more information: https://datatracker.ietf.org/doc/html/rfc6555

   .. versionchanged:: 3.11

      Added the *ssl_shutdown_timeout* parameter.

   .. versionchanged:: 3.12
      *all_errors* was added.

   .. versionchanged:: 3.15
      Raises a ``ValueError`` if ``ssl.check_hostname`` is ``True``
      and ``server_hostname`` is not supplied.

   .. seealso::

      The :func:`open_connection` function is a high-level alternative
      API.  It returns a pair of (:class:`StreamReader`, :class:`StreamWriter`)
      that can be used directly in async/await code.
