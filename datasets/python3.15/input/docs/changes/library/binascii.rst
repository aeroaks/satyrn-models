.. function:: a2b_base64(string, /, *, padded=True, alphabet=BASE64_ALPHABET, strict_mode=False, canonical=False)
              a2b_base64(string, /, *, ignorechars, padded=True, alphabet=BASE64_ALPHABET, strict_mode=True, canonical=False)

   Convert a block of base64 data back to binary and return the binary data. More
   than one line may be passed at a time.

   Optional *alphabet* must be a :class:`bytes` object of length 64 which
   specifies an alternative alphabet.

   If *padded* is true, the last group of 4 base 64 alphabet characters must
   be padded with the '=' character.
   If *padded* is false, padding is neither required nor recognized:
   the '=' character is not treated as padding but as a non-alphabet
   character, which means it is silently discarded when *strict_mode* is false,
   or causes an :exc:`~binascii.Error` when *strict_mode* is true unless
   b'=' is included in *ignorechars*.

   If *ignorechars* is specified, it should be a :term:`bytes-like object`
   containing characters to ignore from the input when *strict_mode* is true.
   If *ignorechars* contains the pad character ``'='``,  the pad characters
   presented before the end of the encoded data and the excess pad characters
   will be ignored.
   The default value of *strict_mode* is ``True`` if *ignorechars* is specified,
   ``False`` otherwise.

   If *strict_mode* is true, only valid base64 data will be converted. Invalid base64
   data will raise :exc:`binascii.Error`.

   Valid base64:

   * Conforms to :rfc:`4648`.
   * Contains only characters from the base64 alphabet.
   * Contains no excess data after padding (including excess padding, newlines, etc.).
   * Does not start with a padding.

   If *canonical* is true, non-zero padding bits in the last group are rejected
   with :exc:`binascii.Error`, enforcing canonical encoding as defined in
   :rfc:`4648` section 3.5.  This check is independent of *strict_mode*.

   .. versionchanged:: 3.11
      Added the *strict_mode* parameter.

   .. versionchanged:: 3.15
      Added the *alphabet*, *canonical*, *ignorechars*, and *padded* parameters.



----

.. function:: b2a_base64(data, *, padded=True, alphabet=BASE64_ALPHABET, wrapcol=0, newline=True)

   Convert binary data to a line(s) of ASCII characters in base64 coding,
   as specified in :rfc:`4648`.

   If *padded* is true (default), pad the encoded data with the '='
   character to a size multiple of 4.
   If *padded* is false, do not add the pad characters.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not insert any newlines.

   If *newline* is true (default), a newline character will be added
   at the end of the output.

   .. versionchanged:: 3.6
      Added the *newline* parameter.

   .. versionchanged:: 3.15
      Added the *alphabet*, *padded* and *wrapcol* parameters.



----

.. function:: a2b_ascii85(string, /, *, foldspaces=False, adobe=False, ignorechars=b'', canonical=False)

   Convert Ascii85 data back to binary and return the binary data.

   Valid Ascii85 data contains characters from the Ascii85 alphabet in groups
   of five (except for the final group, which may have from two to five
   characters). Each group encodes 32 bits of binary data in the range from
   ``0`` to ``2 ** 32 - 1``, inclusive. The special character ``z`` is
   accepted as a short form of the group ``!!!!!``, which encodes four
   consecutive null bytes. A single-character final group is always rejected
   as an encoding violation.

   *foldspaces* is a flag that specifies whether the 'y' short sequence
   should be accepted as shorthand for 4 consecutive spaces (ASCII 0x20).
   This feature is not supported by the "standard" Ascii85 encoding.

   *adobe* controls whether the encoded byte sequence is framed with
   ``<~`` and ``~>``, as in a PostScript base-85 string literal.  If
   *adobe* is true, a leading ``<~`` is optionally accepted, while a
   trailing ``~>`` is *required*, and :exc:`binascii.Error` is raised
   if it is not found.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.
   This should only contain whitespace characters.

   If *canonical* is true, non-canonical encodings are rejected with
   :exc:`binascii.Error`.  Here "canonical" means the encoding that
   :func:`b2a_ascii85` would produce: the ``z`` abbreviation must be used
   for all-zero groups (rather than ``!!!!!``), and partial final groups
   must use the same padding digits as the encoder.

   Invalid Ascii85 data will raise :exc:`binascii.Error`.

   .. versionadded:: 3.15



----

.. function:: b2a_ascii85(data, /, *, foldspaces=False, wrapcol=0, pad=False, adobe=False)

   Convert binary data to a formatted sequence of ASCII characters in Ascii85
   coding. The return value is the converted data.

   *foldspaces* is an optional flag that uses the special short sequence 'y'
   instead of 4 consecutive spaces (ASCII 0x20) as supported by 'btoa'. This
   feature is not supported by the "standard" Ascii85 encoding.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not insert any newlines.

   If *pad* is true, the zero-padding applied to the end of the input
   is fully retained in the output encoding, as done by ``btoa``,
   producing an exact multiple of 5 bytes of output. This is not part
   of the standard encoding used in PDF, as it does not preserve the
   length of the data.

   *adobe* controls whether the encoded byte sequence is framed with
   ``<~`` and ``~>``, as in a PostScript base-85 string literal.  Note
   that while ASCII85Decode streams in PDF documents *must* be
   terminated with ``~>``, they *must not* use a leading ``<~``.

   .. versionadded:: 3.15



----

