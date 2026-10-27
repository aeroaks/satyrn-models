.. c:type:: Py_UNICODE

   This is a typedef of :c:type:`wchar_t`, which is a 16-bit type or 32-bit type
   depending on the platform.
   Please use :c:type:`wchar_t` directly instead.

   .. versionchanged:: 3.3
      In previous versions, this was a 16-bit type or a 32-bit type depending on
      whether you selected a "narrow" or "wide" Unicode version of Python at
      build time.

   .. deprecated-removed:: 3.13 3.15

