UTF-8 mode
==========

.. versionadded:: 3.7
.. versionchanged:: 3.15

   Python UTF-8 mode is now enabled by default (:pep:`686`).

Windows still uses legacy encodings for the system encoding (the ANSI Code
Page).  When the :ref:`Python UTF-8 Mode <utf8-mode>` is disabled, Python
uses the ANSI Code Page as the default encoding of text files, as
returned by :func:`locale.getencoding`.

This may cause issues because UTF-8 is widely used on the internet
and most Unix systems, including WSL (Windows Subsystem for Linux).

The :ref:`Python UTF-8 Mode <utf8-mode>`, enabled by default, ignores the
system encoding and uses UTF-8 as the default text encoding.
When the :ref:`UTF-8 mode <utf8-mode>` is enabled, you can still use the
system encoding (the ANSI Code Page) via the "mbcs" codec.

You can disable the :ref:`Python UTF-8 Mode <utf8-mode>` via
the ``-X utf8=0`` command line option, or the ``PYTHONUTF8=0`` environment
variable.  See :envvar:`PYTHONUTF8` for disabling UTF-8 mode, and
:ref:`setting-envvars` for how to modify environment variables.

.. hint::
   Adding ``PYTHONUTF8={0,1}`` to the default environment variables
   will affect all Python 3.7+ applications on your system.
   If you have any Python 3.7+ applications which rely on the legacy
   system encoding, it is recommended to set the environment variable
   temporarily or use the ``-X utf8`` command line option.

.. note::
   Even when UTF-8 mode is disabled, Python uses UTF-8 by default
   on Windows for:

   * Console I/O including standard I/O (see :pep:`528` for details).
   * The :term:`filesystem encoding <filesystem encoding and error handler>`
     (see :pep:`529` for details).


.. _windows_finding_modules:
