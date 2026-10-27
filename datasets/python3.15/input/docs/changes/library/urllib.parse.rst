.. function:: urlsplit(urlstring, scheme=None, allow_fragments=True, *, missing_as_none=False)

   Parse a URL into five components, returning a 5-item :term:`named tuple`
   :class:`SplitResult` or :class:`SplitResultBytes`.
   This corresponds to the general structure of a URL:
   ``scheme://netloc/path?query#fragment``.
   Each tuple item is a string, possibly empty, or ``None`` if
   *missing_as_none* is true.
   Not defined component are represented an empty string (by default) or
   ``None`` if *missing_as_none* is true.
   The delimiters as shown above are not part of the result, except for a
   leading slash in the *path* component, which is retained if present.

   Additionally, the netloc property is broken down into these additional
   attributes added to the returned object: username, password, hostname, and
   port.

   Percent-encoded sequences are not decoded.

   For example:

   .. doctest::
      :options: +NORMALIZE_WHITESPACE

      >>> from urllib.parse import urlsplit
      >>> urlsplit("scheme://netloc/path?query#fragment")
      SplitResult(scheme='scheme', netloc='netloc', path='/path',
                  query='query', fragment='fragment')
      >>> o = urlsplit("http://docs.python.org:80/3/library/urllib.parse.html?"
      ...              "highlight=params#url-parsing")
      >>> o
      SplitResult(scheme='http', netloc='docs.python.org:80',
                  path='/3/library/urllib.parse.html',
                  query='highlight=params', fragment='url-parsing')
      >>> o.scheme
      'http'
      >>> o.netloc
      'docs.python.org:80'
      >>> o.hostname
      'docs.python.org'
      >>> o.port
      80
      >>> o._replace(fragment="").geturl()
      'http://docs.python.org:80/3/library/urllib.parse.html?highlight=params'
      >>> urlsplit("http://docs.python.org?")
      SplitResult(scheme='http', netloc='docs.python.org', path='',
                  query='', fragment='')
      >>> urlsplit("http://docs.python.org?", missing_as_none=True)
      SplitResult(scheme='http', netloc='docs.python.org', path='',
                  query='', fragment=None)

   Following the syntax specifications in :rfc:`1808`, :func:`!urlsplit` recognizes
   a netloc only if it is properly introduced by '//'.  Otherwise the
   input is presumed to be a relative URL and thus to start with
   a path component.

   .. doctest::
      :options: +NORMALIZE_WHITESPACE

      >>> from urllib.parse import urlsplit
      >>> urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
      SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')
      >>> urlsplit('www.cwi.nl/%7Eguido/Python.html')
      SplitResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html',
                  query='', fragment='')
      >>> urlsplit('help/Python.html')
      SplitResult(scheme='', netloc='', path='help/Python.html',
                  query='', fragment='')
      >>> urlsplit('help/Python.html', missing_as_none=True)
      SplitResult(scheme=None, netloc=None, path='help/Python.html',
                  query=None, fragment=None)

   The *scheme* argument gives the default addressing scheme, to be
   used only if the URL does not specify one.  It should be the same type
   (text or bytes) as *urlstring* or ``None``, except that the ``''`` is
   always allowed, and is automatically converted to ``b''`` if appropriate.

   If the *allow_fragments* argument is false, fragment identifiers are not
   recognized.  Instead, they are parsed as part of the path
   or query component, and :attr:`fragment` is set to ``None`` or the empty
   string (depending on the value of *missing_as_none*) in the return value.

   The return value is a :term:`named tuple`, which means that its items can
   be accessed by index or as named attributes, which are:

   +------------------+-------+-------------------------+-------------------------------+
   | Attribute        | Index | Value                   | Value if not present          |
   +==================+=======+=========================+===============================+
   | :attr:`scheme`   | 0     | URL scheme specifier    | *scheme* parameter or         |
   |                  |       |                         | empty string [1]_             |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`netloc`   | 1     | Network location part   | ``None`` or empty string [1]_ |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`path`     | 2     | Hierarchical path       | empty string                  |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`query`    | 3     | Query component         | ``None`` or empty string [1]_ |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`fragment` | 4     | Fragment identifier     | ``None`` or empty string [1]_ |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`username` |       | User name               | ``None``                      |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`password` |       | Password                | ``None``                      |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`hostname` |       | Host name (lower case)  | ``None``                      |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`port`     |       | Port number as integer, | ``None``                      |
   |                  |       | if present              |                               |
   +------------------+-------+-------------------------+-------------------------------+

   .. [1] Depending on the value of the *missing_as_none* argument.

   Reading the :attr:`port` attribute will raise a :exc:`ValueError` if
   an invalid port is specified in the URL.  See section
   :ref:`urlparse-result-object` for more information on the result object.

   Unmatched square brackets in the :attr:`netloc` attribute will raise a
   :exc:`ValueError`.

   Characters in the :attr:`netloc` attribute that decompose under NFKC
   normalization (as used by the IDNA encoding) into any of ``/``, ``?``,
   ``#``, ``@``, or ``:`` will raise a :exc:`ValueError`. If the URL is
   decomposed before parsing, no error will be raised.

   Following some of the `WHATWG spec`_ that updates :rfc:`3986`, leading C0
   control and space characters are stripped from the URL. ``\n``,
   ``\r`` and tab ``\t`` characters are removed from the URL at any position.

   As is the case with all named tuples, the subclass has a few additional methods
   and attributes that are particularly useful. One such method is :meth:`_replace`.
   The :meth:`_replace` method will return a new :class:`SplitResult` object
   replacing specified fields with new values.

   .. doctest::
      :options: +NORMALIZE_WHITESPACE

      >>> from urllib.parse import urlsplit
      >>> u = urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
      >>> u
      SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')
      >>> u._replace(scheme='http')
      SplitResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')

   .. warning::

      :func:`urlsplit` does not perform validation.  See :ref:`URL parsing
      security <url-parsing-security>` for details.

   .. versionchanged:: 3.2
      Added IPv6 URL parsing capabilities.

   .. versionchanged:: 3.3
      The fragment is now parsed for all URL schemes (unless *allow_fragments* is
      false), in accordance with :rfc:`3986`.  Previously, an allowlist of
      schemes that support fragments existed.

   .. versionchanged:: 3.6
      Out-of-range port numbers now raise :exc:`ValueError`, instead of
      returning ``None``.

   .. versionchanged:: 3.8
      Characters that affect netloc parsing under NFKC normalization will
      now raise :exc:`ValueError`.

   .. versionchanged:: 3.10
      ASCII newline and tab characters are stripped from the URL.

   .. versionchanged:: 3.12
      Leading WHATWG C0 control and space characters are stripped from the URL.

   .. versionchanged:: 3.15
      Added the *missing_as_none* parameter.


----

.. function:: urlunsplit(parts)
              urlunsplit(parts, *, keep_empty)

   Construct a URL from a tuple as returned by :func:`urlsplit`. The *parts*
   argument can be any five-item iterable.

   This may result in a slightly different, but equivalent URL, if the
   URL that was parsed originally had unnecessary delimiters (for example,
   a ``?`` with an empty query; the RFC states that these are equivalent).

   If *keep_empty* is true, empty strings are kept in the result (for example,
   a ``?`` for an empty query), only ``None`` components are omitted.
   This allows rebuilding a URL that was parsed with option
   ``missing_as_none=True``.
   By default, *keep_empty* is true if *parts* is the result of the
   :func:`urlsplit` call with ``missing_as_none=True``.

   .. versionchanged:: 3.15
      Added the *keep_empty* parameter.



----

.. function:: urlunparse(parts)
              urlunparse(parts, *, keep_empty)

   Combine the elements of a tuple as returned by :func:`urlparse` into a
   complete URL as a string. The *parts* argument can be any six-item
   iterable.

   This may result in a slightly different, but equivalent URL, if the
   URL that was parsed originally had unnecessary delimiters (for example,
   a ``?`` with an empty query; the RFC states that these are equivalent).

   If *keep_empty* is true, empty strings are kept in the result (for example,
   a ``?`` for an empty query), only ``None`` components are omitted.
   This allows rebuilding a URL that was parsed with option
   ``missing_as_none=True``.
   By default, *keep_empty* is true if *parts* is the result of the
   :func:`urlparse` call with ``missing_as_none=True``.

   .. versionchanged:: 3.15
      Added the *keep_empty* parameter.



----

.. function:: urldefrag(url, *, missing_as_none=False)

   If *url* contains a fragment identifier, return a modified version of *url*
   with no fragment identifier, and the fragment identifier as a separate
   string.  If there is no fragment identifier in *url*, return *url* unmodified
   and an empty string (by default) or ``None`` if *missing_as_none* is true.

   The return value is a :term:`named tuple`, its items can be accessed by index
   or as named attributes:

   +------------------+-------+-------------------------+-------------------------------+
   | Attribute        | Index | Value                   | Value if not present          |
   +==================+=======+=========================+===============================+
   | :attr:`url`      | 0     | URL with no fragment    | empty string                  |
   +------------------+-------+-------------------------+-------------------------------+
   | :attr:`fragment` | 1     | Fragment identifier     | ``None`` or empty string [3]_ |
   +------------------+-------+-------------------------+-------------------------------+

   .. [3] Depending on the value of the *missing_as_none* argument.

   See section :ref:`urlparse-result-object` for more information on the result
   object.

   .. versionchanged:: 3.2
      Result is a structured object rather than a simple 2-tuple.

   .. versionchanged:: 3.15
      Added the *missing_as_none* parameter.
