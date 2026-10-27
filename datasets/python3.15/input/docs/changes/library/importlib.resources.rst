.. function:: files(anchor: Optional[Anchor] = None)

    Returns a :class:`~importlib.resources.abc.Traversable` object
    representing the resource container (think directory) and its resources
    (think files). A Traversable may contain other containers (think
    subdirectories).

    *anchor* is an optional :class:`Anchor`. If the anchor is a
    package, resources are resolved from that package. If a module,
    resources are resolved adjacent to that module (in the same package
    or the package root). If the anchor is omitted, the caller's module
    is used.

    .. versionadded:: 3.9

    .. versionchanged:: 3.12
      *package* parameter was renamed to *anchor*.
      *package* was still accepted, but deprecated.

    .. versionchanged:: 3.15
       *package* parameter was fully removed. *anchor* can now be a
       non-package module and if omitted will default to the caller's module.
       *package* is no longer accepted since Python 3.15. Consider passing the
       anchor positionally or using ``importlib_resources >= 5.10`` for a
       compatible interface on older Pythons.
