.. c:function:: int PyType_Watch(int watcher_id, PyObject *type)

   Mark *type* as watched. The callback granted *watcher_id* by
   :c:func:`PyType_AddWatcher` will be called whenever
   :c:func:`PyType_Modified` reports a change to *type*. (The callback may be
   called only once for a series of consecutive modifications to *type*, if
   :c:func:`!_PyType_Lookup` is not called on *type* between the modifications;
   this is an implementation detail and subject to change.)

   The callback is also invoked when a watched heap type is deallocated.

   An extension should never call ``PyType_Watch`` with a *watcher_id* that was
   not returned to it by a previous call to :c:func:`PyType_AddWatcher`.

   .. versionadded:: 3.12

   .. versionchanged:: 3.15
      The callback is now also invoked when a watched heap type is deallocated.



----

.. c:type:: int (*PyType_WatchCallback)(PyObject *type)

   Type of a type-watcher callback function.

   The callback must not modify *type* or cause :c:func:`PyType_Modified` to be
   called on *type* or any type in its MRO; violating this rule could cause
   infinite recursion.

   The callback may be called during type deallocation. In this case, the type
   object is temporarily resurrected (its reference count is at least 1) and all
   its attributes are still valid. However, the callback should not store new
   strong references to the type, as this would resurrect the object and prevent
   its deallocation.

   .. versionadded:: 3.12

   .. versionchanged:: 3.15
      The callback may now be called during deallocation of a watched heap type.



----

.. c:function:: PyObject* PyType_GetModuleByToken(PyTypeObject *type, const void *mod_token)

   Find the first superclass whose module has the given
   :ref:`module token <ext-module-token>`, and return that module.

   If no module is found, raises a :py:class:`TypeError` and returns ``NULL``.

   This function is intended to be used together with
   :c:func:`PyModule_GetState()` to get module state from slot methods (such as
   :c:member:`~PyTypeObject.tp_init` or :c:member:`~PyNumberMethods.nb_add`)
   and other places where a method's defining class cannot be passed using the
   :c:type:`PyCMethod` calling convention.

   .. versionadded:: 3.15



----

Type slot IDs
.............

Most type slot IDs are named like the field names of the structures
:c:type:`PyTypeObject`, :c:type:`PyNumberMethods`,
:c:type:`PySequenceMethods`, :c:type:`PyMappingMethods` and
:c:type:`PyAsyncMethods` with an added ``Py_`` prefix.
For example, use:

* :c:data:`Py_tp_dealloc` to set :c:member:`PyTypeObject.tp_dealloc`
* :c:data:`Py_nb_add` to set :c:member:`PyNumberMethods.nb_add`
* :c:data:`Py_sq_length` to set :c:member:`PySequenceMethods.sq_length`

The following slots need additional considerations when specified as slots:

* :c:data:`Py_tp_name`
* :c:data:`Py_tp_basicsize` and :c:data:`Py_tp_extra_basicsize`
* :c:data:`Py_tp_itemsize`
* :c:data:`Py_tp_flags`

Additional slots do not directly correspond to a :c:type:`!PyTypeObject`
struct field:

* :c:data:`Py_tp_token`
* :c:data:`Py_tp_metaclass`
* :c:data:`Py_tp_module`

The following “offset” fields cannot be set using :c:type:`PyType_Slot`:

* :c:member:`~PyTypeObject.tp_weaklistoffset`
  (use :c:macro:`Py_TPFLAGS_MANAGED_WEAKREF` instead if possible)
* :c:member:`~PyTypeObject.tp_dictoffset`
  (use :c:macro:`Py_TPFLAGS_MANAGED_DICT` instead if possible)
* :c:member:`~PyTypeObject.tp_vectorcall_offset`
  (use ``"__vectorcalloffset__"`` in :ref:`PyMemberDef <pymemberdef-offsets>`)

If it is not possible to switch to a ``MANAGED`` flag (for example,
for vectorcall or to support Python older than 3.12), specify the
offset in :c:data:`Py_tp_members`.
See :ref:`PyMemberDef documentation <pymemberdef-offsets>`
for details.

The following internal fields cannot be set at all when creating a heap
type:

* :c:member:`~PyTypeObject.tp_dict`,
  :c:member:`~PyTypeObject.tp_mro`,
  :c:member:`~PyTypeObject.tp_cache`,
  :c:member:`~PyTypeObject.tp_subclasses`, and
  :c:member:`~PyTypeObject.tp_weaklist`.

The :c:data:`Py_tp_base` slot is equivalent to :c:data:`Py_tp_bases`;
both may be set either to a type or a tuple of types.
If both are specified, the value of :c:data:`Py_tp_bases`
is used.

Slot values may not be ``NULL``, except for the following:

* :c:data:`Py_tp_doc`
* :c:data:`Py_tp_token` (for clarity, prefer :c:data:`Py_TP_USE_SPEC`
  rather than ``NULL``)

.. versionchanged:: 3.9
   Slots in :c:type:`PyBufferProcs` may be set in the unlimited API.

.. versionchanged:: 3.11
   :c:member:`~PyBufferProcs.bf_getbuffer` and
   :c:member:`~PyBufferProcs.bf_releasebuffer` are now available
   under the :ref:`limited API <limited-c-api>`.

.. versionchanged:: 3.14
   The field :c:member:`~PyTypeObject.tp_vectorcall` can now be set
   using :c:data:`Py_tp_vectorcall`.  See the field's documentation
   for details.

.. versionchanged:: 3.15
   The :c:data:`Py_tp_bases` slot may be set to a single type object,
   making it equivalent to the :c:data:`Py_tp_base` slot.
   Previously, a tuple of types was required.

The following slots correspond to fields in the underlying type structure,
but need extra remarks for use as slots:

.. c:macro:: Py_tp_name

   :c:member:`Slot ID <PySlot.sl_id>` for the name of the type,
   used to set :c:member:`PyTypeObject.tp_name`.

   This slot (or :c:member:`PyType_Spec.name`) is required to create a type.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:member:`PyType_Spec.name` instead.

   .. impl-detail::

      CPython processes slots in order.
      It is recommended to put ``Py_tp_name`` at the beginning of the slots
      array, so that if processing of a later slots fails, error messages
      can include the name.

   .. versionadded:: 3.15

.. c:macro:: Py_tp_basicsize

   :c:member:`Slot ID <PySlot.sl_id>` for the size of the instance in bytes.
   It is used to set :c:member:`PyTypeObject.tp_basicsize`.

   The value must be positive.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:member:`PyType_Spec.basicsize` instead.

   This slot may not be used with :c:func:`PyType_GetSlot`.
   Use :c:member:`PyTypeObject.tp_basicsize` instead if needed, but be aware
   that a type's size is often considered an implementation detail.

   .. versionadded:: 3.15

.. c:macro:: Py_tp_extra_basicsize

   :c:member:`Slot ID <PySlot.sl_id>` for type data size in bytes, that is,
   how much space instances of the class need *in addition*
   to space needed for superclasses.

   The value is used, together with the size of superclasses, to set
   :c:member:`PyTypeObject.tp_basicsize`.
   Python will insert padding as needed to meet
   :c:member:`!tp_basicsize`'s alignment requirements.

   Use :c:func:`PyObject_GetTypeData` to get a pointer to subclass-specific
   memory reserved this way.

   The value must be positive.
   To specify that instances need no additional size (that is, size should be
   inherited), omit the :c:macro:`!Py_tp_extra_basicsize` slot rather than
   set it to zero.

   Specifying both :c:macro:`Py_tp_basicsize` and
   :c:macro:`!Py_tp_extra_basicsize` is an error.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use negative :c:member:`PyType_Spec.basicsize` instead.

   This slot may not be used with :c:func:`PyType_GetSlot`.

   .. versionadded:: 3.15

