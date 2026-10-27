.. function:: DeleteTree(key, sub_key=None)

   Deletes the specified key and all its subkeys and values recursively.

   *key* is an already open key, or one of the predefined
   :ref:`HKEY_* constants <hkey-constants>`.

   *sub_key* is a string that names the subkey to delete. If ``None``,
   deletes all subkeys and values of the specified key.

   This function deletes a key and all its descendants. If *sub_key* is
   ``None``, all subkeys and values of the specified key are deleted.

   .. audit-event:: winreg.DeleteTree key,sub_key winreg.DeleteTree

   .. versionadded:: 3.15



----

Registry Handle Objects
-----------------------

This object wraps a Windows HKEY object, automatically closing it when the
object is destroyed.  To guarantee cleanup, you can call either the
:meth:`~PyHKEY.Close` method on the object, or the :func:`CloseKey` function.

All registry functions in this module return one of these objects.

All registry functions in this module which accept a handle object also accept
an integer, however, use of the handle object is encouraged.

Handle objects provide semantics for :meth:`~object.__bool__` -- thus ::

   if handle:
       print("Yes")

will print ``Yes`` if the handle is currently valid (has not been closed or
detached).

The object also support equality comparison semantics, so handle objects will
compare equal if they both reference the same underlying Windows handle value.
Closed handle objects (those with a handle value of zero) always compare equal.

Handle objects can be converted to an integer (e.g., using the built-in
:func:`int` function), in which case the underlying Windows handle value is
returned.  You can also use the :meth:`~PyHKEY.Detach` method to return the
integer handle, and also disconnect the Windows handle from the handle object.


.. method:: PyHKEY.Close()

   Closes the underlying Windows handle.

   If the handle is already closed, no error is raised.


.. method:: PyHKEY.Detach()

   Detaches the Windows handle from the handle object.

   The result is an integer that holds the value of the handle before it is
   detached.  If the handle is already detached or closed, this will return
   zero.

   After calling this function, the handle is effectively invalidated, but the
   handle is not closed.  You would call this function when you need the
   underlying Win32 handle to exist beyond the lifetime of the handle object.

   .. audit-event:: winreg.PyHKEY.Detach key winreg.PyHKEY.Detach


.. method:: PyHKEY.__enter__()
            PyHKEY.__exit__(*exc_info)

   The HKEY object implements :meth:`~object.__enter__` and
   :meth:`~object.__exit__` and thus supports the context protocol for the
   :keyword:`with` statement::

      with OpenKey(HKEY_LOCAL_MACHINE, "foo") as key:
          ...  # work with key

   will automatically close *key* when control leaves the :keyword:`with` block.


.. versionchanged:: 3.15
   Handle objects are now compared by their underlying Windows handle value
   instead of object identity for equality comparisons.