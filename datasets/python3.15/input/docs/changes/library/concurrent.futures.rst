.. class:: ProcessPoolExecutor(max_workers=None, mp_context=None, \
                               initializer=None, initargs=(), \
                               max_tasks_per_child=None)

   An :class:`Executor` subclass that executes calls asynchronously using a pool
   of at most *max_workers* processes.  If *max_workers* is ``None`` or not
   given, it will default to :func:`os.process_cpu_count`.
   If *max_workers* is less than or equal to ``0``, then a :exc:`ValueError`
   will be raised.
   On Windows, *max_workers* must be less than or equal to ``61``. If it is not
   then :exc:`ValueError` will be raised. If *max_workers* is ``None``, then
   the default chosen will be at most ``61``, even if more processors are
   available.
   *mp_context* can be a :mod:`multiprocessing` context or ``None``. It will be
   used to launch the workers. If *mp_context* is ``None`` or not given, the
   default :mod:`multiprocessing` context is used.
   See :ref:`multiprocessing-start-methods`.

   *initializer* is an optional callable that is called at the start of
   each worker process; *initargs* is a tuple of arguments passed to the
   initializer.  Should *initializer* raise an exception, all currently
   pending jobs will raise a :exc:`~concurrent.futures.process.BrokenProcessPool`,
   as well as any attempt to submit more jobs to the pool.

   *max_tasks_per_child* is an optional argument that specifies the maximum
   number of tasks a single process can execute before it will exit and be
   replaced with a fresh worker process. By default *max_tasks_per_child* is
   ``None`` which means worker processes will live as long as the pool. When
   a max is specified, the "spawn" multiprocessing start method will be used by
   default in absence of a *mp_context* parameter. This feature is incompatible
   with the "fork" start method.

   .. versionchanged:: 3.3
      When one of the worker processes terminates abruptly, a
      :exc:`~concurrent.futures.process.BrokenProcessPool` error is now raised.
      Previously, behaviour
      was undefined but operations on the executor or its futures would often
      freeze or deadlock.

   .. versionchanged:: 3.7
      The *mp_context* argument was added to allow users to control the
      start_method for worker processes created by the pool.

      Added the *initializer* and *initargs* arguments.

   .. versionchanged:: 3.11
      The *max_tasks_per_child* argument was added to allow users to
      control the lifetime of workers in the pool.

   .. versionchanged:: 3.12
      On POSIX systems, if your application has multiple threads and the
      :mod:`multiprocessing` context uses the ``"fork"`` start method:
      The :func:`os.fork` function called internally to spawn workers may raise a
      :exc:`DeprecationWarning`. Pass a *mp_context* configured to use a
      different start method. See the :func:`os.fork` documentation for
      further explanation.

   .. versionchanged:: 3.13
      *max_workers* uses :func:`os.process_cpu_count` by default, instead of
      :func:`os.cpu_count`.

   .. versionchanged:: 3.14
      The default process start method (see
      :ref:`multiprocessing-start-methods`) changed away from *fork*. If you
      require the *fork* start method for :class:`ProcessPoolExecutor` you must
      explicitly pass ``mp_context=multiprocessing.get_context("fork")``.

   .. versionchanged:: 3.15
      Fixed a deadlock (:gh:`115634`) where the executor could hang after
      a worker process exited upon reaching its *max_tasks_per_child*
      limit while tasks remained queued.

   .. method:: terminate_workers()

      Attempt to terminate all living worker processes immediately by calling
      :meth:`Process.terminate <multiprocessing.Process.terminate>` on each of them.
      Internally, it will also call :meth:`Executor.shutdown` to ensure that all
      other resources associated with the executor are freed.

      After calling this method the caller should no longer submit tasks to the
      executor.

      .. versionadded:: 3.14

   .. method:: kill_workers()

      Attempt to kill all living worker processes immediately by calling
      :meth:`Process.kill <multiprocessing.Process.kill>` on each of them.
      Internally, it will also call :meth:`Executor.shutdown` to ensure that all
      other resources associated with the executor are freed.

      After calling this method the caller should no longer submit tasks to the
      executor.

      .. versionadded:: 3.14

.. _processpoolexecutor-example:

ProcessPoolExecutor Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

   import concurrent.futures
   import math

   PRIMES = [