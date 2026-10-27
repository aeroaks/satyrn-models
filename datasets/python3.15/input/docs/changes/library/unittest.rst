   .. method:: assertWarns(warning, callable, *args, **kwds)
               assertWarns(warning, *, msg=None)

      Test that a warning is triggered when *callable* is called with any
      positional or keyword arguments that are also passed to
      :meth:`assertWarns`.  The test passes if *warning* is triggered and
      fails if it isn't.  Any exception is an error.
      To catch any of a group of warnings, a tuple containing the warning
      classes may be passed as *warnings*.

      If only the *warning* and possibly the *msg* arguments are given,
      return a context manager so that the code under test can be written
      inline rather than as a function::

         with self.assertWarns(SomeWarning):
             do_something()

      When used as a context manager, :meth:`assertWarns` accepts the
      additional keyword argument *msg*.

      The context manager will store the caught warning object in its
      :attr:`!warning` attribute, and the source line which triggered the
      warnings in the :attr:`!filename` and :attr:`!lineno` attributes.
      This can be useful if the intention is to perform additional checks
      on the warning caught::

         with self.assertWarns(SomeWarning) as cm:
             do_something()

         self.assertIn('myfile.py', cm.filename)
         self.assertEqual(320, cm.lineno)

      The context managers can be nested to test that multiple different
      warnings are emitted::

         with (self.assertWarns(SomeWarning),
               self.assertWarns(OtherWarning)):
             do_something()

      This method works regardless of the warning filters in place when it
      is called.

      .. versionadded:: 3.2

      .. versionchanged:: 3.3
         Added the *msg* keyword argument when used as a context manager.

      .. versionchanged:: 3.15
         Warnings that do not match the specified category are no longer
         swallowed.
         Nested context managers are now supported.


----

   .. method:: assertWarnsRegex(warning, regex, callable, *args, **kwds)
               assertWarnsRegex(warning, regex, *, msg=None)

      Like :meth:`assertWarns` but also tests that *regex* matches on the
      message of the triggered warning.  *regex* may be a regular expression
      object or a string containing a regular expression suitable for use
      by :func:`re.search`.  Example::

         self.assertWarnsRegex(DeprecationWarning,
                               r'legacy_function\(\) is deprecated',
                               legacy_function, 'XYZ')

      or::

         with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
             frobnicate('/etc/passwd')

      The context managers can be nested to test that multiple different
      warnings are emitted::

         with (self.assertWarns(SomeWarning, regex1),
               self.assertWarns(OtherWarning, regex2)):
             do_something()

      .. versionadded:: 3.2

      .. versionchanged:: 3.3
         Added the *msg* keyword argument when used as a context manager.

      .. versionchanged:: 3.15
         Warnings that do not match the specified category or regex are
         no longer swallowed.
         Nested context managers are now supported.


----

   .. method:: assertLogs(logger=None, level=None, formatter=None)

      A context manager to test that at least one message is logged on
      the *logger* or one of its children, with at least the given
      *level*.

      If given, *logger* should be a :class:`logging.Logger` object or a
      :class:`str` giving the name of a logger.  The default is the root
      logger, which will catch all messages that were not blocked by a
      non-propagating descendent logger.

      If given, *level* should be either a numeric logging level or
      its string equivalent (for example either ``"ERROR"`` or
      :const:`logging.ERROR`).  The default is :const:`logging.INFO`.

      If given, *formatter* should be a :class:`logging.Formatter` object.
      The default is a formatter with format string
      ``"%(levelname)s:%(name)s:%(message)s"``

      The test passes if at least one message emitted inside the ``with``
      block matches the *logger* and *level* conditions, otherwise it fails.

      The object returned by the context manager is a recording helper
      which keeps tracks of the matching log messages.  It has two
      attributes:

      .. attribute:: records

         A list of :class:`logging.LogRecord` objects of the matching
         log messages.

      .. attribute:: output

         A list of :class:`str` objects with the formatted output of
         matching messages.

      Example::

         with self.assertLogs('foo', level='INFO') as cm:
             logging.getLogger('foo').info('first message')
             logging.getLogger('foo.bar').error('second message')
         self.assertEqual(cm.output, ['INFO:foo:first message',
                                      'ERROR:foo.bar:second message'])

      .. versionadded:: 3.4

      .. versionchanged:: 3.15
         Now accepts a *formatter* to control how messages are formatted.
