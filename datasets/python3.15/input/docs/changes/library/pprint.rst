.. function:: pp(object, stream=None, indent=1, width=80, depth=None, *, \
                 compact=False, expand=False, sort_dicts=False, \
                 underscore_numbers=False)

   Prints the formatted representation of *object*, followed by a newline.
   This function may be used in the interactive interpreter
   instead of the :func:`print` function for inspecting values.
   Tip: you can reassign ``print = pprint.pp`` for use within a scope.

   :param object:
      The object to be printed.

   :param stream:
      A file-like object to which the output will be written
      by calling its :meth:`!write` method.
      If ``None`` (the default), :data:`sys.stdout` is used.
   :type stream: :term:`file-like object` | None

   :param int indent:
      The amount of indentation added for each nesting level.

   :param int width:
      The desired maximum number of characters per line in the output.
      If a structure cannot be formatted within the width constraint,
      a best effort will be made.

   :param depth:
      The number of nesting levels which may be printed.
      If the data structure being printed is too deep,
      the next contained level is replaced by ``...``.
      If ``None`` (the default), there is no constraint
      on the depth of the objects being formatted.
   :type depth: int | None

   :param bool compact:
      Control the way long :term:`sequences <sequence>` are formatted.
      If ``False`` (the default),
      each item of a sequence will be formatted on a separate line,
      otherwise as many items as will fit within the *width*
      will be formatted on each output line.
      Incompatible with *expand*.

   :param bool expand:
      If ``True``,
      opening parentheses and brackets will be followed by a newline and the
      following content will be indented by one level, similar to
      pretty-printed JSON. Incompatible with *compact*.

   :param bool sort_dicts:
      If ``True``, dictionaries will be formatted with
      their keys sorted, otherwise
      they will be displayed in insertion order (the default).

   :param bool underscore_numbers:
      If ``True``,
      integers will be formatted with the ``_`` character for a thousands separator,
      otherwise underscores are not displayed (the default).

   >>> import pprint
   >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
   >>> stuff.insert(0, stuff)
   >>> pprint.pp(stuff)
   [<Recursion on list with id=...>,
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']

   .. versionadded:: 3.8

   .. versionchanged:: 3.10
      Added the *underscore_numbers* parameter.

   .. versionchanged:: 3.11
      No longer attempts to write to :data:`!sys.stdout` if it is ``None``.

   .. versionchanged:: 3.15
      Added the *expand* parameter.



----

.. class:: PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, \
                         compact=False, expand=False, sort_dicts=True, \
                         underscore_numbers=False)

   Construct a :class:`PrettyPrinter` instance.

   Arguments have the same meaning as for :func:`~pprint.pp`.
   Note that they are in a different order, and that *sort_dicts* defaults to ``True``.

   >>> import pprint
   >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
   >>> stuff.insert(0, stuff[:])
   >>> pp = pprint.PrettyPrinter(indent=4)
   >>> pp.pprint(stuff)
   [   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
       'spam',
       'eggs',
       'lumberjack',
       'knights',
       'ni']
   >>> pp = pprint.PrettyPrinter(width=41, compact=True)
   >>> pp.pprint(stuff)
   [['spam', 'eggs', 'lumberjack',
     'knights', 'ni'],
    'spam', 'eggs', 'lumberjack', 'knights',
    'ni']
   >>> pp = pprint.PrettyPrinter(width=41, expand=True, indent=3)
   >>> pp.pprint(stuff)
   [
      [
         'spam',
         'eggs',
         'lumberjack',
         'knights',
         'ni',
      ],
      'spam',
      'eggs',
      'lumberjack',
      'knights',
      'ni',
   ]
   >>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
   ... ('parrot', ('fresh fruit',))))))))
   >>> pp = pprint.PrettyPrinter(depth=6)
   >>> pp.pprint(tup)
   ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))


   .. versionchanged:: 3.4
      Added the *compact* parameter.

   .. versionchanged:: 3.8
      Added the *sort_dicts* parameter.

   .. versionchanged:: 3.10
      Added the *underscore_numbers* parameter.

   .. versionchanged:: 3.11
      No longer attempts to write to :data:`!sys.stdout` if it is ``None``.

   .. versionchanged:: 3.15
      Added the *expand* parameter.

