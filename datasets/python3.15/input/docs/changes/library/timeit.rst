   .. method:: Timer.autorange(callback=None, target_time=None)

      Automatically determine how many times to call :meth:`.timeit`.

      This is a convenience function that calls :meth:`.timeit` repeatedly
      so that the total time >= *Timer.target_time* seconds, returning the eventual
      (number of loops, time taken for that number of loops). It calls
      :meth:`.timeit` with increasing numbers from the sequence 1, 2, 5,
      10, 20, 50, ... until the time taken is at least *target_time* seconds.

      If *callback* is given and is not ``None``, it will be called after
      each trial with two arguments: ``callback(number, time_taken)``.

      .. versionadded:: 3.6

      .. versionchanged:: 3.15
         The optional *target_time* parameter was added.



----

.. option:: -t, --target-time=T

   if :option:`--number` is 0, the code will run until it takes at
   least this many seconds (default: 0.2)

   .. versionadded:: 3.15


----

Command-line interface
----------------------

When called as a program from the command line, the following form is used::

   python -m timeit [-n N] [-r N] [-u U] [-s S] [-p] [-v] [-h] [statement ...]

Where the following options are understood:

.. program:: timeit

.. option:: -n N, --number=N

   how many times to execute 'statement'

.. option:: -r N, --repeat=N

   how many times to repeat the timer (default 5)

.. option:: -s S, --setup=S

   statement to be executed once initially (default ``pass``)

.. option:: -p, --process

   measure process time, not wallclock time, using :func:`time.process_time`
   instead of :func:`time.perf_counter`, which is the default

   .. versionadded:: 3.3

.. option:: -u, --unit=U

   specify a time unit for timer output; can select ``nsec``, ``usec``, ``msec``, or ``sec``

   .. versionadded:: 3.5

.. option:: -t, --target-time=T

   if :option:`--number` is 0, the code will run until it takes at
   least this many seconds (default: 0.2)

   .. versionadded:: 3.15

.. option:: -v, --verbose

   print raw timing results; repeat for more digits precision

.. option:: -h, --help

   print a short usage message and exit

A multi-line statement may be given by specifying each line as a separate
statement argument; indented lines are possible by enclosing an argument in
quotes and using leading spaces.  Multiple :option:`-s` options are treated
similarly.

If :option:`-n` is not given, a suitable number of loops is calculated by trying
increasing numbers from the sequence 1, 2, 5, 10, 20, 50, ... until the total
time is at least :option:`--target-time` seconds (default: 0.2).

:func:`default_timer` measurements can be affected by other programs running on
the same machine, so the best thing to do when accurate timing is necessary is
to repeat the timing a few times and use the best time.  The :option:`-r`
option is good for this; the default of 5 repetitions is probably enough in
most cases.  You can use :func:`time.process_time` to measure CPU time.

.. note::

   There is a certain baseline overhead associated with executing a pass statement.
   The code here doesn't try to hide it, but you should be aware of it.  The
   baseline overhead can be measured by invoking the program without arguments,
   and it might differ between Python versions.

.. versionadded:: 3.15
   Output is in color by default and can be
   :ref:`controlled using environment variables <using-on-controlling-color>`.

.. _timeit-examples:
