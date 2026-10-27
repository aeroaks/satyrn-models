.. function:: epoll(sizehint=-1, flags=0)

   Return an edge polling object,
   which can be used as Edge or Level Triggered interface for I/O
   events.

   *sizehint* informs epoll about the expected number of events to be
   registered.  It must be positive, or ``-1`` to use the default. It is only
   used on older systems where :manpage:`epoll_create1(2)` is not available;
   otherwise it has no effect (though its value is still checked).

   *flags* is deprecated and completely ignored.  However, when supplied, its
   value must be ``0`` or ``select.EPOLL_CLOEXEC``, otherwise ``OSError`` is
   raised.

   See the :ref:`epoll-objects` section below for the methods supported by
   epolling objects.

   ``epoll`` objects support the context management protocol: when used in a
   :keyword:`with` statement, the new file descriptor is automatically closed
   at the end of the block.

   The new file descriptor is :ref:`non-inheritable <fd_inheritance>`.

   .. versionchanged:: 3.3
      Added the *flags* parameter.

   .. versionchanged:: 3.4
      Support for the :keyword:`with` statement was added.
      The new file descriptor is now non-inheritable.

   .. deprecated:: 3.4
      The *flags* parameter.  ``select.EPOLL_CLOEXEC`` is used by default now.
      Use :func:`os.set_inheritable` to make the file descriptor inheritable.

   .. versionchanged:: 3.15

      When CPython is built, this function may be disabled using
      :option:`--disable-epoll`.

   .. availability:: Linux >= 2.5.44.



----

.. function:: select(rlist, wlist, xlist, timeout=None)

   This is a straightforward interface to the Unix :c:func:`!select` system call.
   The first three arguments are iterables of 'waitable objects': either
   integers representing file descriptors or objects with a parameterless method
   named :meth:`~io.IOBase.fileno` returning such an integer:

   * *rlist*: wait until ready for reading
   * *wlist*: wait until ready for writing
   * *xlist*: wait for an "exceptional condition" (see the manual page for what
     your system considers such a condition)

   Empty iterables are allowed, but acceptance of three empty iterables is
   platform-dependent. (It is known to work on Unix but not on Windows.)  The
   optional *timeout* argument specifies a time-out in seconds; it may be
   a non-integer to specify fractions of seconds.
   When the *timeout* argument is omitted or ``None``, the function blocks until
   at least one file descriptor is ready.  A time-out value of zero specifies a
   poll and never blocks.

   The return value is a triple of lists of objects that are ready: subsets of the
   first three arguments.  When the time-out is reached without a file descriptor
   becoming ready, three empty lists are returned.

   .. index::
      single: socket() (in module socket)
      single: popen() (in module os)

   Among the acceptable object types in the iterables are Python :term:`file
   objects <file object>` (e.g. ``sys.stdin``, or objects returned by
   :func:`open` or :func:`os.popen`), socket objects returned by
   :func:`socket.socket`.  You may also define a :dfn:`wrapper` class yourself,
   as long as it has an appropriate :meth:`~io.IOBase.fileno` method (that
   really returns a file descriptor, not just a random integer).

   .. note::

      .. index:: single: WinSock

      File objects on Windows are not acceptable, but sockets are.  On Windows,
      the underlying :c:func:`!select` function is provided by the WinSock
      library, and does not handle file descriptors that don't originate from
      WinSock.

   .. versionchanged:: 3.5
      The function is now retried with a recomputed timeout when interrupted by
      a signal, except if the signal handler raises an exception (see
      :pep:`475` for the rationale), instead of raising
      :exc:`InterruptedError`.

   .. versionchanged:: 3.15
      Accepts any real number as *timeout*, not only integer or float.



----

.. method:: devpoll.poll([timeout])

   Polls the set of registered file descriptors, and returns a possibly empty list
   containing ``(fd, event)`` 2-tuples for the descriptors that have events or
   errors to report. *fd* is the file descriptor, and *event* is a bitmask with
   bits set for the reported events for that descriptor --- :const:`POLLIN` for
   waiting input, :const:`POLLOUT` to indicate that the descriptor can be written
   to, and so forth. An empty list indicates that the call timed out and no file
   descriptors had any events to report. If *timeout* is given, it specifies the
   length of time in milliseconds which the system will wait for events before
   returning. If *timeout* is omitted, -1, or :const:`None`, the call will
   block until there is an event for this poll object.

   .. versionchanged:: 3.5
      The function is now retried with a recomputed timeout when interrupted by
      a signal, except if the signal handler raises an exception (see
      :pep:`475` for the rationale), instead of raising
      :exc:`InterruptedError`.

   .. versionchanged:: 3.15
      Accepts any real number as *timeout*, not only integer or float.


.. _epoll-objects:

Edge and level trigger polling (epoll) objects
----------------------------------------------

   https://linux.die.net/man/4/epoll

   The *eventmask* is a bit mask using the following constants:

   +-------------------------+------------------------------------------------+

----

.. method:: epoll.poll(timeout=None, maxevents=-1)

   Wait for events.
   If *timeout* is given, it specifies the length of time in seconds
   (may be non-integer) which the system will wait for events before returning.

   .. versionchanged:: 3.5
      The function is now retried with a recomputed timeout when interrupted by
      a signal, except if the signal handler raises an exception (see
      :pep:`475` for the rationale), instead of raising
      :exc:`InterruptedError`.

   .. versionchanged:: 3.15
      Accepts any real number as *timeout*, not only integer or float.


.. _poll-objects:

Polling objects
---------------

The :c:func:`!poll` system call, supported on most Unix systems, provides better
scalability for network servers that service many, many clients at the same
time. :c:func:`!poll` scales better because the system call only requires listing
the file descriptors of interest, while :c:func:`!select` builds a bitmap, turns
on bits for the fds of interest, and then afterward the whole bitmap has to be

----

.. method:: poll.poll([timeout])

   Polls the set of registered file descriptors, and returns a possibly empty list
   containing ``(fd, event)`` 2-tuples for the descriptors that have events or
   errors to report. *fd* is the file descriptor, and *event* is a bitmask with
   bits set for the reported events for that descriptor --- :const:`POLLIN` for
   waiting input, :const:`POLLOUT` to indicate that the descriptor can be written
   to, and so forth. An empty list indicates that the call timed out and no file
   descriptors had any events to report. If *timeout* is given, it specifies the
   length of time in milliseconds which the system will wait for events before
   returning. If *timeout* is omitted, negative, or :const:`None`, the call will
   block until there is an event for this poll object.

   .. versionchanged:: 3.5
      The function is now retried with a recomputed timeout when interrupted by
      a signal, except if the signal handler raises an exception (see
      :pep:`475` for the rationale), instead of raising
      :exc:`InterruptedError`.

   .. versionchanged:: 3.15
      Accepts any real number as *timeout*, not only integer or float.
      If ``ppoll()`` function is available, *timeout* has a resolution
      of ``1`` ns (``1e-6`` ms) instead of ``1`` ms.


.. _kqueue-objects:

Kqueue objects
--------------

.. method:: kqueue.close()

   Close the control file descriptor of the kqueue object.



----

.. method:: kqueue.control(changelist, max_events[, timeout]) -> eventlist

   Low level interface to kevent

   - changelist must be an iterable of kevent objects or ``None``
   - max_events must be 0 or a positive integer
   - timeout in seconds (non-integers are possible); the default is ``None``,
     to wait forever

   .. versionchanged:: 3.5
      The function is now retried with a recomputed timeout when interrupted by
      a signal, except if the signal handler raises an exception (see
      :pep:`475` for the rationale), instead of raising
      :exc:`InterruptedError`.

   .. versionchanged:: 3.15
      Accepts any real number as *timeout*, not only integer or float.


.. _kevent-objects:

Kevent objects
--------------

https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2

.. attribute:: kevent.ident

   Value used to identify the event. The interpretation depends on the filter