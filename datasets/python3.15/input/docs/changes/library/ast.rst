      of all child nodes.

      Each instance of a concrete class has one attribute for each child node,
      of the type as defined in the grammar.  For example, :class:`ast.BinOp`
      instances have an attribute :attr:`left` of type :class:`ast.expr`.

      If these attributes are marked as optional in the grammar (using a
      question mark), the value might be ``None``.  If the attributes can have
      zero-or-more values (marked with an asterisk), the values are represented
      as Python lists.  All possible attributes must be present and have valid
      values when compiling an AST with :func:`compile`.

   .. attribute:: _field_types

      The :attr:`!_field_types` attribute on each concrete class is a dictionary
      mapping field names (as also listed in :attr:`_fields`) to their types.

      .. doctest::

           >>> ast.TypeVar._field_types
           {'name': <class 'str'>, 'bound': ast.expr | None, 'default_value': ast.expr | None}

      .. versionadded:: 3.13

   .. attribute:: lineno
                  col_offset
                  end_lineno
                  end_col_offset

      Instances of :class:`ast.expr` and :class:`ast.stmt` subclasses have
      :attr:`lineno`, :attr:`col_offset`, :attr:`end_lineno`, and
      :attr:`end_col_offset` attributes.  The :attr:`lineno` and :attr:`end_lineno`
      are the first and last line numbers of source text span (1-indexed so the
      first line is line 1) and the :attr:`col_offset` and :attr:`end_col_offset`
      are the corresponding UTF-8 byte offsets of the first and last tokens that
      generated the node. The UTF-8 offset is recorded because the parser uses
      UTF-8 internally.

      Note that the end positions are not required by the compiler and are
      therefore optional. The end offset is *after* the last symbol, for example
      one can get the source segment of a one-line expression node using
      ``source_line[node.col_offset : node.end_col_offset]``.

   The constructor of a class :class:`ast.T` parses its arguments as follows:

   * If there are positional arguments, there must be as many as there are items
     in :attr:`T._fields`; they will be assigned as attributes of these names.
   * If there are keyword arguments, they will set the attributes of the same
     names to the given values.

   For example, to create and populate an :class:`ast.UnaryOp` node, you could
   use ::

      node = ast.UnaryOp(ast.USub(), ast.Constant(5, lineno=0, col_offset=0),
                         lineno=0, col_offset=0)

   If a field that is optional in the grammar is omitted from the constructor,
   it defaults to ``None``. If a list field is omitted, it defaults to the empty
   list. If a field of type :class:`!ast.expr_context` is omitted, it defaults to
   :class:`Load() <ast.Load>`. If any other field is omitted, a :exc:`DeprecationWarning` is raised
   and the AST node will not have this field. In Python 3.15, this condition will
   raise an error.

.. versionchanged:: 3.8

   Class :class:`ast.Constant` is now used for all constants.

.. versionchanged:: 3.9

   Simple indices are represented by their value, extended slices are
   represented as tuples.

.. versionchanged:: 3.13

    AST node constructors were changed to provide sensible defaults for omitted
    fields: optional fields now default to ``None``, list fields default to an
    empty list, and fields of type :class:`!ast.expr_context` default to
    :class:`Load() <ast.Load>`. Previously, omitted attributes would not exist on constructed
    nodes (accessing them raised :exc:`AttributeError`).

.. versionchanged:: 3.14

    The :meth:`~object.__repr__` output of :class:`~ast.AST` nodes includes
    the values of the node fields.

.. deprecated-removed:: 3.8 3.14

   Previous versions of Python provided the AST classes :class:`!ast.Num`,
   :class:`!ast.Str`, :class:`!ast.Bytes`, :class:`!ast.NameConstant` and
   :class:`!ast.Ellipsis`, which were deprecated in Python 3.8. These classes
   were removed in Python 3.14, and their functionality has been replaced with
   :class:`ast.Constant`.

.. deprecated:: 3.9

   Old classes :class:`!ast.Index` and :class:`!ast.ExtSlice` are still
   available, but they will be removed in future Python releases.
   In the meantime, instantiating them will return an instance of
   a different class.

.. deprecated-removed:: 3.13 3.15

   Previous versions of Python allowed the creation of AST nodes that were missing
   required fields. Similarly, AST node constructors allowed arbitrary keyword
   arguments that were set as attributes of the AST node, even if they did not
   match any of the fields of the AST node. These cases now raise a :exc:`TypeError`.

.. deprecated-removed:: 3.15 3.20

    In the :ref:`grammar above <abstract-grammar>`, the AST node classes that
    correspond to production rules with variants (aka "sums") are abstract
    classes. Previous versions of Python allowed for the creation of direct
    instances of these abstract node classes. This behavior is deprecated and
    will be removed in Python 3.20.


.. note::
    The descriptions of the specific node classes displayed here
    were initially adapted from the fantastic `Green Tree
    Snakes <https://greentreesnakes.readthedocs.io/en/latest/>`__ project and
    all its contributors.


.. _ast-root-nodes:

Root nodes
^^^^^^^^^^

.. class:: Module(body, type_ignores)

   A Python module, as with :ref:`file input <file-input>`.
   Node type generated by :func:`ast.parse` in the default ``"exec"`` *mode*.

   ``body`` is a :class:`list` of the module's :ref:`ast-statements`.

   ``type_ignores`` is a :class:`list` of the module's type ignore comments;
   see :func:`ast.parse` for more details.

   .. doctest::

        >>> print(ast.dump(ast.parse('x = 1'), indent=4))
        Module(
            body=[
                Assign(
                    targets=[
                        Name(id='x', ctx=Store())],
                    value=Constant(value=1))])


.. class:: Expression(body)

   A single Python :ref:`expression input <expression-input>`.
   Node type generated by :func:`ast.parse` when *mode* is ``"eval"``.

   ``body`` is a single node,
   one of the :ref:`expression types <ast-expressions>`.

   .. doctest::

        >>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
        Expression(
            body=Constant(value=123))


.. class:: Interactive(body)

   A single :ref:`interactive input <interactive>`, like in :ref:`tut-interac`.
   Node type generated by :func:`ast.parse` when *mode* is ``"single"``.

   ``body`` is a :class:`list` of :ref:`statement nodes <ast-statements>`.

   .. doctest::

        >>> print(ast.dump(ast.parse('x = 1; y = 2', mode='single'), indent=4))
        Interactive(
            body=[
                Assign(
                    targets=[
                        Name(id='x', ctx=Store())],
                    value=Constant(value=1)),
                Assign(
                    targets=[
                        Name(id='y', ctx=Store())],
                    value=Constant(value=2))])


.. class:: FunctionType(argtypes, returns)

   A representation of an old-style type comments for functions,
   as Python versions prior to 3.5 didn't support :pep:`484` annotations.
   Node type generated by :func:`ast.parse` when *mode* is ``"func_type"``.

   Such type comments would look like this::

       def sum_two_number(a, b):
           # type: (int, int) -> int
           return a + b

   ``argtypes`` is a :class:`list` of :ref:`expression nodes <ast-expressions>`.


----

.. function:: parse(source, filename='<unknown>', mode='exec', *, type_comments=False, feature_version=None, optimize=-1, module=None)

   Parse the source into an AST node.  Equivalent to ``compile(source,
   filename, mode, flags=FLAGS_VALUE, optimize=optimize, module=module)``,
   where ``FLAGS_VALUE`` is ``ast.PyCF_ONLY_AST`` if ``optimize <= 0``
   and ``ast.PyCF_OPTIMIZED_AST`` otherwise.

   If ``type_comments=True`` is given, the parser is modified to check
   and return type comments as specified by :pep:`484` and :pep:`526`.
   This is equivalent to adding :data:`ast.PyCF_TYPE_COMMENTS` to the
   flags passed to :func:`compile`.  This will report syntax errors
   for misplaced type comments.  Without this flag, type comments will
   be ignored, and the ``type_comment`` field on selected AST nodes
   will always be ``None``.  In addition, the locations of ``# type:
   ignore`` comments will be returned as the ``type_ignores``
   attribute of :class:`Module` (otherwise it is always an empty list).

   In addition, if ``mode`` is ``'func_type'``, the input syntax is
   modified to correspond to :pep:`484` "signature type comments",
   for example ``(str, int) -> List[str]``.

   Setting ``feature_version`` to a tuple ``(major, minor)`` will result in
   a "best-effort" attempt to parse using that Python version's grammar.
   For example, setting ``feature_version=(3, 9)`` will attempt to disallow
   parsing of :keyword:`match` statements.
   Currently ``major`` must equal to ``3``. The lowest supported version is
   ``(3, 7)`` (and this may increase in future Python versions);
   the highest is ``sys.version_info[0:2]``. "Best-effort" attempt means there
   is no guarantee that the parse (or success of the parse) is the same as
   when run on the Python version corresponding to ``feature_version``.

   If source contains a null character (``\0``), :exc:`ValueError` is raised.

   .. warning::
      Note that successfully parsing source code into an AST object doesn't
      guarantee that the source code provided is valid Python code that can
      be executed as the compilation step can raise further :exc:`SyntaxError`
      exceptions. For instance, the source ``return 42`` generates a valid
      AST node for a return statement, but it cannot be compiled alone (it needs
      to be inside a function node).

      In particular, :func:`ast.parse` won't do any scoping checks, which the
      compilation step does.

   .. warning::
      It is possible to crash the Python interpreter with a
      sufficiently large/complex string due to stack depth limitations
      in Python's AST compiler.

   .. versionchanged:: 3.8
      Added ``type_comments``, ``mode='func_type'`` and ``feature_version``.

   .. versionchanged:: 3.13
      The minimum supported version for ``feature_version`` is now ``(3, 7)``.
      The ``optimize`` argument was added.

   .. versionadded:: 3.15
      Added the *module* parameter.



