.. method:: Popen.wait(timeout=None)

   Wait for child process to terminate.  Set and return
   :attr:`~Popen.returncode` attribute.

   If the process does not terminate after *timeout* seconds, raise a
   :exc:`TimeoutExpired` exception.  It is safe to catch this exception and
   retry the wait.

   .. note::

      This will deadlock when using ``stdout=PIPE`` or ``stderr=PIPE``
      and the child process generates enough output to a pipe such that
      it blocks waiting for the OS pipe buffer to accept more data.
      Use :meth:`Popen.communicate` when using pipes to avoid that.

   .. note::

      When ``timeout`` is not ``None`` and the platform supports it, an
      efficient event-driven mechanism is used to wait for process termination:

      - Linux >= 5.3 uses :func:`os.pidfd_open` + :func:`select.poll`
      - macOS and other BSD variants use :func:`select.kqueue` +
        ``KQ_FILTER_PROC`` + ``KQ_NOTE_EXIT``
      - Windows uses ``WaitForSingleObject``

      If none of these mechanisms are available, the function falls back to a
      busy loop (non-blocking call and short sleeps).

   .. note::

      Use the :mod:`asyncio` module for an asynchronous wait: see
      :class:`asyncio.create_subprocess_exec`.

   .. versionchanged:: 3.3
      *timeout* was added.

   .. versionchanged:: 3.15
      if *timeout* is not ``None``, use efficient event-driven implementation
      on Linux >= 5.3 and macOS / BSD.
