.. function:: adler32_combine(adler1, adler2, len2, /)

   Combine two Adler-32 checksums into one.

   Given the Adler-32 checksum *adler1* of a sequence ``A`` and the
   Adler-32 checksum *adler2* of a sequence ``B`` of length *len2*,
   return the Adler-32 checksum of ``A`` and ``B`` concatenated.

   This function is typically useful to combine Adler-32 checksums
   that were concurrently computed. To compute checksums sequentially, use
   :func:`adler32` with the running checksum as the ``value`` argument.

   .. versionadded:: 3.15


----

.. function:: crc32_combine(crc1, crc2, len2, /)

   Combine two CRC-32 checksums into one.

   Given the CRC-32 checksum *crc1* of a sequence ``A`` and the
   CRC-32 checksum *crc2* of a sequence ``B`` of length *len2*,
   return the CRC-32 checksum of ``A`` and ``B`` concatenated.

   This function is typically useful to combine CRC-32 checksums
   that were concurrently computed. To compute checksums sequentially, use
   :func:`crc32` with the running checksum as the ``value`` argument.

   .. versionadded:: 3.15
