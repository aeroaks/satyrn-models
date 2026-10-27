.. class:: ArgumentParser(prog=None, usage=None, description=None, \
                          epilog=None, parents=[], \
                          formatter_class=argparse.HelpFormatter, \
                          prefix_chars='-', fromfile_prefix_chars=None, \
                          argument_default=None, conflict_handler='error', \
                          add_help=True, allow_abbrev=True, exit_on_error=True, \
                          *, suggest_on_error=True, color=True)

   Create a new :class:`ArgumentParser` object. All parameters should be passed
   as keyword arguments. Each parameter has its own more detailed description
   below, but in short they are:

   * prog_ - The name of the program (default: generated from the ``__main__``
     module attributes and ``sys.argv[0]``)

   * usage_ - The string describing the program usage (default: generated from
     arguments added to parser)

   * description_ - Text to display before the argument help
     (by default, no text)

   * epilog_ - Text to display after the argument help (by default, no text)

   * parents_ - A list of :class:`ArgumentParser` objects whose arguments should
     also be included

   * formatter_class_ - A class for customizing the help output

   * prefix_chars_ - The set of characters that prefix optional arguments
     (default: '-')

   * fromfile_prefix_chars_ - The set of characters that prefix files from
     which additional arguments should be read (default: ``None``)

   * argument_default_ - The global default value for arguments
     (default: ``None``)

   * conflict_handler_ - The strategy for resolving conflicting optionals
     (usually unnecessary)

   * add_help_ - Add a ``-h/--help`` option to the parser (default: ``True``)

   * allow_abbrev_ - Allows long options to be abbreviated if the
     abbreviation is unambiguous (default: ``True``)

   * exit_on_error_ - Determines whether or not :class:`!ArgumentParser` exits with
     error info when an error occurs. (default: ``True``)

   * suggest_on_error_ - Enables suggestions for mistyped argument choices
     and subparser names (default: ``True``)

   * color_ - Allow color output (default: ``True``)

   .. versionchanged:: 3.5
      *allow_abbrev* parameter was added.

   .. versionchanged:: 3.8
      In previous versions, *allow_abbrev* also disabled grouping of short
      flags such as ``-vv`` to mean ``-v -v``.

   .. versionchanged:: 3.9
      *exit_on_error* parameter was added.

   .. versionchanged:: 3.14
      *suggest_on_error* and *color* parameters were added.

   .. versionchanged:: 3.15
      *suggest_on_error* default changed to ``True``.


----

suggest_on_error
^^^^^^^^^^^^^^^^

By default, when a user passes an invalid argument choice or subparser name,
:class:`ArgumentParser` will exit with error info and provide suggestions for
mistyped arguments. The error message will list the permissible argument
choices (if specified) or subparser names, along with a "maybe you meant"
suggestion if a close match is found. Note that this only applies for arguments
when the choices specified are strings::

   >>> parser = argparse.ArgumentParser(suggest_on_error=True)
   >>> parser.add_argument('--action', choices=['debug', 'dryrun'])
   >>> parser.parse_args(['--action', 'debugg'])
   usage: tester.py [-h] [--action {debug,dryrun}]
   tester.py: error: argument --action: invalid choice: 'debugg', maybe you meant 'debug'? (choose from debug, dryrun)

You can disable suggestions by setting ``suggest_on_error`` to ``False``.

.. versionadded:: 3.14
.. versionchanged:: 3.15
   Changed default value of ``suggest_on_error`` from ``False`` to ``True``.


----

color
^^^^^

By default, the help message is printed in color using `ANSI escape sequences
<https://en.wikipedia.org/wiki/ANSI_escape_code>`__.
If you want plain text help messages, you can disable this :ref:`in your local
environment <using-on-controlling-color>`, or in the argument parser itself
by setting ``color`` to ``False``::

   >>> parser = argparse.ArgumentParser(description='Process some integers.',
   ...                                  color=False)
   >>> parser.add_argument('--action', choices=['sum', 'max'])
   >>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
   ...                     help='an integer for the accumulator')
   >>> parser.parse_args(['--help'])

Note that when ``color=True``, colored output depends on both environment
variables and terminal capabilities.  However, if ``color=False``, colored
output is always disabled, even if environment variables like ``FORCE_COLOR``
are set.

.. versionadded:: 3.14

To highlight inline code in your description, epilog, or argument ``help``
text, you can use single or double backticks::

   >>> parser = argparse.ArgumentParser(
   ...     formatter_class=argparse.RawDescriptionHelpFormatter,
   ...     description='Run ``python -m myapp`` to start.',
   ...     epilog='''Examples:
   ...   `python -m myapp --verbose`
   ...   ``python -m myapp --config settings.json``
   ... ''')
   >>> parser.add_argument('--foo', help='set the `foo` value')

When colors are enabled, the text inside backticks will be displayed in a
distinct color to help examples stand out. When colors are disabled, backticks
are preserved as-is, which is readable in plain text.

.. versionadded:: 3.15


The add_argument() method
-------------------------

.. method:: ArgumentParser.add_argument(name or flags..., *, [action], [nargs], \
                           [const], [default], [type], [choices], [required], \
                           [help], [metavar], [dest], [deprecated])

   Define how a single command-line argument should be parsed.  Each parameter
   has its own more detailed description below, but in short they are:

   * `name or flags`_ - Either a name or a list of option strings, e.g. ``'foo'``
     or ``'-f', '--foo'``.

   * action_ - The basic type of action to be taken when this argument is
     encountered at the command line.

   * nargs_ - The number of command-line arguments that should be consumed.

   * const_ - A constant value required by some action_ and nargs_ selections.

   * default_ - The value produced if the argument is absent from the
     command line and if it is absent from the namespace object.

   * type_ - The type to which the command-line argument should be converted.

   * choices_ - A sequence of the allowable values for the argument.

   * required_ - Whether or not the command-line option may be omitted
     (optionals only).

   * help_ - A brief description of what the argument does.

   * metavar_ - A name for the argument in usage messages.

   * dest_ - The name of the attribute to be added to the object returned by
     :meth:`parse_args`.

   * deprecated_ - Whether or not use of the argument is deprecated.

   The method returns an :class:`Action` object representing the argument.

The following sections describe how each of these are used.


.. _`name or flags`:

name or flags
^^^^^^^^^^^^^

The :meth:`~ArgumentParser.add_argument` method must know whether an optional
argument, like ``-f`` or ``--foo``, or a positional argument, like a list of
filenames, is expected.  The first arguments passed to
:meth:`~ArgumentParser.add_argument` must therefore be either a series of
flags, or a simple argument name.

For example, an optional argument could be created like::

   >>> parser.add_argument('-f', '--foo')

while a positional argument could be created like::

   >>> parser.add_argument('bar')

When :meth:`~ArgumentParser.parse_args` is called, optional arguments will be
identified by the ``-`` prefix, and the remaining arguments will be assumed to
be positional::

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-f', '--foo')
   >>> parser.add_argument('bar')
   >>> parser.parse_args(['BAR'])
   Namespace(bar='BAR', foo=None)
   >>> parser.parse_args(['BAR', '--foo', 'FOO'])
   Namespace(bar='BAR', foo='FOO')
   >>> parser.parse_args(['--foo', 'FOO'])
   usage: PROG [-h] [-f FOO] bar
   PROG: error: the following arguments are required: bar

By default, :mod:`!argparse` automatically handles the internal naming and
display names of arguments, simplifying the process without requiring
additional configuration.
As such, you do not need to specify the dest_ and metavar_ parameters.
For optional arguments, the dest_ parameter defaults to the argument name, with
underscores ``_`` replacing hyphens ``-``. The metavar_ parameter defaults to
the upper-cased name. For example::

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('--foo-bar')
   >>> parser.parse_args(['--foo-bar', 'FOO-BAR'])
   Namespace(foo_bar='FOO-BAR')
   >>> parser.print_help()
   usage:  [-h] [--foo-bar FOO-BAR]

   optional arguments:
    -h, --help  show this help message and exit
    --foo-bar FOO-BAR


----

dest
^^^^

Most :class:`ArgumentParser` actions add some value as an attribute of the
object returned by :meth:`~ArgumentParser.parse_args`.  The name of this
attribute is determined by the ``dest`` keyword argument of
:meth:`~ArgumentParser.add_argument`.  For positional argument actions,
``dest`` is normally supplied as the first argument to
:meth:`~ArgumentParser.add_argument`::

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('bar')
   >>> parser.parse_args(['XXX'])
   Namespace(bar='XXX')

For optional argument actions, the value of ``dest`` is normally inferred from
the option strings.  :class:`ArgumentParser` generates the value of ``dest`` by
taking the first double-dash long option string and stripping away the initial
``-`` characters.
If no double-dash long option strings were supplied, ``dest`` will be derived
from the first single-dash long option string by stripping the initial ``-``
character.
If no long option strings were supplied, ``dest`` will be derived from
the first short option string by stripping the initial ``-`` character.  Any
internal ``-`` characters will be converted to ``_`` characters to make sure
the string is a valid attribute name.  The examples below illustrate this
behavior::

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('-f', '--foo-bar', '--foo')
   >>> parser.add_argument('-q', '-quz')
   >>> parser.add_argument('-x', '-y')
   >>> parser.parse_args('-f 1 -q 2 -x 3'.split())
   Namespace(foo_bar='1', quz='2', x='3')
   >>> parser.parse_args('--foo 1 -quz 2 -y 3'.split())
   Namespace(foo_bar='1', quz='2', x='2')

``dest`` allows a custom attribute name to be provided::

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', dest='bar')
   >>> parser.parse_args('--foo XXX'.split())
   Namespace(bar='XXX')

Multiple arguments may share the same ``dest``.  By default, the value from the
last such argument given on the command line wins.  Use ``action='append'`` to
collect values from all of them into a list instead.  For conflicting *option
strings* rather than ``dest`` names, see conflict_handler_.

.. versionchanged:: 3.15
   Single-dash long option now takes precedence over short options.


.. _deprecated:


----