----

.. function:: dump(node, annotate_fields=True, include_attributes=False, *, color=False, indent=None, show_empty=False)

   Return a formatted dump of the tree in *node*.  This is mainly useful for
   debugging purposes.  If *annotate_fields* is true (by default),
   the returned string will show the names and the values for fields.
   If *annotate_fields* is false, the result string will be more compact by
   omitting unambiguous field names.  Attributes such as line
   numbers and column offsets are not dumped by default.  If this is wanted,
   *include_attributes* can be set to true.

   If *color* is ``True``, the returned string is syntax highlighted using
   ANSI escape sequences.
   If ``False`` (the default), colored output is always disabled.

   If *indent* is a non-negative integer or string, then the tree will be
   pretty-printed with that indent level.  An indent level
   of 0, negative, or ``""`` will only insert newlines.  ``None`` (the default)
   selects the single line representation. Using a positive integer indent
   indents that many spaces per level.  If *indent* is a string (such as ``"\t"``),
   that string is used to indent each level.

   If *show_empty* is false (the default), optional empty lists and
   ``Load()`` values will be omitted from the output.
   Optional ``None`` values are always omitted.

   .. doctest::

      >>> tree = ast.parse('print(None)', '?', 'eval')
      >>> print(ast.dump(tree, indent=4))
      Expression(
          body=Call(
              func=Name(id='print'),
              args=[
                  Constant(value=None)]))
      >>> print(ast.dump(tree, indent=4, show_empty=True))
      Expression(
          body=Call(
              func=Name(id='print', ctx=Load()),
              args=[
                  Constant(value=None)],
              keywords=[]))

   .. versionchanged:: 3.9
      Added the *indent* option.

   .. versionchanged:: 3.13
      Added the *show_empty* option.

   .. versionchanged:: 3.15
      Omit optional ``Load()`` values by default.

   .. versionchanged:: 3.15
      Added the *color* parameter.



----

Command-line usage
------------------

.. versionadded:: 3.9

.. versionchanged:: 3.15
   The output is now syntax highlighted by default. This can be
   :ref:`controlled using environment variables <using-on-controlling-color>`.

The :mod:`!ast` module can be executed as a script from the command line.
It is as simple as:

.. code-block:: sh

   python -m ast [-m <mode>] [-a] [infile]

The following options are accepted:

.. program:: ast

.. option:: -h, --help

   Show the help message and exit.

.. option:: -m <mode>
            --mode <mode>

   Specify what kind of code must be compiled, like the *mode* argument
   in :func:`parse`.

.. option:: --no-type-comments

   Don't parse type comments.

.. option:: -a, --include-attributes

   Include attributes such as line numbers and column offsets.

.. option:: -i <indent>
            --indent <indent>

   Indentation of nodes in AST (number of spaces).

.. option:: --feature-version <version>

   Python version in the format 3.x (for example, 3.10). Defaults to the
   current version of the interpreter.

   .. versionadded:: 3.14

.. option:: -O <level>
            --optimize <level>

   Optimization level for parser. Defaults to no optimization.

   .. versionadded:: 3.14

.. option:: --show-empty

   Show empty lists and fields that are ``None``. Defaults to not showing empty
   objects.

   .. versionadded:: 3.14


If :file:`infile` is specified its contents are parsed to AST and dumped
to stdout.  Otherwise, the content is read from stdin.


.. seealso::

    `Green Tree Snakes <https://greentreesnakes.readthedocs.io/>`_, an external
    documentation resource, has good details on working with Python ASTs.

    `ASTTokens <https://asttokens.readthedocs.io/en/latest/user-guide.html>`_
    annotates Python ASTs with the positions of tokens and text in the source
    code that generated them. This is helpful for tools that make source code
    transformations.

    `leoAst.py <https://leo-editor.github.io/leo-editor/appendices.html#leoast-py>`_
    unifies the
    token-based and parse-tree-based views of python programs by inserting
    two-way links between tokens and ast nodes.

    `LibCST <https://libcst.readthedocs.io/>`_ parses code as a Concrete Syntax
    Tree that looks like an ast tree and keeps all formatting details. It's
    useful for building automated refactoring (codemod) applications and
    linters.

    `Parso <https://parso.readthedocs.io>`_ is a Python parser that supports
    error recovery and round-trip parsing for different Python versions (in
    multiple Python versions). Parso is also able to list multiple syntax errors
    in your Python file.