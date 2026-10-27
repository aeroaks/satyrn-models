.. class:: Mailbox

   A mailbox, which may be inspected and modified.

   The :class:`!Mailbox` class defines an interface and is not intended to be
   instantiated.  Instead, format-specific subclasses should inherit from
   :class:`!Mailbox` and your code should instantiate a particular subclass.

   The :class:`!Mailbox` interface is dictionary-like, with small keys
   corresponding to messages. Keys are issued by the :class:`!Mailbox` instance
   with which they will be used and are only meaningful to that :class:`!Mailbox`
   instance. A key continues to identify a message even if the corresponding
   message is modified, such as by replacing it with another message.

   Messages may be added to a :class:`!Mailbox` instance using the set-like
   method :meth:`add` and removed using a ``del`` statement or the set-like
   methods :meth:`remove` and :meth:`discard`.

   :class:`!Mailbox` interface semantics differ from dictionary semantics in some
   noteworthy ways. Each time a message is requested, a new representation
   (typically a :class:`Message` instance) is generated based upon the current
   state of the mailbox. Similarly, when a message is added to a
   :class:`!Mailbox` instance, the provided message representation's contents are
   copied. In neither case is a reference to the message representation kept by
   the :class:`!Mailbox` instance.

   The default :class:`!Mailbox` :term:`iterator` iterates over message
   representations, not keys as the default :class:`dictionary <dict>`
   iterator does. Moreover, modification of a
   mailbox during iteration is safe and well-defined. Messages added to the
   mailbox after an iterator is created will not be seen by the
   iterator. Messages removed from the mailbox before the iterator yields them
   will be silently skipped, though using a key from an iterator may result in a
   :exc:`KeyError` exception if the corresponding message is subsequently
   removed.

   .. warning::

      Be very cautious when modifying mailboxes that might be simultaneously
      changed by some other process.  The safest mailbox format to use for such
      tasks is :class:`Maildir`; try to avoid using single-file formats such as
      :class:`mbox` for
      concurrent writing.  If you're modifying a mailbox, you *must* lock it by
      calling the :meth:`lock` and :meth:`unlock` methods *before* reading any
      messages in the file or making any changes by adding or deleting a
      message.  Failing to lock the mailbox runs the risk of losing messages or
      corrupting the entire mailbox.

   The :class:`!Mailbox` class supports the :keyword:`with` statement.  When used
   as a context manager, :class:`!Mailbox` calls :meth:`lock` when the context is entered,
   returns the mailbox object as the context object, and at context end calls :meth:`close`,
   thereby releasing the lock.

   .. versionchanged:: 3.15
      Support for the :keyword:`with` statement was added.

   :class:`!Mailbox` instances have the following methods:


   .. method:: add(message)

      Add *message* to the mailbox and return the key that has been assigned to
      it.

      Parameter *message* may be a :class:`Message` instance, an
      :class:`email.message.Message` instance, a string, a byte string, or a
      file-like object (which should be open in binary mode). If *message* is
      an instance of the
      appropriate format-specific :class:`Message` subclass (e.g., if it's an
      :class:`mboxMessage` instance and this is an :class:`mbox` instance), its
      format-specific information is used. Otherwise, reasonable defaults for
      format-specific information are used.

      .. versionchanged:: 3.2
         Support for binary input was added.


   .. method:: remove(key)
               __delitem__(key)
               discard(key)

      Delete the message corresponding to *key* from the mailbox.

      If no such message exists, a :exc:`KeyError` exception is raised if the
      method was called as :meth:`remove` or :meth:`__delitem__` but no
      exception is raised if the method was called as :meth:`discard`. The
      behavior of :meth:`discard` may be preferred if the underlying mailbox
      format supports concurrent modification by other processes.


   .. method:: __setitem__(key, message)

      Replace the message corresponding to *key* with *message*. Raise a
      :exc:`KeyError` exception if no message already corresponds to *key*.

      As with :meth:`add`, parameter *message* may be a :class:`Message`
      instance, an :class:`email.message.Message` instance, a string, a byte
      string, or a file-like object (which should be open in binary mode). If
      *message* is an
      instance of the appropriate format-specific :class:`Message` subclass
      (e.g., if it's an :class:`mboxMessage` instance and this is an
      :class:`mbox` instance), its format-specific information is
      used. Otherwise, the format-specific information of the message that
      currently corresponds to *key* is left unchanged.


   .. method:: iterkeys()

      Return an :term:`iterator` over all keys


   .. method:: keys()

      The same as :meth:`iterkeys`, except that a :class:`list` is returned
      rather than an :term:`iterator`


   .. method:: itervalues()
               __iter__()

      Return an :term:`iterator` over representations of all messages.
      The messages are represented
      as instances of the appropriate format-specific :class:`Message` subclass
      unless a custom message factory was specified when the :class:`!Mailbox`
      instance was initialized.

      .. note::

         The behavior of :meth:`__iter__` is unlike that of dictionaries, which
         iterate over keys.


   .. method:: values()

      The same as :meth:`itervalues`, except that a :class:`list` is returned
      rather than an :term:`iterator`


   .. method:: iteritems()

      Return an :term:`iterator` over (*key*, *message*) pairs, where *key* is
      a key and *message* is a message representation. The messages are
      represented as instances of the appropriate format-specific
      :class:`Message` subclass unless a custom message factory was specified
      when the :class:`!Mailbox` instance was initialized.


   .. method:: items()

      The same as :meth:`iteritems`, except that a :class:`list` of pairs is
      returned rather than an :term:`iterator` of pairs.


   .. method:: get(key, default=None)
               __getitem__(key)

      Return a representation of the message corresponding to *key*. If no such
      message exists, *default* is returned if the method was called as
      :meth:`get` and a :exc:`KeyError` exception is raised if the method was
      called as :meth:`!__getitem__`. The message is represented as an instance
      of the appropriate format-specific :class:`Message` subclass unless a
      custom message factory was specified when the :class:`!Mailbox` instance
      was initialized.


   .. method:: get_message(key)

      Return a representation of the message corresponding to *key* as an
      instance of the appropriate format-specific :class:`Message` subclass, or
      raise a :exc:`KeyError` exception if no such message exists.


   .. method:: get_bytes(key)

      Return a byte representation of the message corresponding to *key*, or
      raise a :exc:`KeyError` exception if no such message exists.

      .. versionadded:: 3.2


   .. method:: get_string(key)

      Return a string representation of the message corresponding to *key*, or
      raise a :exc:`KeyError` exception if no such message exists.  The
      message is processed through :class:`email.message.Message` to
      convert it to a 7bit clean representation.


   .. method:: get_file(key)

      Return a :term:`file-like <file-like object>` representation of the
      message corresponding to *key*,
      or raise a :exc:`KeyError` exception if no such message exists.  The
      file-like object behaves as if open in binary mode.  This file should be
      closed once it is no longer needed.

      .. versionchanged:: 3.2
         The file object really is a :term:`binary file`; previously it was
         incorrectly returned in text mode.  Also, the :term:`file-like object`
         now supports the :term:`context manager` protocol: you can use a
         :keyword:`with` statement to automatically close it.

      .. note::

         Unlike other representations of messages,
         :term:`file-like <file-like object>` representations are not
         necessarily independent of the :class:`!Mailbox` instance that
         created them or of the underlying mailbox.  More specific documentation
         is provided by each subclass.


   .. method:: __contains__(key)

      Return ``True`` if *key* corresponds to a message, ``False`` otherwise.


   .. method:: __len__()

      Return a count of messages in the mailbox.


   .. method:: clear()

      Delete all messages from the mailbox.


   .. method:: pop(key, default=None)

      Return a representation of the message corresponding to *key* and delete
      the message. If no such message exists, return *default*. The message is
      represented as an instance of the appropriate format-specific
      :class:`Message` subclass unless a custom message factory was specified
      when the :class:`!Mailbox` instance was initialized.


   .. method:: popitem()

      Return an arbitrary (*key*, *message*) pair, where *key* is a key and
      *message* is a message representation, and delete the corresponding
      message. If the mailbox is empty, raise a :exc:`KeyError` exception. The
      message is represented as an instance of the appropriate format-specific
      :class:`Message` subclass unless a custom message factory was specified
      when the :class:`!Mailbox` instance was initialized.


   .. method:: update(arg)

      Parameter *arg* should be a *key*-to-*message* mapping or an iterable of
      (*key*, *message*) pairs. Updates the mailbox so that, for each given
      *key* and *message*, the message corresponding to *key* is set to
      *message* as if by using :meth:`__setitem__`. As with :meth:`__setitem__`,
      each *key* must already correspond to a message in the mailbox or else a
      :exc:`KeyError` exception will be raised, so in general it is incorrect
      for *arg* to be a :class:`!Mailbox` instance.

      .. note::

         Unlike with dictionaries, keyword arguments are not supported.


   .. method:: flush()

      Write any pending changes to the filesystem. For some :class:`Mailbox`
      subclasses, changes are always written immediately and :meth:`!flush` does
      nothing, but you should still make a habit of calling this method.


   .. method:: lock()

      Acquire an exclusive advisory lock on the mailbox so that other processes
      know not to modify it. An :exc:`ExternalClashError` is raised if the lock
      is not available. The particular locking mechanisms used depend upon the
      mailbox format.  You should *always* lock the mailbox before making any
      modifications to its contents.


   .. method:: unlock()

      Release the lock on the mailbox, if any.


   .. method:: close()

      Flush the mailbox, unlock it if necessary, and close any open files. For
      some :class:`!Mailbox` subclasses, this method does nothing.

