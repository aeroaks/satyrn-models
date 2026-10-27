Lazy imports
------------

.. index::
   pair: lazy; import
   single: lazy import

The :keyword:`lazy` keyword is a :ref:`soft keyword <soft-keywords>` that
only has special meaning when it appears immediately before an
:keyword:`import` or :keyword:`from` statement. When an import statement is
preceded by the :keyword:`lazy` keyword, the import becomes *lazy*: the
module is not loaded immediately at the import statement. Instead, a lazy
proxy object is created and bound to the name. The actual module is loaded
on first use of that name.

Lazy imports are only permitted at module scope. Using :keyword:`lazy`
inside a function, class body, or
:keyword:`try`/:keyword:`except`/:keyword:`finally` block raises a
:exc:`SyntaxError`. Star imports cannot be lazy (``lazy from module import
*`` is a syntax error), and :ref:`future statements <future>` cannot be
lazy.

When using ``lazy from ... import``, each imported name is bound to a lazy
proxy object. The first access to any of these names triggers loading of the
entire module and resolves only that specific name to its actual value.
Other names remain as lazy proxies until they are accessed.

Example::

   lazy import json
   import sys

   print('json' in sys.modules)  # False - json module not yet loaded

   # First use triggers loading
   result = json.dumps({"hello": "world"})

   print('json' in sys.modules)  # True - now loaded

If an error occurs during module loading (such as :exc:`ImportError` or
:exc:`SyntaxError`), it is raised at the point where the lazy import is first
used, not at the import statement itself.

See :pep:`810` for the full specification of lazy imports.

.. versionadded:: 3.15

.. _lazy-modules-compat:

Compatibility via ``__lazy_modules__``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: __lazy_modules__

As an alternative to using the :keyword:`lazy` keyword, a module can opt
into lazy loading for specific imports by defining a module-level
:attr:`~module.__lazy_modules__` variable.  When present, it must be a
container of fully qualified module name strings.  Any regular (non-``lazy``)
:keyword:`import` statement at module scope whose target appears in
:attr:`!__lazy_modules__` is treated as a lazy import, exactly as if the
:keyword:`lazy` keyword had been used.

This provides a way to enable lazy loading for specific dependencies without
changing individual ``import`` statements. This is useful when supporting
Python versions older than 3.15 while using lazy imports in 3.15+::

   __lazy_modules__ = ["json", "pathlib"]

   import json     # loaded lazily (name is in __lazy_modules__)
   import os       # loaded eagerly (name not in __lazy_modules__)

   import pathlib  # loaded lazily

Relative imports are resolved to their absolute name before the lookup, so
:attr:`!__lazy_modules__` must always contain fully qualified module names.

For ``from``-style imports, the relevant name is the module following
``from``, not the names of its members::

   # In mypackage/mymodule.py
   __lazy_modules__ = ["mypackage", "mypackage.sub.utils"]

   from . import helper         # loaded lazily: . resolves to mypackage
   from .sub.utils import func  # loaded lazily: .sub.utils resolves to mypackage.sub.utils
   import json                  # loaded eagerly (not in __lazy_modules__)

Imports inside functions, class bodies, or
:keyword:`try`/:keyword:`except`/:keyword:`finally` blocks are always eager,
regardless of :attr:`!__lazy_modules__`.

.. versionadded:: 3.15

.. _future:


----

Compatibility via ``__lazy_modules__``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: __lazy_modules__

As an alternative to using the :keyword:`lazy` keyword, a module can opt
into lazy loading for specific imports by defining a module-level
:attr:`~module.__lazy_modules__` variable.  When present, it must be a
container of fully qualified module name strings.  Any regular (non-``lazy``)
:keyword:`import` statement at module scope whose target appears in
:attr:`!__lazy_modules__` is treated as a lazy import, exactly as if the
:keyword:`lazy` keyword had been used.

This provides a way to enable lazy loading for specific dependencies without
changing individual ``import`` statements. This is useful when supporting
Python versions older than 3.15 while using lazy imports in 3.15+::

   __lazy_modules__ = ["json", "pathlib"]

   import json     # loaded lazily (name is in __lazy_modules__)
   import os       # loaded eagerly (name not in __lazy_modules__)

   import pathlib  # loaded lazily

Relative imports are resolved to their absolute name before the lookup, so
:attr:`!__lazy_modules__` must always contain fully qualified module names.

For ``from``-style imports, the relevant name is the module following
``from``, not the names of its members::

   # In mypackage/mymodule.py
   __lazy_modules__ = ["mypackage", "mypackage.sub.utils"]

   from . import helper         # loaded lazily: . resolves to mypackage
   from .sub.utils import func  # loaded lazily: .sub.utils resolves to mypackage.sub.utils
   import json                  # loaded eagerly (not in __lazy_modules__)

Imports inside functions, class bodies, or
:keyword:`try`/:keyword:`except`/:keyword:`finally` blocks are always eager,
regardless of :attr:`!__lazy_modules__`.

.. versionadded:: 3.15

.. _future:

Future statements
-----------------

.. index::
   pair: future; statement
   single: __future__; future statement

A :dfn:`future statement` is a directive to the compiler that a particular
module should be compiled using syntax or semantics that will be available in a
specified future release of Python where the feature becomes standard.

The future statement is intended to ease migration to future versions of Python
that introduce incompatible changes to the language.  It allows use of the new
features on a per-module basis before the release in which the feature becomes
standard.

.. productionlist:: python-grammar
   future_stmt: "from" "__future__" "import" `feature` ["as" `identifier`]
              : ("," `feature` ["as" `identifier`])*
              : | "from" "__future__" "import" "(" `feature` ["as" `identifier`]
              : ("," `feature` ["as" `identifier`])* [","] ")"
   feature: `identifier`

A future statement must appear near the top of the module.  The only lines that
can appear before a future statement are:

* the module docstring (if any),
* comments,
* blank lines, and
* other future statements.

The only feature that requires using the future statement is
``annotations`` (see :pep:`563`).

All historical features enabled by the future statement are still recognized
by Python 3.  The list includes ``absolute_import``, ``division``,
``generators``, ``generator_stop``, ``unicode_literals``,
``print_function``, ``nested_scopes`` and ``with_statement``.  They are
all redundant because they are always enabled, and only kept for
backwards compatibility.

A future statement is recognized and treated specially at compile time: Changes
to the semantics of core constructs are often implemented by generating
different code.  It may even be the case that a new feature introduces new
incompatible syntax (such as a new reserved word), in which case the compiler
may need to parse the module differently.  Such decisions cannot be pushed off
until runtime.

For any given release, the compiler knows which feature names have been defined,
and raises a compile-time error if a future statement contains a feature not
known to it.

The direct runtime semantics are the same as for any import statement: there is
a standard module :mod:`__future__`, described later, and it will be imported in
the usual way at the time the future statement is executed.

The interesting runtime semantics depend on the specific feature enabled by the
future statement.

Note that there is nothing special about the statement::

   import __future__ [as name]

That is not a future statement; it's an ordinary import statement with no
special semantics or syntax restrictions.

Code compiled by calls to the built-in functions :func:`exec` and :func:`compile`
that occur in a module :mod:`!M` containing a future statement will, by default,
use the new syntax or semantics associated with the future statement.  This can
be controlled by optional arguments to :func:`compile` --- see the documentation
of that function for details.

A future statement typed at an interactive interpreter prompt will take effect
for the rest of the interpreter session.  If an interpreter is started with the
:option:`-i` option, is passed a script name to execute, and the script includes
a future statement, it will be in effect in the interactive session started
after the script is executed.

.. seealso::

   :pep:`236` - Back to the __future__
      The original proposal for the __future__ mechanism.


.. _global:

The :keyword:`!global` statement
================================

