.. function:: b64encode(s, altchars=None, *, padded=True, wrapcol=0)

   Encode the :term:`bytes-like object` *s* using Base64 and return the encoded
   :class:`bytes`.

   Optional *altchars* must be a :term:`bytes-like object` of length 2 which
   specifies an alternative alphabet for the ``+`` and ``/`` characters.
   This allows an application to e.g. generate URL or filesystem safe Base64
   strings.  The default is ``None``, for which the standard Base64 alphabet is used.

   If *padded* is true (default), pad the encoded data with the '='
   character to a size multiple of 4.
   If *padded* is false, do not add the pad characters.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not insert any newlines.

   .. versionchanged:: 3.15
      Added the *padded* and *wrapcol* parameters.



----

.. function:: b64decode(s, altchars=None, validate=False, *, padded=True, canonical=False)
              b64decode(s, altchars=None, validate=True, *, ignorechars, padded=True, canonical=False)

   Decode the Base64 encoded :term:`bytes-like object` or ASCII string
   *s* and return the decoded :class:`bytes`.

   Optional *altchars* must be a :term:`bytes-like object` or ASCII string
   of length 2 which specifies the alternative alphabet used instead of the
   ``+`` and ``/`` characters.

   If *padded* is true, the last group of 4 base 64 alphabet characters must
   be padded with the '=' character.
   If *padded* is false, padding is neither required nor recognized:
   the '=' character is not treated as padding but as a non-alphabet
   character, which means it is silently discarded when *validate* is false,
   or causes an :exc:`~binascii.Error` when *validate* is true unless
   b'=' is included in *ignorechars*.

   A :exc:`binascii.Error` exception is raised
   if *s* is incorrectly padded.

   If *ignorechars* is specified, it should be a :term:`bytes-like object`
   containing characters to ignore from the input when *validate* is true.
   If *ignorechars* contains the pad character ``'='``,  the pad characters
   presented before the end of the encoded data and the excess pad characters
   will be ignored.
   The default value of *validate* is ``True`` if *ignorechars* is specified,
   ``False`` otherwise.

   If *validate* is false, characters that are neither
   in the normal base-64 alphabet nor (if *ignorechars* is not specified)
   the alternative alphabet are
   discarded prior to the padding check, but the ``+`` and ``/`` characters
   keep their meaning if they are not in *altchars* (they will be discarded
   in future Python versions).

   If *validate* is true, these non-alphabet characters in the input
   result in a :exc:`binascii.Error`.

   If *canonical* is true, non-zero padding bits are rejected.
   See :func:`binascii.a2b_base64` for details.

   For more information about the strict base64 check, see :func:`binascii.a2b_base64`

   .. versionchanged:: 3.15
      Added the *canonical*, *ignorechars*, and *padded* parameters.

   .. deprecated:: 3.15
      Accepting the ``+`` and ``/`` characters with an alternative alphabet
      is now deprecated.



----

.. function:: urlsafe_b64encode(s, *, padded=True)

   Encode :term:`bytes-like object` *s* using the
   URL- and filesystem-safe alphabet, which
   substitutes ``-`` instead of ``+`` and ``_`` instead of ``/`` in the
   standard Base64 alphabet, and return the encoded :class:`bytes`.  The result
   can still contain ``=`` if *padded* is true (default).

   .. versionchanged:: 3.15
      Added the *padded* parameter.



----

.. function:: urlsafe_b64decode(s, *, padded=False)

   Decode :term:`bytes-like object` or ASCII string *s*
   using the URL- and filesystem-safe
   alphabet, which substitutes ``-`` instead of ``+`` and ``_`` instead of
   ``/`` in the standard Base64 alphabet, and return the decoded
   :class:`bytes`.

   .. versionchanged:: 3.15
      Added the *padded* parameter.
      Padding of input is no longer required by default.

   .. deprecated:: 3.15
      Accepting the ``+`` and ``/`` characters is now deprecated.



----

.. function:: b32encode(s, *, padded=True, wrapcol=0)

   Encode the :term:`bytes-like object` *s* using Base32 and return the
   encoded :class:`bytes`.

   If *padded* is true (default), pad the encoded data with the '='
   character to a size multiple of 8.
   If *padded* is false, do not add the pad characters.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not add any newlines.

   .. versionchanged:: 3.15
      Added the *padded* and *wrapcol* parameters.



----

.. function:: b32decode(s, casefold=False, map01=None, *, padded=True, ignorechars=b'', canonical=False)

   Decode the Base32 encoded :term:`bytes-like object` or ASCII string *s* and
   return the decoded :class:`bytes`.

   Optional *casefold* is a flag specifying
   whether a lowercase alphabet is acceptable as input.  For security purposes,
   the default is ``False``.

   :rfc:`4648` allows for optional mapping of the digit 0 (zero) to the letter O
   (oh), and for optional mapping of the digit 1 (one) to either the letter I (eye)
   or letter L (el).  The optional argument *map01* when not ``None``, specifies
   which letter the digit 1 should be mapped to (when *map01* is not ``None``, the
   digit 0 is always mapped to the letter O).  For security purposes the default is
   ``None``, so that 0 and 1 are not allowed in the input.

   If *padded* is true, the last group of 8 base 32 alphabet characters must
   be padded with the '=' character.
   If *padded* is false, padding is neither required nor recognized:
   the '=' character is not treated as padding but as a non-alphabet
   character, which means it raises an :exc:`~binascii.Error` unless
   b'=' is included in *ignorechars*.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.

   If *canonical* is true, non-zero padding bits are rejected.
   See :func:`binascii.a2b_base32` for details.

   A :exc:`binascii.Error` is raised if *s* is
   incorrectly padded or if there are non-alphabet characters present in the
   input.

   .. versionchanged:: 3.15
      Added the *canonical*, *ignorechars*, and *padded* parameters.



