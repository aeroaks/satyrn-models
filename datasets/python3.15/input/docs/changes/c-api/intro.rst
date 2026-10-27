.. c:macro:: Py_ALIGNED(num)

   On some GCC-like compilers, specify alignment to *num* bytes.
   This does nothing on other compilers.

   Use the standard ``alignas`` specifier rather than this macro.

   .. soft-deprecated:: 3.15


----

.. c:macro:: PY_FORMAT_SIZE_T

   The :c:func:`printf` formatting modifier for :c:type:`size_t`.
   Use ``"z"`` directly instead.

   .. soft-deprecated:: 3.15


----

.. c:macro:: Py_LL(number)
             Py_ULL(number)

   Use *number* as a ``long long`` or ``unsigned long long`` integer literal,
   respectively.

   Expands to *number* followed by ``LL`` or ``LLU``, respectively, but will
   expand to some compiler-specific suffixes on some older compilers.

   Consider using the C99 standard suffixes ``LL`` and ``LLU`` directly.

   .. soft-deprecated:: 3.15


----

.. c:macro:: PY_LONG_LONG
             PY_INT32_T
             PY_UINT32_T
             PY_INT64_T
             PY_UINT64_T

   Aliases for the types :c:type:`!long long`, :c:type:`!int32_t`,
   :c:type:`!uint32_t`. :c:type:`!int64_t` and :c:type:`!uint64_t`,
   respectively.
   Historically, these types needed compiler-specific extensions.

   .. soft-deprecated:: 3.15


----

.. c:macro:: PY_LLONG_MIN
             PY_LLONG_MAX
             PY_ULLONG_MAX
             PY_SIZE_MAX

   Aliases for the values :c:macro:`!LLONG_MIN`, :c:macro:`!LLONG_MAX`,
   :c:macro:`!ULLONG_MAX`, and :c:macro:`!SIZE_MAX`, respectively.
   Use these standard names instead.

   The required header, ``<limits.h>``,
   :ref:`is included <capi-system-includes>` in ``Python.h``.

   .. soft-deprecated:: 3.15


----

.. c:macro:: Py_UNICODE_SIZE

   Size of the :c:type:`!wchar_t` type.
   Use ``sizeof(wchar_t)`` or ``WCHAR_WIDTH/8`` instead.

   The required header for the latter, ``<limits.h>``,
   :ref:`is included <capi-system-includes>` in ``Python.h``.

   .. soft-deprecated:: 3.15


----

.. c:macro:: Py_UNICODE_WIDE

   Defined if ``wchar_t`` can hold a Unicode character (UCS-4).
   Use ``sizeof(wchar_t) >= 4`` instead

   .. soft-deprecated:: 3.15


----

.. c:macro:: Py_VA_COPY

   This is an alias to the C99-standard ``va_copy`` function.

   Historically, this would use a compiler-specific method to copy a ``va_list``.

   .. versionchanged:: 3.6
      This is now an alias to ``va_copy``.

   .. soft-deprecated:: 3.15