.. function:: a2b_base85(string, /, *, alphabet=BASE85_ALPHABET, ignorechars=b'', canonical=False)

   Convert Base85 data back to binary and return the binary data.
   More than one line may be passed at a time.

   Valid Base85 data contains characters from the Base85 alphabet in groups
   of five (except for the final group, which may have from two to five
   characters). Each group encodes 32 bits of binary data in the range from
   ``0`` to ``2 ** 32 - 1``, inclusive. A single-character final group is
   always rejected as an encoding violation.

   Optional *alphabet* must be a :class:`bytes` object of length 85 which
   specifies an alternative alphabet.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.

   If *canonical* is true, non-canonical encodings are rejected with
   :exc:`binascii.Error`.  Here "canonical" means the encoding that
   :func:`b2a_base85` would produce: partial final groups must use the
   same padding digits as the encoder.

   Invalid Base85 data will raise :exc:`binascii.Error`.

   .. versionadded:: 3.15



----

.. function:: b2a_base85(data, /, *, alphabet=BASE85_ALPHABET, wrapcol=0, pad=False)

   Convert binary data to a line of ASCII characters in Base85 coding.
   The return value is the converted line.

   Optional *alphabet* must be a :term:`bytes-like object` of length 85 which
   specifies an alternative alphabet.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not insert any newlines.

   If *pad* is true, the zero-padding applied to the end of the input
   is retained in the output, which will always be a multiple of 5
   bytes, and thus the length of the data may not be preserved on
   decoding.

   .. versionadded:: 3.15



----

.. function:: a2b_base32(string, /, *, padded=True, alphabet=BASE32_ALPHABET, ignorechars=b'', canonical=False)

   Convert base32 data back to binary and return the binary data.

   Valid base32 data contains characters from the base32 alphabet specified
   in :rfc:`4648` in groups of eight (if necessary, the final group is padded
   to eight characters with ``=``). Each group encodes 40 bits of binary data
   in the range from ``0`` to ``2 ** 40 - 1``, inclusive.

   .. note::
      This function does not map lowercase characters (which are invalid in
      standard base32) to their uppercase counterparts, nor does it
      contextually map ``0`` to ``O`` and ``1`` to ``I``/``L`` as :rfc:`4648`
      allows.

   Optional *alphabet* must be a :class:`bytes` object of length 32 which
   specifies an alternative alphabet.

   If *padded* is true, the last group of 8 base 32 alphabet characters must
   be padded with the '=' character.
   If *padded* is false, the '=' character is treated as other non-alphabet
   characters (depending on the value of *ignorechars*).

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.
   If *ignorechars* contains the pad character ``'='``,  the pad characters
   presented before the end of the encoded data and the excess pad characters
   will be ignored.

   If *canonical* is true, non-zero padding bits in the last group are rejected
   with :exc:`binascii.Error`, enforcing canonical encoding as defined in
   :rfc:`4648` section 3.5.

   Invalid base32 data will raise :exc:`binascii.Error`.

   .. versionadded:: 3.15


----

.. function:: b2a_base32(data, /, *, padded=True, alphabet=BASE32_ALPHABET, wrapcol=0)

   Convert binary data to a line of ASCII characters in base32 coding,
   as specified in :rfc:`4648`. The return value is the converted line.

   Optional *alphabet* must be a :term:`bytes-like object` of length 32 which
   specifies an alternative alphabet.

   If *padded* is true (default), pad the encoded data with the '='
   character to a size multiple of 8.
   If *padded* is false, do not add the pad characters.

   If *wrapcol* is non-zero, insert a newline (``b'\n'``) character
   after at most every *wrapcol* characters.
   If *wrapcol* is zero (default), do not insert any newlines.

   .. versionadded:: 3.15


----

.. function:: a2b_hex(hexstr, *, ignorechars=b'')
              unhexlify(hexstr, *, ignorechars=b'')

   Return the binary data represented by the hexadecimal string *hexstr*.  This
   function is the inverse of :func:`b2a_hex`. *hexstr* must contain an even number
   of hexadecimal digits (which can be upper or lower case), otherwise an
   :exc:`Error` exception is raised.

   *ignorechars* should be a :term:`bytes-like object` containing characters
   to ignore from the input.

   Similar functionality (but more liberal towards whitespace) is also accessible
   using the :meth:`bytes.fromhex` class method.

   .. versionchanged:: 3.15
      Added the *ignorechars* parameter.



----

.. data:: BASE64_ALPHABET

   The Base 64 alphabet according to :rfc:`4648`.

   .. versionadded:: 3.15


----

.. data:: URLSAFE_BASE64_ALPHABET

   The "URL and filename safe" Base 64 alphabet according to :rfc:`4648`.

   .. versionadded:: 3.15


----

.. data:: UU_ALPHABET

   The uuencoding alphabet.

   .. versionadded:: 3.15


----

.. data:: CRYPT_ALPHABET

   The Base 64 alphabet used in the :manpage:`crypt(3)` routine and in the GEDCOM format.

   .. versionadded:: 3.15


----

.. data:: BINHEX_ALPHABET

   The Base 64 alphabet used in BinHex 4 (HQX) within the classic Mac OS.

   .. versionadded:: 3.15


----

.. data:: BASE85_ALPHABET

   The Base85 alphabet.

   .. versionadded:: 3.15


----

.. data:: ASCII85_ALPHABET

   The Ascii85 alphabet.

   .. versionadded:: 3.15


----

.. data:: Z85_ALPHABET

   The `Z85 <https://rfc.zeromq.org/spec/32/>`_ alphabet.

   .. versionadded:: 3.15


----

.. data:: BASE32_ALPHABET

   The Base 32 alphabet according to :rfc:`4648`.

   .. versionadded:: 3.15


----

.. data:: BASE32HEX_ALPHABET

   The "Extended Hex" Base 32 alphabet according to :rfc:`4648`.
   Data encoded with this alphabet maintains its sort order during bitwise
   comparisons.

   .. versionadded:: 3.15

