.. class:: SimpleHTTPRequestHandler(request, client_address, server, \
                                    *, directory=None, extra_response_headers=None)

   This class serves files from the directory *directory* and below,
   or the current directory if *directory* is not provided, directly
   mapping the directory structure to HTTP requests.

   .. versionchanged:: 3.7
      Added the *directory* parameter.

   .. versionchanged:: 3.9
      The *directory* parameter accepts a :term:`path-like object`.

   .. versionchanged:: 3.15
      Added *extra_response_headers* parameter.

   A lot of the work, such as parsing the request, is done by the base class
   :class:`BaseHTTPRequestHandler`.  This class implements the :func:`do_GET`
   and :func:`do_HEAD` functions.

   The following are defined as class-level attributes of
   :class:`SimpleHTTPRequestHandler`:

   .. attribute:: server_version

      This will be ``"SimpleHTTP/" + __version__``, where ``__version__`` is
      defined at the module level.

   .. attribute:: default_content_type

      Specifies the Content-Type header value sent when the MIME type
      cannot be guessed from the file extension of the requested URL.
      By default, it is set to ``'application/octet-stream'``.

      .. versionadded:: 3.15

   .. attribute:: index_pages

      Specifies the filenames that are treated as directory index pages.

      Defaults to ``("index.html", "index.htm")``.

      .. versionadded:: 3.12

   .. attribute:: extensions_map

      A dictionary mapping suffixes into MIME types, contains custom overrides
      for the default system mappings. The mapping is used case-insensitively,
      and so should contain only lower-cased keys.

      .. versionchanged:: 3.9
         This dictionary is no longer filled with the default system mappings,
         but only contains overrides.

   .. attribute:: extra_response_headers

      A sequence of ``(name, value)`` pairs containing user-defined extra HTTP
      response headers to add to each successful HTTP status 200 response. These
      headers are not included in other status code responses.

      Headers that the server sends automatically such as ``Content-Type``
      will not be overwritten by :attr:`!extra_response_headers`.

   The :class:`SimpleHTTPRequestHandler` class defines the following methods:

   .. method:: do_HEAD()

      This method serves the ``'HEAD'`` request type: it sends the headers it
      would send for the equivalent ``GET`` request. See the :meth:`do_GET`
      method for a more complete explanation of the possible headers.

   .. method:: do_GET()

      The request is mapped to a local file by interpreting the request as a
      path relative to the current working directory.

      If the request was mapped to a directory, the directory is checked for
      an index page as specified by :attr:`index_pages`. If found, the
      file's contents are returned; otherwise a directory listing is generated
      by calling the :meth:`list_directory` method. This method uses
      :func:`os.listdir` to scan the directory, and returns a ``404`` error
      response if the :func:`~os.listdir` fails.

      If the request was mapped to a file, it is opened. Any :exc:`OSError`
      exception in opening the requested file is mapped to a ``404``,
      ``'File not found'`` error. If there was an ``'If-Modified-Since'``
      header in the request, and the file was not modified after this time,
      a ``304``, ``'Not Modified'`` response is sent. Otherwise, the content
      type is guessed by calling the :meth:`guess_type` method, which in turn
      uses the *extensions_map* variable, and the file contents are returned.

      A ``'Content-type:'`` header with the guessed content type is output,
      followed by a ``'Content-Length:'`` header with the file's size and a
      ``'Last-Modified:'`` header with the file's modification time.

      The instance attribute :attr:`extra_response_headers` is a sequence of
      ``(name, value)`` pairs containing user-defined extra response headers.

      Then follows a blank line signifying the end of the headers, and then the
      contents of the file are output.

      For example usage, see the implementation of the ``test`` function
      in :source:`Lib/http/server.py`.

      .. versionchanged:: 3.7
         Support of the ``'If-Modified-Since'`` header.

   .. method:: list_directory(path)

      Helper to list the contents of *path* when no index page is present.

      This returns either a :term:`file-like object` (which must be closed
      by the caller) or ``None`` to indicate an error, in which case the
      caller has nothing further to do. In either case, the headers are sent.

   .. method:: guess_type(path)

      Guess the type of the file at the given *path*.

      This returns a string of the form ``type/subtype``, usable for
      a MIME Content-type header.

      The default implementation looks the file's extension up in
      :attr:`extensions_map`, falling back to
      :func:`mimetypes.guess_file_type` and then to
      :attr:`default_content_type`.

      .. versionchanged:: 3.13
         Add :func:`mimetypes.guess_file_type` as a fallback.



----

   .. attribute:: default_content_type

      Specifies the Content-Type header value sent when the MIME type
      cannot be guessed from the file extension of the requested URL.
      By default, it is set to ``'application/octet-stream'``.

      .. versionadded:: 3.15


----

.. option:: --content-type <content_type>

   Specifies the default Content-Type HTTP header used when the MIME type
   cannot be guessed from the URL's file extension. By default, the server
   uses ``'application/octet-stream'``:

   .. code-block:: bash

      python -m http.server --content-type text/html

   .. versionadded:: 3.15


----

.. option:: -H, --header <header> <value>

   Specify an additional HTTP Response Header to send on successful HTTP 200
   responses. Can be used multiple times to send additional custom response
   headers. Headers that are sent automatically by the server (for instance
   Content-Type) will not be overwritten by the server.

   .. versionadded:: 3.15


.. _http.server-security:

Security considerations
-----------------------

.. index:: pair: http.server; security

:class:`SimpleHTTPRequestHandler` will follow symbolic links when handling
requests which makes it possible for files outside of the specified directory
to be served.