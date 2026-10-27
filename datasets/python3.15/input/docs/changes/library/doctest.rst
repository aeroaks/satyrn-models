.. function:: DocFileSuite(*paths, module_relative=True, package=None, setUp=None, tearDown=None, globs=None, optionflags=0, parser=DocTestParser(), encoding=None)

   Convert doctest tests from one or more text files to a
   :class:`unittest.TestSuite`.

   The returned :class:`unittest.TestSuite` is to be run by the unittest
   framework and runs the interactive examples in each file.
   Each file is run as a separate unit test, and each example in a file
   is run as a :ref:`subtest <subtests>`.
   If any example in a file fails, then the synthesized unit test fails.
   The traceback for failure or error contains the name of the file
   containing the test and a (sometimes approximate) line number.
   If all the examples in a file are skipped, then the synthesized unit
   test is also marked as skipped.

   Pass one or more paths (as strings) to text files to be examined.

   Options may be provided as keyword arguments:

   Optional argument *module_relative* specifies how the filenames in *paths*
   should be interpreted:

   * If *module_relative* is ``True`` (the default), then each filename in
     *paths* specifies an OS-independent module-relative path.  By default, this
     path is relative to the calling module's directory; but if the *package*
     argument is specified, then it is relative to that package.  To ensure
     OS-independence, each filename should use ``/`` characters to separate path
     segments, and may not be an absolute path (i.e., it may not begin with
     ``/``).

   * If *module_relative* is ``False``, then each filename in *paths* specifies
     an OS-specific path.  The path may be absolute or relative; relative paths
     are resolved with respect to the current working directory.

   Optional argument *package* is a Python package or the name of a Python
   package whose directory should be used as the base directory for
   module-relative filenames in *paths*.  If no package is specified, then the
   calling module's directory is used as the base directory for module-relative
   filenames.  It is an error to specify *package* if *module_relative* is
   ``False``.

   Optional argument *setUp* specifies a set-up function for the test suite.
   This is called before running the tests in each file.  The *setUp* function
   will be passed a :class:`DocTest` object.  The *setUp* function can access the
   test globals as the :attr:`~DocTest.globs` attribute of the test passed.

   Optional argument *tearDown* specifies a tear-down function for the test
   suite.  This is called after running the tests in each file.  The *tearDown*
   function will be passed a :class:`DocTest` object.  The *tearDown* function can
   access the test globals as the :attr:`~DocTest.globs` attribute of the test
   passed.

   Optional argument *globs* is a dictionary containing the initial global
   variables for the tests.  A new copy of this dictionary is created for each
   test.  By default, *globs* is a new empty dictionary.

   Optional argument *optionflags* specifies the default doctest options for the
   tests, created by or-ing together individual option flags.  See section
   :ref:`doctest-options`. See function :func:`set_unittest_reportflags` below
   for a better way to set reporting options.

   Optional argument *parser* specifies a :class:`DocTestParser` (or subclass)
   that should be used to extract tests from the files.  It defaults to a normal
   parser (i.e., ``DocTestParser()``).

   Optional argument *encoding* specifies an encoding that should be used to
   convert the file to unicode.

   The global ``__file__`` is added to the globals provided to doctests loaded
   from a text file using :func:`DocFileSuite`.

   .. versionchanged:: 3.15
      Run each example as a :ref:`subtest <subtests>`.



----

.. function:: DocTestSuite(module=None, globs=None, extraglobs=None, test_finder=None, setUp=None, tearDown=None, optionflags=0, checker=None)

   Convert doctest tests for a module to a :class:`unittest.TestSuite`.

   The returned :class:`unittest.TestSuite` is to be run by the unittest
   framework and runs each doctest in the module.
   Each docstring is run as a separate unit test, and each example in
   a docstring is run as a :ref:`subtest <subtests>`.
   If any of the doctests fail, then the synthesized unit test fails.
   The traceback for failure or error contains the name of the file
   containing the test and a (sometimes approximate) line number.
   If all the examples in a docstring are skipped, then the
   synthesized unit test is also marked as skipped.

   Optional argument *module* provides the module to be tested.  It can be a module
   object or a (possibly dotted) module name.  If not specified, the module calling
   this function is used.

   Optional argument *globs* is a dictionary containing the initial global
   variables for the tests.  A new copy of this dictionary is created for each
   test.  By default, *globs* is the module's :attr:`~module.__dict__`.

   Optional argument *extraglobs* specifies an extra set of global variables, which
   is merged into *globs*.  By default, no extra globals are used.

   Optional argument *test_finder* is the :class:`DocTestFinder` object (or a
   drop-in replacement) that is used to extract doctests from the module.

   Optional arguments *setUp*, *tearDown*, and *optionflags* are the same as for
   function :func:`DocFileSuite` above, but they are called for each docstring.

   This function uses the same search technique as :func:`testmod`.

   .. versionchanged:: 3.5
      :func:`DocTestSuite` returns an empty :class:`unittest.TestSuite` if *module*
      contains no docstrings instead of raising :exc:`ValueError`.

   .. versionchanged:: 3.15
      Run each example as a :ref:`subtest <subtests>`.


----

   .. method:: report_skip(out, test, example)

      Report that the given example was skipped.  This method is provided to
      allow subclasses of :class:`DocTestRunner` to customize their output; it
      should not be called directly.

      *example* is the example about to be processed.  *test* is the test
      containing *example*.  *out* is the output function that was passed to
      :meth:`DocTestRunner.run`.

      .. versionadded:: 3.15

