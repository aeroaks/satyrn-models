Contexts and start methods
^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the platform, :mod:`!multiprocessing` supports three ways
to start a process.  These *start methods* are

  .. _multiprocessing-start-method-spawn:

  *spawn*
    The parent process starts a fresh Python interpreter process.  The
    child process will only inherit those resources necessary to run
    the process object's :meth:`~Process.run` method.  In particular,
    unnecessary file descriptors and handles from the parent process
    will not be inherited.  Starting a process using this method is
    rather slow compared to using *fork* or *forkserver*.

    Available on POSIX and Windows platforms.  The default on Windows and macOS.

  .. _multiprocessing-start-method-fork:

  *fork*
    The parent process uses :func:`os.fork` to fork the Python
    interpreter.  The child process, when it begins, is effectively
    identical to the parent process.  All resources of the parent are
    inherited by the child process.  Note that safely forking a
    multithreaded process is problematic.

    Available on POSIX systems.

    .. versionchanged:: 3.14
       This is no longer the default start method on any platform.
       Code that requires *fork* must explicitly specify that via
       :func:`get_context` or :func:`set_start_method`.

    .. versionchanged:: 3.12
       If Python is able to detect that your process has multiple threads, the
       :func:`os.fork` function that this start method calls internally will
       raise a :exc:`DeprecationWarning`. Use a different start method.
       See the :func:`os.fork` documentation for further explanation.

  .. _multiprocessing-start-method-forkserver:

  *forkserver*
    When the program starts and selects the *forkserver* start method,
    a server process is spawned.  From then on, whenever a new process
    is needed, the parent process connects to the server and requests
    that it fork a new process.  The fork server process is single threaded
    unless system libraries or preloaded imports spawn threads as a
    side-effect so it is generally safe for it to use :func:`os.fork`.
    No unnecessary resources are inherited.

    Available on POSIX platforms which support passing file descriptors over
    Unix pipes such as Linux.  The default on those, unless there is no
    writable temporary directory (see :func:`tempfile.gettempdir`), which
    the fork server requires; *spawn* is the default in that case.

    .. versionchanged:: 3.14
       This became the default start method on POSIX platforms.

    .. versionchanged:: 3.15.1
       *spawn* is now the default start method when there is no writable
       temporary directory, for example on a read-only file system.
       Previously *forkserver* remained the default there and starting a
       process failed with an :exc:`OSError`.  The default is determined
       when it is first needed rather than when :mod:`!multiprocessing`
       is imported.  See :gh:`155717`.

.. versionchanged:: 3.4
   *spawn* added on all POSIX platforms, and *forkserver* added for
   some POSIX platforms.
   Child processes no longer inherit all of the parents inheritable
   handles on Windows.

.. versionchanged:: 3.8

   On macOS, the *spawn* start method is now the default.  The *fork* start
   method should be considered unsafe as it can lead to crashes of the
   subprocess as macOS system libraries may start threads. See :issue:`33725`.

.. versionchanged:: 3.14

   On POSIX platforms the default start method was changed from *fork* to
   *forkserver* to retain the performance but avoid common multithreaded
   process incompatibilities. See :gh:`84559`.


On POSIX using the *spawn* or *forkserver* start methods will also
start a *resource tracker* process which tracks the unlinked named
system resources (such as named semaphores or
:class:`~multiprocessing.shared_memory.SharedMemory` objects) created
by processes of the program.  When all processes
have exited the resource tracker unlinks any remaining tracked object.
Usually there should be none, but if a process was killed by a signal
there may be some "leaked" resources.  (Neither leaked semaphores nor shared
memory segments will be automatically unlinked until the next reboot. This is
problematic for both objects because the system allows only a limited number of
named semaphores, and shared memory segments occupy some space in the main
memory.)

To select a start method you use the :func:`set_start_method` in
the ``if __name__ == '__main__'`` clause of the main module.  For
example::

       import multiprocessing as mp

       def foo(q):
           q.put('hello')

       if __name__ == '__main__':
           mp.set_start_method('spawn')
           q = mp.Queue()
           p = mp.Process(target=foo, args=(q,))
           p.start()
           print(q.get())
           p.join()

:func:`set_start_method` should not be used more than once in the
program.

Alternatively, you can use :func:`get_context` to obtain a context
object.  Context objects have the same API as the multiprocessing
module, and allow one to use multiple start methods in the same
program. ::

       import multiprocessing as mp

       def foo(q):
           q.put('hello')

       if __name__ == '__main__':
           ctx = mp.get_context('spawn')
           q = ctx.Queue()
           p = ctx.Process(target=foo, args=(q,))
           p.start()
           print(q.get())
           p.join()

Note that objects related to one context may not be compatible with
processes for a different context.  In particular, locks created using
the *fork* context cannot be passed to processes started using the
*spawn* or *forkserver* start methods.

Libraries using :mod:`!multiprocessing` or
:class:`~concurrent.futures.ProcessPoolExecutor` should be designed to allow
their users to provide their own multiprocessing context.  Using a specific
context of your own within a library can lead to incompatibilities with the
rest of the library user's application.  Always document if your library
requires a specific start method.

.. warning::

   The ``'spawn'`` and ``'forkserver'`` start methods generally cannot
   be used with "frozen" executables (i.e., binaries produced by
   packages like **PyInstaller** and **cx_Freeze**) on POSIX systems.
   The ``'fork'`` start method may work if code does not use threads.



----

.. function:: set_forkserver_preload(module_names, *, on_error='ignore')

   Set a list of module names for the forkserver main process to attempt to
   import so that their already imported state is inherited by forked
   processes. This can be used as a performance enhancement to avoid repeated
   work in every process.

   For this to work, it must be called before the forkserver process has been
   launched (before creating a :class:`Pool` or starting a :class:`Process`).

   The *on_error* parameter controls how :exc:`ImportError` exceptions during
   module preloading are handled: ``"ignore"`` (default) silently ignores
   failures, ``"warn"`` causes the forkserver subprocess to emit an
   :exc:`ImportWarning` to stderr, and ``"fail"`` causes the forkserver
   subprocess to exit with the exception traceback on stderr, making
   subsequent process creation fail with :exc:`EOFError` or
   :exc:`ConnectionError`.

   Only meaningful when using the ``'forkserver'`` start method.
   See :ref:`multiprocessing-start-methods`.

   .. versionadded:: 3.4

   .. versionchanged:: 3.15
      Added the *on_error* parameter.
