.. data:: SO_*
          SOMAXCONN
          MSG_*
          SOL_*
          SCM_*
          IPPROTO_*
          IPPORT_*
          INADDR_*
          IP_*
          IPV6_*
          EAI_*
          AI_*
          NI_*
          TCP_*

   Many constants of these forms, documented in the Unix documentation on sockets
   and/or the IP protocol, are also defined in the socket module. They are
   generally used in arguments to the :meth:`~socket.setsockopt` and :meth:`~socket.getsockopt`
   methods of socket objects.  In most cases, only those symbols that are defined
   in the Unix header files are defined; for a few symbols, default values are
   provided.

   .. versionchanged:: 3.6
      ``SO_DOMAIN``, ``SO_PROTOCOL``, ``SO_PEERSEC``, ``SO_PASSSEC``,
      ``TCP_USER_TIMEOUT``, ``TCP_CONGESTION`` were added.

   .. versionchanged:: 3.6.5
      Added support for ``TCP_FASTOPEN``, ``TCP_KEEPCNT`` on Windows platforms
      when available.

   .. versionchanged:: 3.7
      ``TCP_NOTSENT_LOWAT`` was added.

      Added support for ``TCP_KEEPIDLE``, ``TCP_KEEPINTVL`` on Windows platforms
      when available.

   .. versionchanged:: 3.10
      ``IP_RECVTOS`` was added.
       Added ``TCP_KEEPALIVE``. On MacOS this constant can be used in the same
       way that ``TCP_KEEPIDLE`` is used on Linux.

   .. versionchanged:: 3.11
      Added ``TCP_CONNECTION_INFO``. On MacOS this constant can be used in the
      same way that ``TCP_INFO`` is used on Linux and BSD.

   .. versionchanged:: 3.12
      Added ``SO_RTABLE`` and ``SO_USER_COOKIE``. On OpenBSD
      and FreeBSD respectively those constants can be used in the same way that
      ``SO_MARK`` is used on Linux. Also added missing TCP socket options from
      Linux: ``TCP_MD5SIG``, ``TCP_THIN_LINEAR_TIMEOUTS``, ``TCP_THIN_DUPACK``,
      ``TCP_REPAIR``, ``TCP_REPAIR_QUEUE``, ``TCP_QUEUE_SEQ``,
      ``TCP_REPAIR_OPTIONS``, ``TCP_TIMESTAMP``, ``TCP_CC_INFO``,
      ``TCP_SAVE_SYN``, ``TCP_SAVED_SYN``, ``TCP_REPAIR_WINDOW``,
      ``TCP_FASTOPEN_CONNECT``, ``TCP_ULP``, ``TCP_MD5SIG_EXT``,
      ``TCP_FASTOPEN_KEY``, ``TCP_FASTOPEN_NO_COOKIE``,
      ``TCP_ZEROCOPY_RECEIVE``, ``TCP_INQ``, ``TCP_TX_DELAY``.
      Added ``IP_PKTINFO``, ``IP_UNBLOCK_SOURCE``, ``IP_BLOCK_SOURCE``,
      ``IP_ADD_SOURCE_MEMBERSHIP``, ``IP_DROP_SOURCE_MEMBERSHIP``.

   .. versionchanged:: 3.13
      Added ``SO_BINDTOIFINDEX``. On Linux this constant can be used in the
      same way that ``SO_BINDTODEVICE`` is used, but with the index of a
      network interface instead of its name.

   .. versionchanged:: 3.14
      Added missing ``IP_FREEBIND``, ``IP_RECVERR``, ``IPV6_RECVERR``,
      ``IP_RECVTTL``, and ``IP_RECVORIGDSTADDR`` on Linux.

   .. versionchanged:: 3.14
      Added support for ``TCP_QUICKACK`` on Windows platforms when available.

   .. versionchanged:: 3.15
      ``IPV6_HDRINCL`` was added.
      Added support for ``SO_PASSRIGHTS`` on Linux platforms when available.



----

.. function:: setdefaulttimeout(timeout)

   Set the default timeout in seconds (real number) for new socket objects.  When
   the socket module is first imported, the default is ``None``.  See
   :meth:`~socket.settimeout` for possible values and their respective
   meanings.

   .. versionchanged:: 3.15
      Accepts any real number, not only integer or float.



----

   .. method:: settimeout(value)

      Set a timeout on blocking socket operations.  The *value* argument can be a
      nonnegative real number expressing seconds, or ``None``.
      If a non-zero value is given, subsequent socket operations will raise a
      :exc:`timeout` exception if the timeout period *value* has elapsed before
      the operation has completed.  If zero is given, the socket is put in
      non-blocking mode. If ``None`` is given, the socket is put in blocking mode.

      For further information, please consult the :ref:`notes on socket timeouts <socket-timeouts>`.

      .. versionchanged:: 3.7
         The method no longer toggles :const:`SOCK_NONBLOCK` flag on
         :attr:`socket.type`.

      .. versionchanged:: 3.15
         Accepts any real number, not only integer or float.