.. class:: BooleanOptionalAction

   A subclass of :class:`Action` for handling boolean flags with positive
   and negative options. Adding a single argument such as ``--foo`` automatically
   creates both ``--foo`` and ``--no-foo`` options, storing ``True`` and ``False``
   respectively::

       >>> import argparse
       >>> parser = argparse.ArgumentParser()
       >>> parser.add_argument('--foo', action=argparse.BooleanOptionalAction)
       >>> parser.parse_args(['--no-foo'])
       Namespace(foo=False)

   Single-dash long options are also supported.
   For example, negative option ``-nofoo`` is automatically added for
   positive option ``-foo``.
   But no additional options are added for short options such as ``-f``.

   .. versionadded:: 3.9

   .. versionchanged:: 3.15
      Added support for single-dash options.

      Added support for alternate prefix_chars_.


The parse_args() method
-----------------------

.. method:: ArgumentParser.parse_args(args=None, namespace=None)

   Convert argument strings to objects and assign them as attributes of the
   namespace.  Return the populated namespace.

   Previous calls to :meth:`add_argument` determine exactly what objects are
   created and how they are assigned. See the documentation for
   :meth:`!add_argument` for details.

   * args_ - List of strings to parse.  The default is taken from
     :data:`sys.argv`.

   * namespace_ - An object to take the attributes.  The default is a new empty
     :class:`Namespace` object.


Option value syntax
^^^^^^^^^^^^^^^^^^^

The :meth:`~ArgumentParser.parse_args` method supports several ways of
specifying the value of an option (if it takes one).  In the simplest case, the
option and its value are passed as two separate arguments::

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x')
   >>> parser.add_argument('--foo')
   >>> parser.parse_args(['-x', 'X'])
   Namespace(foo=None, x='X')
   >>> parser.parse_args(['--foo', 'FOO'])
   Namespace(foo='FOO', x=None)

For long options (options with names longer than a single character), the option
and value can also be passed as a single command-line argument, using ``=`` to
separate them::

   >>> parser.parse_args(['--foo=FOO'])
   Namespace(foo='FOO', x=None)

For short options (options only one character long), the option and its value
can be concatenated::

   >>> parser.parse_args(['-xX'])
   Namespace(foo=None, x='X')

Several short options can be joined together, using only a single ``-`` prefix,
as long as only the last option (or none of them) requires a value::

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x', action='store_true')
   >>> parser.add_argument('-y', action='store_true')
   >>> parser.add_argument('-z')
   >>> parser.parse_args(['-xyzZ'])
   Namespace(x=True, y=True, z='Z')


Invalid arguments
^^^^^^^^^^^^^^^^^

