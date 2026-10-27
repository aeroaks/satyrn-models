.. function:: prefixmatch(pattern, string, flags=0)

   If zero or more characters at the beginning of *string* match the regular
   expression *pattern*, return a corresponding :class:`~re.Match`.  Return
   ``None`` if the string does not match the pattern; note that this is
   different from a zero-length match.

   .. note::

      Even in :const:`MULTILINE` mode, this will only match at the
      beginning of the string and not at the beginning of each line.

   If you want to locate a match anywhere in *string*, use :func:`search`
   instead (see also :ref:`search-vs-match`).

   The expression's behaviour can be modified by specifying a *flags* value.
   Values can be any of the `flags`_ variables, combined using bitwise OR
   (the ``|`` operator).

   This function now has two names and has long been known as
   :func:`~re.match`.  Use that name when you need to retain compatibility with
   older Python versions.

   .. versionadded:: 3.15


----

.. function:: match(pattern, string, flags=0)

   .. soft-deprecated:: 3.15
      :func:`~re.match` has been :term:`soft deprecated` in favor of
      the alternate :func:`~re.prefixmatch` name of this API which is
      more explicitly descriptive. Use it to better
      express intent. The norm in other languages and regular expression
      implementations is to use the term *match* to refer to the behavior of
      what Python has always called :func:`~re.search`.
      See :ref:`prefixmatch-vs-match`.



----

.. method:: Pattern.prefixmatch(string[, pos[, endpos]])

   If zero or more characters at the *beginning* of *string* match this regular
   expression, return a corresponding :class:`~re.Match`. Return ``None`` if the
   string does not match the pattern; note that this is different from a
   zero-length match.

   Note that even in :const:`MULTILINE` mode, this will only match at the
   beginning of the string and not at the beginning of each line.

   The optional *pos* and *endpos* parameters have the same meaning as for the
   :meth:`~Pattern.search` method. ::

      >>> pattern = re.compile("o")
      >>> pattern.prefixmatch("dog")     # No match as "o" is not at the start of "dog".
      >>> pattern.prefixmatch("dog", 1)  # Match as "o" is the 2nd character of "dog".
      <re.Match object; span=(1, 2), match='o'>

   If you want to locate a match anywhere in *string*, use
   :meth:`~Pattern.search` instead (see also :ref:`search-vs-match`).

   This method now has two names and has long been known as
   :meth:`~Pattern.match`.  Use that name when you need to retain compatibility
   with older Python versions.

   .. versionadded:: 3.15


----

.. method:: Pattern.match(string[, pos[, endpos]])

   .. soft-deprecated:: 3.15
      :meth:`~Pattern.match` has been :term:`soft deprecated` in favor of
      the alternate :meth:`~Pattern.prefixmatch` name of this API which is
      more explicitly descriptive. Use it to
      better express intent. The norm in other languages and regular expression
      implementations is to use the term *match* to refer to the behavior of
      what Python has always called :meth:`~Pattern.search`.
      See :ref:`prefixmatch-vs-match`.



----

prefixmatch() vs. match()
^^^^^^^^^^^^^^^^^^^^^^^^^

Why is the :func:`~re.match` function and method discouraged in
favor of the longer :func:`~re.prefixmatch` spelling?

Many other languages have gained regex support libraries since regular
expressions were added to Python. However in the most popular of those, they
use the term *match* in their APIs to mean the unanchored behavior provided in
Python by :func:`~re.search`. Thus use of the plain term *match* can be
unclear to those used to other languages when reading or writing code and
not familiar with the Python API's divergence from what otherwise become the
industry norm.

Quoting from the Zen Of Python (``python3 -m this``): *"Explicit is better than
implicit"*. Anyone reading the name :func:`!prefixmatch` is likely to
understand the intended semantics. When reading :func:`!match` there remains
a seed of doubt about the intended behavior to anyone not already familiar with
this old Python gotcha.

We **do not** plan to remove the older :func:`!match` name,
as it has been used in code for over 30 years.
It has been :term:`soft deprecated`:
code supporting older versions of Python should continue to use :func:`!match`,
while new code should prefer :func:`!prefixmatch`.

.. versionadded:: 3.15
   :func:`!prefixmatch`

.. soft-deprecated:: 3.15
   :func:`!match`
