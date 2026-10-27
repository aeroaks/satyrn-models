   .. attribute:: utf8

      If ``False``, follow :rfc:`5322`, supporting non-ASCII characters in
      headers by encoding them as :rfc:`2047` "encoded words".  If ``True``,
      follow :rfc:`6532` and use ``utf-8`` encoding for headers.  Messages
      formatted in this way may be passed to SMTP servers that support
      the ``SMTPUTF8`` extension (:rfc:`6531`).

      When ``False``, the generator will raise
      :exc:`~email.errors.HeaderWriteError` if any header includes non-ASCII
      characters in a context where :rfc:`2047` does not permit encoded words.
      This particularly applies to mailboxes ("addr-spec") with non-ASCII
      characters, which can be created via
      :class:`~email.headerregistry.Address`. To use a mailbox with a non-ASCII
      domain name with ``utf8=False``, first encode the domain using the
      third-party :pypi:`idna` or :pypi:`uts46` module or with
      :mod:`encodings.idna`. It is not possible to use a non-ASCII username
      ("local-part") in a mailbox when ``utf8=False``.

      .. versionchanged:: 3.15
         Can trigger the raising of :exc:`~email.errors.HeaderWriteError`.
         (Earlier versions incorrectly applied :rfc:`2047` in certain contexts,
         mostly notably in addr-specs.)
