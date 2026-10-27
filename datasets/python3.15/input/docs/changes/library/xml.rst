.. function:: is_valid_name(name)

   Return ``True`` if the string is a valid element or attribute name,
   ``False`` otherwise.

   Almost all characters are permitted in names, except control characters and
   those which either are or reasonably could be used as delimiters.
   Characters like ":", "-", ".", "_", and "·" are permitted, but "<", "/",
   "!", "?", and "=" are forbidden.
   The name cannot start with a digit or a character like "-", ".", and "·".

   .. versionadded:: 3.15



----

.. function:: is_valid_text(data)

   Return ``True`` if the string is a sequence of legal XML 1.0 characters,
   ``False`` otherwise.

   Almost all characters are permitted in XML 1.0 documents, except C0 control
   characters (excluding TAB, CR and LF), surrogate characters and special
   Unicode characters U+FFFE and U+FFFF.

   .. versionadded:: 3.15

