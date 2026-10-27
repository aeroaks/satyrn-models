.. function:: clock_settime(clk_id, time, /)

   Set the time of the specified clock *clk_id*.  Currently,
   :data:`CLOCK_REALTIME` is the only accepted value for *clk_id*.

   Use :func:`clock_settime_ns` to avoid the precision loss caused by the
   :class:`float` type.

   .. availability:: Unix, not Android, not iOS.

   .. versionadded:: 3.3

   .. versionchanged:: 3.15
      Accepts any real number as *time*, not only integer or float.



----

.. function:: ctime(seconds=None, /)

   Convert a time expressed in seconds since the epoch_ to a string of a form:
   ``'Sun Jun 20 23:21:05 1993'`` representing local time. The day field
   is two characters long and is space padded if the day is a single digit,
   for example: ``'Wed Jun  9 04:26:40 1993'``.

   If *seconds* is not provided or :const:`None`, the current time as
   returned by :func:`.time` is used. ``ctime(seconds)`` is equivalent to
   ``asctime(localtime(seconds))``. Locale information is not used by
   :func:`ctime`.

   .. versionchanged:: 3.15
      Accepts any real number, not only integer or float.



----

.. function:: gmtime(seconds=None, /)

   Convert a time expressed in seconds since the epoch_ to a :class:`struct_time` in
   UTC in which the dst flag is always zero.  If *seconds* is not provided or
   :const:`None`, the current time as returned by :func:`.time` is used.  Fractions
   of a second are ignored.  See above for a description of the
   :class:`struct_time` object. See :func:`calendar.timegm` for the inverse of this
   function.

   .. versionchanged:: 3.15
      Accepts any real number, not only integer or float.



----

.. function:: localtime(seconds=None, /)

   Like :func:`gmtime` but converts to local time.
   If *seconds* is not provided or :const:`None`,
   the current time as returned by :func:`.time` is used.
   The dst flag is set to ``1`` when DST applies to the given time.

   :func:`localtime` may raise :exc:`OverflowError`, if the timestamp is
   outside the range of values supported by the platform C :c:func:`localtime`
   or :c:func:`gmtime` functions, and :exc:`OSError` on :c:func:`localtime` or
   :c:func:`gmtime` failure. It's common for this to be restricted to years
   between 1970 and 2038.

   .. versionchanged:: 3.15
      Accepts any real number, not only integer or float.



----

.. function:: sleep(seconds, /)

   Suspend execution of the calling thread for the given number of seconds.
   The argument may be a non-integer to indicate a more precise sleep time.

   If the sleep is interrupted by a signal and no exception is raised by the
   signal handler, the sleep is restarted with a recomputed timeout.

   The suspension time may be longer than requested by an arbitrary amount,
   because of the scheduling of other activity in the system.

   .. rubric:: Windows implementation

   On Windows, if *seconds* is zero,
   the thread relinquishes the remainder of its time slice
   to any other thread that is ready to run.
   If there are no other threads ready to run,
   the function returns immediately, and the thread continues execution.
   On Windows 10 and newer the implementation uses
   a `high-resolution timer
   <https://learn.microsoft.com/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw>`_
   which provides resolution of 100 nanoseconds.
   If *seconds* is zero, ``Sleep(0)`` is used.

   .. rubric:: Unix implementation

   * Use ``clock_nanosleep()`` if available (resolution: 1 nanosecond);
   * Or use ``nanosleep()`` if available (resolution: 1 nanosecond);
   * Or use ``select()`` (resolution: 1 microsecond).

   .. note::

      To emulate a "no-op", use :keyword:`pass` instead of ``time.sleep(0)``.

      To voluntarily relinquish the CPU, specify a real-time :ref:`scheduling
      policy <os-scheduling-policy>` and use :func:`os.sched_yield` instead.

   .. audit-event:: time.sleep seconds

   .. versionchanged:: 3.5
      The function now sleeps at least *seconds*
      even if the sleep is interrupted by a signal,
      except if the signal handler raises an exception
      (see :pep:`475` for the rationale).

   .. versionchanged:: 3.11
      On Unix, the ``clock_nanosleep()`` and ``nanosleep()`` functions are now
      used if available. On Windows, a waitable timer is now used.

   .. versionchanged:: 3.13
      Raises an auditing event.

   .. versionchanged:: 3.15
      Accepts any real number, not only integer or float.
