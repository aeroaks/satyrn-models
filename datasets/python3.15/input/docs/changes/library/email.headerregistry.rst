    .. attribute:: params

       A dictionary mapping parameter names to parameter values.

       .. versionchanged:: 3.15
          It is now a :class:`frozendict` instead of a
          :class:`types.MappingProxyType`.


.. class:: ContentTypeHeader

    A :class:`ParameterizedMIMEHeader` class that handles the
    :mailheader:`Content-Type` header.

    .. attribute:: content_type

       The content type string, in the form ``maintype/subtype``.

    .. attribute:: maintype

    .. attribute:: subtype


.. class:: ContentDispositionHeader

    A :class:`ParameterizedMIMEHeader` class that handles the
    :mailheader:`Content-Disposition` header.

    .. attribute:: content_disposition

       ``inline`` and ``attachment`` are the only valid values in common use.


.. class:: ContentTransferEncodingHeader

   Handles the :mailheader:`Content-Transfer-Encoding` header.

   .. attribute:: cte

      Valid values are ``7bit``, ``8bit``, ``base64``, and
      ``quoted-printable``.  See :rfc:`2045` for more information.



.. class:: HeaderRegistry(base_class=BaseHeader, \
                          default_class=UnstructuredHeader, \
                          use_default_map=True)

    This is the factory used by :class:`~email.policy.EmailPolicy` by default.
    ``HeaderRegistry`` builds the class used to create a header instance
    dynamically, using *base_class* and a specialized class retrieved from a
    registry that it holds.  When a given header name does not appear in the
    registry, the class specified by *default_class* is used as the specialized
    class.  When *use_default_map* is ``True`` (the default), the standard
    mapping of header names to classes is copied in to the registry during
    initialization.  *base_class* is always the last class in the generated
    class's :class:`~type.__bases__` list.

    The default mappings are:

      :subject:                   UniqueUnstructuredHeader
      :date:                      UniqueDateHeader
      :resent-date:               DateHeader
      :orig-date:                 UniqueDateHeader
      :sender:                    UniqueSingleAddressHeader
      :resent-sender:             SingleAddressHeader
      :to:                        UniqueAddressHeader
      :resent-to:                 AddressHeader
      :cc:                        UniqueAddressHeader
      :resent-cc:                 AddressHeader
      :bcc:                       UniqueAddressHeader
      :resent-bcc:                AddressHeader
      :from:                      UniqueAddressHeader
      :resent-from:               AddressHeader
      :reply-to:                  UniqueAddressHeader
      :mime-version:              MIMEVersionHeader
      :content-type:              ContentTypeHeader
      :content-disposition:       ContentDispositionHeader
      :content-transfer-encoding: ContentTransferEncodingHeader
      :message-id:                MessageIDHeader

    ``HeaderRegistry`` has the following methods:


    .. method:: map_to_type(self, name, cls)

       *name* is the name of the header to be mapped.  It will be converted to
       lower case in the registry.  *cls* is the specialized class to be used,
       along with *base_class*, to create the class used to instantiate headers
       that match *name*.


    .. method:: __getitem__(name)

       Construct and return a class to handle creating a *name* header.


    .. method:: __call__(name, value)

       Retrieves the specialized header associated with *name* from the
       registry (using *default_class* if *name* does not appear in the
       registry) and composes it with *base_class* to produce a class,
       calls the constructed class's constructor, passing it the same
       argument list, and finally returns the class instance created thereby.


The following classes are the classes used to represent data parsed from
structured headers and can, in general, be used by an application program to
construct structured values to assign to specific headers.


.. class:: Address(display_name='', username='', domain='', addr_spec=None)

   The class used to represent an email address.  The general form of an
   address is::

      [display_name] <username@domain>

   or::

      username@domain

   where each part must conform to specific syntax rules spelled out in
   :rfc:`5322`.

   As a convenience *addr_spec* can be specified instead of *username* and
   *domain*, in which case *username* and *domain* will be parsed from the
   *addr_spec*.  An *addr_spec* must be a properly RFC quoted string; if it is
   not ``Address`` will raise an error.  Unicode characters are allowed and
   will be property encoded when serialized.  However, per the RFCs, Unicode is
   *not* allowed in the username portion of the address.

   .. attribute:: display_name

      The display name portion of the address, if any, with all quoting
      removed.  If the address does not have a display name, this attribute
      will be an empty string.

   .. attribute:: username

      The ``username`` portion of the address, with all quoting removed.

   .. attribute:: domain

      The ``domain`` portion of the address.

   .. attribute:: addr_spec

      The ``username@domain`` portion of the address, correctly quoted
      for use as a bare address (the second form shown above).  This
      attribute is not mutable.

   .. method:: __str__()

      The ``str`` value of the object is the address quoted according to
      :rfc:`5322` rules, but with no Content Transfer Encoding of any non-ASCII
      characters.

   To support SMTP (:rfc:`5321`), ``Address`` handles one special case: if
   ``username`` and ``domain`` are both the empty string (or ``None``), then
   the string value of the ``Address`` is ``<>``.


.. class:: Group(display_name=None, addresses=None)

   The class used to represent an address group.  The general form of an
   address group is::

     display_name: [address-list];

   As a convenience for processing lists of addresses that consist of a mixture
   of groups and single addresses, a ``Group`` may also be used to represent
   single addresses that are not part of a group by setting *display_name* to
   ``None`` and providing a list of the single address as *addresses*.

   .. attribute:: display_name

      The ``display_name`` of the group.  If it is ``None`` and there is
      exactly one ``Address`` in ``addresses``, then the ``Group`` represents a
      single address that is not in a group.

   .. attribute:: addresses

      A possibly empty tuple of :class:`.Address` objects representing the
      addresses in the group.

   .. method:: __str__()

      The ``str`` value of a ``Group`` is formatted according to :rfc:`5322`,
      but with no Content Transfer Encoding of any non-ASCII characters.  If
      ``display_name`` is none and there is a single ``Address`` in the
      ``addresses`` list, the ``str`` value will be the same as the ``str`` of
      that single ``Address``.


.. rubric:: Footnotes

.. [1] Originally added in 3.3 as a :term:`provisional module <provisional
       package>`