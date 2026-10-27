   .. method:: start_tls(sslcontext, *, server_hostname=None, \
                         ssl_handshake_timeout=None, ssl_shutdown_timeout=None)
      :async:

      Upgrade an existing stream-based connection to TLS.

      Parameters:

      * *sslcontext*: a configured instance of :class:`~ssl.SSLContext`.

      * *server_hostname*: sets or overrides the host name that the target
        server's certificate will be matched against.

      * *ssl_handshake_timeout* is the time in seconds to wait for the TLS
        handshake to complete before aborting the connection.  ``60.0`` seconds
        if ``None`` (default).

      * *ssl_shutdown_timeout* is the time in seconds to wait for the SSL shutdown
        to complete before aborting the connection. ``30.0`` seconds if ``None``
        (default).

      .. versionadded:: 3.11

      .. versionchanged:: 3.12
         Added the *ssl_shutdown_timeout* parameter.

      .. versionchanged:: 3.15
         Raises a ``ValueError`` if ``sslcontext.check_hostname`` is ``True``
         and ``server_hostname`` is not supplied.

