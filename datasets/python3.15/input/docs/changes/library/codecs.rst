.. function:: lookup(encoding, /)

   Looks up the codec info in the Python codec registry and returns a
   :class:`CodecInfo` object as defined below.

   This function first normalizes the *encoding*: all ASCII letters are
   converted to lower case, spaces are replaced with hyphens.
   Then encoding is looked up in the registry's cache. If not found, the list of
   registered search functions is scanned. If no :class:`CodecInfo` object is
   found, a :exc:`LookupError` is raised. Otherwise, the :class:`CodecInfo` object
   is stored in the cache and returned to the caller.

   .. versionchanged:: 3.9
      Any characters except ASCII letters and digits and a dot are converted to underscore.

   .. versionchanged:: 3.15
      No characters are converted to underscore anymore.
      Spaces are converted to hyphens.

