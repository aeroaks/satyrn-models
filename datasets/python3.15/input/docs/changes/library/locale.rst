.. function:: setlocale(category, locale=None)

   If *locale* is given and not ``None``, :func:`setlocale` modifies the locale
   setting for the *category*. The available categories are listed in the data
   description below. *locale* may be a :ref:`string <locale_name>`, or a pair,
   language code and encoding. An empty string specifies the user's
   default settings. If the modification of the locale fails, the exception
   :exc:`Error` is raised. If successful, the new locale setting is returned.

   If *locale* is a pair, it is converted to a locale name using
   the locale aliasing engine.
   The language code has the same format as a :ref:`locale name <locale_name>`,
   but without encoding.
   The language code and encoding can be ``None``.

   If *locale* is omitted or ``None``, the current setting for *category* is
   returned.

   Example::

      >>> import locale
      >>> loc = locale.setlocale(locale.LC_ALL)  # get current locale
      # use German locale; name and availability varies with platform
      >>> locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
      >>> locale.strcoll('f\xe4n', 'foo')  # compare a string containing an umlaut
      >>> locale.setlocale(locale.LC_ALL, '')   # use user's preferred locale
      >>> locale.setlocale(locale.LC_ALL, 'C')  # use default (C) locale
      >>> locale.setlocale(locale.LC_ALL, loc)  # restore saved locale

   :func:`setlocale` is not thread-safe on most systems. Applications typically
   start with a call of::

      import locale
      locale.setlocale(locale.LC_ALL, '')

   This sets the locale for all categories to the user's default setting (typically
   specified in the :envvar:`LANG` environment variable).  If the locale is not
   changed thereafter, using multithreading should not cause problems.

   .. versionchanged:: 3.15
      Support language codes with ``@``-modifiers.



----

.. function:: getlocale(category=LC_CTYPE)

   Returns the current setting for the given locale category as a tuple containing
   the language code and encoding. *category* may be one of the :const:`!LC_\*`
   values except :const:`LC_ALL`.  It defaults to :const:`LC_CTYPE`.

   The language code has the same format as a :ref:`locale name <locale_name>`,
   but without encoding.
   The language code and encoding may be ``None`` if their values cannot be
   determined.
   The "C" locale is represented as ``(None, None)``.

   .. versionchanged:: 3.15
      ``@``-modifier are no longer silently removed, but included in
      the language code.