----

.. function:: b32hexencode(s, *, padded=True, wrapcol=0)

   Similar to :func:`b32encode` but uses the Extended Hex Alphabet, as defined in
   :rfc:`4648`.

   .. versionadded:: 3.10

   .. versionchanged:: 3.15
      Added the *padded* and *wrapcol* parameters.



----

.. function:: b32hexdecode(s, casefold=False, *, padded=True, ignorechars=b'', canonical=False)

   Similar to :func:`b32decode` but uses the Extended Hex Alphabet, as defined in
   :rfc:`4648`.

   This version does not allow the digit 0 (zero) to the letter O (oh) and digit
   1 (one) to either the letter I (eye) or letter L (el) mappings, all these
   characters are included in the Extended Hex Alphabet and are not
   interchangeable.

   .. versionadded:: 3.10

   .. versionchanged:: 3.15
      Added the *canonical*, *ignorechars*, and *padded* parameters.



----

.. function:: b16encode(s, *, wrapcol=0)

   Encode the :term:`bytes-like object` *s* using Base16 and return the
   encoded :class:`bytes`.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not add any newlines.

   .. versionchanged:: 3.15
      Added the *wrapcol* parameter.



----

.. function:: b16decode(s, casefold=False, *, ignorechars=b'')

   Decode the Base16 encoded :term:`bytes-like object` or ASCII string *s* and
   return the decoded :class:`bytes`.

   Optional *casefold* is a flag specifying whether a
   lowercase alphabet is acceptable as input.  For security purposes, the default
   is ``False``.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.

   A :exc:`binascii.Error` is raised if *s* is
   incorrectly padded or if there are non-alphabet characters present in the
   input.

   .. versionchanged:: 3.15
      Added the *ignorechars* parameter.



----

.. function:: a85decode(b, *, foldspaces=False, adobe=False, ignorechars=b' \t\n\r\v', canonical=False)

   Decode the Ascii85 encoded :term:`bytes-like object` or ASCII string *b* and
   return the decoded :class:`bytes`.

   *foldspaces* is a flag that specifies whether the 'y' short sequence
   should be accepted as shorthand for 4 consecutive spaces (ASCII 0x20).
   This feature is not supported by the standard Ascii85 encoding used in
   PDF and PostScript.

   *adobe* controls whether the ``<~`` and ``~>`` markers are
   present. While the leading ``<~`` is not required, the input must
   end with ``~>``, or a :exc:`ValueError` is raised.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.
   This should only contain whitespace characters, and by
   default contains all whitespace characters in ASCII.

   If *canonical* is true, non-canonical encodings are rejected.
   See :func:`binascii.a2b_ascii85` for details.

   .. versionadded:: 3.4

   .. versionchanged:: 3.15
      Added the *canonical* parameter.
      Single-character final groups are now always rejected as encoding
      violations.



----

.. function:: b85encode(b, pad=False, *, wrapcol=0)

   Encode the :term:`bytes-like object` *b* using base85 (as used in e.g.
   git-style binary diffs) and return the encoded :class:`bytes`.

   The input is padded with ``b'\0'`` so its length is a multiple of 4
   bytes before encoding.  If *pad* is true, all the resulting
   characters are retained in the output, which will always be a
   multiple of 5 bytes, and thus the length of the data may not be
   preserved on decoding.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not add any newlines.

   .. versionadded:: 3.4

   .. versionchanged:: 3.15
      Added the *wrapcol* parameter.



----

.. function:: b85decode(b, *, ignorechars=b'', canonical=False)

   Decode the base85-encoded :term:`bytes-like object` or ASCII string *b* and
   return the decoded :class:`bytes`.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.

   If *canonical* is true, non-canonical encodings are rejected.
   See :func:`binascii.a2b_base85` for details.

   .. versionadded:: 3.4

   .. versionchanged:: 3.15
      Added the *canonical* and *ignorechars* parameters.
      Single-character final groups are now always rejected as encoding
      violations.



----

.. function:: z85encode(s, pad=False, *, wrapcol=0)

   Encode the :term:`bytes-like object` *s* using Z85 (as used in ZeroMQ)
   and return the encoded :class:`bytes`.

   The input is padded with ``b'\0'`` so its length is a multiple of 4
   bytes before encoding.  If *pad* is true, all the resulting
   characters are retained in the output, which will always be a
   multiple of 5 bytes, as required by the ZeroMQ standard.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not add any newlines.

   .. versionadded:: 3.13

   .. versionchanged:: 3.15
      The *pad* parameter was added.

   .. versionchanged:: 3.15
      Added the *wrapcol* parameter.



----

.. function:: z85decode(s, *, ignorechars=b'', canonical=False)

   Decode the Z85-encoded :term:`bytes-like object` or ASCII string *s* and
   return the decoded :class:`bytes`.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.

   If *canonical* is true, non-canonical encodings are rejected.
   See :func:`binascii.a2b_base85` for details.

   .. versionadded:: 3.13

   .. versionchanged:: 3.15
      Added the *canonical* and *ignorechars* parameters.
      Single-character final groups are now always rejected as encoding
      violations.

