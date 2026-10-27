Path extensions (:file:`.pth` files)
------------------------------------

:file:`{name}.pth` contains additional items (one per line) to be appended to
``sys.path``.  Items that name non-existing directories are never added to
``sys.path``, and no check is made that the item refers to a directory rather
than a file.  No item is added to ``sys.path`` more than once.  Blank lines
and lines beginning with ``#`` are skipped.

For backward compatibility, lines starting with ``import`` (followed by space
or tab) are executed with :func:`exec`.

.. versionchanged:: 3.13

   The :file:`.pth` files are now decoded by UTF-8 at first and then by the
   :term:`locale encoding` if it fails.

.. versionchanged:: 3.15

   :file:`.pth` file lines starting with ``import`` are deprecated.  During
   the deprecation period, such lines are still executed (except in the case
   below), but a diagnostic message is emitted only when the :option:`-v` flag
   is given.

   ``import`` lines in :file:`{name}.pth` are silently ignored when a
   :ref:`matching <site-start-files>` :file:`{name}.start` file exists.

   Errors on individual lines no longer abort processing of the rest of the
   file.  Each error is reported and the remaining lines continue to be
   processed.

.. deprecated-removed:: 3.15 3.20

   Decoding :file:`{name}.pth` files in any encoding other than ``utf-8-sig``
   is deprecated in Python 3.15, and support for decoding from the locale
   encoding will be removed in Python 3.20.

   ``import`` lines in :file:`{name}.pth` files are deprecated and will be
   silently ignored in Python 3.18 and 3.19.  In Python 3.20 a warning will be
   produced for ``import`` lines in :file:`{name}.pth` files.


.. _site-start-files:


----

Startup entry points (:file:`.start` files)
-------------------------------------------

.. versionadded:: 3.15

A startup entry point file is a file whose name has the form
:file:`{name}.start` and exists in one of the site-packages directories
described above.  Each file specifies entry points to be called during
interpreter startup, using the ``pkg.mod:callable`` syntax understood by
:func:`pkgutil.resolve_name`.

Each non-blank line that does not begin with ``#`` must contain an entry
point reference in the form ``pkg.mod:callable``.  The colon and callable
portion are mandatory.  Each callable is invoked with no arguments, and
any return value is discarded.

:file:`.start` files are processed after all :file:`.pth` path extensions
have been applied to :data:`sys.path`, ensuring that paths are available
before any startup code runs.

Unlike :data:`sys.path` extensions from :file:`.pth` files, duplicate entry
points are **not** de-duplicated --- if an entry point appears more than once,
it will be called more than once.

If an exception occurs during resolution or invocation of an entry point,
a traceback is printed to :data:`sys.stderr` and processing continues with
the remaining entry points.

:file:`.start` files must be encoded in UTF-8.

:pep:`829` defined the original specification for these features.

.. note::

   If a :file:`{name}.start` file exists alongside a :file:`{name}.pth` file
   with the same base name, any ``import`` lines in the :file:`.pth` file are
   ignored in favor of the entry points in the :file:`.start` file.

.. note::

   Executable lines (``import`` lines in :file:`{name}.pth` files and
   :file:`{name}.start` file entry points) are always run at Python startup
   (unless :option:`-S` is given to disable the ``site.py`` module entirely),
   regardless of whether a particular module is actually going to be used.

.. note::

   :file:`{name}.start` files invoke :func:`pkgutil.resolve_name` with
   ``strict=True``, which requires the full ``pkg.mod:callable`` form.

.. index::
   single: package
   triple: path; configuration; file



----

.. class:: StartupState(known_paths=None)

   Instances of this class accumulate interpreter startup configuration data
   from one or more site directories.  They are the preferred interface for
   batching the processing of :file:`.pth` and :file:`.start` files across
   multiple site directories, so that every :data:`sys.path` extension is
   visible before any startup code runs.

   The optional *known_paths* argument is a set of case-normalized paths
   (which can be produced by :func:`makepath`) used to prevent duplicate
   :data:`sys.path` entries.  When ``None`` (the default), the set is built
   from the current :data:`sys.path`.  :func:`main` implicitly uses an
   instance of this class.

   Typical use:

   .. code-block:: python

      state = site.StartupState()
      for sitedir in site_dirs:
          state.addsitedir(sitedir)
      state.process()

   .. versionadded:: 3.15

   .. method:: addsitedir(sitedir)

      Read the :file:`.pth` and :file:`.start` files in *sitedir* and
      record their :data:`sys.path` extensions, deprecated :file:`.pth`
      ``import`` lines, and :file:`.start` entry points on this state.
      The recorded data is not applied until :meth:`process` is called.

   .. method:: addusersitepackages()

      Add the per-user site-packages directory, if enabled and if it exists.
      The directory's startup data is accumulated for later processing by
      :meth:`process`.

   .. method:: addsitepackages(prefixes=None)

      Add global site-packages directories, computed from *prefixes* or from
      the global :data:`PREFIXES` when *prefixes* is ``None``.  Each
      directory's startup data is accumulated for later processing by
      :meth:`process`.

   .. method:: process()

      Apply the accumulated state by first adding the path extensions to
      :data:`sys.path`, then executing the :file:`.start` file entry points
      and :file:`.pth` file ``import`` lines (:ref:`deprecated
      <site-pth-files>`).

      This method is not idempotent and must not be called more than once
      on the same instance.  Doing so will apply the accumulated state
      more than once, re-running entry points and ``import`` lines.



----

.. function:: addsitedir(sitedir, known_paths=None)

   Add a directory to sys.path and parse the :file:`.pth` and :file:`.start`
   files found in that directory.  Typically used in :mod:`sitecustomize` or
   :mod:`usercustomize` (see above).

   The *known_paths* argument is an optional set of case-normalized paths
   used to prevent duplicate :data:`sys.path` entries.  When ``None`` (the
   default), the set is built from the current :data:`sys.path`.

   For batched processing across multiple site directories, build a
   :class:`StartupState` explicitly and call :meth:`StartupState.addsitedir`
   on it; that defers :file:`.pth` and :file:`.start` processing until a
   single :meth:`StartupState.process` call, ensuring every :data:`sys.path`
   extension is visible before any startup code runs.

   .. versionchanged:: 3.15

      Also processes :file:`.start` files.  See :ref:`site-start-files`.

