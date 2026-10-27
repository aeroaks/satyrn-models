.. c:var:: PyHash_FuncDef PyHash_Func

   When Python is built with :c:macro:`Py_HASH_ALGORITHM` set to
   :c:macro:`Py_HASH_EXTERNAL`, the application embedding Python must define
   this variable to supply a hash implementation instead of using one of
   Python's built-in hash algorithms.

   .. versionadded:: 3.4

   .. deprecated-removed:: 3.15 3.19
      Use one of the built-in hash algorithms instead.

