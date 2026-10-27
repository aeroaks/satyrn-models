.. c:macro:: PyDescr_COMMON

   This is a macro including the common fields for a
   descriptor object.

   This was included in Python's C API by mistake; do not use it in extensions.
   For creating custom descriptor objects, create a class implementing the
   descriptor protocol (:c:member:`~PyTypeObject.tp_descr_get` and
   :c:member:`~PyTypeObject.tp_descr_set`).

   .. soft-deprecated:: 3.15