.. c:macro:: Py_tp_itemsize

   :c:member:`Slot ID <PySlot.sl_id>` for the size of one element of a
   variable-size type, in bytes.
   Used to set :c:member:`PyTypeObject.tp_itemsize`.
   See :c:member:`!tp_itemsize` documentation for caveats.

   The value must be positive.

   If this slot is missing, :c:member:`~PyTypeObject.tp_itemsize` is inherited.
   Extending arbitrary variable-sized classes is dangerous,
   since some types use a fixed offset for variable-sized memory,
   which can then overlap fixed-sized memory used by a subclass.
   To help prevent mistakes, inheriting ``itemsize`` is only possible
   in the following situations:

   - The base is not variable-sized (its
     :c:member:`~PyTypeObject.tp_itemsize` is zero).
   - The requested :c:member:`PyType_Spec.basicsize` is positive,
     suggesting that the memory layout of the base class is known.
   - The requested :c:member:`PyType_Spec.basicsize` is zero,
     suggesting that the subclass does not access the instance's memory
     directly.
   - With the :c:macro:`Py_TPFLAGS_ITEMS_AT_END` flag.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:member:`PyType_Spec.itemsize` instead.


----

.. c:macro:: Py_tp_name

   :c:member:`Slot ID <PySlot.sl_id>` for the name of the type,
   used to set :c:member:`PyTypeObject.tp_name`.

   This slot (or :c:member:`PyType_Spec.name`) is required to create a type.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:member:`PyType_Spec.name` instead.

   .. impl-detail::

      CPython processes slots in order.
      It is recommended to put ``Py_tp_name`` at the beginning of the slots
      array, so that if processing of a later slots fails, error messages
      can include the name.

   .. versionadded:: 3.15


----

.. c:macro:: Py_tp_basicsize

   :c:member:`Slot ID <PySlot.sl_id>` for the size of the instance in bytes.
   It is used to set :c:member:`PyTypeObject.tp_basicsize`.

   The value must be positive.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:member:`PyType_Spec.basicsize` instead.

   This slot may not be used with :c:func:`PyType_GetSlot`.
   Use :c:member:`PyTypeObject.tp_basicsize` instead if needed, but be aware
   that a type's size is often considered an implementation detail.

   .. versionadded:: 3.15


----

.. c:macro:: Py_tp_extra_basicsize

   :c:member:`Slot ID <PySlot.sl_id>` for type data size in bytes, that is,
   how much space instances of the class need *in addition*
   to space needed for superclasses.

   The value is used, together with the size of superclasses, to set
   :c:member:`PyTypeObject.tp_basicsize`.
   Python will insert padding as needed to meet
   :c:member:`!tp_basicsize`'s alignment requirements.

   Use :c:func:`PyObject_GetTypeData` to get a pointer to subclass-specific
   memory reserved this way.

   The value must be positive.
   To specify that instances need no additional size (that is, size should be
   inherited), omit the :c:macro:`!Py_tp_extra_basicsize` slot rather than
   set it to zero.

   Specifying both :c:macro:`Py_tp_basicsize` and
   :c:macro:`!Py_tp_extra_basicsize` is an error.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use negative :c:member:`PyType_Spec.basicsize` instead.

   This slot may not be used with :c:func:`PyType_GetSlot`.

   .. versionadded:: 3.15


----

.. c:macro:: Py_tp_itemsize

   :c:member:`Slot ID <PySlot.sl_id>` for the size of one element of a
   variable-size type, in bytes.
   Used to set :c:member:`PyTypeObject.tp_itemsize`.
   See :c:member:`!tp_itemsize` documentation for caveats.

   The value must be positive.

   If this slot is missing, :c:member:`~PyTypeObject.tp_itemsize` is inherited.
   Extending arbitrary variable-sized classes is dangerous,
   since some types use a fixed offset for variable-sized memory,
   which can then overlap fixed-sized memory used by a subclass.
   To help prevent mistakes, inheriting ``itemsize`` is only possible
   in the following situations:

   - The base is not variable-sized (its
     :c:member:`~PyTypeObject.tp_itemsize` is zero).
   - The requested :c:member:`PyType_Spec.basicsize` is positive,
     suggesting that the memory layout of the base class is known.
   - The requested :c:member:`PyType_Spec.basicsize` is zero,
     suggesting that the subclass does not access the instance's memory
     directly.
   - With the :c:macro:`Py_TPFLAGS_ITEMS_AT_END` flag.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:member:`PyType_Spec.itemsize` instead.

   This slot may not be used with :c:func:`PyType_GetSlot`.

   .. versionadded:: 3.15


----

.. c:macro:: Py_tp_flags

   :c:member:`Slot ID <PySlot.sl_id>` for type flags, used to set
   :c:member:`PyTypeObject.tp_flags`.

   The ``Py_TPFLAGS_HEAPTYPE`` flag is not set,
   :c:func:`PyType_FromSpecWithBases` sets it automatically.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use negative :c:member:`PyType_Spec.basicsize` instead.

   This slot may not be used with :c:func:`PyType_GetSlot`.
   Use :c:func:`PyType_GetFlags` instead.

   .. versionadded:: 3.15


----

.. c:macro:: Py_tp_bases

   :c:member:`Slot ID <PySlot.sl_id>` for type flags, used to set
   :c:member:`PyTypeObject.tp_bases`.

   The slot can be set to a tuple of type objects which the newly created
   type should inherit from, like the "positional arguments" of
   a Python :ref:`class definition <class>`.

   Alternately, the slot can be set to a single type object to specify
   a single base.
   The effect is the same as specifying a one-element tuple.

   .. versionchanged:: 3.15

      Previously, :c:macro:`!Py_tp_bases` required a tuple of types.


----

.. c:macro:: Py_tp_base

   Equivalent to :c:macro:`Py_tp_bases` (with ``s`` at the end).
   If both are specified, :c:macro:`!Py_tp_bases` takes priority and
   this slot is ignored.

   .. versionchanged:: 3.15

      Previously, :c:macro:`!Py_tp_base` required a single type, not a tuple.

   .. soft-deprecated:: 3.15

      When not targeting older Python versions, prefer :c:macro:`!Py_tp_bases`.


----

.. c:macro:: Py_tp_metaclass

   :c:member:`Slot ID <PySlot.sl_id>` for the metaclass used to construct
   the resulting type object.
   When omitted the metaclass is derived from bases
   (:c:macro:`Py_tp_bases` or the *bases* argument of
   :c:func:`PyType_FromMetaclass`).

   Metaclasses that override :c:member:`~PyTypeObject.tp_new` are not
   supported, except if ``tp_new`` is ``NULL``.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:func:`PyType_FromMetaclass` to specify a metaclass with
   :c:type:`!PyType_Spec`.

   This slot may not be used with :c:func:`PyType_GetSlot`.
   Use :c:func:`Py_TYPE` on the type object instead.

   .. versionadded:: 3.15


----

.. c:macro:: Py_tp_module

   :c:member:`Slot ID <PySlot.sl_id>` for recording the module in which
   the new class is defined.

   The value must be a module object.
   The module is associated with the new type and can later be
   retrieved with :c:func:`PyType_GetModule`.
   The associated module is not inherited by subclasses; it must be specified
   for each class individually.

   This may not be used in :c:member:`PyType_Spec.slots`.
   Use :c:func:`PyType_FromMetaclass` to specify a module with
   :c:type:`!PyType_Spec`.

   This slot may not be used with :c:func:`PyType_GetSlot`.
   Use :c:func:`PyType_GetModule` instead.

   .. versionadded:: 3.15


----

.. c:macro:: Py_tp_slots

   :c:member:`Slot ID <PySlot.sl_id>` that works like
   :c:macro:`Py_slot_subslots`, except it specifies an array of
   :c:type:`PyType_Slot` structures.

   .. versionadded:: 3.15


Soft-deprecated API
-------------------

The following functions are :term:`soft deprecated`.
They will continue to work, but new features will be added as slots for
:c:func:`PyType_FromSlots`, not as arguments to new ``PyType_From*`` functions.

.. c:function:: PyObject* PyType_FromMetaclass(PyTypeObject *metaclass, PyObject *module, PyType_Spec *spec, PyObject *bases)

   Create and return a :ref:`heap type <heap-types>` from the *spec*
   (see :c:macro:`Py_TPFLAGS_HEAPTYPE`).

   A non-``NULL`` *metaclass* argument corresponds to the
   :c:macro:`Py_tp_metaclass` slot.

   A non-``NULL`` *bases* argument corresponds to the :c:data:`Py_tp_bases`
   slot, and takes precedence over :c:data:`Py_tp_bases` and
   :c:data:`Py_tp_bases` slots.

   A non-``NULL`` *module* argument corresponds to the
   :c:macro:`Py_tp_module` slot.

   This function calls :c:func:`PyType_Ready` on the new type.

   Note that this function does *not* fully match the behavior of
   calling :py:class:`type() <type>` or using the :keyword:`class` statement.
   See the note in :c:func:`PyType_FromSlots` documentation for details.

   .. versionadded:: 3.12

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.


.. c:function:: PyObject* PyType_FromModuleAndSpec(PyObject *module, PyType_Spec *spec, PyObject *bases)

   Equivalent to ``PyType_FromMetaclass(NULL, module, spec, bases)``.

   .. versionadded:: 3.9

   .. versionchanged:: 3.10

      The function now accepts a single class as the *bases* argument and
      ``NULL`` as the ``tp_doc`` slot.

   .. versionchanged:: 3.12

      The function now finds and uses a metaclass corresponding to the provided
      base classes.  Previously, only :class:`type` instances were returned.

      The :c:member:`~PyTypeObject.tp_new` of the metaclass is *ignored*.
      which may result in incomplete initialization.
      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is deprecated.

   .. versionchanged:: 3.14

      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is no longer allowed.

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.


.. c:function:: PyObject* PyType_FromSpecWithBases(PyType_Spec *spec, PyObject *bases)

   Equivalent to ``PyType_FromMetaclass(NULL, NULL, spec, bases)``.

   .. versionadded:: 3.3

   .. versionchanged:: 3.12

      The function now finds and uses a metaclass corresponding to the provided
      base classes.  Previously, only :class:`type` instances were returned.

      The :c:member:`~PyTypeObject.tp_new` of the metaclass is *ignored*.
      which may result in incomplete initialization.
      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is deprecated.

   .. versionchanged:: 3.14

      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is no longer allowed.

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.


.. c:function:: PyObject* PyType_FromSpec(PyType_Spec *spec)

   Equivalent to ``PyType_FromMetaclass(NULL, NULL, spec, NULL)``.

   .. versionchanged:: 3.12

      The function now finds and uses a metaclass corresponding to the
      base classes provided in *Py_tp_base[s]* slots.
      Previously, only :class:`type` instances were returned.

      The :c:member:`~PyTypeObject.tp_new` of the metaclass is *ignored*.
      which may result in incomplete initialization.
      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is deprecated.

   .. versionchanged:: 3.14

      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is no longer allowed.

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.

.. raw:: html

   <!-- Keep old URL fragments working (see gh-97908) -->
   <span id='c.PyType_Spec.PyType_Spec.name'></span>
   <span id='c.PyType_Spec.PyType_Spec.basicsize'></span>
   <span id='c.PyType_Spec.PyType_Spec.itemsize'></span>
   <span id='c.PyType_Spec.PyType_Spec.flags'></span>
   <span id='c.PyType_Spec.PyType_Spec.slots'></span>

.. c:type:: PyType_Spec

   Structure defining a type's behavior, used for soft-deprecated functions
   like :c:func:`PyType_FromMetaclass`.

   This structure contains several members that can instead be specified
   as :ref:`slots <pyslot_type_slot_ids>` for :c:func:`PyType_FromSlots`,
   and an array of slot entries with a simpler structure.

   .. c:member:: const char* name

      Corresponds to :c:macro:`Py_tp_name`.

   .. c:member:: int basicsize

      If positive, corresponds to :c:macro:`Py_tp_basicsize`.

      If negative, corresponds to :c:macro:`Py_tp_extra_basicsize` set to
      the absolute value.

      .. versionchanged:: 3.12

         Previously, this field could not be negative.

   .. c:member:: int itemsize

      Corresponds to :c:macro:`Py_tp_itemsize`.

   .. c:member:: unsigned int flags

      Corresponds to :c:macro:`Py_tp_flags`.

   .. c:member:: PyType_Slot *slots

      Array of :c:type:`PyType_Slot` (not :c:type:`PySlot`) structures.

      Terminated by the special slot value ``{0, NULL}``.
      Each slot ID should be specified at most once.

      .. c:namespace:: NULL

      .. raw:: html

         <!-- Keep old URL fragments working (see gh-97908) -->
         <span id='c.PyType_Slot.PyType_Slot.slot'></span>
         <span id='c.PyType_Slot.PyType_Slot.pfunc'></span>

      .. c:type:: PyType_Slot

         Structure defining optional functionality of a type, used for
         soft-deprecated functions like :c:func:`PyType_FromMetaclass`.

         Note that a :c:type:`!PyType_Slot` array may be included in a
         :c:type:`!PySlot` array using :c:macro:`Py_tp_slots`,
         and vice versa using :c:macro:`Py_slot_subslots`.

         Each :c:type:`!PyType_Slot` structure ``tpslot`` is interpreted
         as the following :c:type:`PySlot` structure::

            (PySlot){
               .sl_id=tpslot.slot,
               .sl_flags=PySlot_INTPTR | sub_static,
               .sl_ptr=tpslot.func
            }

         where ``sub_static`` is ``PySlot_STATIC`` if the slot requires
         the flag (such as for :c:macro:`Py_tp_methods`), or if this flag
         is present on the "parent" :c:macro:`!Py_tp_slots` slot (if any).

         .. c:member:: int slot

            Corresponds to :c:member:`PySlot.sl_id`.

         .. c:member:: void *pfunc

            Corresponds to :c:member:`PySlot.sl_ptr`.

----

.. c:function:: PyObject* PyType_FromMetaclass(PyTypeObject *metaclass, PyObject *module, PyType_Spec *spec, PyObject *bases)

   Create and return a :ref:`heap type <heap-types>` from the *spec*
   (see :c:macro:`Py_TPFLAGS_HEAPTYPE`).

   A non-``NULL`` *metaclass* argument corresponds to the
   :c:macro:`Py_tp_metaclass` slot.

   A non-``NULL`` *bases* argument corresponds to the :c:data:`Py_tp_bases`
   slot, and takes precedence over :c:data:`Py_tp_bases` and
   :c:data:`Py_tp_bases` slots.

   A non-``NULL`` *module* argument corresponds to the
   :c:macro:`Py_tp_module` slot.

   This function calls :c:func:`PyType_Ready` on the new type.

   Note that this function does *not* fully match the behavior of
   calling :py:class:`type() <type>` or using the :keyword:`class` statement.
   See the note in :c:func:`PyType_FromSlots` documentation for details.

   .. versionadded:: 3.12

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.



----

.. c:function:: PyObject* PyType_FromModuleAndSpec(PyObject *module, PyType_Spec *spec, PyObject *bases)

   Equivalent to ``PyType_FromMetaclass(NULL, module, spec, bases)``.

   .. versionadded:: 3.9

   .. versionchanged:: 3.10

      The function now accepts a single class as the *bases* argument and
      ``NULL`` as the ``tp_doc`` slot.

   .. versionchanged:: 3.12

      The function now finds and uses a metaclass corresponding to the provided
      base classes.  Previously, only :class:`type` instances were returned.

      The :c:member:`~PyTypeObject.tp_new` of the metaclass is *ignored*.
      which may result in incomplete initialization.
      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is deprecated.

   .. versionchanged:: 3.14

      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is no longer allowed.

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.



----

.. c:function:: PyObject* PyType_FromSpecWithBases(PyType_Spec *spec, PyObject *bases)

   Equivalent to ``PyType_FromMetaclass(NULL, NULL, spec, bases)``.

   .. versionadded:: 3.3

   .. versionchanged:: 3.12

      The function now finds and uses a metaclass corresponding to the provided
      base classes.  Previously, only :class:`type` instances were returned.

      The :c:member:`~PyTypeObject.tp_new` of the metaclass is *ignored*.
      which may result in incomplete initialization.
      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is deprecated.

   .. versionchanged:: 3.14

      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is no longer allowed.

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.



----

.. c:function:: PyObject* PyType_FromSpec(PyType_Spec *spec)

   Equivalent to ``PyType_FromMetaclass(NULL, NULL, spec, NULL)``.

   .. versionchanged:: 3.12

      The function now finds and uses a metaclass corresponding to the
      base classes provided in *Py_tp_base[s]* slots.
      Previously, only :class:`type` instances were returned.

      The :c:member:`~PyTypeObject.tp_new` of the metaclass is *ignored*.
      which may result in incomplete initialization.
      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is deprecated.

   .. versionchanged:: 3.14

      Creating classes whose metaclass overrides
      :c:member:`~PyTypeObject.tp_new` is no longer allowed.

   .. soft-deprecated:: 3.15

      Prefer :c:func:`PyType_FromSlots` in new code.
