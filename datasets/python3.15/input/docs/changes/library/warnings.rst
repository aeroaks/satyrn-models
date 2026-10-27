.. function:: warn_explicit(message, category, filename, lineno, module=None, registry=None, module_globals=None, source=None)

   This is a low-level interface to the functionality of :func:`warn`, passing in
   explicitly the message, category, filename and line number, and optionally
   other arguments.
   *message* must be a string and *category* a subclass of :exc:`Warning` or
   *message* may be a :exc:`Warning` instance, in which case *category* will be
   ignored.

   *module*, if supplied, should be the module name.
   If no module is passed, the module regular expression in
   :ref:`warnings filter <warning-filter>` will be tested against the module
   names constructed from the path components starting from all parent
   directories (with ``/__init__.py``, ``.py`` and, on Windows, ``.pyw``
   stripped) and against the filename with ``.py`` stripped.
   For example, when the filename is ``'/path/to/package/module.py'``, it will
   be tested against  ``'path.to.package.module'``, ``'to.package.module'``
   ``'package.module'``, ``'module'``, and ``'/path/to/package/module'``.

   *registry*, if supplied, should be the ``__warningregistry__`` dictionary
   of the module.
   If no registry is passed, each warning is treated as the first occurrence,
   that is, filter actions ``"default"``, ``"module"`` and ``"once"`` are
   handled as ``"always"``.

   *module_globals*, if supplied, should be the global namespace in use by the code
   for which the warning is issued.  (This argument is used to support displaying
   source for modules found in zipfiles or other non-filesystem import
   sources).

   *source*, if supplied, is the destroyed object which emitted a
   :exc:`ResourceWarning`.

   .. versionchanged:: 3.6
      Add the *source* parameter.

   .. versionchanged:: 3.15
      If no module is passed, test the filter regular expression against
      module names created from the path, not only the path itself.



----

.. class:: catch_warnings(*, record=False, module=None, action=None, category=Warning, lineno=0, append=False)

    A context manager that copies and, upon exit, restores the warnings filter
    and the :func:`showwarning` function.
    If the *record* argument is :const:`False` (the default) the context manager
    returns :class:`None` on entry. If *record* is :const:`True`, a list is
    returned that is progressively populated with objects as seen by a custom
    :func:`showwarning` function (which also suppresses output to ``sys.stderr``).
    Each object in the list is guaranteed to have the following attributes:

      - ``message``: the warning message (an instance of :exc:`Warning`)
      - ``category``: the warning category (a subclass of :exc:`Warning`)
      - ``filename``: the file name where the warning occurred (:class:`str`)
      - ``lineno``: the line number in the file (:class:`int`)
      - ``file``: the file object used for output (if any), or ``None``
      - ``line``: the line of source code (if available), or ``None``
      - ``source``: the original object that generated the warning (if
        available), or ``None``
      - ``module``: the module name where the warning occurred
        (:class:`str`), or ``None``

    .. versionchanged:: 3.6
      The ``source`` attribute was added.

    .. versionchanged:: 3.15
      The ``module`` attribute was added.

    The type of these objects is not specified and may change; only the
    presence of these attributes is guaranteed.

    The *module* argument takes a module that will be used instead of the
    module returned when you import :mod:`!warnings` whose filter will be
    protected. This argument exists primarily for testing the :mod:`!warnings`
    module itself.

    If the *action* argument is not ``None``, the remaining arguments are
    passed to :func:`simplefilter` as if it were called immediately on
    entering the context.

    See :ref:`warning-filter` for the meaning of the *category* and *lineno*
    parameters.

    .. note::

        See :ref:`warning-concurrent-safe` for details on the
        concurrency-safety of the :class:`catch_warnings` context manager when
        used in programs using multiple threads or async functions.


    .. versionchanged:: 3.11

        Added the *action*, *category*, *lineno*, and *append* parameters.

