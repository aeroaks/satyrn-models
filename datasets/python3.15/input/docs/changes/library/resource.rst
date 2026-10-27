.. data:: RLIM_INFINITY

   Constant used to represent the limit for an unlimited resource.

   .. versionchanged:: 3.15
      It is now always positive.
      Previously, it could be negative, such as -1 or -3.



----

.. data:: RLIM_SAVED_MAX

   Constants used to represent the soft and hard limit values if they
   cannot be represented in the ``rlim_t`` value in C.
   Can be equal to :data:`RLIM_INFINITY`.

   .. versionadded:: 3.15



----

.. data:: RLIMIT_NTHR

   The maximum number of threads for this user id, not counting the main
   and kernel threads.

   .. availability:: NetBSD >= 7.0.

   .. versionadded:: 3.15



----

.. data:: RLIMIT_PIPEBUF

   The maximum total size of in-kernel buffers for bi-directional pipes/fifos
   that this user id is allowed to consume.

   .. availability:: FreeBSD >= 14.2.

   .. versionadded:: 3.15



----

.. data:: RLIMIT_THREADS

   The maximum number of threads each process can create.

   .. availability:: AIX.

   .. versionadded:: 3.15



----

.. data:: RLIMIT_UMTXP

   The limit of the number of process-shared Posix thread library objects
   allocated by user id.

   .. availability:: FreeBSD >= 11.

   .. versionadded:: 3.15


Resource Usage
--------------

These functions are used to retrieve resource usage information:


.. function:: getrusage(who)

   This function returns an object that describes the resources consumed by either
   the current process or its children, as specified by the *who* parameter.  The
   *who* parameter should be specified using one of the :const:`!RUSAGE_\*`
   constants described below.

   A simple example::

      from resource import *
      import time

      # a non CPU-bound task
      time.sleep(3)
      print(getrusage(RUSAGE_SELF))

      # a CPU-bound task
      for i in range(10 ** 8):
         _ = 1 + 1
      print(getrusage(RUSAGE_SELF))

   The fields of the return value each describe how a particular system resource
   has been used, e.g. amount of time spent running in user mode or number of times
   the process was swapped out of main memory. Some values are dependent on the
   clock tick interval, e.g. the amount of memory the process is using.

   For backward compatibility, the return value is also accessible as a tuple of 16
   elements.

   The fields :attr:`!ru_utime` and :attr:`!ru_stime` of the return value are
   floating-point values representing the amount of time spent executing in user
   mode and the amount of time spent executing in system mode, respectively. The
   remaining values are integers. Consult the :manpage:`getrusage(2)` man page for
   detailed information about these values. A brief summary is presented here:

   +--------+----------------------+---------------------------------------+
   | Index  | Field                | Resource                              |
   +========+======================+=======================================+
   | ``0``  | :attr:`!ru_utime`    | time in user mode (float seconds)     |
   +--------+----------------------+---------------------------------------+
   | ``1``  | :attr:`!ru_stime`    | time in system mode (float seconds)   |
   +--------+----------------------+---------------------------------------+
   | ``2``  | :attr:`!ru_maxrss`   | maximum resident set size             |
   +--------+----------------------+---------------------------------------+
   | ``3``  | :attr:`!ru_ixrss`    | shared memory size                    |
   +--------+----------------------+---------------------------------------+
   | ``4``  | :attr:`!ru_idrss`    | unshared memory size                  |
   +--------+----------------------+---------------------------------------+
   | ``5``  | :attr:`!ru_isrss`    | unshared stack size                   |
   +--------+----------------------+---------------------------------------+
   | ``6``  | :attr:`!ru_minflt`   | page faults not requiring I/O         |
   +--------+----------------------+---------------------------------------+
   | ``7``  | :attr:`!ru_majflt`   | page faults requiring I/O             |
   +--------+----------------------+---------------------------------------+
   | ``8``  | :attr:`!ru_nswap`    | number of swap outs                   |
   +--------+----------------------+---------------------------------------+
   | ``9``  | :attr:`!ru_inblock`  | block input operations                |
   +--------+----------------------+---------------------------------------+
   | ``10`` | :attr:`!ru_oublock`  | block output operations               |
   +--------+----------------------+---------------------------------------+
   | ``11`` | :attr:`!ru_msgsnd`   | messages sent                         |
   +--------+----------------------+---------------------------------------+
   | ``12`` | :attr:`!ru_msgrcv`   | messages received                     |
   +--------+----------------------+---------------------------------------+
   | ``13`` | :attr:`!ru_nsignals` | signals received                      |
   +--------+----------------------+---------------------------------------+
   | ``14`` | :attr:`!ru_nvcsw`    | voluntary context switches            |
   +--------+----------------------+---------------------------------------+
   | ``15`` | :attr:`!ru_nivcsw`   | involuntary context switches          |
   +--------+----------------------+---------------------------------------+

   This function will raise a :exc:`ValueError` if an invalid *who* parameter is
   specified. It may also raise :exc:`error` exception in unusual circumstances.


.. function:: getpagesize()

   Returns the number of bytes in a system page. (This need not be the same as the
   hardware page size.)

The following :const:`!RUSAGE_\*` symbols are passed to the :func:`getrusage`
function to specify which processes information should be provided for.


.. data:: RUSAGE_SELF

   Pass to :func:`getrusage` to request resources consumed by the calling
   process, which is the sum of resources used by all threads in the process.


.. data:: RUSAGE_CHILDREN

   Pass to :func:`getrusage` to request resources consumed by child processes
   of the calling process which have been terminated and waited for.


.. data:: RUSAGE_BOTH

   Pass to :func:`getrusage` to request resources consumed by both the current
   process and child processes.  May not be available on all systems.


.. data:: RUSAGE_THREAD

   Pass to :func:`getrusage` to request resources consumed by the current
   thread.  May not be available on all systems.

   .. versionadded:: 3.2