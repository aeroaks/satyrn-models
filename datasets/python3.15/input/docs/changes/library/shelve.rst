.. function:: open(filename, flag='c', protocol=None, writeback=False, *, \
                   serializer=None, deserializer=None)

   Open a persistent dictionary.  The filename specified is the base filename for
   the underlying database.  As a side-effect, an extension may be added to the
   filename and more than one file may be created.  By default, the underlying
   database file is opened for reading and writing.  The optional *flag* parameter
   has the same interpretation as the *flag* parameter of :func:`dbm.open`.

   By default, pickles created with :const:`pickle.DEFAULT_PROTOCOL` are used
   to serialize values.  The version of the pickle protocol can be specified
   with the *protocol* parameter.

   Because of Python semantics, a shelf cannot know when a mutable
   persistent-dictionary entry is modified.  By default modified objects are
   written *only* when assigned to the shelf (see :ref:`shelve-example`).  If the
   optional *writeback* parameter is set to ``True``, all entries accessed are also
   cached in memory, and written back on :meth:`~Shelf.sync` and
   :meth:`~Shelf.close`; this can make it handier to mutate mutable entries in
   the persistent dictionary, but, if many entries are accessed, it can consume
   vast amounts of memory for the cache, and it can make the close operation
   very slow since all accessed entries are written back (there is no way to
   determine which accessed entries are mutable, nor which ones were actually
   mutated).

   By default, :mod:`!shelve` uses :func:`pickle.dumps` and :func:`pickle.loads`
   for serializing and deserializing. This can be changed by supplying
   *serializer* and *deserializer*, respectively.

   The *serializer* argument must be a callable which takes an object ``obj``
   and the *protocol* as inputs and returns the representation ``obj`` as a
   :term:`bytes-like object`; the *protocol* value may be ignored by the
   serializer.

   The *deserializer* argument must be a callable which takes a serialized object
   given as a :class:`bytes` object and returns the corresponding object.

   A :exc:`ShelveError` is raised if *serializer* is given but *deserializer*
   is not, or vice-versa.

   .. versionchanged:: 3.10
      :const:`pickle.DEFAULT_PROTOCOL` is now used as the default pickle
      protocol.

   .. versionchanged:: 3.11
      Accepts :term:`path-like object` for filename.

   .. versionchanged:: 3.15
      Accepts custom *serializer* and *deserializer* functions in place of
      :func:`pickle.dumps` and :func:`pickle.loads`.

   .. note::

      Do not rely on the shelf being closed automatically; always call
      :meth:`~Shelf.close` explicitly when you don't need it any more, or
      use :func:`shelve.open` as a context manager::

          with shelve.open('spam') as db:
              db['eggs'] = 'eggs'


----

.. method:: Shelf.reorganize()

   Calls :meth:`sync` and attempts to shrink space used on disk by removing empty
   space resulting from deletions.

   .. versionadded:: 3.15


----

.. class:: Shelf(dict, protocol=None, writeback=False, \
                 keyencoding='utf-8', *, serializer=None, deserializer=None)

   A subclass of :class:`collections.abc.MutableMapping` which stores pickled
   values in the *dict* object.

   By default, pickles created with :const:`pickle.DEFAULT_PROTOCOL` are used
   to serialize values.  The version of the pickle protocol can be specified
   with the *protocol* parameter.  See the :mod:`pickle` documentation for a
   discussion of the pickle protocols.

   If the *writeback* parameter is ``True``, the object will hold a cache of all
   entries accessed and write them back to the *dict* at sync and close times.
   This allows natural operations on mutable entries, but can consume much more
   memory and make sync and close take a long time.

   The *keyencoding* parameter is the encoding used to encode keys before they
   are used with the underlying dict.

   The *serializer* and *deserializer* parameters have the same interpretation
   as in :func:`~shelve.open`.

   A :class:`Shelf` object can also be used as a context manager, in which
   case it will be automatically closed when the :keyword:`with` block ends.

   .. versionchanged:: 3.2
      Added the *keyencoding* parameter; previously, keys were always encoded in
      UTF-8.

   .. versionchanged:: 3.4
      Added context manager support.

   .. versionchanged:: 3.10
      :const:`pickle.DEFAULT_PROTOCOL` is now used as the default pickle
      protocol.

   .. versionchanged:: 3.15
      Added the *serializer* and *deserializer* parameters.



----

.. class:: BsdDbShelf(dict, protocol=None, writeback=False, \
                      keyencoding='utf-8', *, \
                      serializer=None, deserializer=None)

   A subclass of :class:`Shelf` which exposes :meth:`!first`, :meth:`!next`,
   :meth:`!previous`, :meth:`!last` and :meth:`!set_location` methods.
   These are available
   in the third-party :mod:`!bsddb` module from `pybsddb
   <https://www.jcea.es/programacion/pybsddb.htm>`_ but not in other database
   modules.  The *dict* object passed to the constructor must support those
   methods.  This is generally accomplished by calling one of
   :func:`!bsddb.hashopen`, :func:`!bsddb.btopen` or :func:`!bsddb.rnopen`.  The
   optional *protocol*, *writeback*, *keyencoding*, *serializer* and *deserializer*
   parameters have the same interpretation as in :func:`~shelve.open`.

   .. versionchanged:: 3.15
      Added the *serializer* and *deserializer* parameters.



----

.. class:: DbfilenameShelf(filename, flag='c', protocol=None, \
                           writeback=False, *, serializer=None, \
                           deserializer=None)

   A subclass of :class:`Shelf` which accepts a *filename* instead of a dict-like
   object.  The underlying file will be opened using :func:`dbm.open`.  By
   default, the file will be created and opened for both read and write.  The
   optional *flag* parameter has the same interpretation as for the
   :func:`.open` function.  The optional *protocol*, *writeback*, *serializer*
   and *deserializer* parameters have the same interpretation as in
   :func:`~shelve.open`.

   .. versionchanged:: 3.15
      Added the *serializer* and *deserializer* parameters.



----

.. exception:: ShelveError

   Exception raised when one of the arguments *deserializer* and *serializer*
   is missing in the :func:`~shelve.open`, :class:`Shelf`, :class:`BsdDbShelf`
   and :class:`DbfilenameShelf`.

   The *deserializer* and *serializer* arguments must be given together.

   .. versionadded:: 3.15

