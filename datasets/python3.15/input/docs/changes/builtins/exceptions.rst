.. exception:: ImportCycleError

   A subclass of :exc:`ImportError` which is raised when a lazy import fails
   because it (directly or indirectly) tries to import itself.

   .. versionadded:: 3.15


----

.. exception:: PythonFinalizationError

   This exception is derived from :exc:`RuntimeError`.  It is raised when
   an operation is blocked during interpreter shutdown also known as
   :term:`Python finalization <interpreter shutdown>`.

   Examples of operations which can be blocked with a
   :exc:`PythonFinalizationError` during the Python finalization:

   * Creating a new Python thread.
   * :meth:`Joining <threading.Thread.join>` a running daemon thread.
   * :func:`os.fork`,
   * acquiring a lock such as :class:`threading.Lock`, when it is known that
     the operation would otherwise deadlock.

   See also the :func:`sys.is_finalizing` function.

   .. versionadded:: 3.13
      Previously, a plain :exc:`RuntimeError` was raised.

   .. versionchanged:: 3.14

      :meth:`threading.Thread.join` can now raise this exception.

   .. versionchanged:: 3.15

      This exception may be raised when acquiring :meth:`threading.Lock`
      or :meth:`threading.RLock`.
