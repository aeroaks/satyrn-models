Legacy locking APIs
-------------------

These APIs are obsolete since Python 3.13 with the introduction of
:c:type:`PyMutex`.

.. versionchanged:: 3.15
   These APIs are now a simple wrapper around ``PyMutex``.


.. c:type:: PyThread_type_lock

   A pointer to a mutual exclusion lock.


.. c:macro:: PY_TIMEOUT_T

   A :term:`soft deprecated` alias to :c:expr:`long long`, the integer
   type used for the timeout argument of :c:func:`PyThread_acquire_lock_timed`.

   .. soft-deprecated:: 3.15.2

.. c:var:: const long long PY_TIMEOUT_MAX

   The maximum timeout, in microseconds, supported by
   :c:func:`PyThread_acquire_lock_timed`.

   .. note::
      This differs from :data:`_thread.TIMEOUT_MAX`, which is expressed in seconds.


.. c:type:: PyLockStatus

   The result of acquiring a lock with a timeout.

   .. c:namespace:: NULL

   .. c:enumerator:: PY_LOCK_FAILURE

      Failed to acquire the lock.

   .. c:enumerator:: PY_LOCK_ACQUIRED

      The lock was successfully acquired.

   .. c:enumerator:: PY_LOCK_INTR

      The lock was interrupted by a signal.


.. c:function:: PyThread_type_lock PyThread_allocate_lock(void)

   Allocate a new lock.

   On success, this function returns a lock; on failure, this
   function returns ``0`` without an exception set.

   The caller does not need to hold an :term:`attached thread state`.

   .. versionchanged:: 3.15
      This function now always uses :c:type:`PyMutex`. In prior versions, this
      would use a lock provided by the operating system.


.. c:function:: void PyThread_free_lock(PyThread_type_lock lock)

   Destroy *lock*. The lock should not be held by any thread when calling
   this.

   The caller does not need to hold an :term:`attached thread state`.


.. c:function:: PyLockStatus PyThread_acquire_lock_timed(PyThread_type_lock lock, long long microseconds, int intr_flag)

   Acquire *lock* with a timeout.

   This will wait for *microseconds* microseconds to acquire the lock. If the
   timeout expires, this function returns :c:enumerator:`PY_LOCK_FAILURE`.
   If *microseconds* is ``-1``, this will wait indefinitely until the lock has
   been released.

   If *intr_flag* is ``1``, acquiring the lock may be interrupted by a signal,
   in which case this function returns :c:enumerator:`PY_LOCK_INTR`. Upon
   interruption, it's generally expected that the caller makes a call to
   :c:func:`Py_MakePendingCalls` to propagate an exception to Python code.

   If the lock is successfully acquired, this function returns
   :c:enumerator:`PY_LOCK_ACQUIRED`.

   The caller does not need to hold an :term:`attached thread state`.


.. c:function:: int PyThread_acquire_lock(PyThread_type_lock lock, int waitflag)

   Acquire *lock*.

   If *waitflag* is ``1`` and another thread currently holds the lock, this
   function will wait until the lock can be acquired and will always return
   ``1``.

   If *waitflag* is ``0`` and another thread holds the lock, this function will
   not wait and instead return ``0``. If the lock is not held by any other
   thread, then this function will acquire it and return ``1``.

   Unlike :c:func:`PyThread_acquire_lock_timed`, acquiring the lock cannot be
   interrupted by a signal.

   The caller does not need to hold an :term:`attached thread state`.


.. c:function:: int PyThread_release_lock(PyThread_type_lock lock)

   Release *lock*. If *lock* is not held, then this function issues a
   fatal error.

   The caller does not need to hold an :term:`attached thread state`.

----

.. c:macro:: PY_TIMEOUT_T

   A :term:`soft deprecated` alias to :c:expr:`long long`, the integer
   type used for the timeout argument of :c:func:`PyThread_acquire_lock_timed`.

   .. soft-deprecated:: 3.15.2


----

.. c:function:: PyThread_type_lock PyThread_allocate_lock(void)

   Allocate a new lock.

   On success, this function returns a lock; on failure, this
   function returns ``0`` without an exception set.

   The caller does not need to hold an :term:`attached thread state`.

   .. versionchanged:: 3.15
      This function now always uses :c:type:`PyMutex`. In prior versions, this
      would use a lock provided by the operating system.