.. index::
   ! pair: statement; global
   triple: global; name; binding
   single: , (comma); identifier list

.. productionlist:: python-grammar
   global_stmt: "global" `identifier` ("," `identifier`)*

The :keyword:`global` statement causes the listed identifiers to be interpreted
as globals. It would be impossible to assign to a global variable without
:keyword:`!global`, although free variables may refer to globals without being
declared global.

The :keyword:`!global` statement applies to the entire current scope
(module, function body or class definition).
A :exc:`SyntaxError` is raised if a variable is used or
assigned to prior to its global declaration in the scope.

At the module level, all variables are global, so a :keyword:`!global`
statement has no effect.
However, variables must still not be used or
assigned to prior to their :keyword:`!global` declaration.
This requirement is relaxed in the interactive prompt (:term:`REPL`).

.. index::
   pair: built-in function; exec
   pair: built-in function; eval
   pair: built-in function; compile

**Programmer's note:** :keyword:`global` is a directive to the parser.  It
applies only to code parsed at the same time as the :keyword:`!global` statement.
In particular, a :keyword:`!global` statement contained in a string or code
object supplied to the built-in :func:`exec` function does not affect the code
block *containing* the function call, and code contained in such a string is
unaffected by :keyword:`!global` statements in the code containing the function
call.  The same applies to the :func:`eval` and :func:`compile` functions.


.. _nonlocal:

The :keyword:`!nonlocal` statement
==================================

.. index:: pair: statement; nonlocal
   single: , (comma); identifier list

.. productionlist:: python-grammar
   nonlocal_stmt: "nonlocal" `identifier` ("," `identifier`)*

When the definition of a function or class is nested (enclosed) within
the definitions of other functions, its nonlocal scopes are the local
scopes of the enclosing functions. The :keyword:`nonlocal` statement
causes the listed identifiers to refer to names previously bound in
nonlocal scopes. It allows encapsulated code to rebind such nonlocal
identifiers.  If a name is bound in more than one nonlocal scope, the
nearest binding is used. If a name is not bound in any nonlocal scope,
or if there is no nonlocal scope, a :exc:`SyntaxError` is raised.

The :keyword:`nonlocal` statement applies to the entire scope of a function or
class body. A :exc:`SyntaxError` is raised if a variable is used or
assigned to prior to its nonlocal declaration in the scope.

.. seealso::

   :pep:`3104` - Access to Names in Outer Scopes
      The specification for the :keyword:`nonlocal` statement.

**Programmer's note:** :keyword:`nonlocal` is a directive to the parser
and applies only to code parsed along with it.  See the note for the
:keyword:`global` statement.


.. _type:

The :keyword:`!type` statement
==============================

.. index:: pair: statement; type

.. productionlist:: python-grammar
   type_stmt: 'type' `identifier` [`type_params`] "=" `expression`

The :keyword:`!type` statement declares a type alias, which is an instance
of :class:`typing.TypeAliasType`.

For example, the following statement creates a type alias::

   type Point = tuple[float, float]

This code is roughly equivalent to::

   annotation-def VALUE_OF_Point():
       return tuple[float, float]
   Point = typing.TypeAliasType("Point", VALUE_OF_Point())

``annotation-def`` indicates an :ref:`annotation scope <annotation-scopes>`, which behaves
mostly like a function, but with several small differences.

The value of the
type alias is evaluated in the annotation scope. It is not evaluated when the
type alias is created, but only when the value is accessed through the type alias's
:attr:`!__value__` attribute (see :ref:`lazy-evaluation`).
This allows the type alias to refer to names that are not yet defined.

Type aliases may be made generic by adding a :ref:`type parameter list <type-params>`
after the name. See :ref:`generic-type-aliases` for more.

:keyword:`!type` is a :ref:`soft keyword <soft-keywords>`.

.. versionadded:: 3.12

.. seealso::

   :pep:`695` - Type Parameter Syntax
      Introduced the :keyword:`!type` statement and syntax for
      generic classes and functions.