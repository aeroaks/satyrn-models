Command-line interface
----------------------

.. program:: webbrowser

The script :program:`webbrowser` can be used as a command-line interface for the
module. It accepts a URL as the argument. It accepts the following optional
parameters:

.. option:: -n, --new-window

   Opens the URL in a new browser window, if possible.

.. option:: -t, --new-tab

   Opens the URL in a new browser tab.

The options are, naturally, mutually exclusive.  Usage example:

.. code-block:: bash

   python -m webbrowser -t "https://www.python.org"

.. availability:: not WASI, not Android.

The following exception is defined:


.. exception:: Error

   Exception raised when a browser control error occurs.

The following functions are defined:


.. function:: open(url, new=0, autoraise=True)

   Display *url* using the default browser. If *new* is 0, the *url* is opened
   in the same browser window if possible.  If *new* is 1, a new browser window
   is opened if possible.  If *new* is 2, a new browser page ("tab") is opened
   if possible.  If *autoraise* is ``True``, the window is raised if possible
   (note that under many window managers this will occur regardless of the
   setting of this variable).

   Returns ``True`` if a browser was successfully launched, ``False`` otherwise.

   Note that on some platforms, trying to open a filename using this function,
   may work and start the operating system's associated program.  However, this
   is neither supported nor portable.

   .. audit-event:: webbrowser.open url webbrowser.open


.. function:: open_new(url)

   Open *url* in a new window of the default browser, if possible, otherwise, open
   *url* in the only browser window.

   Returns ``True`` if a browser was successfully launched, ``False`` otherwise.


.. function:: open_new_tab(url)

   Open *url* in a new page ("tab") of the default browser, if possible, otherwise
   equivalent to :func:`open_new`.

   Returns ``True`` if a browser was successfully launched, ``False`` otherwise.


.. function:: get(using=None)

   Return a controller object for the browser type *using*.  If *using* is
   ``None``, return a controller for a default browser appropriate to the
   caller's environment.


.. function:: register(name, constructor, instance=None, *, preferred=False)

   Register the browser type *name*.  Once a browser type is registered, the
   :func:`get` function can return a controller for that browser type.  If
   *instance* is not provided, or is ``None``, *constructor* will be called without
   parameters to create an instance when needed.  If *instance* is provided,
   *constructor* will never be called, and may be ``None``.

   Setting *preferred* to ``True`` makes this browser a preferred result for
   a :func:`get` call with no argument.  Otherwise, this entry point is only
   useful if you plan to either set the :envvar:`BROWSER` variable or call
   :func:`get` with a nonempty argument matching the name of a handler you
   declare.

   .. versionchanged:: 3.7
      *preferred* keyword-only parameter was added.

A number of browser types are predefined.  This table gives the type names that
may be passed to the :func:`get` function and the corresponding instantiations
for the controller classes, all defined in this module.

+------------------------+-----------------------------------------+-------+
| Type Name              | Class Name                              | Notes |
+========================+=========================================+=======+
| ``'mozilla'``          | ``Mozilla('mozilla')``                  |       |
+------------------------+-----------------------------------------+-------+
| ``'firefox'``          | ``Mozilla('mozilla')``                  |       |
+------------------------+-----------------------------------------+-------+
| ``'epiphany'``         | ``Epiphany('epiphany')``                |       |
+------------------------+-----------------------------------------+-------+
| ``'kfmclient'``        | ``Konqueror()``                         | \(1)  |
+------------------------+-----------------------------------------+-------+
| ``'konqueror'``        | ``Konqueror()``                         | \(1)  |
+------------------------+-----------------------------------------+-------+
| ``'kfm'``              | ``Konqueror()``                         | \(1)  |
+------------------------+-----------------------------------------+-------+
| ``'opera'``            | ``Opera()``                             |       |
+------------------------+-----------------------------------------+-------+
| ``'links'``            | ``GenericBrowser('links')``             |       |
+------------------------+-----------------------------------------+-------+
| ``'elinks'``           | ``Elinks('elinks')``                    |       |
+------------------------+-----------------------------------------+-------+
| ``'lynx'``             | ``GenericBrowser('lynx')``              |       |
+------------------------+-----------------------------------------+-------+
| ``'w3m'``              | ``GenericBrowser('w3m')``               |       |
+------------------------+-----------------------------------------+-------+
| ``'windows-default'``  | ``WindowsDefault``                      | \(2)  |
+------------------------+-----------------------------------------+-------+
| ``'macos'``            | ``MacOS('default')``                    | \(3)  |
+------------------------+-----------------------------------------+-------+
| ``'safari'``           | ``MacOS('safari')``                     | \(3)  |
+------------------------+-----------------------------------------+-------+
| ``'chrome'``           | ``MacOS('google chrome')``              | \(3)  |
+------------------------+-----------------------------------------+-------+
| ``'firefox'``          | ``MacOS('firefox')``                    | \(3)  |
+------------------------+-----------------------------------------+-------+
| ``'google-chrome'``    | ``Chrome('google-chrome')``             |       |
+------------------------+-----------------------------------------+-------+
| ``'chromium'``         | ``Chromium('chromium')``                |       |
+------------------------+-----------------------------------------+-------+
| ``'chromium-browser'`` | ``Chromium('chromium-browser')``        |       |
+------------------------+-----------------------------------------+-------+
| ``'iosbrowser'``       | ``IOSBrowser``                          | \(4)  |
+------------------------+-----------------------------------------+-------+

Notes:

(1)
   "Konqueror" is the file manager for the KDE desktop environment for Unix, and
   only makes sense to use if KDE is running.  Some way of reliably detecting KDE
   would be nice; the :envvar:`!KDEDIR` variable is not sufficient.  Note also that
   the name "kfm" is used even when using the :program:`konqueror` command with KDE
   2 --- the implementation selects the best strategy for running Konqueror.

(2)
   Only on Windows platforms.

(3)
   Only on macOS.

(4)
   Only on iOS.

.. versionadded:: 3.2
   A new :class:`!MacOSXOSAScript` class has been added
   and is used on Mac instead of the previous :class:`!MacOSX` class.
   This adds support for opening browsers not currently set as the OS default.

.. versionadded:: 3.3
   Support for Chrome/Chromium has been added.

.. versionchanged:: 3.12
   Support for several obsolete browsers has been removed.
   Removed browsers include Grail, Mosaic, Netscape, Galeon,
   Skipstone, Iceape, and Firefox versions 35 and below.

.. versionchanged:: 3.13
   Support for iOS has been added.

.. versionadded:: 3.15
   :class:`!MacOS` has been added as a replacement for :class:`!MacOSXOSAScript`,
   opening browsers via :program:`/usr/bin/open` instead of :program:`osascript`.

.. deprecated-removed:: 3.15 3.17
   :class:`!MacOSXOSAScript` is deprecated in favour of :class:`!MacOS`.
   Using :program:`/usr/bin/open` instead of :program:`osascript` is a
   security and usability improvement: :program:`osascript` may be blocked
   on managed systems due to its abuse potential as a general-purpose
   scripting interpreter.

Here are some simple examples::

   url = 'https://docs.python.org/'

   # Open URL in a new tab, if a browser window is already open.
   webbrowser.open_new_tab(url)

   # Open URL in new window, raising the window if possible.
   webbrowser.open_new(url)


.. _browser-controllers:
