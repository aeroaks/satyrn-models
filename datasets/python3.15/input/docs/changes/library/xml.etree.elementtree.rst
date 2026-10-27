.. function:: iterparse(source, events=None, parser=None)

   Parses an XML section into an element tree incrementally, and reports what's
   going on to the user.  *source* is a filename or :term:`file object`
   containing XML data.  *events* is a sequence of events to report back.  The
   supported events are the strings ``"start"``, ``"end"``, ``"comment"``,
   ``"pi"``, ``"start-ns"`` and ``"end-ns"``
   (the "ns" events are used to get detailed namespace
   information).  If *events* is omitted, only ``"end"`` events are reported.
   *parser* is an optional parser instance.
   If not given, the standard :class:`XMLParser` parser is used.
   *parser* must be an instance of :class:`XMLParser` or its subclass
   and can only use the default :class:`TreeBuilder` as a target.
   Returns an :term:`iterator` providing ``(event, elem)`` pairs;
   it has a ``root`` attribute that references the root element of the
   resulting XML tree once *source* is fully read.
   The iterator has the :meth:`!close` method that closes the internal
   file object if *source* is a filename.

   Note that while :func:`iterparse` builds the tree incrementally, it issues
   blocking reads on *source* (or the file it names).  As such, it's unsuitable
   for applications where blocking reads can't be made.  For fully non-blocking
   parsing, see :class:`XMLPullParser`.

   The tree is only built incrementally, it is not freed incrementally:
   every parsed element is kept until the whole document is read.
   See :ref:`elementtree-pull-parsing` for how to keep the memory usage low.

   .. note::

      :func:`iterparse` only guarantees that it has seen the ">" character of a
      starting tag when it emits a "start" event, so the attributes are defined,
      but the contents of the text and tail attributes are undefined at that
      point.  The same applies to the element children; they may or may not be
      present.

      If you need a fully populated element, look for "end" events instead.

   .. deprecated:: 3.4
      The *parser* argument.

   .. versionchanged:: 3.8
      The ``comment`` and ``pi`` events were added.

   .. versionchanged:: 3.13
      Added the :meth:`!close` method.

   .. versionchanged:: 3.15
      A :exc:`ResourceWarning` is now emitted if the iterator opened a file
      and is not explicitly closed.



----

.. function:: SubElement(parent, tag, /, attrib={}, **extra)

   Subelement factory.  This function creates an element instance, and appends
   it to an existing element.

   *parent* is the parent element.  *tag* is
   the subelement name.  *attrib* is an optional dictionary, containing element
   attributes.  *extra* contains additional attributes, given as keyword
   arguments.  Returns an element instance.

   .. versionchanged:: 3.15
      *attrib* can now be a :class:`frozendict`.

   .. versionchanged:: 3.15
      *parent* and *tag* are now positional-only parameters.



----

.. class:: Element(tag, /, attrib={}, **extra)

   Element class.  This class defines the Element interface, and provides a
   reference implementation of this interface.

   *tag* is the element name.  *attrib* is
   an optional dictionary, containing element attributes.  *extra* contains
   additional attributes, given as keyword arguments.

   The element name and the attribute names and values are strings or
   :class:`QName` instances, and the text and the tail are strings or
   ``None``.
   The element name can also be :func:`Comment` or
   :func:`ProcessingInstruction`, which are used for special elements.
   If it is ``None``, the element itself is not serialized: only its text
   and its children are written, and its attributes are ignored.
   This can be used for a fragment which contains several elements.
   With ``method="html"`` the attribute value can also be ``None``,
   which produces an empty attribute (such as ``checked``).
   Other objects can be stored in the tree, but they cannot be serialized.

   .. versionchanged:: 3.15
      *attrib* can now be a :class:`frozendict`.

   .. versionchanged:: 3.15
      *tag* is now a positional-only parameter.


   .. attribute:: tag

      A string identifying what kind of data this element represents (the
      element type, in other words).


   .. attribute:: text
                  tail

      These attributes can be used to hold additional data associated with
      the element.  Their values are usually strings but may be any
      application-specific object.  If the element is created from
      an XML file, the *text* attribute holds either the text between
      the element's start tag and its first child or end tag, or ``None``, and
      the *tail* attribute holds either the text between the element's
      end tag and the next tag, or ``None``.  For the XML data

      .. code-block:: xml

         <a><b>1<c>2<d/>3</c></b>4</a>

      the *a* element has ``None`` for both *text* and *tail* attributes,
      the *b* element has *text* ``"1"`` and *tail* ``"4"``,
      the *c* element has *text* ``"2"`` and *tail* ``None``,
      and the *d* element has *text* ``None`` and *tail* ``"3"``.

      To collect the inner text of an element, see :meth:`itertext`, for
      example ``"".join(element.itertext())``.

      Applications may store arbitrary objects in these attributes.


   .. attribute:: attrib

      A dictionary containing the element's attributes.  Note that while the
      *attrib* value is always a real mutable Python dictionary, an ElementTree
      implementation may choose to use another internal representation, and
      create the dictionary only if someone asks for it.  To take advantage of
      such implementations, use the dictionary methods below whenever possible.

   The following dictionary-like methods work on the element attributes.


   .. method:: clear()

      Resets an element.  This function removes all subelements, clears all
      attributes, and sets the text and tail attributes to ``None``.


   .. method:: get(key, default=None)

      Gets the element attribute named *key*.

      Returns the attribute value, or *default* if the attribute was not found.


   .. method:: items()

      Returns the element attributes as (name, value) pairs.


   .. method:: keys()

      Returns the element attribute names.


   .. method:: set(key, value)

      Set the attribute *key* on the element to *value*.

   The following methods work on the element's children (subelements).


   .. method:: append(subelement)

      Adds the element *subelement* to the end of this element's internal list
      of subelements.  Raises :exc:`TypeError` if *subelement* is not an
      :class:`Element`.


   .. method:: extend(subelements)

      Appends *subelements* from an iterable of elements.
      Raises :exc:`TypeError` if a subelement is not an :class:`Element`.

      .. versionadded:: 3.2


   .. method:: find(match, namespaces=None)

      Finds the first subelement matching *match*.  *match* may be a tag name
      or a :ref:`path <elementtree-xpath>`.  Returns an element instance
      or ``None``.  *namespaces* is an optional mapping from namespace prefix
      to full name.  Pass ``''`` as prefix to move all unprefixed tag names
      in the expression into the given namespace.


   .. method:: findall(match, namespaces=None)

      Finds all matching subelements, by tag name or
      :ref:`path <elementtree-xpath>`.  Returns a list containing all matching
      elements in document order.  *namespaces* is an optional mapping from
      namespace prefix to full name.  Pass ``''`` as prefix to move all
      unprefixed tag names in the expression into the given namespace.


   .. method:: findtext(match, default=None, namespaces=None)

      Finds text for the first subelement matching *match*.  *match* may be
      a tag name or a :ref:`path <elementtree-xpath>`.  Returns the text content
      of the first matching element, or *default* if no element was found.
      Note that if the matching element has no text content an empty string
      is returned. *namespaces* is an optional mapping from namespace prefix
      to full name.  Pass ``''`` as prefix to move all unprefixed tag names
      in the expression into the given namespace.


   .. method:: insert(index, subelement)

      Inserts *subelement* at the given position in this element.  Raises
      :exc:`TypeError` if *subelement* is not an :class:`Element`.


   .. method:: iter(tag=None)

      Creates a tree :term:`iterator` with the current element as the root.
      The iterator iterates over this element and all elements below it, in
      document (depth first) order.  If *tag* is not ``None`` or ``'*'``, only
      elements whose tag equals *tag* are returned from the iterator.  If the
      tree structure is modified during iteration, the result is undefined.

      .. versionadded:: 3.2


   .. method:: iterfind(match, namespaces=None)

      Finds all matching subelements, by tag name or
      :ref:`path <elementtree-xpath>`.  Returns an iterable yielding all
      matching elements in document order. *namespaces* is an optional mapping
      from namespace prefix to full name.


      .. versionadded:: 3.2


   .. method:: itertext()

      Creates a text iterator.  The iterator loops over this element and all
      subelements, in document order, and returns all inner text.

      .. versionadded:: 3.2


   .. method:: makeelement(tag, attrib)

      Creates a new element object of the same type as this element.  Do not
      call this method, use the :func:`SubElement` factory function instead.


   .. method:: remove(subelement)

      Removes *subelement* from the element.  Unlike the find\* methods this
      method compares elements based on the instance identity, not on tag value
      or contents.

   :class:`Element` objects also support the following sequence type methods
   for working with subelements: :meth:`~object.__delitem__`,
   :meth:`~object.__getitem__`, :meth:`~object.__setitem__`,
   :meth:`~object.__len__`.

   Caution: Elements with no subelements will test as ``False``.  In a future
   release of Python, all elements will test as ``True`` regardless of whether
   subelements exist.  Instead, prefer explicit ``len(elem)`` or
   ``elem is not None`` tests.::

     element = root.find('foo')

     if not element:  # careful!
         print("element not found, or element has no subelements")

     if element is None:
         print("element not found")

   .. versionchanged:: 3.12
      Testing the truth value of an Element emits :exc:`DeprecationWarning`.

   Prior to Python 3.8, the serialisation order of the XML attributes of
   elements was artificially made predictable by sorting the attributes by
   their name. Based on the now guaranteed ordering of dicts, this arbitrary
   reordering was removed in Python 3.8 to preserve the order in which
   attributes were originally parsed or created by user code.

   In general, user code should try not to depend on a specific ordering of
   attributes, given that the `XML Information Set
   <https://www.w3.org/TR/xml-infoset/>`_ explicitly excludes the attribute
   order from conveying information. Code should be prepared to deal with
   any ordering on input. In cases where deterministic XML output is required,
   e.g. for cryptographic signing or test data sets, canonical serialisation
   is available with the :func:`canonicalize` function.

   In cases where canonical output is not applicable but a specific attribute
   order is still desirable on output, code should aim for creating the
   attributes directly in the desired order, to avoid perceptual mismatches
   for readers of the code. In cases where this is difficult to achieve, a
   recipe like the following can be applied prior to serialisation to enforce
   an order independently from the Element creation::

     def reorder_attributes(root):
         for el in root.iter():
             attrib = el.attrib
             if len(attrib) > 1:
                 # adjust attribute order, e.g. by sorting
                 attribs = sorted(attrib.items())
                 attrib.clear()
                 attrib.update(attribs)

