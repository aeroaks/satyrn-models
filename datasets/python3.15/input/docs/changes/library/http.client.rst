.. class:: HTTPConnection(host, port=None[, timeout], source_address=None, \
                          blocksize=8192, max_response_headers=None)

   An :class:`HTTPConnection` instance represents one transaction with an HTTP
   server.  It should be instantiated by passing it a host and optional port
   number.  If no port number is passed, the port is extracted from the host
   string if it has the form ``host:port``, else the default HTTP port (80) is
   used.  If the optional *timeout* parameter is given, blocking
   operations (like connection attempts) will timeout after that many seconds
   (if it is not given, the global default timeout setting is used).
   The optional *source_address* parameter may be a tuple of a (host, port)
   to use as the source address the HTTP connection is made from.
   The optional *blocksize* parameter sets the buffer size in bytes for
   sending a file-like message body. The optional *max_response_headers*
   parameter sets the maximum number of allowed response headers to help
   prevent denial-of-service attacks, otherwise the default value (100) is used.

   For example, the following calls all create instances that connect to the server
   at the same host and port::

      >>> h1 = http.client.HTTPConnection('www.python.org')
      >>> h2 = http.client.HTTPConnection('www.python.org:80')
      >>> h3 = http.client.HTTPConnection('www.python.org', 80)
      >>> h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)

   .. versionchanged:: 3.2
      *source_address* was added.

   .. versionchanged:: 3.4
      The  *strict* parameter was removed. HTTP 0.9-style "Simple Responses" are
      no longer supported.

   .. versionchanged:: 3.7
      *blocksize* parameter was added.

   .. versionchanged:: 3.15
      *max_response_headers* parameter was added.



----

.. class:: HTTPSConnection(host, port=None, *[, timeout], \
                           source_address=None, context=None, \
                           blocksize=8192, max_response_headers=None)

   A subclass of :class:`HTTPConnection` that uses SSL for communication with
   secure servers.  Default port is ``443``.  If *context* is specified, it
   must be a :class:`ssl.SSLContext` instance describing the various SSL
   options.

   Please read :ref:`ssl-security` for more information on best practices.

   .. versionchanged:: 3.2
      *source_address*, *context* and *check_hostname* were added.

   .. versionchanged:: 3.2
      This class now supports HTTPS virtual hosts if possible (that is,
      if :const:`ssl.HAS_SNI` is true).

   .. versionchanged:: 3.4
      The *strict* parameter was removed. HTTP 0.9-style "Simple Responses" are
      no longer supported.

   .. versionchanged:: 3.4.3
      This class now performs all the necessary certificate and hostname checks
      by default. To revert to the previous, unverified, behavior
      :func:`!ssl._create_unverified_context` can be passed to the *context*
      parameter.

   .. versionchanged:: 3.8
      This class now enables TLS 1.3
      :attr:`ssl.SSLContext.post_handshake_auth` for the default *context* or
      when *cert_file* is passed with a custom *context*.

   .. versionchanged:: 3.10
      This class now sends an ALPN extension with protocol indicator
      ``http/1.1`` when no *context* is given. Custom *context* should set
      ALPN protocols with :meth:`~ssl.SSLContext.set_alpn_protocols`.

   .. versionchanged:: 3.12
      The deprecated *key_file*, *cert_file* and *check_hostname* parameters
      have been removed.

   .. versionchanged:: 3.15
      *max_response_headers* parameter was added.



----

.. attribute:: HTTPConnection.max_response_headers

   The maximum number of allowed response headers to help prevent denial-of-service
   attacks. By default, the maximum number of allowed headers is set to 100.
   The same limit applies to the trailer section of a chunked response.

   .. versionadded:: 3.15

