.. class:: TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)

   This uses the internet TCP protocol, which provides for
   continuous streams of data between the client and server.
   If *bind_and_activate* is true, the constructor automatically attempts to
   invoke :meth:`~BaseServer.server_bind` and
   :meth:`~BaseServer.server_activate`.  The other parameters are passed to
   the :class:`BaseServer` base class.

   .. versionchanged:: 3.15
      The default queue size is now ``socket.SOMAXCONN`` for :class:`socketserver.TCPServer`.
