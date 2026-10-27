Soft Keywords
-------------

.. index:: soft keyword, keyword

.. versionadded:: 3.10

Some names are only reserved under specific contexts. These are known as
*soft keywords*:

- ``match``, ``case``, and ``_``, when used in the :keyword:`match` statement.
- ``type``, when used in the :keyword:`type` statement.
- ``lazy``, when used before an :keyword:`import` statement.

These syntactically act as keywords in their specific contexts,
but this distinction is done at the parser level, not when tokenizing.

As soft keywords, their use in the grammar is possible while still
preserving compatibility with existing code that uses these names as
identifier names.

.. versionchanged:: 3.12
   ``type`` is now a soft keyword.

.. versionchanged:: 3.15
   ``lazy`` is now a soft keyword.

.. index::
   single: _, identifiers
   single: __, identifiers
.. _id-classes:
