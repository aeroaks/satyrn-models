Soft-deprecated aliases
^^^^^^^^^^^^^^^^^^^^^^^

.. soft-deprecated:: 3.15

These are aliases to existing functions and macros.
They exist solely for backwards compatibility.


.. list-table::
   :widths: auto
   :header-rows: 1

   * * Soft-deprecated alias
     * Function
   * * .. c:macro:: PyObject_NEW(type, typeobj)
     * :c:macro:`PyObject_New`
   * * .. c:macro:: PyObject_NEW_VAR(type, typeobj, n)
     * :c:macro:`PyObject_NewVar`
   * * .. c:macro:: PyObject_INIT(op, typeobj)
     * :c:func:`PyObject_Init`
   * * .. c:macro:: PyObject_INIT_VAR(op, typeobj, n)
     * :c:func:`PyObject_InitVar`
   * * .. c:macro:: PyObject_MALLOC(n)
     * :c:func:`PyObject_Malloc`
   * * .. c:macro:: PyObject_REALLOC(p, n)
     * :c:func:`PyObject_Realloc`
   * * .. c:macro:: PyObject_FREE(p)
     * :c:func:`PyObject_Free`
   * * .. c:macro:: PyObject_DEL(p)
     * :c:func:`PyObject_Free`
   * * .. c:macro:: PyObject_Del(p)
     * :c:func:`PyObject_Free`