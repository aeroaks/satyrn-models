|                 | gi_state          | state of the generator,   |
|                 |                   | one of ``GEN_CREATED``,   |
|                 |                   | ``GEN_RUNNING``,          |
|                 |                   | ``GEN_SUSPENDED``, or     |
|                 |                   | ``GEN_CLOSED``            |
+-----------------+-------------------+---------------------------+
| async generator | __name__          | name                      |
+-----------------+-------------------+---------------------------+
|                 | __qualname__      | qualified name            |
+-----------------+-------------------+---------------------------+
|                 | ag_await          | object being awaited on,  |
|                 |                   | or ``None``               |
+-----------------+-------------------+---------------------------+
|                 | ag_frame          | frame                     |
+-----------------+-------------------+---------------------------+
|                 | ag_running        | is the generator running? |
+-----------------+-------------------+---------------------------+
|                 | ag_suspended      | is the generator          |
|                 |                   | suspended?                |
+-----------------+-------------------+---------------------------+
|                 | ag_code           | code                      |
+-----------------+-------------------+---------------------------+
|                 | ag_state          | state of the async        |
|                 |                   | generator, one of         |
|                 |                   | ``AGEN_CREATED``,         |
|                 |                   | ``AGEN_RUNNING``,         |
|                 |                   | ``AGEN_SUSPENDED``, or    |
|                 |                   | ``AGEN_CLOSED``           |
+-----------------+-------------------+---------------------------+
| coroutine       | __name__          | name                      |
+-----------------+-------------------+---------------------------+
|                 | __qualname__      | qualified name            |
+-----------------+-------------------+---------------------------+
|                 | cr_await          | object being awaited on,  |
|                 |                   | or ``None``               |
+-----------------+-------------------+---------------------------+
|                 | cr_frame          | frame                     |
+-----------------+-------------------+---------------------------+
|                 | cr_running        | is the coroutine running? |
+-----------------+-------------------+---------------------------+
|                 | cr_suspended      | is the coroutine          |
|                 |                   | suspended?                |
+-----------------+-------------------+---------------------------+
|                 | cr_code           | code                      |
+-----------------+-------------------+---------------------------+
|                 | cr_origin         | where coroutine was       |
|                 |                   | created, or ``None``. See |
|                 |                   | |coroutine-origin-link|   |
+-----------------+-------------------+---------------------------+
|                 | cr_state          | state of the coroutine,   |
|                 |                   | one of ``CORO_CREATED``,  |
|                 |                   | ``CORO_RUNNING``,         |
|                 |                   | ``CORO_SUSPENDED``, or    |
|                 |                   | ``CORO_CLOSED``           |
+-----------------+-------------------+---------------------------+
| builtin         | __doc__           | documentation string      |
+-----------------+-------------------+---------------------------+
|                 | __name__          | original name of this     |
|                 |                   | function or method        |
+-----------------+-------------------+---------------------------+
|                 | __qualname__      | qualified name            |
+-----------------+-------------------+---------------------------+
|                 | __self__          | instance to which a       |
|                 |                   | method is bound, or       |
|                 |                   | module object a function  |
|                 |                   | was defined in, or        |
|                 |                   | ``None``                  |
+-----------------+-------------------+---------------------------+

.. versionchanged:: 3.5

   Add ``__qualname__`` and ``gi_yieldfrom`` attributes to generators.

   The ``__name__`` attribute of generators is now set from the function
   name, instead of the code name, and it can now be modified.

.. versionchanged:: 3.7

   Add ``cr_origin`` attribute to coroutines.

.. versionchanged:: 3.10

   Add ``__builtins__`` attribute to functions.

.. versionchanged:: 3.11

   Add ``gi_suspended`` attribute to generators.

.. versionchanged:: 3.11

   Add ``cr_suspended`` attribute to coroutines.

.. versionchanged:: 3.12

   Add ``ag_suspended`` attribute to async generators.

.. versionchanged:: 3.14

   Add ``f_generator`` attribute to frames.

.. versionchanged:: 3.15

   Add ``gi_state`` attribute to generators, ``cr_state`` attribute to
   coroutines, and ``ag_state`` attribute to async generators.

.. function:: getmembers(object[, predicate])

   Return all the members of an object in a list of ``(name, value)``
   pairs sorted by name. If the optional *predicate* argument—which will be
   called with the ``value`` object of each member—is supplied, only members
   for which the predicate returns a true value are included.

   .. note::

      :func:`getmembers` will only return class attributes defined in the
      metaclass when the argument is a class and those attributes have been
      listed in the metaclass' custom :meth:`~object.__dir__`.


.. function:: getmembers_static(object[, predicate])

    Return all the members of an object in a list of ``(name, value)``
    pairs sorted by name without triggering dynamic lookup via the descriptor
    protocol, __getattr__ or __getattribute__. Optionally, only return members
    that satisfy a given predicate.

    .. note::

        :func:`getmembers_static` may not be able to retrieve all members
        that getmembers can fetch (like dynamically created attributes)
        and may find members that getmembers can't (like descriptors
        that raise AttributeError). It can also return descriptor objects
        instead of instance members in some cases.

    .. versionadded:: 3.11


.. function:: getmodulename(path)

   Return the name of the module named by the file *path*, without including the
   names of enclosing packages. The file extension is checked against all of
   the entries in :func:`importlib.machinery.all_suffixes`. If it matches,
   the final path component is returned with the extension removed.
   Otherwise, ``None`` is returned.

   Note that this function *only* returns a meaningful name for actual
   Python modules - paths that potentially refer to Python packages will
   still return ``None``.

   .. versionchanged:: 3.3
      The function is based directly on :mod:`importlib`.


.. function:: ismodule(object)

   Return ``True`` if the object is a module.


.. function:: isclass(object)

   Return ``True`` if the object is a class, whether built-in or created in Python
   code.

   This function returns ``False`` for :ref:`generic aliases <types-genericalias>` of classes,
   such as ``list[int]``.


.. function:: ismethod(object)

   Return ``True`` if the object is a bound method written in Python.

   .. note::

      For example, given this class::

          >>> class Greeter:
          ...     def say_hello(self):
          ...         print('hello!')

      A bound method (also known as an *instance method*) is created when
      accessing ``say_hello`` (a :term:`function` defined in the
      ``Greeter`` namespace) through an instance of the ``Greeter`` class::

          >>> instance = Greeter()

          >>> instance.say_hello
          <bound method Greeter.say_hello of <__main__.Greeter object ...>>
          >>> ismethod(instance.say_hello)
          True
          >>> isfunction(instance.say_hello)
          False

      Accessing ``say_hello`` through the ``Greeter`` class will return the
      function itself. For this function, :func:`ismethod` will return
      ``False``, but :func:`isfunction` will return ``True``::

          >>> Greeter.say_hello
          <function Greeter.say_hello at 0x7f7503854a90>
          >>> ismethod(Greeter.say_hello)
          False

----

.. function:: getdoc(object, *, inherit_class_doc=True, fallback_to_class_doc=True)

   Get the documentation string for an object, cleaned up with :func:`cleandoc`.
   If the documentation string for an object is not provided:

   * if the object is a class and *inherit_class_doc* is true (by default),
     retrieve the documentation string from the inheritance hierarchy;
   * if the object is a method, a property or a descriptor, retrieve
     the documentation string from the inheritance hierarchy;
   * otherwise, if *fallback_to_class_doc* is true (by default), retrieve
     the documentation string from the class of the object.

   Return ``None`` if the documentation string is invalid or missing.

   .. versionchanged:: 3.5
      Documentation strings are now inherited if not overridden.

   .. versionchanged:: 3.15
      Added parameters *inherit_class_doc* and *fallback_to_class_doc*.

      Documentation strings on :class:`~functools.cached_property`
      objects are now inherited if not overridden.



----

.. function:: getfullargspec(func, *, annotation_format=Format.VALUE)

   Get the names and default values of a Python function's parameters.  A
   :term:`named tuple` is returned:

   ``FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults,
   annotations)``

   *args* is a list of the positional parameter names.
   *varargs* is the name of the ``*`` parameter or ``None`` if arbitrary
   positional arguments are not accepted.
   *varkw* is the name of the ``**`` parameter or ``None`` if arbitrary
   keyword arguments are not accepted.
   *defaults* is an *n*-tuple of default argument values corresponding to the
   last *n* positional parameters, or ``None`` if there are no such defaults
   defined.
   *kwonlyargs* is a list of keyword-only parameter names in declaration order.
   *kwonlydefaults* is a dictionary mapping parameter names from *kwonlyargs*
   to the default values used if no argument is supplied.
   *annotations* is a dictionary mapping parameter names to annotations.
   The special key ``"return"`` is used to report the function return value
   annotation (if any).

   Note that :func:`signature` and
   :ref:`Signature Object <inspect-signature-object>` provide the recommended
   API for callable introspection, and support additional behaviours (like
   positional-only arguments) that are sometimes encountered in extension module
   APIs. This function is retained primarily for use in code that needs to
   maintain compatibility with the Python 2 ``inspect`` module API.

   A member of the
   :class:`annotationlib.Format` enum can be passed to the
   *annotation_format* parameter to control the format of the returned
   annotations. For example, use
   ``annotation_format=annotationlib.Format.STRING`` to return annotations in string
   format. Note that with the default ``VALUE`` format, creation of some argspecs
   may raise an exception.

   .. versionchanged:: 3.4
      This function is now based on :func:`signature`, but still ignores
      ``__wrapped__`` attributes and includes the already bound first
      parameter in the signature output for bound methods.

   .. versionchanged:: 3.6
      This method was previously documented as deprecated in favour of
      :func:`signature` in Python 3.5, but that decision has been reversed
      in order to restore a clearly supported standard interface for
      single-source Python 2/3 code migrating away from the legacy
      :func:`!getargspec` API.

   .. versionchanged:: 3.7
      Python only explicitly guaranteed that it preserved the declaration
      order of keyword-only parameters as of version 3.7, although in practice
      this order had always been preserved in Python 3.

   .. versionchanged:: 3.15
      The *annotation_format* parameter was added.



----

Command-line interface
----------------------

The :mod:`!inspect` module also provides a basic introspection capability
from the command line.

.. program:: inspect

By default, accepts the name of a module and prints the source of that
module. A class or function within the module can be printed instead by
appending a colon and the qualified name of the target object.

.. option:: --details

   Print information about the specified object rather than the source code

.. versionchanged:: 3.15

   The ``--details`` option now supports basic introspection for modules
   without available source code and indicates when modules are frozen.
   It also indicates when the given target reference is not the canonical
   name of the referenced object.