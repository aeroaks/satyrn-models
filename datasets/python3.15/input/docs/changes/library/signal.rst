.. function:: setitimer(which, seconds, interval=0)

   Sets given interval timer (one of :const:`signal.ITIMER_REAL`,
   :const:`signal.ITIMER_VIRTUAL` or :const:`signal.ITIMER_PROF`) specified
   by *which* to fire after *seconds* (rounded up to microseconds, different from
   :func:`alarm`) and after that every *interval* seconds (if *interval*
   is non-zero). The interval timer specified by *which* can be cleared by
   setting *seconds* to zero.

   When an interval timer fires, a signal is sent to the process.
   The signal sent is dependent on the timer being used;
   :const:`signal.ITIMER_REAL` will deliver :const:`SIGALRM`,
   :const:`signal.ITIMER_VIRTUAL` sends :const:`SIGVTALRM`,
   and :const:`signal.ITIMER_PROF` will deliver :const:`SIGPROF`.

   The old values are returned as a two-tuple of floats:
   (``delay``, ``interval``).

   Attempting to pass an invalid interval timer will cause an
   :exc:`ItimerError`.

   .. availability:: Unix.

   .. versionchanged:: 3.15
      Accepts any real numbers as *seconds* and *interval*, not only integers
      or floats.



----

.. function:: sigtimedwait(sigset, timeout)

   Like :func:`sigwaitinfo`, but takes an additional *timeout* argument
   specifying a timeout. If *timeout* is specified as ``0``, a poll is
   performed. Returns :const:`None` if a timeout occurs.

   .. availability:: Unix.

      See the man page :manpage:`sigtimedwait(2)` for further information.

   See also :func:`pause`, :func:`sigwait` and :func:`sigwaitinfo`.

   .. versionadded:: 3.3

   .. versionchanged:: 3.5
      The function is now retried with the recomputed *timeout* if interrupted
      by a signal not in *sigset* and the signal handler does not raise an
      exception (see :pep:`475` for the rationale).

   .. versionchanged:: 3.15
      Accepts any real number as *timeout*, not only integer or float.

