.. c:function:: PyObject* PyDictProxy_New(PyObject *mapping)

   Return a :class:`types.MappingProxyType` object for a mapping which
   enforces read-only behavior.  This is normally used to create a view to
   prevent modification of the dictionary for non-dynamic class types.

   The first argument can be a :class:`dict`, a :class:`frozendict`, or a
   mapping.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: int PyDict_Contains(PyObject *p, PyObject *key)

   Determine if dictionary *p* contains *key*.  If an item in *p* matches
   *key*, return ``1``, otherwise return ``0``.  On error, return ``-1``.
   This is equivalent to the Python expression ``key in p``.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   .. note::

      The operation is atomic on :term:`free threading <free-threaded build>`
      when *key* is :class:`str`, :class:`int`, :class:`float`, :class:`bool` or :class:`bytes`.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: int PyDict_ContainsString(PyObject *p, const char *key)

   This is the same as :c:func:`PyDict_Contains`, but *key* is specified as a
   :c:expr:`const char*` UTF-8 encoded bytes string, rather than a
   :c:expr:`PyObject*`.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   .. versionadded:: 3.13

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: int PyDict_GetItemRef(PyObject *p, PyObject *key, PyObject **result)

   Return a new :term:`strong reference` to the object from dictionary *p*
   which has a key *key*:

   * If the key is present, set *\*result* to a new :term:`strong reference`
     to the value and return ``1``.
   * If the key is missing, set *\*result* to ``NULL`` and return ``0``.
   * On error, raise an exception, set *\*result* to ``NULL`` and return ``-1``.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   .. note::

      The operation is atomic on :term:`free threading <free-threaded build>`
      when *key* is :class:`str`, :class:`int`, :class:`float`, :class:`bool` or :class:`bytes`.

   .. versionadded:: 3.13

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.

   See also the :c:func:`PyObject_GetItem` function.



----

.. c:function:: PyObject* PyDict_GetItem(PyObject *p, PyObject *key)

   Return a :term:`borrowed reference` to the object from dictionary *p* which
   has a key *key*.  Return ``NULL`` if the key *key* is missing *without*
   setting an exception.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   .. note::

      Exceptions that occur while this calls :meth:`~object.__hash__` and
      :meth:`~object.__eq__` methods are silently ignored.
      Prefer the :c:func:`PyDict_GetItemWithError` function instead.

   .. note::

      In the :term:`free-threaded build`, the returned
      :term:`borrowed reference` may become invalid if another thread modifies
      the dictionary concurrently. Prefer :c:func:`PyDict_GetItemRef`, which
      returns a :term:`strong reference`.

   .. versionchanged:: 3.10
      Calling this API without an :term:`attached thread state` had been allowed for historical
      reason. It is no longer allowed.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: PyObject* PyDict_GetItemWithError(PyObject *p, PyObject *key)

   Variant of :c:func:`PyDict_GetItem` that does not suppress
   exceptions. Return ``NULL`` **with** an exception set if an exception
   occurred.  Return ``NULL`` **without** an exception set if the key
   wasn't present.

   .. note::

      In the :term:`free-threaded build`, the returned
      :term:`borrowed reference` may become invalid if another thread modifies
      the dictionary concurrently. Prefer :c:func:`PyDict_GetItemRef`, which
      returns a :term:`strong reference`.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: PyObject* PyDict_GetItemString(PyObject *p, const char *key)

   This is the same as :c:func:`PyDict_GetItem`, but *key* is specified as a
   :c:expr:`const char*` UTF-8 encoded bytes string, rather than a
   :c:expr:`PyObject*`.

   .. note::

      Exceptions that occur while this calls :meth:`~object.__hash__` and
      :meth:`~object.__eq__` methods or while creating the temporary :class:`str`
      object are silently ignored.
      Prefer using the :c:func:`PyDict_GetItemWithError` function with your own
      :c:func:`PyUnicode_FromString` *key* instead.

   .. note::

      In the :term:`free-threaded build`, the returned
      :term:`borrowed reference` may become invalid if another thread modifies
      the dictionary concurrently. Prefer :c:func:`PyDict_GetItemStringRef`,
      which returns a :term:`strong reference`.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: int PyDict_GetItemStringRef(PyObject *p, const char *key, PyObject **result)

   Similar to :c:func:`PyDict_GetItemRef`, but *key* is specified as a
   :c:expr:`const char*` UTF-8 encoded bytes string, rather than a
   :c:expr:`PyObject*`.

   .. versionadded:: 3.13

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: PyObject* PyDict_Items(PyObject *p)

   Return a :c:type:`PyListObject` containing all the items from the dictionary.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: PyObject* PyDict_Keys(PyObject *p)

   Return a :c:type:`PyListObject` containing all the keys from the dictionary.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: PyObject* PyDict_Values(PyObject *p)

   Return a :c:type:`PyListObject` containing all the values from the dictionary
   *p*.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: Py_ssize_t PyDict_Size(PyObject *p)

   .. index:: pair: built-in function; len

   Return the number of items in the dictionary.  This is equivalent to
   ``len(p)`` on a dictionary.

   The argument can be a :class:`dict` or a :class:`frozendict`.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: Py_ssize_t PyDict_GET_SIZE(PyObject *p)

   Similar to :c:func:`PyDict_Size`, but without error checking.

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.



