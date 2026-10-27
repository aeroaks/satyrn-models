.. c:macro:: PyDateTime_IMPORT()

   Import the datetime C API.

   On success, populate the :c:var:`PyDateTimeAPI` pointer.
   On failure, set :c:var:`PyDateTimeAPI` to ``NULL`` and set an exception.
   The caller must check if an error occurred via :c:func:`PyErr_Occurred`:

   .. code-block::

      PyDateTime_IMPORT;
      if (PyErr_Occurred()) { /* cleanup */ }

   .. warning::

      This is not compatible with subinterpreters.

   .. versionchanged:: 3.15

      This macro is now thread safe.


----

.. c:var:: PyDateTime_CAPI *PyDateTimeAPI

   Dynamically allocated object containing the datetime C API.

   This variable is only available once :c:macro:`PyDateTime_IMPORT` succeeds.

   .. versionchanged:: 3.15

      This variable should not be accessed directly as direct access is not thread-safe.
      Use :c:func:`PyDateTime_IMPORT` instead.