While parsing the command line, :meth:`~ArgumentParser.parse_args` checks for a
variety of errors, including ambiguous options, invalid types, invalid options,
wrong number of positional arguments, etc.  When it encounters such an error,
it exits and prints the error along with a usage message::

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('--foo', type=int)
   >>> parser.add_argument('bar', nargs='?')

   >>> # invalid type
   >>> parser.parse_args(['--foo', 'spam'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: argument --foo: invalid int value: 'spam'

   >>> # invalid option
   >>> parser.parse_args(['--bar'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: unrecognized arguments: --bar

   >>> # wrong number of arguments
   >>> parser.parse_args(['spam', 'badger'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: unrecognized arguments: badger


Arguments containing ``-``
^^^^^^^^^^^^^^^^^^^^^^^^^^

The :meth:`~ArgumentParser.parse_args` method attempts to give errors whenever
the user has clearly made a mistake, but some situations are inherently
ambiguous.  For example, the command-line argument ``-1`` could either be an
attempt to specify an option or an attempt to provide a positional argument.
The :meth:`~ArgumentParser.parse_args` method is cautious here: positional
arguments may only begin with ``-`` if they look like negative numbers and
there are no options in the parser that look like negative numbers::

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x')
   >>> parser.add_argument('foo', nargs='?')

   >>> # no negative number options, so -1 is a positional argument
   >>> parser.parse_args(['-x', '-1'])
   Namespace(foo=None, x='-1')

   >>> # no negative number options, so -1 and -5 are positional arguments
   >>> parser.parse_args(['-x', '-1', '-5'])
   Namespace(foo='-5', x='-1')

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-1', dest='one')
   >>> parser.add_argument('foo', nargs='?')

   >>> # negative number options present, so -1 is an option
   >>> parser.parse_args(['-1', 'X'])
   Namespace(foo=None, one='X')

   >>> # negative number options present, so -2 is an option
   >>> parser.parse_args(['-2'])
   usage: PROG [-h] [-1 ONE] [foo]
   PROG: error: unrecognized arguments: -2

   >>> # negative number options present, so both -1s are options
   >>> parser.parse_args(['-1', '-1'])
   usage: PROG [-h] [-1 ONE] [foo]
   PROG: error: argument -1: expected one argument

If you have positional arguments that must begin with ``-`` and don't look
like negative numbers, you can insert the pseudo-argument ``'--'`` which tells
:meth:`~ArgumentParser.parse_args` that everything after that is a positional
argument::

   >>> parser.parse_args(['--', '-f'])
   Namespace(foo='-f', one=None)

See also :ref:`the argparse howto on ambiguous arguments <specifying-ambiguous-arguments>`
for more details.

.. versionchanged:: 3.14
   Negative-number matching was expanded to include numbers in scientific
   notation (``-2.5e-6``), numbers containing underscores (``-1_234.5``),
   and complex numbers (``-1.2e-3j``).

.. _prefix-matching:

Argument abbreviations (prefix matching)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :meth:`~ArgumentParser.parse_args` method :ref:`by default <allow_abbrev>`
allows long options to be abbreviated to a prefix, if the abbreviation is
unambiguous (the prefix matches a unique option)::

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-bacon')
   >>> parser.add_argument('-badger')
   >>> parser.parse_args('-bac MMM'.split())
   Namespace(bacon='MMM', badger=None)
   >>> parser.parse_args('-bad WOOD'.split())
   Namespace(bacon=None, badger='WOOD')
   >>> parser.parse_args('-ba BA'.split())
   usage: PROG [-h] [-bacon BACON] [-badger BADGER]
   PROG: error: ambiguous option: -ba could match -badger, -bacon

An error is produced for arguments that could produce more than one options.
This feature can be disabled by setting :ref:`allow_abbrev` to ``False``.

.. _args:

Beyond ``sys.argv``
^^^^^^^^^^^^^^^^^^^

Sometimes it may be useful to have an :class:`ArgumentParser` parse arguments other than those
of :data:`sys.argv`.  This can be accomplished by passing a list of strings to
:meth:`~ArgumentParser.parse_args`.  This is useful for testing at the
interactive prompt::

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument(
   ...     'integers', metavar='int', type=int, choices=range(10),
   ...     nargs='+', help='an integer in the range 0..9')
   >>> parser.add_argument(
   ...     '--sum', dest='accumulate', action='store_const', const=sum,
   ...     default=max, help='sum the integers (default: find the max)')
   >>> parser.parse_args(['1', '2', '3', '4'])
   Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
   >>> parser.parse_args(['1', '2', '3', '4', '--sum'])
   Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])

.. _namespace:

The Namespace object
^^^^^^^^^^^^^^^^^^^^

.. class:: Namespace

   Simple class used by default by :meth:`~ArgumentParser.parse_args` to create
   an object holding attributes and return it.

   This class is deliberately simple, just an :class:`object` subclass with a
   readable string representation. If you prefer to have dict-like view of the
   attributes, you can use the standard Python idiom, :func:`vars`::

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> args = parser.parse_args(['--foo', 'BAR'])
      >>> vars(args)
      {'foo': 'BAR'}

   It may also be useful to have an :class:`ArgumentParser` assign attributes to an
   already existing object, rather than a new :class:`Namespace` object.  This can
   be achieved by specifying the ``namespace=`` keyword argument::

      >>> class C:
      ...     pass
      ...
      >>> c = C()
      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
      >>> c.foo
      'BAR'


Other utilities
---------------

Subcommands
^^^^^^^^^^^^

.. method:: ArgumentParser.add_subparsers(*, [title], [description], [prog], \
                                          [parser_class], [action], \
                                          [dest], [required], \
                                          [help], [metavar])

   Many programs split up their functionality into a number of subcommands,
   for example, the ``svn`` program can invoke subcommands like ``svn
   checkout``, ``svn update``, and ``svn commit``.  Splitting up functionality
   this way can be a particularly good idea when a program performs several
   different functions which require different kinds of command-line arguments.
   :class:`ArgumentParser` supports the creation of such subcommands with the
   :meth:`!add_subparsers` method.  The :meth:`!add_subparsers` method is normally
   called with no arguments and returns a special action object.  This object
   has a single method, :meth:`~_SubParsersAction.add_parser`, which takes a
   command name and any :class:`!ArgumentParser` constructor arguments, and
   returns an :class:`!ArgumentParser` object that can be modified as usual.

   Description of parameters:

   * *title* - title for the sub-parser group in help output; by default
     "subcommands" if description is provided, otherwise uses title for
     positional arguments

   * *description* - description for the sub-parser group in help output, by
     default ``None``

   * *prog* - usage information that will be displayed with subcommand help,
     by default the name of the program and any positional arguments before the
     subparser argument

   * *parser_class* - class which will be used to create sub-parser instances, by
     default the class of the current parser (e.g. :class:`ArgumentParser`)

   * action_ - the basic type of action to be taken when this argument is
     encountered at the command line

   * dest_ - name of the attribute under which subcommand name will be
     stored; by default ``None`` and no value is stored

   * required_ - Whether or not a subcommand must be provided, by default
     ``False`` (added in 3.7)

   * help_ - help for sub-parser group in help output, by default ``None``

   * metavar_ - string presenting available subcommands in help; by default it
     is ``None`` and presents subcommands in form {cmd1, cmd2, ..}

   Some example usage::

     >>> # create the top-level parser
     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> parser.add_argument('--foo', action='store_true', help='foo help')
     >>> subparsers = parser.add_subparsers(help='subcommand help')
     >>>
     >>> # create the parser for the "a" command
     >>> parser_a = subparsers.add_parser('a', help='a help')
     >>> parser_a.add_argument('bar', type=int, help='bar help')
     >>>
     >>> # create the parser for the "b" command
     >>> parser_b = subparsers.add_parser('b', help='b help')
     >>> parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')
     >>>
     >>> # parse some argument lists
     >>> parser.parse_args(['a', '12'])
     Namespace(bar=12, foo=False)
     >>> parser.parse_args(['--foo', 'b', '--baz', 'Z'])
     Namespace(baz='Z', foo=True)

   Note that the object returned by :meth:`~ArgumentParser.parse_args` will only contain
   attributes for the main parser and the subparser that was selected by the
   command line (and not any other subparsers).  So in the example above, when
   the ``a`` command is specified, only the ``foo`` and ``bar`` attributes are
   present, and when the ``b`` command is specified, only the ``foo`` and
   ``baz`` attributes are present.

   If a subparser defines an argument with the same ``dest`` as the parent
   parser, the two share a single namespace attribute, so the parent's value
   won't be retained. Users should give them  distinct ``dest`` values to
   keep both.

   Similarly, when a help message is requested from a subparser, only the help
   for that particular parser will be printed.  The help message will not
   include parent parser or sibling parser messages.  (A help message for each
   subparser command, however, can be given by supplying the ``help=`` argument
   to :meth:`~_SubParsersAction.add_parser` as above.)

   ::

     >>> parser.parse_args(['--help'])
     usage: PROG [-h] [--foo] {a,b} ...

     positional arguments:
       {a,b}   subcommand help
         a     a help
         b     b help

     options:
       -h, --help  show this help message and exit
       --foo   foo help

     >>> parser.parse_args(['a', '--help'])
     usage: PROG a [-h] bar

     positional arguments:
       bar     bar help

     options:
       -h, --help  show this help message and exit

     >>> parser.parse_args(['b', '--help'])
     usage: PROG b [-h] [--baz {X,Y,Z}]

     options:
       -h, --help     show this help message and exit
       --baz {X,Y,Z}  baz help

   The :meth:`~ArgumentParser.add_subparsers` method also supports ``title`` and ``description``
   keyword arguments.  When either is present, the subparser's commands will
   appear in their own group in the help output.  For example::

     >>> parser = argparse.ArgumentParser()
     >>> subparsers = parser.add_subparsers(title='subcommands',
     ...                                    description='valid subcommands',
     ...                                    help='additional help')
     >>> subparsers.add_parser('foo')
     >>> subparsers.add_parser('bar')
     >>> parser.parse_args(['-h'])
     usage:  [-h] {foo,bar} ...

     options:
       -h, --help  show this help message and exit

     subcommands:
       valid subcommands

       {foo,bar}   additional help

   One particularly effective way of handling subcommands is to combine the use
   of the :meth:`~ArgumentParser.add_subparsers` method with calls to :meth:`~ArgumentParser.set_defaults` so
   that each subparser knows which Python function it should execute.  For
   example::

     >>> # subcommand functions
     >>> def foo(args):
     ...     print(args.x * args.y)
     ...
     >>> def bar(args):
     ...     print('((%s))' % args.z)
     ...
     >>> # create the top-level parser
     >>> parser = argparse.ArgumentParser()
     >>> subparsers = parser.add_subparsers(required=True)
     >>>
     >>> # create the parser for the "foo" command
     >>> parser_foo = subparsers.add_parser('foo')
     >>> parser_foo.add_argument('-x', type=int, default=1)
     >>> parser_foo.add_argument('y', type=float)
     >>> parser_foo.set_defaults(func=foo)
     >>>
     >>> # create the parser for the "bar" command
     >>> parser_bar = subparsers.add_parser('bar')
     >>> parser_bar.add_argument('z')
     >>> parser_bar.set_defaults(func=bar)
     >>>
     >>> # parse the args and call whatever function was selected
     >>> args = parser.parse_args('foo 1 -x 2'.split())
     >>> args.func(args)
     2.0
     >>>
     >>> # parse the args and call whatever function was selected
     >>> args = parser.parse_args('bar XYZYX'.split())
     >>> args.func(args)
     ((XYZYX))

   This way, you can let :meth:`~ArgumentParser.parse_args` do the job of calling the
   appropriate function after argument parsing is complete.  Associating
   functions with actions like this is typically the easiest way to handle the
   different actions for each of your subparsers.  However, if it is necessary
   to check the name of the subparser that was invoked, the ``dest`` keyword
   argument to the :meth:`~ArgumentParser.add_subparsers` call will work::

     >>> parser = argparse.ArgumentParser()
     >>> subparsers = parser.add_subparsers(dest='subparser_name')
     >>> subparser1 = subparsers.add_parser('1')
     >>> subparser1.add_argument('-x')
     >>> subparser2 = subparsers.add_parser('2')
     >>> subparser2.add_argument('y')
     >>> parser.parse_args(['2', 'frobble'])
     Namespace(subparser_name='2', y='frobble')

   .. versionchanged:: 3.7
      New *required* keyword-only parameter.

   .. versionchanged:: 3.14
      Subparser's *prog* is no longer affected by a custom usage message in
      the main parser.


.. method:: _SubParsersAction.add_parser(name, *, help=None, aliases=None, \
                                         deprecated=False, **kwargs)

   Create and return a new :class:`ArgumentParser` object for the
   subcommand *name*.

   The *name* argument is the name of the sub-command.

   The *help* argument provides a short description for this sub-command.

   The *aliases* argument allows providing alternative names for this
   sub-command. For example::

      >>> parser = argparse.ArgumentParser()
      >>> subparsers = parser.add_subparsers()
      >>> checkout = subparsers.add_parser('checkout', aliases=['co'])
      >>> checkout.add_argument('foo')
      >>> parser.parse_args(['co', 'bar'])
      Namespace(foo='bar')

   The *deprecated* argument, if ``True``, marks the sub-command as
   deprecated and will issue a warning when used. For example::

      >>> parser = argparse.ArgumentParser(prog='chicken.py')
      >>> subparsers = parser.add_subparsers()
      >>> fly = subparsers.add_parser('fly', deprecated=True)
      >>> args = parser.parse_args(['fly'])
      chicken.py: warning: command 'fly' is deprecated
      Namespace()

   All other keyword arguments are passed directly to the
   :class:`!ArgumentParser` constructor.

   .. versionadded:: 3.13
      Added the *deprecated* parameter.


FileType objects
^^^^^^^^^^^^^^^^

.. class:: FileType(mode='r', bufsize=-1, encoding=None, errors=None)

   The :class:`FileType` factory creates objects that can be passed to the type
   argument of :meth:`ArgumentParser.add_argument`.  Arguments that have
   :class:`FileType` objects as their type will open command-line arguments as
   files with the requested modes, buffer sizes, encodings and error handling
   (see the :func:`open` function for more details)::

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--raw', type=argparse.FileType('wb', 0))
      >>> parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
      >>> parser.parse_args(['--raw', 'raw.dat', 'file.txt'])
      Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<_io.FileIO name='raw.dat' mode='wb'>)

   FileType objects understand the pseudo-argument ``'-'`` and automatically
   convert this into :data:`sys.stdin` for readable :class:`FileType` objects and
   :data:`sys.stdout` for writable :class:`FileType` objects::

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('infile', type=argparse.FileType('r'))
      >>> parser.parse_args(['-'])
      Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)

   .. note::

      If one argument uses *FileType* and then a subsequent argument fails,
      an error is reported but the file is not automatically closed.
      This can also clobber the output files.
      In this case, it would be better to wait until after the parser has
      run and then use the :keyword:`with`-statement to manage the files.

   .. versionchanged:: 3.4
      Added the *encoding* and *errors* parameters.

   .. deprecated:: 3.14


Argument groups
^^^^^^^^^^^^^^^

.. method:: ArgumentParser.add_argument_group(title=None, description=None, *, \
                                              [argument_default], [conflict_handler])

   By default, :class:`ArgumentParser` groups command-line arguments into
   "positional arguments" and "options" when displaying help
   messages. When there is a better conceptual grouping of arguments than this
   default one, appropriate groups can be created using the
   :meth:`!add_argument_group` method::

     >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
     >>> group = parser.add_argument_group('group')
     >>> group.add_argument('--foo', help='foo help')
     >>> group.add_argument('bar', help='bar help')
     >>> parser.print_help()
     usage: PROG [--foo FOO] bar

     group:
       bar    bar help
       --foo FOO  foo help

   The :meth:`add_argument_group` method returns an argument group object which
   has an :meth:`~ArgumentParser.add_argument` method just like a regular
   :class:`ArgumentParser`.  When an argument is added to the group, the parser
   treats it just like a normal argument, but displays the argument in a
   separate group for help messages.  The :meth:`!add_argument_group` method
   accepts *title* and *description* arguments which can be used to
   customize this display::

     >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
     >>> group1 = parser.add_argument_group('group1', 'group1 description')
     >>> group1.add_argument('foo', help='foo help')
     >>> group2 = parser.add_argument_group('group2', 'group2 description')
     >>> group2.add_argument('--bar', help='bar help')
     >>> parser.print_help()
     usage: PROG [--bar BAR] foo

     group1:
       group1 description

       foo    foo help

     group2:
       group2 description

       --bar BAR  bar help

   The optional, keyword-only parameters argument_default_ and conflict_handler_
   allow for finer-grained control of the behavior of the argument group. These
   parameters have the same meaning as in the :class:`ArgumentParser` constructor,
   but apply specifically to the argument group rather than the entire parser.

   Note that any arguments not in your user-defined groups will end up back
   in the usual "positional arguments" and "optional arguments" sections.

   Within each argument group, arguments are displayed in help output in the
   order in which they are added.

   .. deprecated-removed:: 3.11 3.14
      Calling :meth:`add_argument_group` on an argument group now raises an
      exception. This nesting was never supported, often failed to work
      correctly, and was unintentionally exposed through inheritance.

   .. deprecated:: 3.14
      Passing prefix_chars_ to :meth:`add_argument_group`
      is now deprecated.


Mutual exclusion
^^^^^^^^^^^^^^^^

.. method:: ArgumentParser.add_mutually_exclusive_group(required=False)

   Create a mutually exclusive group. :mod:`!argparse` will make sure that only
   one of the arguments in the mutually exclusive group was present on the
   command line::

     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> group = parser.add_mutually_exclusive_group()
     >>> group.add_argument('--foo', action='store_true')
     >>> group.add_argument('--bar', action='store_false')
     >>> parser.parse_args(['--foo'])
     Namespace(bar=True, foo=True)
     >>> parser.parse_args(['--bar'])
     Namespace(bar=False, foo=False)
     >>> parser.parse_args(['--foo', '--bar'])
     usage: PROG [-h] [--foo | --bar]
     PROG: error: argument --bar: not allowed with argument --foo

   The :meth:`add_mutually_exclusive_group` method also accepts a *required*
   argument, to indicate that at least one of the mutually exclusive arguments
   is required::

     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> group = parser.add_mutually_exclusive_group(required=True)
     >>> group.add_argument('--foo', action='store_true')
     >>> group.add_argument('--bar', action='store_false')
     >>> parser.parse_args([])
     usage: PROG [-h] (--foo | --bar)
     PROG: error: one of the arguments --foo --bar is required

   Note that currently mutually exclusive argument groups do not support the
   *title* and *description* arguments of
   :meth:`~ArgumentParser.add_argument_group`. However, a mutually exclusive
   group can be added to an argument group that has a title and description.
   For example::

     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> group = parser.add_argument_group('Group title', 'Group description')
     >>> exclusive_group = group.add_mutually_exclusive_group(required=True)
     >>> exclusive_group.add_argument('--foo', help='foo help')
     >>> exclusive_group.add_argument('--bar', help='bar help')
     >>> parser.print_help()
     usage: PROG [-h] (--foo FOO | --bar BAR)

     options:
       -h, --help  show this help message and exit

     Group title:
       Group description

       --foo FOO   foo help
       --bar BAR   bar help

   .. deprecated-removed:: 3.11 3.14
      Calling :meth:`add_argument_group` or :meth:`add_mutually_exclusive_group`
      on a mutually exclusive group now raises an exception. This nesting was
      never supported, often failed to work correctly, and was unintentionally
      exposed through inheritance.


Parser defaults
^^^^^^^^^^^^^^^

.. method:: ArgumentParser.set_defaults(**kwargs)

   Most of the time, the attributes of the object returned by :meth:`parse_args`
   will be fully determined by inspecting the command-line arguments and the argument
   actions.  :meth:`set_defaults` allows some additional
   attributes that are determined without any inspection of the command line to
   be added::

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('foo', type=int)
     >>> parser.set_defaults(bar=42, baz='badger')
     >>> parser.parse_args(['736'])
     Namespace(bar=42, baz='badger', foo=736)

   Note that defaults can be set at both the parser level using :meth:`set_defaults`
   and at the argument level using :meth:`add_argument`. If both are called for the
   same argument, the last default set for an argument is used::

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', default='bar')
     >>> parser.set_defaults(foo='spam')
     >>> parser.parse_args([])
     Namespace(foo='spam')

   Parser-level defaults can be particularly useful when working with multiple
   parsers.  See the :meth:`~ArgumentParser.add_subparsers` method for an
   example of this type.

.. method:: ArgumentParser.get_default(dest)

   Get the default value for a namespace attribute, as set by either
   :meth:`~ArgumentParser.add_argument` or by
   :meth:`~ArgumentParser.set_defaults`::

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', default='badger')
     >>> parser.get_default('foo')
     'badger'


Printing help
^^^^^^^^^^^^^

In most typical applications, :meth:`~ArgumentParser.parse_args` will take
care of formatting and printing any usage or error messages.  However, several
formatting methods are available:

.. method:: ArgumentParser.print_usage(file=None)

   Print a brief description of how the :class:`ArgumentParser` should be
   invoked on the command line.  If *file* is ``None``, :data:`sys.stdout` is
   assumed.

.. method:: ArgumentParser.print_help(file=None)

   Print a help message, including the program usage and information about the
   arguments registered with the :class:`ArgumentParser`.  If *file* is
   ``None``, :data:`sys.stdout` is assumed.

There are also variants of these methods that simply return a string instead of
printing it:

.. method:: ArgumentParser.format_usage()

   Return a string containing a brief description of how the
   :class:`ArgumentParser` should be invoked on the command line.

.. method:: ArgumentParser.format_help()

   Return a string containing a help message, including the program usage and
   information about the arguments registered with the :class:`ArgumentParser`.


Partial parsing
^^^^^^^^^^^^^^^

.. method:: ArgumentParser.parse_known_args(args=None, namespace=None)

   Sometimes a script only needs to handle a specific set of command-line
   arguments, leaving any unrecognized arguments for another script or program.
   In these cases, the :meth:`~ArgumentParser.parse_known_args` method can be
   useful.

   This method works similarly to :meth:`~ArgumentParser.parse_args`, but it does
   not raise an error for extra, unrecognized arguments. Instead, it parses the
   known arguments and returns a two item tuple that contains the populated
   namespace and the list of any unrecognized arguments.

   ::

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', action='store_true')
      >>> parser.add_argument('bar')
      >>> parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
      (Namespace(bar='BAR', foo=True), ['--badger', 'spam'])

.. warning::
   :ref:`Prefix matching <prefix-matching>` rules apply to
   :meth:`~ArgumentParser.parse_known_args`. The parser may consume an option even if it's just
   a prefix of one of its known options, instead of leaving it in the remaining
   arguments list.


Customizing file parsing
^^^^^^^^^^^^^^^^^^^^^^^^

.. method:: ArgumentParser.convert_arg_line_to_args(arg_line)

   Arguments that are read from a file (see the *fromfile_prefix_chars*
   keyword argument to the :class:`ArgumentParser` constructor) are read one
   argument per line. :meth:`convert_arg_line_to_args` can be overridden for
   fancier reading.

   This method takes a single argument *arg_line* which is a string read from
   the argument file.  It returns a list of arguments parsed from this string.
   The method is called once per line read from the argument file, in order.

   A useful override of this method is one that treats each space-separated word
   as an argument.  The following example demonstrates how to do this::

    class MyArgumentParser(argparse.ArgumentParser):
        def convert_arg_line_to_args(self, arg_line):
            return arg_line.split()

   Note that with this override an argument can no longer contain spaces, since
   each space-separated word becomes a separate argument.


Exiting methods
^^^^^^^^^^^^^^^

.. method:: ArgumentParser.exit(status=0, message=None)

   This method terminates the program, exiting with the specified *status*
   and, if given, it prints a *message* to :data:`sys.stderr` before that.
   The user can override this method to handle these steps differently::

    class ErrorCatchingArgumentParser(argparse.ArgumentParser):
        def exit(self, status=0, message=None):
            if status:
                raise Exception(f'Exiting because of an error: {message}')
            exit(status)

.. method:: ArgumentParser.error(message)

   This method prints a usage message, including the *message*, to
   :data:`sys.stderr` and terminates the program with a status code of 2.


Intermixed parsing
^^^^^^^^^^^^^^^^^^

.. method:: ArgumentParser.parse_intermixed_args(args=None, namespace=None)
.. method:: ArgumentParser.parse_known_intermixed_args(args=None, namespace=None)

   A number of Unix commands allow the user to intermix optional arguments with
   positional arguments.  The :meth:`~ArgumentParser.parse_intermixed_args`
   and :meth:`~ArgumentParser.parse_known_intermixed_args` methods
   support this parsing style.

   These parsers do not support all the :mod:`!argparse` features, and will raise
   exceptions if unsupported features are used.  In particular, subparsers,
   and mutually exclusive groups that include both
   optionals and positionals are not supported.

   The following example shows the difference between
   :meth:`~ArgumentParser.parse_known_args` and
   :meth:`~ArgumentParser.parse_intermixed_args`: the former returns ``['2',
   '3']`` as unparsed arguments, while the latter collects all the positionals
   into ``rest``.  ::

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> parser.add_argument('cmd')
      >>> parser.add_argument('rest', nargs='*', type=int)
      >>> parser.parse_known_args('doit 1 --foo bar 2 3'.split())
      (Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
      >>> parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
      Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])

   :meth:`~ArgumentParser.parse_known_intermixed_args` returns a two item tuple
   containing the populated namespace and the list of remaining argument strings.
   :meth:`~ArgumentParser.parse_intermixed_args` raises an error if there are any
   remaining unparsed argument strings.

   .. versionadded:: 3.7


Registering custom types or actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. method:: ArgumentParser.register(registry_name, value, object)

   Sometimes it's desirable to use a custom string in error messages to provide
   more user-friendly output. In these cases, :meth:`!register` can be used to
   register custom actions or types with a parser and allow you to reference the
   type by their registered name instead of their callable name.

   The :meth:`!register` method accepts three arguments - a *registry_name*,
   specifying the internal registry where the object will be stored (e.g.,
   ``action``, ``type``), *value*, which is the key under which the object will
   be registered, and object, the callable to be registered.

   The following example shows how to register a custom type with a parser::

      >>> import argparse
      >>> parser = argparse.ArgumentParser()
      >>> parser.register('type', 'hexadecimal integer', lambda s: int(s, 16))
      >>> parser.add_argument('--foo', type='hexadecimal integer')
      _StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type='hexadecimal integer', choices=None, required=False, help=None, metavar=None, deprecated=False)
      >>> parser.parse_args(['--foo', '0xFA'])
      Namespace(foo=250)
      >>> parser.parse_args(['--foo', '1.2'])
      usage: PROG [-h] [--foo FOO]
      PROG: error: argument --foo: invalid 'hexadecimal integer' value: '1.2'

Exceptions
----------

.. exception:: ArgumentError

   An error from creating or using an argument (optional or positional).

   The string value of this exception is the message, augmented with
   information about the argument that caused it.

.. exception:: ArgumentTypeError

   Raised when something goes wrong converting a command line string to a type.


.. rubric:: Guides and Tutorials

.. toctree::
   :maxdepth: 1

   ../howto/argparse.rst
   ../howto/argparse-optparse.rst