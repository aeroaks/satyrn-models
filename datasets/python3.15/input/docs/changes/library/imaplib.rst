.. method:: IMAP4.login_cram_md5(user, password)

   Force use of ``CRAM-MD5`` authentication when identifying the client to protect
   the password.  Will only work if the server ``CAPABILITY`` response includes the
   phrase ``AUTH=CRAM-MD5``.

   .. versionchanged:: 3.15
      An :exc:`IMAP4.error` is raised if MD5 support is not available.



----

.. property:: IMAP4.file

   Internal :class:`~io.BufferedReader` associated with the underlying socket.
   This property is documented for legacy purposes but not part of the public
   interface. The caller is responsible to ensure that the current file is
   closed before changing it.

   .. deprecated-removed:: 3.15 3.19


.. _imap4-example:

IMAP4 Example
-------------

Here is a minimal example (without error checking) that opens a mailbox and
retrieves and prints all messages::

   import getpass, imaplib
