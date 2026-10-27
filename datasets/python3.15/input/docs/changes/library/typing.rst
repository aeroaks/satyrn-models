.. data:: TypeForm

   A special form representing the value that results from evaluating a
   type expression.

   This value encodes the information supplied in the type expression, and
   it represents the type described by that type expression.

   When used in a type expression, ``TypeForm`` describes a set of type form
   objects. It accepts a single type argument, which must be a valid type
   expression. ``TypeForm[T]`` describes the set of all type form objects that
   represent the type ``T`` or types assignable to ``T``.

   ``TypeForm(obj)`` simply returns ``obj`` unchanged. This is useful for
   explicitly marking a value as a type form for static type checkers.

   Example::

      from typing import Any, TypeForm

      def cast[T](typ: TypeForm[T], value: Any) -> T: ...

      reveal_type(cast(int, "x"))  # Revealed type is "int"

   See :pep:`747` for details.

   .. versionadded:: 3.15



----

   .. attribute:: __covariant__

      Whether the type variable tuple has been explicitly marked as covariant.

      .. versionadded:: 3.15


----

   .. attribute:: __contravariant__

      Whether the type variable tuple has been explicitly marked as contravariant.

      .. versionadded:: 3.15


----

   .. attribute:: __infer_variance__

      Whether the type variable tuple's variance should be inferred by type checkers.

      .. versionadded:: 3.15


----

.. class:: TypeVarTuple(name, *, bound=None, covariant=False, contravariant=False, infer_variance=False, default=typing.NoDefault)

   Type variable tuple. A specialized form of :ref:`type variable <typevar>`
   that enables *variadic* generics.

   Type variable tuples can be declared in :ref:`type parameter lists <type-params>`
   using a single asterisk (``*``) before the name::

      def move_first_element_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
          return (*tup[1:], tup[0])

   Or by explicitly invoking the ``TypeVarTuple`` constructor::

      T = TypeVar("T")
      Ts = TypeVarTuple("Ts")

      def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
          return (*tup[1:], tup[0])

   A normal type variable enables parameterization with a single type. A type
   variable tuple, in contrast, allows parameterization with an
   *arbitrary* number of types by acting like an *arbitrary* number of type
   variables wrapped in a tuple. For example::

      # T is bound to int, Ts is bound to ()
      # Return value is (1,), which has type tuple[int]
      move_first_element_to_last(tup=(1,))

      # T is bound to int, Ts is bound to (str,)
      # Return value is ('spam', 1), which has type tuple[str, int]
      move_first_element_to_last(tup=(1, 'spam'))

      # T is bound to int, Ts is bound to (str, float)
      # Return value is ('spam', 3.0, 1), which has type tuple[str, float, int]
      move_first_element_to_last(tup=(1, 'spam', 3.0))

      # This fails to type check (and fails at runtime)
      # because tuple[()] is not compatible with tuple[T, *Ts]
      # (at least one element is required)
      move_first_element_to_last(tup=())

   Note the use of the unpacking operator ``*`` in ``tuple[T, *Ts]``.
   Conceptually, you can think of ``Ts`` as a tuple of type variables
   ``(T1, T2, ...)``. ``tuple[T, *Ts]`` would then become
   ``tuple[T, *(T1, T2, ...)]``, which is equivalent to
   ``tuple[T, T1, T2, ...]``. (Note that in older versions of Python, you might
   see this written using :data:`Unpack <Unpack>` instead, as
   ``Unpack[Ts]``.)

   Type variable tuples must *always* be unpacked. This helps distinguish type
   variable tuples from normal type variables::

      x: Ts          # Not valid
      x: tuple[Ts]   # Not valid
      x: tuple[*Ts]  # The correct way to do it

   Type variable tuples can be used in the same contexts as normal type
   variables. For example, in class definitions, arguments, and return types::

      class Array[*Shape]:
          def __getitem__(self, key: tuple[*Shape]) -> float: ...
          def __abs__(self) -> "Array[*Shape]": ...
          def get_shape(self) -> tuple[*Shape]: ...

   Type variable tuples can be happily combined with normal type variables:

   .. testcode::

      class Array[DType, *Shape]:  # This is fine
          pass

      class Array2[*Shape, DType]:  # This would also be fine
          pass

      class Height: ...
      class Width: ...

      float_array_1d: Array[float, Height] = Array()     # Totally fine
      int_array_2d: Array[int, Height, Width] = Array()  # Yup, fine too

   However, note that at most one type variable tuple may appear in a single
   list of type arguments or type parameters::

      x: tuple[*Ts, *Ts]            # Not valid
      class Array[*Shape, *Shape]:  # Not valid
          pass

   Finally, an unpacked type variable tuple can be used as the type annotation
   of ``*args``::

      def call_soon[*Ts](
          callback: Callable[[*Ts], None],
          *args: *Ts
      ) -> None:
          ...
          callback(*args)

   In contrast to non-unpacked annotations of ``*args`` - e.g. ``*args: int``,
   which would specify that *all* arguments are ``int`` - ``*args: *Ts``
   enables reference to the types of the *individual* arguments in ``*args``.
   Here, this allows us to ensure the types of the ``*args`` passed
   to ``call_soon`` match the types of the (positional) arguments of
   ``callback``.

   See :pep:`646` for more details on type variable tuples.

   .. attribute:: __name__

      The name of the type variable tuple.

   .. attribute:: __covariant__

      Whether the type variable tuple has been explicitly marked as covariant.

      .. versionadded:: 3.15

   .. attribute:: __contravariant__

      Whether the type variable tuple has been explicitly marked as contravariant.

      .. versionadded:: 3.15

   .. attribute:: __infer_variance__

      Whether the type variable tuple's variance should be inferred by type checkers.

      .. versionadded:: 3.15

   .. attribute:: __default__

      The default value of the type variable tuple, or :data:`typing.NoDefault` if it
      has no default.

      .. versionadded:: 3.13

   .. method:: evaluate_default

      An :term:`evaluate function` corresponding to the :attr:`~TypeVarTuple.__default__` attribute.
      When called directly, this method supports only the :attr:`~annotationlib.Format.VALUE`
      format, which is equivalent to accessing the :attr:`~TypeVarTuple.__default__` attribute directly,
      but the method object can be passed to :func:`annotationlib.call_evaluate_function`
      to evaluate the value in a different format.

      .. versionadded:: 3.14

   .. method:: has_default()

      Return whether or not the type variable tuple has a default value. This is equivalent
      to checking whether :attr:`__default__` is not the :data:`typing.NoDefault`
      singleton, except that it does not force evaluation of the
      :ref:`lazily evaluated <lazy-evaluation>` default value.

      .. versionadded:: 3.13

   Type variable tuples created with ``covariant=True`` or
   ``contravariant=True`` can be used to declare covariant or contravariant
   generic types.  The ``bound`` argument is also accepted, similar to
   :class:`TypeVar`, but its actual semantics are yet to be decided.

   .. versionadded:: 3.11

   .. versionchanged:: 3.12

      Type variable tuples can now be declared using the
      :ref:`type parameter <type-params>` syntax introduced by :pep:`695`.

   .. versionchanged:: 3.13

      Support for default values was added.

   .. versionchanged:: 3.15

      Added support for the ``bound``, ``covariant``, ``contravariant``, and
      ``infer_variance`` parameters.


----

   .. attribute:: __qualname__

      The :term:`qualified name` of the type alias:

      .. doctest::

        >>> class Class:
        ...     type Alias = int
        ...
        >>> Class.Alias.__qualname__
        'Class.Alias'

      .. versionadded:: 3.15


----

   .. attribute:: __module__

      The name of the module in which the type alias was defined::

         >>> type Alias = int
         >>> Alias.__module__
         '__main__'

      This attribute is writable.

      .. versionchanged:: 3.15

         The attribute is now writable.


----

.. class:: Protocol(Generic)

   Base class for protocol classes.

   Protocol classes are defined like this::

      class Proto(Protocol):
          def meth(self) -> int:
              ...

   Such classes are primarily used with static type checkers that recognize
   structural subtyping (static duck-typing), for example::

      class C:
          def meth(self) -> int:
              return 0

      def func(x: Proto) -> int:
          return x.meth()

      func(C())  # Passes static type check

   See :pep:`544` for more details. Protocol classes decorated with
   :deco:`runtime_checkable` (described later) act as simple-minded runtime
   protocols that check only the presence of given attributes, ignoring their
   type signatures. Protocol classes without this decorator cannot be used
   as the second argument to :func:`isinstance` or :func:`issubclass`.

   Protocol classes can be generic, for example::

      class GenProto[T](Protocol):
          def meth(self) -> T:
              ...

   In code that needs to be compatible with Python 3.11 or older, generic
   Protocols can be written as follows::

      T = TypeVar("T")

      class GenProto(Protocol[T]):
          def meth(self) -> T:
              ...

   .. versionadded:: 3.8

   .. deprecated-removed:: 3.15 3.20
      It is deprecated to call :func:`isinstance` and :func:`issubclass` checks on
      protocol classes that were not explicitly decorated with :func:`!runtime_checkable`
      but that inherit from a runtime-checkable protocol class. This will throw
      a :exc:`TypeError` in Python 3.20.


----

.. decorator:: runtime_checkable

   Mark a protocol class as a runtime protocol.

   Such a protocol can be used with :func:`isinstance` and :func:`issubclass`.
   This allows a simple-minded structural check, very similar to "one-trick ponies"
   in :mod:`collections.abc` such as :class:`~collections.abc.Iterable`.  For example::

      @runtime_checkable
      class Closable(Protocol):
          def close(self): ...

      assert isinstance(open('/some/file'), Closable)

      @runtime_checkable
      class Named(Protocol):
          name: str

      import threading
      assert isinstance(threading.Thread(name='Bob'), Named)

   Runtime checkability of protocols is not inherited. A subclass of a runtime-checkable protocol
   is only runtime-checkable if it is explicitly marked as such, regardless of class hierarchy::

      @runtime_checkable
      class Iterable(Protocol):
          def __iter__(self): ...

      # Without @runtime_checkable, Reversible would no longer be runtime-checkable.
      @runtime_checkable
      class Reversible(Iterable, Protocol):
          def __reversed__(self): ...

   This decorator raises :exc:`TypeError` when applied to a non-protocol class.

   .. note::

        :deco:`!runtime_checkable` will check only the presence of the required
        methods or attributes, not their type signatures or types.
        For example, :class:`ssl.SSLObject`
        is a class, therefore it passes an :func:`issubclass`
        check against :ref:`Callable <annotating-callables>`. However, the
        ``ssl.SSLObject.__init__`` method exists only to raise a
        :exc:`TypeError` with a more informative message, therefore making
        it impossible to call (instantiate) :class:`ssl.SSLObject`.

   .. note::

        An :func:`isinstance` check against a runtime-checkable protocol can be
        surprisingly slow compared to an ``isinstance()`` check against
        a non-protocol class. Consider using alternative idioms such as
        :func:`hasattr` calls for structural checks in performance-sensitive
        code.

   .. versionadded:: 3.8

   .. versionchanged:: 3.12
      The internal implementation of :func:`isinstance` checks against
      runtime-checkable protocols now uses :func:`inspect.getattr_static`
      to look up attributes (previously, :func:`hasattr` was used).
      As a result, some objects which used to be considered instances
      of a runtime-checkable protocol may no longer be considered instances
      of that protocol on Python 3.12+, and vice versa.
      Most users are unlikely to be affected by this change.

   .. versionchanged:: 3.12
      The members of a runtime-checkable protocol are now considered "frozen"
      at runtime as soon as the class has been created. Monkey-patching
      attributes onto a runtime-checkable protocol will still work, but will
      have no impact on :func:`isinstance` checks comparing objects to the
      protocol. See :ref:`What's new in Python 3.12 <whatsnew-typing-py312>`
      for more details.

   .. deprecated-removed:: 3.15 3.20
      It is deprecated to call :func:`isinstance` and :func:`issubclass` checks on
      protocol classes that were not explicitly decorated with :func:`!runtime_checkable`
      but that inherit from a runtime-checkable protocol class. This will throw
      a :exc:`TypeError` in Python 3.20.


----

.. class:: TypedDict(dict)

   Special construct to add type hints to a dictionary.
   At runtime ":class:`!TypedDict` instances" are simply :class:`dicts <dict>`.

   ``TypedDict`` declares a dictionary type that expects all of its
   instances to have a certain set of keys, where each key is
   associated with a value of a consistent type. This expectation
   is not checked at runtime but is only enforced by type checkers.
   Usage::

      class Point2D(TypedDict):
          x: int
          y: int
          label: str

      a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
      b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

      assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

   An alternative way to create a ``TypedDict`` is by using
   function-call syntax. The second argument must be a literal :class:`dict`::

      Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})

   This functional syntax allows defining keys which are not valid
   :ref:`identifiers <identifiers>`, for example because they are
   keywords or contain hyphens, or when key names must not be
   :ref:`mangled <private-name-mangling>` like regular private names::

      # raises SyntaxError
      class Point2D(TypedDict):
          in: int  # 'in' is a keyword
          x-y: int  # name with hyphens

      class Definition(TypedDict):
          __schema: str  # mangled to `_Definition__schema`

      # OK, functional syntax
      Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
      Definition = TypedDict('Definition', {'__schema': str})  # not mangled

   By default, all keys must be present in a ``TypedDict``. It is possible to
   mark individual keys as non-required using :data:`NotRequired`::

      class Point2D(TypedDict):
          x: int
          y: int
          label: NotRequired[str]

      # Alternative syntax
      Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': NotRequired[str]})

   This means that a ``Point2D`` ``TypedDict`` can have the ``label``
   key omitted.

   It is also possible to mark all keys as non-required by default
   by specifying a totality of ``False``::

      class Point2D(TypedDict, total=False):
          x: int
          y: int

      # Alternative syntax
      Point2D = TypedDict('Point2D', {'x': int, 'y': int}, total=False)

   This means that a ``Point2D`` ``TypedDict`` can have any of the keys
   omitted. A type checker is only expected to support a literal ``False`` or
   ``True`` as the value of the ``total`` argument. ``True`` is the default,
   and makes all items defined in the class body required.

   Individual keys of a ``total=False`` ``TypedDict`` can be marked as
   required using :data:`Required`::

      class Point2D(TypedDict, total=False):
          x: Required[int]
          y: Required[int]
          label: str

      # Alternative syntax
      Point2D = TypedDict('Point2D', {
          'x': Required[int],
          'y': Required[int],
          'label': str
      }, total=False)

   It is possible for a ``TypedDict`` type to inherit from one or more other ``TypedDict`` types
   using the class-based syntax.
   Usage::

      class Point3D(Point2D):
          z: int

   ``Point3D`` has three items: ``x``, ``y`` and ``z``. It is equivalent to this
   definition::

      class Point3D(TypedDict):
          x: int
          y: int
          z: int

   By default, a ``TypedDict`` is open, meaning that it may contain additional keys
   at runtime beyond those defined in the class body. The *closed* class argument can
   be used to control this; if ``closed=True``, the ``TypedDict`` cannot contain additional keys.

   ::

      class ClosedPoint(TypedDict, closed=True):
          x: int
          y: int

      class ClosedPoint3D(ClosedPoint):  # type checker error: cannot add keys to a closed TypedDict
          z: int

   Setting ``closed=False`` explicitly requests the default open behavior. If the argument is not
   passed, this state is inherited from the parent class.

   In addition to being open or closed, a ``TypedDict`` can also be configured to have extra items.
   If the *extra_items* class argument is set to a type, the ``TypedDict`` can contain arbitrary
   additional keys, but the values of those keys must be of the specified type.

   ::

      class ExtraItemsPoint(TypedDict, extra_items=int):
          x: int
          y: int

      point: ExtraItemsPoint = {'x': 1, 'y': 2, 'anything': 3}  # OK

   The *extra_items* argument is also inherited through subclassing. It is unset
   by default, and it may not be used together with the *closed* argument.

   A ``TypedDict`` cannot inherit from a non-\ ``TypedDict`` class,
   except for :class:`Generic`. For example::

      class X(TypedDict):
          x: int

      class Y(TypedDict):
          y: int

      class Z(object): pass  # A non-TypedDict class

      class XY(X, Y): pass  # OK

      class XZ(X, Z): pass  # raises TypeError

   A ``TypedDict`` can be generic::

      class Group[T](TypedDict):
          key: T
          group: list[T]

   To create a generic ``TypedDict`` that is compatible with Python 3.11
   or lower, inherit from :class:`Generic` explicitly:

   .. testcode::

      T = TypeVar("T")

      class Group(TypedDict, Generic[T]):
          key: T
          group: list[T]

   A ``TypedDict`` can be introspected via :func:`annotationlib.get_annotations`
   (see :ref:`annotations-howto` for more information on annotations best practices)
   and the following attributes:

   .. attribute:: __total__

      ``Point2D.__total__`` gives the value of the ``total`` argument.
      Example:

      .. doctest::

         >>> from typing import TypedDict
         >>> class Point2D(TypedDict): pass
         >>> Point2D.__total__
         True
         >>> class Point2D(TypedDict, total=False): pass
         >>> Point2D.__total__
         False
         >>> class Point3D(Point2D): pass
         >>> Point3D.__total__
         True

      This attribute reflects *only* the value of the ``total`` argument
      to the current ``TypedDict`` class, not whether the class is semantically
      total. For example, a ``TypedDict`` with ``__total__`` set to ``True`` may
      have keys marked with :data:`NotRequired`, or it may inherit from another
      ``TypedDict`` with ``total=False``. Therefore, it is generally better to use
      :attr:`__required_keys__` and :attr:`__optional_keys__` for introspection.

   .. attribute:: __required_keys__

      .. versionadded:: 3.9

   .. attribute:: __optional_keys__

      ``Point2D.__required_keys__`` and ``Point2D.__optional_keys__`` return
      :class:`frozenset` objects containing required and non-required keys, respectively.

      Keys marked with :data:`Required` will always appear in ``__required_keys__``
      and keys marked with :data:`NotRequired` will always appear in ``__optional_keys__``.

      For backwards compatibility with Python 3.10 and below,
      it is also possible to use inheritance to declare both required and
      non-required keys in the same ``TypedDict``. This is done by declaring a
      ``TypedDict`` with one value for the ``total`` argument and then
      inheriting from it in another ``TypedDict`` with a different value for
      ``total``:

      .. doctest::

         >>> class Point2D(TypedDict, total=False):
         ...     x: int
         ...     y: int
         ...
         >>> class Point3D(Point2D):
         ...     z: int
         ...
         >>> Point3D.__required_keys__ == frozenset({'z'})
         True
         >>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
         True

      .. versionadded:: 3.9

      .. note::

         If ``from __future__ import annotations`` is used or if annotations
         are given as strings, annotations are not evaluated when the
         ``TypedDict`` is defined. Therefore, the runtime introspection that
         ``__required_keys__`` and ``__optional_keys__`` rely on may not work
         properly, and the values of the attributes may be incorrect.

   .. attribute:: __readonly_keys__

      A :class:`frozenset` containing the names of all read-only keys. Keys
      are read-only if they carry the :data:`ReadOnly` qualifier.

      .. versionadded:: 3.13

   .. attribute:: __mutable_keys__

      A :class:`frozenset` containing the names of all mutable keys. Keys
      are mutable if they do not carry the :data:`ReadOnly` qualifier.

      .. versionadded:: 3.13

   .. attribute:: __closed__

      The value of the *closed* class argument. It can be ``True``, ``False``, or :data:`None`.

   .. attribute:: __extra_items__

      The value of the *extra_items* class argument. It can be a valid type or :data:`NoExtraItems`.

   See the `TypedDict <https://typing.python.org/en/latest/spec/typeddict.html#typeddict>`_ section in the typing documentation for more examples and detailed rules.

   .. versionadded:: 3.8

   .. versionchanged:: 3.9
      ``TypedDict`` is now a function rather than a class.
      It can still be used as a class base, as described above.

   .. versionchanged:: 3.11
      Added support for marking individual keys as :data:`Required` or :data:`NotRequired`.
      See :pep:`655`.

   .. versionchanged:: 3.11
      Added support for generic ``TypedDict``\ s.

   .. versionchanged:: 3.13
      Removed support for the keyword-argument method of creating ``TypedDict``\ s.

   .. versionchanged:: 3.13
      Support for the :data:`ReadOnly` qualifier was added. See :pep:`705`.

   .. versionchanged:: 3.15
      Support for the *closed* and *extra_items* class arguments was added. See :pep:`728`.


Protocols
---------

The following protocols are provided by the :mod:`!typing` module. All are decorated
with :deco:`runtime_checkable`.

.. class:: SupportsAbs

    A protocol with one abstract method ``__abs__`` that is covariant
    in its return type.

.. class:: SupportsBytes

    A protocol with one abstract method ``__bytes__``.

.. class:: SupportsComplex

    A protocol with one abstract method ``__complex__``.

.. class:: SupportsFloat

    A protocol with one abstract method ``__float__``.

.. class:: SupportsIndex

    A protocol with one abstract method ``__index__``.

    .. versionadded:: 3.8

.. class:: SupportsInt

    A protocol with one abstract method ``__int__``.

.. class:: SupportsRound

    A protocol with one abstract method ``__round__``
    that is covariant in its return type.

.. _typing-io:

ABCs and Protocols for working with I/O
---------------------------------------

.. class:: IO[AnyStr]
           TextIO
           BinaryIO

   Generic class ``IO[AnyStr]`` and its subclasses ``TextIO(IO[str])``
   and ``BinaryIO(IO[bytes])``
   represent the types of I/O streams such as returned by
   :func:`open`. Please note that these classes are not protocols, and
   their interface is fairly broad.

The protocols :class:`io.Reader` and :class:`io.Writer` offer a simpler
alternative for argument types, when only the ``read()`` or ``write()``
methods are accessed, respectively::

   def read_and_write(reader: Reader[str], writer: Writer[bytes]):
       data = reader.read()
       writer.write(data.encode())

Also consider using :class:`collections.abc.Iterable` for iterating over
the lines of an input stream::

   def read_config(stream: Iterable[str]):
       for line in stream:
           ...

Functions and decorators
------------------------

.. function:: cast(typ, val)

   Cast a value to a type.

   This returns the value unchanged.  To the type checker this
   signals that the return value has the designated type, but at
   runtime we intentionally don't check anything (we want this
   to be as fast as possible).

.. function:: assert_type(val, typ, /)

   Ask a static type checker to confirm that *val* has an inferred type of *typ*.

   At runtime this does nothing: it returns the first argument unchanged with no
   checks or side effects, no matter the actual type of the argument.

   When a static type checker encounters a call to ``assert_type()``, it
   emits an error if the value is not of the specified type::

       def greet(name: str) -> None:
           assert_type(name, str)  # OK, inferred type of `name` is `str`
           assert_type(name, int)  # type checker error

   This function is useful for ensuring the type checker's understanding of a
   script is in line with the developer's intentions::

       def complex_function(arg: object):
           # Do some complex type-narrowing logic,
           # after which we hope the inferred type will be `int`
           ...
           # Test whether the type checker correctly understands our function
           assert_type(arg, int)

   .. versionadded:: 3.11

.. function:: assert_never(arg, /)

   Ask a static type checker to confirm that a line of code is unreachable.

   Example::

       def int_or_str(arg: int | str) -> None:
           match arg:
               case int():
                   print("It's an int")
               case str():
                   print("It's a str")
               case _ as unreachable:
                   assert_never(unreachable)

   Here, the annotations allow the type checker to infer that the
   last case can never execute, because ``arg`` is either
   an :class:`int` or a :class:`str`, and both options are covered by
   earlier cases.

   If a type checker finds that a call to ``assert_never()`` is
   reachable, it will emit an error. For example, if the type annotation
   for ``arg`` was instead ``int | str | float``, the type checker would
   emit an error pointing out that ``unreachable`` is of type :class:`float`.
   For a call to ``assert_never`` to pass type checking, the inferred type of
   the argument passed in must be the bottom type, :data:`Never`, and nothing
   else.

   At runtime, this throws an exception when called.

   .. seealso::
      `Unreachable Code and Exhaustiveness Checking
      <https://typing.python.org/en/latest/guides/unreachable.html>`__ has more
      information about exhaustiveness checking with static typing.

   .. versionadded:: 3.11

.. function:: reveal_type(obj, /)

   Ask a static type checker to reveal the inferred type of an expression.

   When a static type checker encounters a call to this function,
   it emits a diagnostic with the inferred type of the argument. For example::

      x: int = 1
      reveal_type(x)  # Revealed type is "builtins.int"

   This can be useful when you want to debug how your type checker
   handles a particular piece of code.

   At runtime, this function prints the runtime type of its argument to
   :data:`sys.stderr` and returns the argument unchanged (allowing the call to
   be used within an expression)::

      x = reveal_type(1)  # prints "Runtime type is int"
      print(x)  # prints "1"

   Note that the runtime type may be different from (more or less specific
   than) the type statically inferred by a type checker.

   Most type checkers support ``reveal_type()`` anywhere, even if the
   name is not imported from ``typing``. Importing the name from
   ``typing``, however, allows your code to run without runtime errors and
   communicates intent more clearly.

   .. versionadded:: 3.11

.. decorator:: dataclass_transform(*, eq_default=True, order_default=False, \
                                   kw_only_default=False, frozen_default=False, \
                                   field_specifiers=(), **kwargs)

   Decorator to mark an object as providing
   :func:`dataclass <dataclasses.dataclass>`-like behavior.

   ``@dataclass_transform`` may be used to
   decorate a class, metaclass, or a function that is itself a decorator.
   The presence of ``@dataclass_transform()`` tells a static type checker that the
   decorated object performs runtime "magic" that
   transforms a class in a similar way to
   :deco:`dataclasses.dataclass`.

   Example usage with a decorator function:

   .. testcode::

      @dataclass_transform()
      def create_model[T](cls: type[T]) -> type[T]:
          ...
          return cls

      @create_model
      class CustomerModel:
          id: int
          name: str

   On a base class::

      @dataclass_transform()
      class ModelBase: ...

      class CustomerModel(ModelBase):
          id: int
          name: str

   On a metaclass::

      @dataclass_transform()
      class ModelMeta(type): ...

      class ModelBase(metaclass=ModelMeta): ...

      class CustomerModel(ModelBase):
          id: int
          name: str

   The ``CustomerModel`` classes defined above will
   be treated by type checkers similarly to classes created with
   :deco:`dataclasses.dataclass`.
   For example, type checkers will assume these classes have
   ``__init__`` methods that accept ``id`` and ``name``.

   The decorated class, metaclass, or function may accept the following bool
   arguments which type checkers will assume have the same effect as they
   would have on the
   :deco:`dataclasses.dataclass` decorator: ``init``,
   ``eq``, ``order``, ``unsafe_hash``, ``frozen``, ``match_args``,
   ``kw_only``, and ``slots``. It must be possible for the value of these
   arguments (``True`` or ``False``) to be statically evaluated.

   The arguments to the ``@dataclass_transform`` decorator can be used to
   customize the default behaviors of the decorated class, metaclass, or
   function:

   :param bool eq_default:
       Indicates whether the ``eq`` parameter is assumed to be
       ``True`` or ``False`` if it is omitted by the caller.
       Defaults to ``True``.

   :param bool order_default:
       Indicates whether the ``order`` parameter is
       assumed to be ``True`` or ``False`` if it is omitted by the caller.
       Defaults to ``False``.

   :param bool kw_only_default:
       Indicates whether the ``kw_only`` parameter is
       assumed to be ``True`` or ``False`` if it is omitted by the caller.
       Defaults to ``False``.

   :param bool frozen_default:
       Indicates whether the ``frozen`` parameter is
       assumed to be ``True`` or ``False`` if it is omitted by the caller.
       Defaults to ``False``.

       .. versionadded:: 3.12

   :param field_specifiers:
       Specifies a static list of supported classes
       or functions that describe fields, similar to :func:`dataclasses.field`.
       Defaults to ``()``.
   :type field_specifiers: tuple[Callable[..., Any], ...]

   :param Any \**kwargs:
       Arbitrary other keyword arguments are accepted in order to allow for
       possible future extensions.

   Type checkers recognize the following optional parameters on field
   specifiers:

   .. list-table:: **Recognised parameters for field specifiers**
      :header-rows: 1
      :widths: 20 80

      * - Parameter name
        - Description
      * - ``init``
        - Indicates whether the field should be included in the
          synthesized ``__init__`` method. If unspecified, ``init`` defaults to
          ``True``.
      * - ``default``
        - Provides the default value for the field.
      * - ``default_factory``
        - Provides a runtime callback that returns the
          default value for the field. If neither ``default`` nor
          ``default_factory`` are specified, the field is assumed to have no
          default value and must be provided a value when the class is
          instantiated.
      * - ``factory``
        - An alias for the ``default_factory`` parameter on field specifiers.
      * - ``kw_only``
        - Indicates whether the field should be marked as
          keyword-only. If ``True``, the field will be keyword-only. If
          ``False``, it will not be keyword-only. If unspecified, the value of
          the ``kw_only`` parameter on the object decorated with
          ``@dataclass_transform`` will be used, or if that is unspecified, the
          value of ``kw_only_default`` on ``@dataclass_transform`` will be used.
      * - ``alias``
        - Provides an alternative name for the field. This alternative
          name is used in the synthesized ``__init__`` method.

   At runtime, this decorator records its arguments in the
   ``__dataclass_transform__`` attribute on the decorated object.
   It has no other runtime effect.

   See :pep:`681` for more details.

   .. versionadded:: 3.11

.. _overload:

.. decorator:: overload

   Decorator for creating overloaded functions and methods.

   The ``@overload`` decorator allows describing functions and methods
   that support multiple different combinations of argument types. A series
   of ``@overload``-decorated definitions must be followed by exactly one
   non-``@overload``-decorated definition (for the same function/method).

   ``@overload``-decorated definitions are for the benefit of the
   type checker only, since they will be overwritten by the
   non-``@overload``-decorated definition. The non-``@overload``-decorated
   definition, meanwhile, will be used at
   runtime but should be ignored by a type checker.  At runtime, calling
   an ``@overload``-decorated function directly will raise
   :exc:`NotImplementedError`.

   An example of overload that gives a more
   precise type than can be expressed using a union or a type variable:

   .. testcode::

      @overload
      def process(response: None) -> None:
          ...
      @overload
      def process(response: int) -> tuple[int, str]:
          ...
      @overload
      def process(response: bytes) -> str:
          ...
      def process(response):
          ...  # actual implementation goes here

   See :pep:`484` for more details and comparison with other typing semantics.

   .. versionchanged:: 3.11
      Overloaded functions can now be introspected at runtime using
      :func:`get_overloads`.


.. function:: get_overloads(func)

   Return a sequence of :deco:`overload`-decorated definitions for
   *func*.

   *func* is the function object for the implementation of the
   overloaded function. For example, given the definition of ``process`` in
   the documentation for :deco:`overload`,
   ``get_overloads(process)`` will return a sequence of three function objects
   for the three defined overloads. If called on a function with no overloads,
   ``get_overloads()`` returns an empty sequence.

   ``get_overloads()`` can be used for introspecting an overloaded function at
   runtime.

   .. versionadded:: 3.11


.. function:: clear_overloads()

   Clear all registered overloads in the internal registry.

   This can be used to reclaim the memory used by the registry.

   .. versionadded:: 3.11


.. decorator:: final

   Decorator to indicate final methods and final classes.

   Decorating a method with ``@final`` indicates to a type checker that the
   method cannot be overridden in a subclass. Decorating a class with ``@final``
   indicates that it cannot be subclassed.

   For example::

      class Base:
          @final
          def done(self) -> None:
              ...
      class Sub(Base):
          def done(self) -> None:  # Error reported by type checker
              ...

      @final
      class Leaf:
          ...
      class Other(Leaf):  # Error reported by type checker
          ...

   There is no runtime checking of these properties. See :pep:`591` for
   more details.

   .. versionadded:: 3.8

   .. versionchanged:: 3.11
      The decorator will now attempt to set a ``__final__`` attribute to ``True``
      on the decorated object. Thus, a check like
      ``if getattr(obj, "__final__", False)`` can be used at runtime
      to determine whether an object ``obj`` has been marked as final.
      If the decorated object does not support setting attributes,
      the decorator returns the object unchanged without raising an exception.


.. decorator:: no_type_check

   Decorator to indicate that annotations are not type hints.

   This works as a class or function :term:`decorator`.  With a class, it
   applies recursively to all methods and classes defined in that class
   (but not to methods defined in its superclasses or subclasses). Type
   checkers will ignore all annotations in a function or class with this
   decorator.

   ``@no_type_check`` mutates the decorated object in place.

.. decorator:: override

   Decorator to indicate that a method in a subclass is intended to override a
   method or attribute in a superclass.

   Type checkers should emit an error if a method decorated with ``@override``
   does not, in fact, override anything.
   This helps prevent bugs that may occur when a base class is changed without
   an equivalent change to a child class.

   For example:

   .. testcode::

      class Base:
          def log_status(self) -> None:
              ...

      class Sub(Base):
          @override
          def log_status(self) -> None:  # Okay: overrides Base.log_status
              ...

          @override
          def done(self) -> None:  # Error reported by type checker
              ...

   There is no runtime checking of this property.

   The decorator will attempt to set an ``__override__`` attribute to ``True`` on
   the decorated object. Thus, a check like
   ``if getattr(obj, "__override__", False)`` can be used at runtime to determine
   whether an object ``obj`` has been marked as an override.  If the decorated object
   does not support setting attributes, the decorator returns the object unchanged
   without raising an exception.

   See :pep:`698` for more details.

   .. versionadded:: 3.12

.. decorator:: disjoint_base

   Decorator to mark a class as a disjoint base.

   Type checkers do not allow child classes of a disjoint base ``C`` to
   inherit from other disjoint bases that are not parent or child classes of ``C``.

   For example::

       @disjoint_base
       class Disjoint1: pass

       @disjoint_base
       class Disjoint2: pass

       class Disjoint3(Disjoint1, Disjoint2): pass  # Type checker error

   Type checkers can use knowledge of disjoint bases to detect unreachable code
   and determine when two types can overlap.

   The corresponding runtime concept is a solid base (see :ref:`multiple-inheritance`).
   Classes that are solid bases at runtime can be marked with ``@disjoint_base`` in stub files.
   Users may also mark other classes as disjoint bases to indicate to type checkers that
   multiple inheritance with other disjoint bases should not be allowed.

   Note that the concept of a solid base is a CPython implementation
   detail, and the exact set of standard library classes that are
   disjoint bases at runtime may change in future versions of Python.

   .. versionadded:: 3.15

.. decorator:: type_check_only

   Decorator to mark a class or function as unavailable at runtime.

   This decorator is itself not available at runtime. It is mainly
   intended to mark classes that are defined in type stub files if
   an implementation returns an instance of a private class::

      @type_check_only
      class Response:  # private or not available at runtime
          code: int
          def get_header(self, name: str) -> str: ...

      def fetch_response() -> Response: ...

   Note that returning instances of private classes is not recommended.
   It is usually preferable to make such classes public.

Introspection helpers
---------------------

.. function:: get_type_hints(obj, globalns=None, localns=None, include_extras=False, *, format=Format.VALUE)

   Return a dictionary containing type hints for a function, method, module,
   class object, or other callable object.

   This is often the same as :func:`annotationlib.get_annotations`, but this
   function makes the following changes to the annotations dictionary:

   * Forward references encoded as string literals or :class:`ForwardRef`
     objects are handled by evaluating them in *globalns*, *localns*, and
     (where applicable) *obj*'s :ref:`type parameter <type-params>` namespace.
     If *globalns* or *localns* is not given, appropriate namespace
     dictionaries are inferred from *obj*.
   * ``None`` is replaced with :class:`types.NoneType`.
   * If :deco:`no_type_check` has been applied to *obj*, an
     empty dictionary is returned.
   * If *obj* is a class ``C``, the function returns a dictionary that merges
     annotations from ``C``'s base classes with those on ``C`` directly. This
     is done by traversing :attr:`C.__mro__ <type.__mro__>` and iteratively
     combining
     :term:`annotations <variable annotation>` of each base class. Annotations
     on classes appearing earlier in the :term:`method resolution order` always
     take precedence over annotations on classes appearing later in the method
     resolution order.
   * The function recursively replaces all occurrences of
     ``Annotated[T, ...]``, ``Required[T]``, ``NotRequired[T]``, and ``ReadOnly[T]``
     with ``T``, unless *include_extras* is set to ``True`` (see
     :class:`Annotated` for more information).

   .. caution::

      This function may execute arbitrary code contained in annotations.
      See :ref:`annotationlib-security` for more information.

   .. note::

      If :attr:`Format.VALUE <annotationlib.Format.VALUE>` is used and any
      forward references in the annotations of *obj* are not resolvable, a
      :exc:`NameError` exception is raised. For example, this can happen
      with names imported under :data:`if TYPE_CHECKING <TYPE_CHECKING>`.
      More generally, any kind of exception can be raised if an annotation
      contains invalid Python code.

   .. note::

      Calling :func:`get_type_hints` on an instance is not supported.
      To retrieve annotations for an instance, call
      :func:`get_type_hints` on the instance's class instead
      (for example, ``get_type_hints(type(obj))``).

   .. versionchanged:: 3.9
      Added ``include_extras`` parameter as part of :pep:`593`.
      See the documentation on :data:`Annotated` for more information.

   .. versionchanged:: 3.11
      Previously, ``Optional[t]`` was added for function and method annotations
      if a default value equal to ``None`` was set.
      Now the annotation is returned unchanged.

   .. versionchanged:: 3.14
      Added the ``format`` parameter. See the documentation on
      :func:`annotationlib.get_annotations` for more information.

   .. versionchanged:: 3.14
      Calling :func:`get_type_hints` on instances is no longer supported.
      Some instances were accepted in earlier versions as an undocumented
      implementation detail.

.. function:: get_origin(tp)

   Get the unsubscripted version of a type: for a typing object of the form
   ``X[Y, Z, ...]`` return ``X``.

   If ``X`` is a typing-module alias for a builtin or
   :mod:`collections` class, it will be normalized to the original class.
   If ``X`` is an instance of :class:`ParamSpecArgs` or :class:`ParamSpecKwargs`,
   return the underlying :class:`ParamSpec`.
   Return ``None`` for unsupported objects.

   Examples:

   .. testcode::

      assert get_origin(str) is None
      assert get_origin(Dict[str, int]) is dict
      assert get_origin(Union[int, str]) is Union
      assert get_origin(Annotated[str, "metadata"]) is Annotated
      P = ParamSpec('P')
      assert get_origin(P.args) is P
      assert get_origin(P.kwargs) is P

   .. versionadded:: 3.8

.. function:: get_args(tp)

   Get type arguments with all substitutions performed: for a typing object
   of the form ``X[Y, Z, ...]`` return ``(Y, Z, ...)``.

   If ``X`` is a union or :class:`Literal` contained in another
   generic type, the order of ``(Y, Z, ...)`` may be different from the order
   of the original arguments ``[Y, Z, ...]`` due to type caching.
   Return ``()`` for unsupported objects.

   Examples:

   .. testcode::

      assert get_args(int) == ()
      assert get_args(Dict[int, str]) == (int, str)
      assert get_args(Union[int, str]) == (int, str)

   .. versionadded:: 3.8

.. function:: get_protocol_members(tp)

   Return the set of members defined in a :class:`Protocol`.

   .. doctest::

      >>> from typing import Protocol, get_protocol_members
      >>> class P(Protocol):
      ...     def a(self) -> str: ...
      ...     b: int
      >>> get_protocol_members(P) == frozenset({'a', 'b'})
      True

   Raise :exc:`TypeError` for arguments that are not Protocols.

   .. versionadded:: 3.13

.. function:: is_protocol(tp)

   Determine if a type is a :class:`Protocol`.

   For example:

   .. testcode::

      class P(Protocol):
          def a(self) -> str: ...
          b: int

      assert is_protocol(P)
      assert not is_protocol(int)

   This function only returns true for ``Protocol`` classes, not for
   :ref:`generic aliases <types-genericalias>` of them:

   .. testcode::

      class GenericP[T](Protocol):
          def a(self) -> T: ...
          b: int

      assert not is_protocol(GenericP[int])

   .. versionadded:: 3.13

.. function:: is_typeddict(tp)

   Check if a type is a :class:`TypedDict`.

   For example:

   .. testcode::

      class Film(TypedDict):
          title: str
          year: int

      assert is_typeddict(Film)
      assert not is_typeddict(list | str)

      # TypedDict is a factory for creating typed dicts,
      # not a typed dict itself
      assert not is_typeddict(TypedDict)

   This function only returns true for ``TypedDict`` classes, not for
   :ref:`generic aliases <types-genericalias>` of them:

   .. testcode::

      class GenericFilm[T](TypedDict):
          title: str
          year: T

      assert not is_typeddict(GenericFilm[int])

   .. versionadded:: 3.10

.. class:: ForwardRef

   Class used for internal typing representation of string forward references.

   For example, ``List["SomeClass"]`` is implicitly transformed into
   ``List[ForwardRef("SomeClass")]``.  :class:`!ForwardRef` should not be instantiated by
   a user, but may be used by introspection tools.

   .. note::
      :pep:`585` generic types such as ``list["SomeClass"]`` will not be
      implicitly transformed into ``list[ForwardRef("SomeClass")]`` and thus
      will not automatically resolve to ``list[SomeClass]``.

   .. versionadded:: 3.7.4

   .. versionchanged:: 3.14
      This is now an alias for :class:`annotationlib.ForwardRef`. Several undocumented
      behaviors of this class have been changed; for example, after a ``ForwardRef`` has
      been evaluated, the evaluated value is no longer cached.

.. function:: evaluate_forward_ref(forward_ref, *, owner=None, globals=None, locals=None, type_params=None, format=annotationlib.Format.VALUE)

   Evaluate an :class:`annotationlib.ForwardRef` as a :term:`type hint`.

   This is similar to calling :meth:`annotationlib.ForwardRef.evaluate`,
   but unlike that method, :func:`!evaluate_forward_ref` also
   recursively evaluates forward references nested within the type hint.

   See the documentation for :meth:`annotationlib.ForwardRef.evaluate` for
   the meaning of the *owner*, *globals*, *locals*, *type_params*, and *format* parameters.

   .. caution::

      This function may execute arbitrary code contained in annotations.
      See :ref:`annotationlib-security` for more information.

   .. versionadded:: 3.14

.. data:: NoDefault

   A sentinel object used to indicate that a type parameter has no default
   value. For example:

   .. doctest::

      >>> T = TypeVar("T")
      >>> T.__default__ is typing.NoDefault
      True
      >>> S = TypeVar("S", default=None)
      >>> S.__default__ is None
      True

   .. versionadded:: 3.13

.. data:: NoExtraItems

   A :class:`sentinel` object used to indicate that a :class:`TypedDict`
   does not have the *extra_items* class argument.

   .. doctest::

      >>> from typing import TypedDict, NoExtraItems
      >>> class Point(TypedDict):
      ...     x: int
      ...     y: int
      ...
      >>> Point.__extra_items__ is NoExtraItems
      True

Constant
--------

.. data:: TYPE_CHECKING

   A special constant that is assumed to be ``True`` by static
   type checkers. It's ``False`` at runtime.

   A module which is expensive to import, and which only contain types
   used for typing annotations, can be safely imported inside an
   ``if TYPE_CHECKING:`` block.  This prevents the module from actually
   being imported at runtime; annotations aren't eagerly evaluated
   (see :pep:`649`) so using undefined symbols in annotations is
   harmless--as long as you don't later examine them.
   Your static type analysis tool will set ``TYPE_CHECKING`` to
   ``True`` during static type analysis, which means the module will
   be imported and the types will be checked properly during such analysis.

   Usage::

      if TYPE_CHECKING:
          import expensive_mod

      def fun(arg: expensive_mod.SomeType) -> None:
          local_var: expensive_mod.AnotherType = other_fun()

   If you occasionally need to examine type annotations at runtime
   which may contain undefined symbols, use
   :meth:`annotationlib.get_annotations` with a ``format`` parameter
   of :attr:`annotationlib.Format.STRING` or
   :attr:`annotationlib.Format.FORWARDREF` to safely retrieve the
   annotations without raising :exc:`NameError`.

   .. versionadded:: 3.5.2

.. _generic-concrete-collections:
.. _deprecated-aliases:

Deprecated aliases
------------------

This module defines several deprecated aliases to pre-existing
standard library classes. These were originally included in the :mod:`!typing`
module in order to support parameterizing these generic classes using ``[]``.
However, the aliases became redundant in Python 3.9 when the
corresponding pre-existing classes were enhanced to support ``[]`` (see
:pep:`585`).

The redundant types are deprecated as of Python 3.9. However, while the aliases
may be removed at some point, removal of these aliases is not currently
planned. As such, no deprecation warnings are currently issued by the
interpreter for these aliases.

If at some point it is decided to remove these deprecated aliases, a
deprecation warning will be issued by the interpreter for at least two releases
prior to removal. The aliases are guaranteed to remain in the :mod:`!typing` module
without deprecation warnings until at least Python 3.14.

Type checkers are encouraged to flag uses of the deprecated types if the
program they are checking targets a minimum Python version of 3.9 or newer.

.. _corresponding-to-built-in-types:

Aliases to built-in types
"""""""""""""""""""""""""

.. class:: Dict(dict, MutableMapping[KT, VT])

   Deprecated alias to :class:`dict`.

   Note that to annotate arguments, it is preferred
   to use an abstract collection type such as :class:`~collections.abc.Mapping`
   rather than to use :class:`dict` or :class:`!typing.Dict`.

   .. deprecated:: 3.9
      :class:`builtins.dict <dict>` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: List(list, MutableSequence[T])

   Deprecated alias to :class:`list`.

   Note that to annotate arguments, it is preferred
   to use an abstract collection type such as
   :class:`~collections.abc.Sequence` or :class:`~collections.abc.Iterable`
   rather than to use :class:`list` or :class:`!typing.List`.

   .. deprecated:: 3.9
      :class:`builtins.list <list>` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Set(set, MutableSet[T])

   Deprecated alias to :class:`builtins.set <set>`.

   Note that to annotate arguments, it is preferred
   to use an abstract collection type such as :class:`collections.abc.Set`
   rather than to use :class:`set` or :class:`typing.Set`.

   .. deprecated:: 3.9
      :class:`builtins.set <set>` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: FrozenSet(frozenset, AbstractSet[T_co])

   Deprecated alias to :class:`builtins.frozenset <frozenset>`.

   .. deprecated:: 3.9
      :class:`builtins.frozenset <frozenset>`
      now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. data:: Tuple

   Deprecated alias for :class:`tuple`.

   :class:`tuple` and ``Tuple`` are special-cased in the type system; see
   :ref:`annotating-tuples` for more details.

   .. deprecated:: 3.9
      :class:`builtins.tuple <tuple>` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Type(Generic[CT_co])

   Deprecated alias to :class:`type`.

   See :ref:`type-of-class-objects` for details on using :class:`type` or
   ``typing.Type`` in type annotations.

   .. versionadded:: 3.5.2

   .. deprecated:: 3.9
      :class:`builtins.type <type>` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. _corresponding-to-types-in-collections:

Aliases to types in :mod:`collections`
""""""""""""""""""""""""""""""""""""""

.. class:: DefaultDict(collections.defaultdict, MutableMapping[KT, VT])

   Deprecated alias to :class:`collections.defaultdict`.

   .. versionadded:: 3.5.2

   .. deprecated:: 3.9
      :class:`collections.defaultdict` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: OrderedDict(collections.OrderedDict, MutableMapping[KT, VT])

   Deprecated alias to :class:`collections.OrderedDict`.

   .. versionadded:: 3.7.2

   .. deprecated:: 3.9
      :class:`collections.OrderedDict` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: ChainMap(collections.ChainMap, MutableMapping[KT, VT])

   Deprecated alias to :class:`collections.ChainMap`.

   .. versionadded:: 3.6.1

   .. deprecated:: 3.9
      :class:`collections.ChainMap` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Counter(collections.Counter, Dict[T, int])

   Deprecated alias to :class:`collections.Counter`.

   .. versionadded:: 3.6.1

   .. deprecated:: 3.9
      :class:`collections.Counter` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Deque(deque, MutableSequence[T])

   Deprecated alias to :class:`collections.deque`.

   .. versionadded:: 3.6.1

   .. deprecated:: 3.9
      :class:`collections.deque` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. _other-concrete-types:

Aliases to other concrete types
"""""""""""""""""""""""""""""""

.. class:: Pattern
           Match

   Deprecated aliases corresponding to the return types from
   :func:`re.compile` and :func:`re.search`.

   These types (and the corresponding functions) are generic over
   :data:`AnyStr`. ``Pattern`` can be specialised as ``Pattern[str]`` or
   ``Pattern[bytes]``; ``Match`` can be specialised as ``Match[str]`` or
   ``Match[bytes]``.

   .. deprecated:: 3.9
      Classes ``Pattern`` and ``Match`` from :mod:`re` now support ``[]``.
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Text

   Deprecated alias for :class:`str`.

   ``Text`` is provided to supply a forward
   compatible path for Python 2 code: in Python 2, ``Text`` is an alias for
   ``unicode``.

   Use ``Text`` to indicate that a value must contain a unicode string in
   a manner that is compatible with both Python 2 and Python 3::

       def add_unicode_checkmark(text: Text) -> Text:
           return text + u' \u2713'

   .. versionadded:: 3.5.2

   .. deprecated:: 3.11
      Python 2 is no longer supported, and most type checkers also no longer
      support type checking Python 2 code. Removal of the alias is not
      currently planned, but users are encouraged to use
      :class:`str` instead of ``Text``.

.. _abstract-base-classes:
.. _corresponding-to-collections-in-collections-abc:

Aliases to container ABCs in :mod:`collections.abc`
"""""""""""""""""""""""""""""""""""""""""""""""""""

.. class:: AbstractSet(Collection[T_co])

   Deprecated alias to :class:`collections.abc.Set`.

   .. deprecated:: 3.9
      :class:`collections.abc.Set` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: ByteString(Sequence[int])

   Deprecated alias to :class:`collections.abc.ByteString`.

   Use ``isinstance(obj, collections.abc.Buffer)`` to test if ``obj``
   implements the :ref:`buffer protocol <bufferobjects>` at runtime. For use in
   type annotations, either use :class:`~collections.abc.Buffer` or a union
   that explicitly specifies the types your code supports (e.g.,
   ``bytes | bytearray | memoryview``).

   :class:`!ByteString` was originally intended to be an abstract class that
   would serve as a supertype of both :class:`bytes` and :class:`bytearray`.
   However, since the ABC never had any methods, knowing that an object was an
   instance of :class:`!ByteString` never actually told you anything useful
   about the object. Other common buffer types such as :class:`memoryview` were
   also never understood as subtypes of :class:`!ByteString` (either at runtime
   or by static type checkers).

   See :pep:`PEP 688 <688#current-options>` for more details.

   .. deprecated-removed:: 3.9 3.17

.. class:: Collection(Sized, Iterable[T_co], Container[T_co])

   Deprecated alias to :class:`collections.abc.Collection`.

   .. versionadded:: 3.6

   .. deprecated:: 3.9
      :class:`collections.abc.Collection` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Container(Generic[T_co])

   Deprecated alias to :class:`collections.abc.Container`.

   .. deprecated:: 3.9
      :class:`collections.abc.Container` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: ItemsView(MappingView, AbstractSet[tuple[KT_co, VT_co]])

   Deprecated alias to :class:`collections.abc.ItemsView`.

   .. deprecated:: 3.9
      :class:`collections.abc.ItemsView` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: KeysView(MappingView, AbstractSet[KT_co])

   Deprecated alias to :class:`collections.abc.KeysView`.

   .. deprecated:: 3.9
      :class:`collections.abc.KeysView` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Mapping(Collection[KT], Generic[KT, VT_co])

   Deprecated alias to :class:`collections.abc.Mapping`.

   .. deprecated:: 3.9
      :class:`collections.abc.Mapping` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: MappingView(Sized)

   Deprecated alias to :class:`collections.abc.MappingView`.

   .. deprecated:: 3.9
      :class:`collections.abc.MappingView` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: MutableMapping(Mapping[KT, VT])

   Deprecated alias to :class:`collections.abc.MutableMapping`.

   .. deprecated:: 3.9
      :class:`collections.abc.MutableMapping`
      now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: MutableSequence(Sequence[T])

   Deprecated alias to :class:`collections.abc.MutableSequence`.

   .. deprecated:: 3.9
      :class:`collections.abc.MutableSequence`
      now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: MutableSet(AbstractSet[T])

   Deprecated alias to :class:`collections.abc.MutableSet`.

   .. deprecated:: 3.9
      :class:`collections.abc.MutableSet` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Sequence(Reversible[T_co], Collection[T_co])

   Deprecated alias to :class:`collections.abc.Sequence`.

   .. deprecated:: 3.9
      :class:`collections.abc.Sequence` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: ValuesView(MappingView, Collection[_VT_co])

   Deprecated alias to :class:`collections.abc.ValuesView`.

   .. deprecated:: 3.9
      :class:`collections.abc.ValuesView` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. _asynchronous-programming:

Aliases to asynchronous ABCs in :mod:`collections.abc`
""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. class:: Coroutine(Awaitable[ReturnType], Generic[YieldType, SendType, ReturnType])

   Deprecated alias to :class:`collections.abc.Coroutine`.

   See :ref:`annotating-generators-and-coroutines`
   for details on using :class:`collections.abc.Coroutine`
   and ``typing.Coroutine`` in type annotations.

   .. versionadded:: 3.5.3

   .. deprecated:: 3.9
      :class:`collections.abc.Coroutine` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: AsyncGenerator(AsyncIterator[YieldType], Generic[YieldType, SendType])

   Deprecated alias to :class:`collections.abc.AsyncGenerator`.

   See :ref:`annotating-generators-and-coroutines`
   for details on using :class:`collections.abc.AsyncGenerator`
   and ``typing.AsyncGenerator`` in type annotations.

   .. versionadded:: 3.6.1

   .. deprecated:: 3.9
      :class:`collections.abc.AsyncGenerator`
      now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

   .. versionchanged:: 3.13
      The ``SendType`` parameter now has a default.

.. class:: AsyncIterable(Generic[T_co])

   Deprecated alias to :class:`collections.abc.AsyncIterable`.

   .. versionadded:: 3.5.2

   .. deprecated:: 3.9
      :class:`collections.abc.AsyncIterable` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: AsyncIterator(AsyncIterable[T_co])

   Deprecated alias to :class:`collections.abc.AsyncIterator`.

   .. versionadded:: 3.5.2

   .. deprecated:: 3.9
      :class:`collections.abc.AsyncIterator` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Awaitable(Generic[T_co])

   Deprecated alias to :class:`collections.abc.Awaitable`.

   .. versionadded:: 3.5.2

   .. deprecated:: 3.9
      :class:`collections.abc.Awaitable` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. _corresponding-to-other-types-in-collections-abc:

Aliases to other ABCs in :mod:`collections.abc`
"""""""""""""""""""""""""""""""""""""""""""""""

