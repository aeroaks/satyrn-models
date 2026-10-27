:class:`Counter` objects
------------------------

A counter tool is provided to support convenient and rapid tallies.
For example::

    >>> # Tally occurrences of words in a list
    >>> cnt = Counter()
    >>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    ...     cnt[word] += 1
    ...
    >>> cnt
    Counter({'blue': 3, 'red': 2, 'green': 1})

    >>> # Find the ten most common words in Hamlet
    >>> import re
    >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
    >>> Counter(words).most_common(10)
    [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
     ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

.. class:: Counter(**kwargs)
           Counter(iterable, /, **kwargs)
           Counter(mapping, /, **kwargs)

    A :class:`Counter` is a :class:`dict` subclass for counting :term:`hashable` objects.
    It is a collection where elements are stored as dictionary keys
    and their counts are stored as dictionary values.  Counts are allowed to be
    any integer value including zero or negative counts.  The :class:`Counter`
    class is similar to bags or multisets in other languages.

    Elements are counted from an *iterable* or initialized from another
    *mapping* (or counter):

        >>> c = Counter()                           # a new, empty counter
        >>> c = Counter('gallahad')                 # a new counter from an iterable
        >>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
        >>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

    Counter objects have a dictionary interface except that they return a zero
    count for missing items instead of raising a :exc:`KeyError`:

        >>> c = Counter(['eggs', 'ham'])
        >>> c['bacon']                              # count of a missing element is zero
        0

    Setting a count to zero does not remove an element from a counter.
    Use ``del`` to remove it entirely:

        >>> c['sausage'] = 0                        # counter entry with a zero count
        >>> del c['sausage']                        # del actually removes the entry

    .. versionadded:: 3.1

    .. versionchanged:: 3.7 As a :class:`dict` subclass, :class:`Counter`
       inherited the capability to remember insertion order.  Math operations
       on *Counter* objects also preserve order.  Results are ordered
       according to when an element is first encountered in the left operand
       and then by the order encountered in the right operand.

    Counter objects support additional methods beyond those available for all
    dictionaries:

    .. method:: elements()

        Return an iterator over elements repeating each as many times as its
        count.  Elements are returned in the order first encountered. If an
        element's count is less than one, :meth:`elements` will ignore it.

            >>> c = Counter(a=4, b=2, c=0, d=-2)
            >>> sorted(c.elements())
            ['a', 'a', 'a', 'a', 'b', 'b']

    .. method:: most_common(n=None)

        Return a list of the *n* most common elements and their counts from the
        most common to the least.  If *n* is omitted or ``None``,
        :meth:`most_common` returns *all* elements in the counter.
        Elements with equal counts are ordered in the order first encountered:

            >>> Counter('abracadabra').most_common(3)
            [('a', 5), ('b', 2), ('r', 2)]

    .. method:: subtract(**kwargs)
                subtract(iterable, /, **kwargs)
                subtract(mapping, /, **kwargs)

        Elements are subtracted from an *iterable* or from another *mapping*
        (or counter).  Like :meth:`dict.update` but subtracts counts instead
        of replacing them.  Both inputs and outputs may be zero or negative.

            >>> c = Counter(a=4, b=2, c=0, d=-2)
            >>> d = Counter(a=1, b=2, c=3, d=4)
            >>> c.subtract(d)
            >>> c
            Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

        .. versionadded:: 3.2

    .. method:: total()

        Compute the sum of the counts.

            >>> c = Counter(a=10, b=5, c=0)
            >>> c.total()
            15

        .. versionadded:: 3.10

    The usual dictionary methods are available for :class:`Counter` objects
    except for these two which work differently for counters:

    .. method:: fromkeys(iterable)

        This class method is not implemented for :class:`Counter` objects.

    .. method:: update(**kwargs)
                update(iterable, /, **kwargs)
                update(mapping, /, **kwargs)

        Elements are counted from an *iterable* or added-in from another
        *mapping* (or counter).  Like :meth:`dict.update` but adds counts
        instead of replacing them.  Also, the *iterable* is expected to be a
        sequence of elements, not a sequence of ``(key, value)`` pairs.

Counters support rich comparison operators for equality, subset, and
superset relationships: ``==``, ``!=``, ``<``, ``<=``, ``>``, ``>=``.
All of those tests treat missing elements as having zero counts so that
``Counter(a=1) == Counter(a=1, b=0)`` returns true.

.. versionchanged:: 3.10
   Rich comparison operations were added.

.. versionchanged:: 3.10
   In equality tests, missing elements are treated as having zero counts.
   Formerly, ``Counter(a=3)`` and ``Counter(a=3, b=0)`` were considered
   distinct.

Common patterns for working with :class:`Counter` objects::

    c.total()                       # total of all counts
    c.clear()                       # reset all counts
    list(c)                         # list unique elements
    set(c)                          # convert to a set
    dict(c)                         # convert to a regular dictionary
    c.items()                       # access the (elem, cnt) pairs
    Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
    c.most_common()[:-n-1:-1]       # n least common elements
    +c                              # remove zero and negative counts

Several mathematical operations are provided for combining :class:`Counter`
objects to produce multisets (counters that have counts greater than zero).
Addition and subtraction combine counters by adding or subtracting the counts
of corresponding elements.  Intersection and union return the minimum and
maximum of corresponding counts.  Symmetric difference returns the difference
between the maximum and minimum of the corresponding counts. Equality and
inclusion compare corresponding counts.  Each operation can accept inputs
with signed counts, but the output will exclude results with counts of zero
or below.

.. doctest::

    >>> c = Counter(a=3, b=1)
    >>> d = Counter(a=1, b=2)
    >>> c + d                       # add two counters together:  c[x] + d[x]
    Counter({'a': 4, 'b': 3})
    >>> c - d                       # subtract (keeping only positive counts)
    Counter({'a': 2})
    >>> c & d                       # intersection:  min(c[x], d[x])
    Counter({'a': 1, 'b': 1})
    >>> c | d                       # union:  max(c[x], d[x])
    Counter({'a': 3, 'b': 2})
    >>> c ^ d                       # max(c[x], d[x]) - min(c[x], d[x])
    Counter({'a': 2, 'b': 1})
    >>> c == d                      # equality:  c[x] == d[x]
    False
    >>> c <= d                      # inclusion:  c[x] <= d[x]
    False

Unary addition and subtraction are shortcuts for adding an empty counter
or subtracting from an empty counter.

    >>> c = Counter(a=2, b=-4)
    >>> +c
    Counter({'a': 2})
    >>> -c
    Counter({'b': 4})

.. versionadded:: 3.3
    Added support for unary plus, unary minus, and in-place multiset operations.

.. versionadded:: 3.15
    Added support for the symmetric difference multiset operation, ``c ^ d``.

.. note::

    Counters were primarily designed to work with positive integers to represent
    running counts; however, care was taken to not unnecessarily preclude use
    cases needing other types or negative values.  To help with those use cases,
    this section documents the minimum range and type restrictions.

    * The :class:`Counter` class itself is a dictionary subclass with no
      restrictions on its keys and values.  The values are intended to be numbers
      representing counts, but you *could* store anything in the value field.

    * The :meth:`~Counter.most_common` method requires only that the values be orderable.

    * For in-place operations such as ``c[key] += 1``, the value type need only
      support addition and subtraction.  So fractions, floats, and decimals would
      work and negative values are supported.  The same is also true for
      :meth:`~Counter.update` and :meth:`~Counter.subtract` which allow negative and zero values
      for both inputs and outputs.

    * The multiset methods are designed only for use cases with positive values.
      The inputs may be negative or zero, but only outputs with positive values
      are created.  There are no type restrictions, but the value type needs to
      support addition, subtraction, and comparison.

    * The :meth:`~Counter.elements` method requires integer counts.  It ignores zero and
      negative counts.

.. seealso::

   * `Bag class <https://www.gnu.org/software/smalltalk/manual-base/html_node/Bag.html>`_
     in Smalltalk.

   * Wikipedia entry for `Multisets <https://en.wikipedia.org/wiki/Multiset>`_.

   * `C++ multisets <http://www.java2s.com/Tutorial/Cpp/0380__set-multiset/Catalog0380__set-multiset.htm>`_
     tutorial with examples.

   * For mathematical operations on multisets and their use cases, see
     *Knuth, Donald. The Art of Computer Programming Volume II,
     Section 4.6.3, Exercise 19*.

   * To enumerate all distinct multisets of a given size over a given set of
     elements, see :func:`itertools.combinations_with_replacement`::

        map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC

