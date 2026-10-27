.. function:: commonprefix(list, /)

   Return the longest string prefix (taken character-by-character) that is a
   prefix of all strings in *list*.  If *list* is empty, return the empty string
   (``''``).

   .. warning::

      This function may return invalid paths because it works a
      character at a time.
      If you need a **common path prefix**, then the algorithm
      implemented in this function is not secure. Use
      :func:`commonpath` for finding a common path prefix.

      ::

        >>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
        '/usr/l'

        >>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
        '/usr'

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. deprecated:: 3.15
      Deprecated in favor of :func:`os.path.commonpath` for path prefixes.
      The :func:`os.path.commonprefix` function is being deprecated due to
      having a misleading name and module. The function is not safe to use for
      path prefixes despite being included in a module about path manipulation,
      meaning it is easy to accidentally introduce path traversal
      vulnerabilities into Python programs by using this function.



----

.. function:: realpath(path, /, *, strict=False)

   Return the canonical path of the specified filename, eliminating any symbolic
   links encountered in the path (if they are supported by the operating
   system). On Windows, this function will also resolve MS-DOS (also called 8.3)
   style names such as ``C:\\PROGRA~1`` to ``C:\\Program Files``.
   The returned path uses the case reported by the operating system,
   which can differ from the case of *path*,
   in particular the drive letter is capitalized.

   By default, the path is evaluated up to the first component that does not
   exist, is a symlink loop, or whose evaluation raises :exc:`OSError`.
   All such components are appended unchanged to the existing part of the path.

   Some errors that are handled this way include "access denied", "not a
   directory", or "bad argument to internal function". Thus, the
   resulting path may be missing or inaccessible, may still contain
   links or loops, and may traverse non-directories.

   This behavior can be modified by keyword arguments:

   If *strict* is ``True``, the first error encountered when evaluating the path is
   re-raised.
   In particular, :exc:`FileNotFoundError` is raised if *path* does not exist,
   or another :exc:`OSError` if it is otherwise inaccessible.
   If *strict* is :data:`ALL_BUT_LAST`, the last component of the path
   is allowed to be missing, but all other errors are raised.

   If *strict* is :py:data:`os.path.ALLOW_MISSING`, errors other than
   :exc:`FileNotFoundError` are re-raised (as with ``strict=True``).
   Thus, the returned path will not contain any symbolic links, but the named
   file and some of its parent directories may be missing.

   .. note::
      This function emulates the operating system's procedure for making a path
      canonical, which differs slightly between Windows and UNIX with respect
      to how links and subsequent path components interact.

      Operating system APIs make paths canonical as needed, so it's not
      normally necessary to call this function.

   .. versionchanged:: 3.6
      Accepts a :term:`path-like object`.

   .. versionchanged:: 3.8
      Symbolic links and junctions are now resolved on Windows.

   .. versionchanged:: 3.10
      The *strict* parameter was added.

   .. versionchanged:: 3.15
      The :data:`ALL_BUT_LAST` and :data:`ALLOW_MISSING` values for
      the *strict* parameter was added.


----

.. data:: ALL_BUT_LAST

   Special value used for the *strict* argument in :func:`realpath`.

   .. versionadded:: 3.15


----

.. data:: ALLOW_MISSING

   Special value used for the *strict* argument in :func:`realpath`.

   .. versionadded:: 3.15

