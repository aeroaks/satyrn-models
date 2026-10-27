.. class:: ContextDecorator()

   A base class that enables a context manager to also be used as a decorator.

   Context managers inheriting from ``ContextDecorator`` have to implement
   :meth:`~object.__enter__` and :meth:`~object.__exit__` as normal.
   ``__exit__`` retains its optional
   exception handling even when used as a decorator.

   ``ContextDecorator`` is used by :deco:`contextmanager`, so you get this
   functionality automatically.

   Example of ``ContextDecorator``::

      from contextlib import ContextDecorator

      class mycontext(ContextDecorator):
          def __enter__(self):
              print('Starting')
              return self

          def __exit__(self, *exc):
              print('Finishing')
              return False

   The class can then be used like this::

      >>> @mycontext()
      ... def function():
      ...     print('The bit in the middle')
      ...
      >>> function()
      Starting
      The bit in the middle
      Finishing

      >>> with mycontext():
      ...     print('The bit in the middle')
      ...
      Starting
      The bit in the middle
      Finishing

   This change is just syntactic sugar for any construct of the following form::

      def f():
          with cm():
              # Do stuff

   ``ContextDecorator`` lets you instead write::

      @cm()
      def f():
          # Do stuff

   It makes it clear that the ``cm`` applies to the whole function, rather than
   just a piece of it (and saving an indentation level is nice, too).

   Existing context managers that already have a base class can be extended by
   using ``ContextDecorator`` as a mixin class::

      from contextlib import ContextDecorator

      class mycontext(ContextBaseClass, ContextDecorator):
          def __enter__(self):
              return self

          def __exit__(self, *exc):
              return False

   .. note::
      As the decorated function must be able to be called multiple times, the
      underlying context manager must support use in multiple :keyword:`with`
      statements. If this is not the case, then the original construct with the
      explicit :keyword:`!with` statement inside the function should be used.

   When the decorated callable is a generator function, coroutine function, or
   asynchronous generator function, the returned wrapper is of the same kind
   and keeps the context manager open for the lifetime of the iteration or
   await rather than only for the call that creates the generator or coroutine
   object.  Wrapped generators and asynchronous generators are explicitly
   closed when iteration ends, as if by :func:`closing` or :func:`aclosing`.

   .. note::
      For asynchronous generators the wrapper re-yields each value with
      ``async for``; values sent with :meth:`~agen.asend` and exceptions
      thrown with :meth:`~agen.athrow` are not forwarded to the wrapped
      generator.

   .. versionadded:: 3.2

   .. versionchanged:: 3.15
      Decorating a generator function, coroutine function, or asynchronous
      generator function now keeps the context manager open across iteration
      or await.  Previously the context manager exited as soon as the
      generator or coroutine object was created.



----

.. class:: AsyncContextDecorator

   Similar to :class:`ContextDecorator`, but the context manager is entered
   and exited with :keyword:`async with`.  Decorate coroutine functions and
   asynchronous generator functions with this class; the returned wrapper is
   of the same kind.

   .. note::
      Synchronous functions and generators are accepted, but the wrapper is
      always asynchronous, so the decorated callable must then be awaited or
      iterated with ``async for``.  If that change of calling convention is
      not intended, use :class:`ContextDecorator` instead.

   Example of ``AsyncContextDecorator``::

      from asyncio import run
      from contextlib import AsyncContextDecorator

      class mycontext(AsyncContextDecorator):
          async def __aenter__(self):
              print('Starting')
              return self

          async def __aexit__(self, *exc):
              print('Finishing')
              return False

   The class can then be used like this::

      >>> @mycontext()
      ... async def function():
      ...     print('The bit in the middle')
      ...
      >>> run(function())
      Starting
      The bit in the middle
      Finishing

      >>> async def function():
      ...    async with mycontext():
      ...         print('The bit in the middle')
      ...
      >>> run(function())
      Starting
      The bit in the middle
      Finishing

   .. versionadded:: 3.10

   .. versionchanged:: 3.15
      Decorating an asynchronous generator function now keeps the context
      manager open across iteration.  Previously the context manager exited
      as soon as the generator object was created.  Synchronous functions
      and synchronous generator functions are also now accepted, with an
      asynchronous wrapper returned.



----

   .. method:: enter_context(cm)

      Enters a new context manager and adds its :meth:`~object.__exit__` method to
      the callback stack. The return value is the result of the context
      manager's own :meth:`~object.__enter__` method.

      These context managers may suppress exceptions just as they normally
      would if used directly as part of a :keyword:`with` statement.

      .. versionchanged:: 3.11
         Raises :exc:`TypeError` instead of :exc:`AttributeError` if *cm*
         is not a context manager.

      .. versionchanged:: 3.15
         Added support for arbitrary descriptors :meth:`!__enter__` and
         :meth:`!__exit__`.


----

   .. method:: push(exit)

      Adds a context manager's :meth:`~object.__exit__` method to the callback stack.

      As ``__enter__`` is *not* invoked, this method can be used to cover
      part of an :meth:`~object.__enter__` implementation with a context manager's own
      :meth:`~object.__exit__` method.

      If passed an object that is not a context manager, this method assumes
      it is a callback with the same signature as a context manager's
      :meth:`~object.__exit__` method and adds it directly to the callback stack.

      By returning true values, these callbacks can suppress exceptions the
      same way context manager :meth:`~object.__exit__` methods can.

      The passed in object is returned from the function, allowing this
      method to be used as a function decorator.

      .. versionchanged:: 3.15
         Added support for arbitrary descriptors :meth:`!__exit__`.


----

   .. method:: enter_async_context(cm)
      :async:

      Similar to :meth:`ExitStack.enter_context` but expects an asynchronous context
      manager.

      .. versionchanged:: 3.11
         Raises :exc:`TypeError` instead of :exc:`AttributeError` if *cm*
         is not an asynchronous context manager.

      .. versionchanged:: 3.15
         Added support for arbitrary descriptors :meth:`!__aenter__` and :meth:`!__aexit__`.


----

   .. method:: push_async_exit(exit)

      Similar to :meth:`ExitStack.push` but expects either an asynchronous context manager
      or a coroutine function.

      .. versionchanged:: 3.15
         Added support for arbitrary descriptors :meth:`!__aexit__`.
