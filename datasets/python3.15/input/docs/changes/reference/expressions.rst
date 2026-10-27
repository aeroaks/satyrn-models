Unpacking in comprehensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the expression of a list or set comprehension is starred, the result will
be :ref:`unpacked <iterable-unpacking>` to produce
zero or more elements.

This is often used for "flattening" lists, for example::

   >>> students = ['Petr', 'Blaise', 'Jarka']
   >>> teachers = ['Salim', 'Bartosz']
   >>> lists_of_people = [students, teachers]
   >>> [*people for people in lists_of_people]
   ['Petr', 'Blaise', 'Jarka', 'Salim', 'Bartosz']

At run time, this comprehension roughly corresponds to::

   def flatten_names(lists_of_people):
       result = []
       for people in lists_of_people:
           result.extend(people)
       return result

In dict comprehensions, a double-starred expression will be evaluated and
then unpacked using :ref:`dictionary unpacking <dict-unpacking>`,
inserting zero or more key/value pairs into the new dictionary.
As in other kinds of dictionary displays, if the same key is specified
multiple times, the associated value in the resulting dictionary
will be the last one specified.

For example::

   >>> system_defaults = {'color': 'blue', 'count': 8}
   >>> user_defaults = {'color': 'yellow'}
   >>> overrides = {'count': 5}

   >>> configuration_sets = [system_defaults, user_defaults, overrides]

   >>> {**d for d in configuration_sets}
   {'color': 'yellow', 'count': 5}

.. versionadded:: 3.15

   Unpacking in comprehensions using the ``*`` and ``**`` operators
   was introduced in :pep:`798`.


.. index::
   single: async for; in comprehensions
   single: await; in comprehensions
