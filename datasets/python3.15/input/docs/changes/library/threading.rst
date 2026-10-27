.. function:: get_native_id()

   Return the native integral Thread ID of the current thread assigned by the kernel.
   This is a non-negative integer.
   Its value may be used to uniquely identify this particular thread system-wide
   (until the thread terminates, after which the value may be recycled by the OS).

   .. availability:: Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD, Solaris.

   .. versionadded:: 3.8

   .. versionchanged:: 3.13
      Added support for GNU/kFreeBSD.

   .. versionchanged:: 3.15
      Added support for Solaris.



----

   .. method:: join(timeout=None)

      Wait until the thread terminates. This blocks the calling thread until
      the thread whose :meth:`~Thread.join` method is called terminates -- either
      normally or through an unhandled exception -- or until the optional
      timeout occurs.

      When the *timeout* argument is present and not ``None``, it should be a
      real number specifying a timeout for the operation in seconds
      (or fractions thereof). As :meth:`~Thread.join` always returns ``None``,
      you must call :meth:`~Thread.is_alive` after :meth:`~Thread.join` to
      decide whether a timeout happened -- if the thread is still alive, the
      :meth:`~Thread.join` call timed out.

      When the *timeout* argument is not present or ``None``, the operation will
      block until the thread terminates.

      A thread can be joined many times.

      :meth:`~Thread.join` raises a :exc:`RuntimeError` if an attempt is made
      to join the current thread as that would cause a deadlock. It is also
      an error to :meth:`~Thread.join` a thread before it has been started
      and attempts to do so raise the same exception.

      If an attempt is made to join a running daemonic thread in late stages
      of :term:`Python finalization <interpreter shutdown>` :meth:`!join`
      raises a :exc:`PythonFinalizationError`.

      .. versionchanged:: 3.14

         May raise :exc:`PythonFinalizationError`.

      .. versionchanged:: 3.15
         Accepts any real number as *timeout*, not only integer or float.


----

   .. method:: acquire(blocking=True, timeout=-1)

      Acquire a lock, blocking or non-blocking.

      When invoked with the *blocking* argument set to ``True`` (the default),
      block until the lock is unlocked, then set it to locked and return ``True``.

      When invoked with the *blocking* argument set to ``False``, do not block.
      If a call with *blocking* set to ``True`` would block, return ``False``
      immediately; otherwise, set the lock to locked and return ``True``.

      When invoked with the *timeout* argument set to a positive
      value, block for at most the number of seconds specified by *timeout*
      and as long as the lock cannot be acquired.  A *timeout* argument of ``-1``
      specifies an unbounded wait.  It is forbidden to specify a *timeout*
      when *blocking* is ``False``.

      The return value is ``True`` if the lock is acquired successfully,
      ``False`` if not (for example if the *timeout* expired).

      .. versionchanged:: 3.2
         The *timeout* parameter is new.

      .. versionchanged:: 3.2
         Lock acquisition can now be interrupted by signals on POSIX if the
         underlying threading implementation supports it.

      .. versionchanged:: 3.14
         Lock acquisition can now be interrupted by signals on Windows.

      .. versionchanged:: 3.15
         Accepts any real number as *timeout*, not only integer or float.



----

   .. method:: acquire(blocking=True, timeout=-1)

      Acquire a lock, blocking or non-blocking.

      .. seealso::

         :ref:`Using RLock as a context manager <with-locks>`
            Recommended over manual :meth:`!acquire` and :meth:`release` calls
            whenever practical.


      When invoked with the *blocking* argument set to ``True`` (the default):

         * If no thread owns the lock, acquire the lock and return immediately.

         * If another thread owns the lock, block until we are able to acquire
           lock, or *timeout*, if set to a positive value.

         * If the same thread owns the lock, acquire the lock again, and
           return immediately. This is the difference between :class:`Lock` and
           :class:`!RLock`; :class:`Lock` handles this case the same as the previous,
           blocking until the lock can be acquired.

      When invoked with the *blocking* argument set to ``False``:

         * If no thread owns the lock, acquire the lock and return immediately.

         * If another thread owns the lock, return immediately.

         * If the same thread owns the lock, acquire the lock again and return
           immediately.

      In all cases, if the thread was able to acquire the lock, return ``True``.
      If the thread was unable to acquire the lock (i.e. if not blocking or
      the timeout was reached) return ``False``.

      If called multiple times, failing to call :meth:`~RLock.release` as many times
      may lead to deadlock. Consider using :class:`!RLock` as a context manager rather than
      calling acquire/release directly.

      .. versionchanged:: 3.2
         The *timeout* parameter is new.

      .. versionchanged:: 3.15
         Accepts any real number as *timeout*, not only integer or float.



----

   .. method:: acquire(blocking=True, timeout=None)

      Acquire a semaphore.

      When invoked without arguments:

      * If the internal counter is larger than zero on entry, decrement it by
        one and return ``True`` immediately.
      * If the internal counter is zero on entry, block until awoken by a call to
        :meth:`~Semaphore.release`.  Once awoken (and the counter is greater
        than 0), decrement the counter by 1 and return ``True``.  Exactly one
        thread will be awoken by each call to :meth:`~Semaphore.release`.  The
        order in which threads are awoken should not be relied on.

      When invoked with *blocking* set to ``False``, do not block.  If a call
      without an argument would block, return ``False`` immediately; otherwise, do
      the same thing as when called without arguments, and return ``True``.

      When invoked with a *timeout* other than ``None``, it will block for at
      most *timeout* seconds.  If acquire does not complete successfully in
      that interval, return ``False``.  Return ``True`` otherwise.

      .. versionchanged:: 3.2
         The *timeout* parameter is new.

      .. versionchanged:: 3.15
         Accepts any real number as *timeout*, not only integer or float.


----

.. class:: serialize_iterator(iterable)

   Return an iterator wrapper that serializes concurrent calls to
   :meth:`~iterator.__next__` using a lock.

   If the wrapped iterator also defines :meth:`~generator.send`,
   :meth:`~generator.throw`, or :meth:`~generator.close`, those calls
   are serialized as well.

   This makes it possible to share a single iterator, including a generator
   iterator, between multiple threads. A lock ensures that calls are handled
   one at a time. No values are duplicated or skipped by the wrapper itself.
   Each item from the underlying iterator is given to exactly one caller.

   This wrapper does not copy or buffer values. Threads that call
   :func:`next` while another thread is already advancing the iterator will
   block until the active call completes.

   Example:

   .. code-block:: python

      import threading

      def squares(n):
          for x in range(n):
              yield x * x

      def consume(name, iterable):
          for item in iterable:
              print(name, item)

      source = threading.serialize_iterator(squares(5))

      t1 = threading.Thread(target=consume, args=("left", source))
      t2 = threading.Thread(target=consume, args=("right", source))
      t1.start()
      t2.start()
      t1.join()
      t2.join()

   In this example, each number is printed exactly once, but the work is shared
   between the two threads.

   .. versionadded:: 3.15



----

.. function:: synchronized_iterator(func)

   Wrap an iterator-producing callable so that each iterator it returns is
   automatically passed through :class:`serialize_iterator`.

   This is especially useful as a :term:`decorator` for generator functions,
   allowing their generator-iterators to be consumed from multiple threads.

   Example:

   .. code-block:: python

      import threading

      @threading.synchronized_iterator
      def squares(n):
          for x in range(n):
              yield x * x

      def consume(name, iterable):
          for item in iterable:
              print(name, item)

      source = squares(5)

      t1 = threading.Thread(target=consume, args=("left", source))
      t2 = threading.Thread(target=consume, args=("right", source))
      t1.start()
      t2.start()
      t1.join()
      t2.join()

   The returned wrapper preserves the metadata of *func*, such as its name and
   wrapped function reference.

   .. versionadded:: 3.15



----

.. function:: concurrent_tee(iterable, n=2)

   Return *n* independent iterators from a single input *iterable*, with
   guaranteed behavior when the derived iterators are consumed concurrently.

   This function is similar to :func:`itertools.tee`, but is intended for cases
   where the source iterator may feed consumers running in different threads.
   Each returned iterator yields every value from the underlying iterable, in
   the same order.

   Internally, values are buffered until every derived iterator has consumed
   them.

   The returned iterators share the same underlying synchronization lock. Each
   individual derived iterator is intended to be consumed by one thread at a
   time. If a single derived iterator must itself be shared by multiple
   threads, wrap it with :class:`serialize_iterator`.

   If *n* is ``0``, return an empty tuple. If *n* is negative, raise
   :exc:`ValueError`.

   Example:

   .. code-block:: python

      import threading

      def squares(n):
          for x in range(n):
              yield x * x

      def consume(name, iterable):
          for item in iterable:
              print(name, item)

      source = squares(5)
      left, right = threading.concurrent_tee(source)

      t1 = threading.Thread(target=consume, args=("left", left))
      t2 = threading.Thread(target=consume, args=("right", right))
      t1.start()
      t2.start()
      t1.join()
      t2.join()

   In this example, both consumer threads see the full sequence of squares
   from a single generator expression.

   .. versionadded:: 3.15