----

.. c:function:: int PyDict_Next(PyObject *p, Py_ssize_t *ppos, PyObject **pkey, PyObject **pvalue)

   Iterate over all key-value pairs in the dictionary *p*.  The
   :c:type:`Py_ssize_t` referred to by *ppos* must be initialized to ``0``
   prior to the first call to this function to start the iteration; the
   function returns true for each pair in the dictionary, and false once all
   pairs have been reported.  The parameters *pkey* and *pvalue* should either
   point to :c:expr:`PyObject*` variables that will be filled in with each key
   and value, respectively, or may be ``NULL``.  Any references returned through
   them are borrowed.  *ppos* should not be altered during iteration. Its
   value represents offsets within the internal dictionary structure, and
   since the structure is sparse, the offsets are not consecutive.

   The first argument can be a :class:`dict` or a :class:`frozendict`.

   For example::

      PyObject *key, *value;
      Py_ssize_t pos = 0;

      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          /* do something interesting with the values... */
          ...
      }

   The dictionary *p* should not be mutated during iteration.  It is safe to
   modify the values of the keys as you iterate over the dictionary, but only
   so long as the set of keys does not change.  For example::

      PyObject *key, *value;
      Py_ssize_t pos = 0;

      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          long i = PyLong_AsLong(value);
          if (i == -1 && PyErr_Occurred()) {
              return -1;
          }
          PyObject *o = PyLong_FromLong(i + 1);
          if (o == NULL)
              return -1;
          if (PyDict_SetItem(self->dict, key, o) < 0) {
              Py_DECREF(o);
              return -1;
          }
          Py_DECREF(o);
      }

   The function is not thread-safe in the :term:`free-threaded <free threading>`
   build without external synchronization for a mutable :class:`dict`. You can use
   :c:macro:`Py_BEGIN_CRITICAL_SECTION` to lock the dictionary while iterating
   over it::

      Py_BEGIN_CRITICAL_SECTION(self->dict);
      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          ...
      }
      Py_END_CRITICAL_SECTION();

   The function is thread-safe on a :class:`frozendict`.

   .. note::

      On the free-threaded build, this function can be used safely inside a
      critical section. However, the references returned for *pkey* and *pvalue*
      are :term:`borrowed <borrowed reference>` and are only valid while the
      critical section is held. If you need to use these objects outside the
      critical section or when the critical section can be suspended, create a
      :term:`strong reference <strong reference>` (for example, using
      :c:func:`Py_NewRef`).

   .. versionchanged:: 3.15
      Also accept :class:`frozendict`.


----

Frozen dictionary objects
^^^^^^^^^^^^^^^^^^^^^^^^^

.. versionadded:: 3.15


.. c:var:: PyTypeObject PyFrozenDict_Type

   This instance of :c:type:`PyTypeObject` represents the Python frozen
   dictionary type.
   This is the same object as :class:`frozendict` in the Python layer.


.. c:function:: int PyAnyDict_Check(PyObject *p)

   Return true if *p* is a :class:`dict` object, a :class:`frozendict` object,
   or an instance of a subtype of the :class:`!dict` or :class:`!frozendict`
   type.
   This function always succeeds.


.. c:function:: int PyAnyDict_CheckExact(PyObject *p)

   Return true if *p* is a :class:`dict` object or a :class:`frozendict` object,
   but not an instance of a subtype of the :class:`!dict` or
   :class:`!frozendict` type.
   This function always succeeds.


.. c:function:: int PyFrozenDict_Check(PyObject *p)

   Return true if *p* is a :class:`frozendict` object or an instance of a
   subtype of the :class:`!frozendict` type.
   This function always succeeds.


.. c:function:: int PyFrozenDict_CheckExact(PyObject *p)

   Return true if *p* is a :class:`frozendict` object, but not an instance of a
   subtype of the :class:`!frozendict` type.
   This function always succeeds.


.. c:function:: PyObject* PyFrozenDict_New(PyObject *iterable)

   Return a new :class:`frozendict` from an iterable, or ``NULL`` on failure
   with an exception set.

   Create an empty dictionary if *iterable* is ``NULL``.

