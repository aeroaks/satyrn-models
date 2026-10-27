.. function:: block(chr, /)

   Returns the `block
   <https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G64189>`_
   assigned to the character *chr*. For example::

      >>> unicodedata.block('S')
      'Basic Latin'

   .. versionadded:: 3.15



----

.. function:: isxidstart(chr, /)

   Return ``True`` if *chr* is a valid identifier start per the
   `Unicode Standard Annex #31 <https://www.unicode.org/reports/tr31/>`_,
   that is, it has the ``XID_Start`` property. Return ``False`` otherwise.
   For example::

      >>> unicodedata.isxidstart('S')
      True
      >>> unicodedata.isxidstart('0')
      False

   .. versionadded:: 3.15



----

.. function:: isxidcontinue(chr, /)

   Return ``True`` if *chr* is a valid identifier character per the
   `Unicode Standard Annex #31 <https://www.unicode.org/reports/tr31/>`_,
   that is, it has the ``XID_Continue`` property. Return ``False`` otherwise.
   For example::

      >>> unicodedata.isxidcontinue('S')
      True
      >>> unicodedata.isxidcontinue(' ')
      False

   .. versionadded:: 3.15



----

.. function:: grapheme_cluster_break(chr, /)

   Returns the Grapheme_Cluster_Break property assigned to the character.

   .. versionadded:: 3.15



----

.. function:: indic_conjunct_break(chr, /)

   Returns the Indic_Conjunct_Break property assigned to the character.

   .. versionadded:: 3.15



----

.. function:: extended_pictographic(chr, /)

   Returns ``True`` if the character has the Extended_Pictographic property,
   ``False`` otherwise.

   .. versionadded:: 3.15



----

.. function:: iter_graphemes(unistr, start=0, end=sys.maxsize, /)

   Returns an iterator to iterate over grapheme clusters.
   With optional *start*, iteration begins at that position.
   With optional *end*, iteration stops at that position.

   Converting an emitted item to string returns a substring corresponding to
   the grapheme cluster.
   Its ``start`` and ``end`` attributes denote the start and end of
   the grapheme cluster.

   It uses extended grapheme cluster rules defined by Unicode
   Standard Annex #29, `"Unicode Text Segmentation"
   <https://www.unicode.org/reports/tr29/>`_.

   .. versionadded:: 3.15