.. class:: Iterable(Generic[T_co])

   Deprecated alias to :class:`collections.abc.Iterable`.

   .. deprecated:: 3.9
      :class:`collections.abc.Iterable` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Iterator(Iterable[T_co])

   Deprecated alias to :class:`collections.abc.Iterator`.

   .. deprecated:: 3.9
      :class:`collections.abc.Iterator` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. data:: Callable

   Deprecated alias to :class:`collections.abc.Callable`.

   See :ref:`annotating-callables` for details on how to use
   :class:`collections.abc.Callable` and ``typing.Callable`` in type annotations.

   .. deprecated:: 3.9
      :class:`collections.abc.Callable` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

   .. versionchanged:: 3.10
      ``Callable`` now supports :class:`ParamSpec` and :data:`Concatenate`.
      See :pep:`612` for more details.

.. class:: Generator(Iterator[YieldType], Generic[YieldType, SendType, ReturnType])

   Deprecated alias to :class:`collections.abc.Generator`.

   See :ref:`annotating-generators-and-coroutines`
   for details on using :class:`collections.abc.Generator`
   and ``typing.Generator`` in type annotations.

   .. deprecated:: 3.9
      :class:`collections.abc.Generator` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

   .. versionchanged:: 3.13
      Default values for the send and return types were added.

.. class:: Hashable

   Deprecated alias to :class:`collections.abc.Hashable`.

   .. deprecated:: 3.12
      Use :class:`collections.abc.Hashable` directly instead.

.. class:: Reversible(Iterable[T_co])

   Deprecated alias to :class:`collections.abc.Reversible`.

   .. deprecated:: 3.9
      :class:`collections.abc.Reversible` now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

.. class:: Sized

   Deprecated alias to :class:`collections.abc.Sized`.

   .. deprecated:: 3.12
      Use :class:`collections.abc.Sized` directly instead.

.. _context-manager-types:

Aliases to :mod:`contextlib` ABCs
"""""""""""""""""""""""""""""""""

.. class:: ContextManager(Generic[T_co, ExitT_co])

   Deprecated alias to :class:`contextlib.AbstractContextManager`.

   The first type parameter, ``T_co``, represents the type returned by
   the :meth:`~object.__enter__` method. The optional second type parameter, ``ExitT_co``,
   which defaults to ``bool | None``, represents the type returned by the
   :meth:`~object.__exit__` method.

   .. versionadded:: 3.5.4

   .. deprecated:: 3.9
      :class:`contextlib.AbstractContextManager`
      now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

   .. versionchanged:: 3.13
      Added the optional second type parameter, ``ExitT_co``.

.. class:: AsyncContextManager(Generic[T_co, AExitT_co])

   Deprecated alias to :class:`contextlib.AbstractAsyncContextManager`.

   The first type parameter, ``T_co``, represents the type returned by
   the :meth:`~object.__aenter__` method. The optional second type parameter, ``AExitT_co``,
   which defaults to ``bool | None``, represents the type returned by the
   :meth:`~object.__aexit__` method.

   .. versionadded:: 3.6.2

   .. deprecated:: 3.9
      :class:`contextlib.AbstractAsyncContextManager`
      now supports subscripting (``[]``).
      See :pep:`585` and :ref:`types-genericalias`.

   .. versionchanged:: 3.13
      Added the optional second type parameter, ``AExitT_co``.

Deprecation Timeline of Major Features
======================================

Certain features in ``typing`` are deprecated and may be removed in a future
version of Python. The following table summarizes major deprecations for your
convenience. This is subject to change, and not all deprecations are listed.

.. list-table::
   :header-rows: 1

   * - Feature
     - Deprecated in
     - Projected removal
     - PEP/issue
   * - ``typing`` versions of standard collections
     - 3.9
     - Undecided (see :ref:`deprecated-aliases` for more information)
     - :pep:`585`
   * - :class:`typing.ByteString`
     - 3.9
     - 3.17
     - :gh:`91896`
   * - :data:`typing.Text`
     - 3.11
     - Undecided
     - :gh:`92332`
   * - :class:`typing.Hashable` and :class:`typing.Sized`
     - 3.12
     - Undecided
     - :gh:`94309`
   * - :data:`typing.TypeAlias`
     - 3.12
     - Undecided
     - :pep:`695`
   * - :data:`typing.AnyStr`
     - 3.13
     - 3.18
     - :gh:`105578`

----

.. decorator:: disjoint_base

   Decorator to mark a class as a disjoint base.

   Type checkers do not allow child classes of a disjoint base ``C`` to
   inherit from other disjoint bases that are not parent or child classes of ``C``.

   For example::

       @disjoint_base
       class Disjoint1: pass

       @disjoint_base
       class Disjoint2: pass

       class Disjoint3(Disjoint1, Disjoint2): pass  # Type checker error

   Type checkers can use knowledge of disjoint bases to detect unreachable code
   and determine when two types can overlap.

   The corresponding runtime concept is a solid base (see :ref:`multiple-inheritance`).
   Classes that are solid bases at runtime can be marked with ``@disjoint_base`` in stub files.
   Users may also mark other classes as disjoint bases to indicate to type checkers that
   multiple inheritance with other disjoint bases should not be allowed.

   Note that the concept of a solid base is a CPython implementation
   detail, and the exact set of standard library classes that are
   disjoint bases at runtime may change in future versions of Python.

   .. versionadded:: 3.15
