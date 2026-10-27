.. classmethod:: date.fromtimestamp(timestamp)

   Return the local date corresponding to the POSIX *timestamp*, such as is
   returned by :func:`time.time`.

   This may raise :exc:`OverflowError`, if the timestamp is out
   of the range of values supported by the platform C :c:func:`localtime`
   function, and :exc:`OSError` on :c:func:`localtime` failure.
   It's common for this to be restricted to years from 1970 through 2038. Note
   that on non-POSIX systems that include leap seconds in their notion of a
   timestamp, leap seconds are ignored by :meth:`fromtimestamp`.

   .. versionchanged:: 3.3
      Raise :exc:`OverflowError` instead of :exc:`ValueError` if the timestamp
      is out of the range of values supported by the platform C
      :c:func:`localtime` function. Raise :exc:`OSError` instead of
      :exc:`ValueError` on :c:func:`localtime` failure.

   .. versionchanged:: 3.15
      Accepts any real number as *timestamp*, not only integer or float.



----

.. classmethod:: datetime.fromtimestamp(timestamp, tz=None)

   Return the local date and time corresponding to the POSIX timestamp, such as is
   returned by :func:`time.time`. If optional argument *tz* is ``None`` or not
   specified, the timestamp is converted to the platform's local date and time, and
   the returned :class:`.datetime` object is naive.

   If *tz* is not ``None``, it must be an instance of a :class:`tzinfo` subclass, and the
   timestamp is converted to *tz*’s time zone.

   :meth:`fromtimestamp` may raise :exc:`OverflowError`, if the timestamp is out of
   the range of values supported by the platform C :c:func:`localtime` or
   :c:func:`gmtime` functions, and :exc:`OSError` on :c:func:`localtime` or
   :c:func:`gmtime` failure.
   It's common for this to be restricted to years in
   1970 through 2038. Note that on non-POSIX systems that include leap seconds in
   their notion of a timestamp, leap seconds are ignored by :meth:`fromtimestamp`,
   and then it's possible to have two timestamps differing by a second that yield
   identical :class:`.datetime` objects. This method is preferred over
   :meth:`utcfromtimestamp`.

   .. versionchanged:: 3.3
      Raise :exc:`OverflowError` instead of :exc:`ValueError` if the timestamp
      is out of the range of values supported by the platform C
      :c:func:`localtime` or :c:func:`gmtime` functions. Raise :exc:`OSError`
      instead of :exc:`ValueError` on :c:func:`localtime` or :c:func:`gmtime`
      failure.

   .. versionchanged:: 3.6
      :meth:`fromtimestamp` may return instances with :attr:`.fold` set to 1.

   .. versionchanged:: 3.15
      Accepts any real number as *timestamp*, not only integer or float.



----

.. classmethod:: datetime.utcfromtimestamp(timestamp)

   Return the UTC :class:`.datetime` corresponding to the POSIX timestamp, with
   :attr:`.tzinfo` ``None``.  (The resulting object is naive.)

   This may raise :exc:`OverflowError`, if the timestamp is
   out of the range of values supported by the platform C :c:func:`gmtime` function,
   and :exc:`OSError` on :c:func:`gmtime` failure.
   It's common for this to be restricted to years in 1970 through 2038.

   To get an aware :class:`.datetime` object, call :meth:`fromtimestamp`::

     datetime.fromtimestamp(timestamp, timezone.utc)

   On the POSIX compliant platforms, it is equivalent to the following
   expression::

     datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=timestamp)

   except the latter formula always supports the full years range: between
   :const:`MINYEAR` and :const:`MAXYEAR` inclusive.

   .. warning::

      Because naive ``datetime`` objects are treated by many ``datetime`` methods
      as local times, it is preferred to use aware datetimes to represent times
      in UTC. As such, the recommended way to create an object representing a
      specific timestamp in UTC is by calling
      ``datetime.fromtimestamp(timestamp, tz=timezone.utc)``.

   .. versionchanged:: 3.3
      Raise :exc:`OverflowError` instead of :exc:`ValueError` if the timestamp
      is out of the range of values supported by the platform C
      :c:func:`gmtime` function. Raise :exc:`OSError` instead of
      :exc:`ValueError` on :c:func:`gmtime` failure.

   .. versionchanged:: 3.15
      Accepts any real number as *timestamp*, not only integer or float.

   .. deprecated:: 3.12

      Use :meth:`datetime.fromtimestamp` with :const:`UTC` instead.



----

.. classmethod:: datetime.strptime(date_string, format)

   Return a :class:`.datetime` corresponding to *date_string*, parsed according to
   *format*.

   If *format* does not contain microseconds or time zone information, this is equivalent to::

     datetime(*(time.strptime(date_string, format)[0:6]))

   :exc:`ValueError` is raised if the date_string and format
   can't be parsed by :func:`time.strptime` or if it returns a value which isn't a
   time tuple.  See also :ref:`strftime-strptime-behavior` and
   :meth:`datetime.fromisoformat`.

   .. versionchanged:: 3.15

      If *format* specifies a day of month (``%d``) without a year,
      :exc:`ValueError` is raised.  This is to avoid a quadrennial
      leap year bug in code seeking to parse only a month and day as the
      default year used in absence of one in the format is not a leap year.
      The workaround is to always include a year in your *format*.  If parsing
      *date_string* values that do not have a year, explicitly add a year that
      is a leap year before parsing:

      .. doctest::

         >>> import datetime as dt
         >>> date_string = "02/29"
         >>> when = dt.datetime.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
         >>> when.strftime("%B %d")  # doctest: +SKIP
         'February 29'



----

:meth:`!strftime` and :meth:`!strptime` format codes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These methods accept format codes that can be used to parse and format dates::

   >>> import datetime as dt
   >>> dt.datetime.strptime('31/01/22 23:59:59.999999',
   ...                      '%d/%m/%y %H:%M:%S.%f')
   datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
   >>> _.strftime('%a %d %b %Y, %I:%M%p')
   'Mon 31 Jan 2022, 11:59PM'

The following is a list of all the format codes that the 2011 C standard
requires, and these work on all supported platforms.

+-----------+--------------------------------+------------------------+-------+
| Directive |           Meaning              |        Example         | Notes |
|           |                                |                        |       |
+===========+================================+========================+=======+
|  ``%a``   | Weekday as locale's            || Sun, Mon, ..., Sat    | \(1)  |
|           | abbreviated name.              |  (en_US);              |       |
|           |                                || So, Mo, ..., Sa       |       |
|           |                                |  (de_DE)               |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%A``   | Weekday as locale's full name. || Sunday, Monday, ...,  | \(1)  |
|           |                                |  Saturday (en_US);     |       |
|           |                                || Sonntag, Montag, ..., |       |
|           |                                |  Samstag (de_DE)       |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%b``   | Month as locale's abbreviated  || Jan, Feb, ..., Dec    | \(1)  |
|           | name.                          |  (en_US);              |       |
|           |                                || Jan, Feb, ..., Dez    |       |
|           |                                |  (de_DE)               |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%B``   | Month as locale's full name.   || January, February,    | \(1)  |
|           |                                |  ..., December (en_US);|       |
|           |                                || Januar, Februar, ..., |       |
|           |                                |  Dezember (de_DE)      |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%c``   | Locale's appropriate date and  || Tue Aug 16 21:30:00   | \(1)  |
|           | time representation.           |  1988 (en_US);         |       |
|           |                                || Di 16 Aug 21:30:00    |       |
|           |                                |  1988 (de_DE)          |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%C``   | The year divided by 100 and    | 01, 02, ..., 99        | \(0)  |
|           | truncated to an integer as a   |                        |       |
|           | zero-padded decimal number.    |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%d``   | Day of the month as a          | 01, 02, ..., 31        | \(9), |
|           | zero-padded decimal number.    |                        | \(10) |
+-----------+--------------------------------+------------------------+-------+
|  ``%D``   | Equivalent to ``%m/%d/%y``.    | 11/28/25               | \(9)  |
|           |                                |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%e``   | The day of the month as a      | ␣1, ␣2, ..., 31        | \(10) |
|           | space-padded decimal number.   |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%F``   | Equivalent to ``%Y-%m-%d``,    | 2025-10-11,            |       |
|           | the ISO 8601 format.           | 1001-12-30             |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%g``   | Last 2 digits of ISO 8601 year | 00, 01, ..., 99        | \(0)  |
|           | representing the year that     |                        |       |
|           | contains the greater part of   |                        |       |
|           | the ISO week (``%V``).         |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%G``   | ISO 8601 year with century     | 0001, 0002, ..., 2013, | \(8)  |
|           | representing the year that     | 2014, ..., 9998, 9999  |       |
|           | contains the greater part of   |                        |       |
|           | the ISO week (``%V``).         |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%h``   | Equivalent to ``%b``.          | See ``%b``.            | \(0)  |
+-----------+--------------------------------+------------------------+-------+
|  ``%H``   | Hour (24-hour clock) as a      | 00, 01, ..., 23        | \(9)  |
|           | zero-padded decimal number.    |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%I``   | Hour (12-hour clock) as a      | 01, 02, ..., 12        | \(9)  |
|           | zero-padded decimal number.    |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%j``   | Day of the year as a           | 001, 002, ..., 366     | \(9)  |
|           | zero-padded decimal number.    |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%m``   | Month as a zero-padded         | 01, 02, ..., 12        | \(9)  |
|           | decimal number.                |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%M``   | Minute as a zero-padded        | 00, 01, ..., 59        | \(9)  |
|           | decimal number.                |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%n``   | The newline character          | ``\n``                 |       |
|           | (``'\n'``). For                |                        |       |
|           | :meth:`!strptime`, zero or     |                        |       |
|           | more whitespace.               |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%p``   | Locale's equivalent of either  || AM, PM (en_US);       | \(1), |
|           | AM or PM.                      || am, pm (de_DE)        | \(3)  |
+-----------+--------------------------------+------------------------+-------+
|  ``%r``   | Locale's 12-hour clock time.   | 12:00:00 AM            | \(1), |
|           |                                |                        | \(0)  |
+-----------+--------------------------------+------------------------+-------+
|  ``%R``   | Equivalent to ``%H:%M``.       | 10:01                  |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%S``   | Second as a zero-padded        | 00, 01, ..., 59        | \(4), |
|           | decimal number.                |                        | \(9)  |
+-----------+--------------------------------+------------------------+-------+
|  ``%t``   | The tab character (``'\t'``).  | ``\t``                 |       |
|           | For :meth:`!strptime`,         |                        |       |
|           | zero or more whitespace.       |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%T``   | ISO 8601 time format,          | 10:01:59               |       |
|           | equivalent to ``%H:%M:%S``.    |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%u``   | ISO 8601 weekday as a decimal  | 1, 2, ..., 7           |       |
|           | number where 1 is Monday.      |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%U``   | Week number of the year        | 00, 01, ..., 53        | \(7), |
|           | (Sunday as the first day of    |                        | \(9)  |
|           | the week) as a zero-padded     |                        |       |
|           | decimal number. All days in a  |                        |       |
|           | new year preceding the first   |                        |       |
|           | Sunday are considered to be in |                        |       |
|           | week 0.                        |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%V``   | ISO 8601 week as a decimal     | 01, 02, ..., 53        | \(8), |
|           | number with Monday as          |                        | \(9)  |
|           | the first day of the week.     |                        |       |
|           | Week 01 is the week containing |                        |       |
|           | Jan 4.                         |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%w``   | Weekday as a decimal number,   | 0, 1, ..., 6           |       |
|           | where 0 is Sunday and 6 is     |                        |       |
|           | Saturday.                      |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%W``   | Week number of the year        | 00, 01, ..., 53        | \(7), |
|           | (Monday as the first day of    |                        | \(9)  |
|           | the week) as a zero-padded     |                        |       |
|           | decimal number. All days in a  |                        |       |
|           | new year preceding the first   |                        |       |
|           | Monday are considered to be in |                        |       |
|           | week 0.                        |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%x``   | Locale's appropriate date      || 08/16/88 (None);      | \(1)  |
|           | representation.                || 08/16/1988 (en_US);   |       |
|           |                                || 16.08.1988 (de_DE)    |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%X``   | Locale's appropriate time      || 21:30:00 (en_US);     | \(1)  |
|           | representation.                || 21:30:00 (de_DE)      |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%y``   | Year without century as a      | 00, 01, ..., 99        | \(9)  |
|           | zero-padded decimal number.    |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%Y``   | Year with century as a decimal | 0001, 0002, ..., 2013, | \(2)  |
|           | number.                        | 2014, ..., 9998, 9999  |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%z``   | UTC offset in the form         | (empty), +0000,        | \(6)  |
|           | ``±HHMM[SS[.ffffff]]`` (empty  | -0400, +1030,          |       |
|           | string if the object is        | +063415,               |       |
|           | naive).                        | -030712.345216         |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%Z``   | Time zone name (empty string   | (empty), UTC, GMT      | \(6)  |
|           | if the object is naive).       |                        |       |
+-----------+--------------------------------+------------------------+-------+
|  ``%%``   | A literal ``'%'`` character.   | %                      |       |
+-----------+--------------------------------+------------------------+-------+

The ISO 8601 year and ISO 8601 week directives are not interchangeable
with the year and week number directives above. Calling :meth:`~.datetime.strptime` with
incomplete or ambiguous ISO 8601 directives will raise a :exc:`ValueError`.

Several additional directives not required by the C11 standard are included for
convenience.

+-----------+--------------------------------+------------------------+-------+
| Directive | Meaning                        | Example                | Notes |
+===========+================================+========================+=======+
|  ``%f``   | Microsecond as a decimal       | 000000, 000001, ...,   | \(5)  |
|           | number, zero-padded to 6       | 999999                 |       |
|           | digits.                        |                        |       |
+-----------+--------------------------------+------------------------+-------+
| ``%:z``   | UTC offset in the form         | (empty), +00:00,       | \(6)  |
|           | ``±HH:MM[:SS[.ffffff]]``       | -04:00, +10:30,        |       |
|           | (empty string if the object is | +06:34:15,             |       |
|           | naive).                        | -03:07:12.345216       |       |
+-----------+--------------------------------+------------------------+-------+

The full set of format codes supported varies across platforms, because Python
calls the platform C library's :c:func:`strftime` function, and platform
variations are common. To see the full set of format codes supported on your
platform, consult the :manpage:`strftime(3)` documentation. There are also
differences between platforms in handling of unsupported format specifiers.

.. versionadded:: 3.6
   ``%G``, ``%u`` and ``%V`` were added.

.. versionadded:: 3.12
   ``%:z`` was added for :meth:`~.datetime.strftime`.

.. versionadded:: 3.15
   ``%D``, ``%F``, ``%n``, ``%t``, and ``%:z`` were added for
   :meth:`~.datetime.strptime`.



----

Technical detail
^^^^^^^^^^^^^^^^

Broadly speaking, ``d.strftime(fmt)`` acts like the :mod:`time` module's
``time.strftime(fmt, d.timetuple())`` although not all objects support a
:meth:`~date.timetuple` method.

For the :meth:`.datetime.strptime` and :meth:`.date.strptime` class methods,
the default value is ``1900-01-01T00:00:00.000``: any components not specified
in the format string will be pulled from the default value.

.. note::
   Format strings without separators can be ambiguous for parsing. For
   example, with ``%Y%m%d``, the string ``2026111`` may be parsed either as
   ``2026-11-01`` or as ``2026-01-11``.
   Use separators to ensure the input is parsed as intended.

.. note::
   When used to parse partial dates lacking a year, :meth:`.datetime.strptime`
   and :meth:`.date.strptime` will raise when encountering February 29 because
   the default year of 1900 is *not* a leap year.  Always add a default leap
   year to partial date strings before parsing.

.. note::
   If a :meth:`~.datetime.strptime` format string contains more than
   one directive for the same field, for example both ``%Y`` and ``%y``,
   every directive must still match the input, but only the value of the
   last one is used. For example, parsing ``200099`` with ``%Y%y`` gives
   the year 1999. Repeating the same directive, like ``%Y%Y``, raises an error.

.. testsetup::

    # doctest seems to turn the warning into an error which makes it
    # show up and require matching and prevents the actual interesting
    # exception from being raised.
    # Manually apply the catch_warnings context manager
    import warnings
    catch_warnings = warnings.catch_warnings()
    catch_warnings.__enter__()
    warnings.simplefilter("ignore")

.. testcleanup::

    catch_warnings.__exit__()

.. doctest::

    >>> import datetime as dt
    >>> value = "2/29"
    >>> dt.datetime.strptime(value, "%m/%d")
    Traceback (most recent call last):
    ...
    ValueError: day 29 must be in range 1..28 for month 2 in year 1900
    >>> dt.datetime.strptime(f"1904 {value}", "%Y %m/%d")
    datetime.datetime(1904, 2, 29, 0, 0)

Using ``datetime.strptime(date_string, format)`` is equivalent to::

  datetime(*(time.strptime(date_string, format)[0:6]))

except when the format includes sub-second components or time zone offset
information, which are supported in ``datetime.strptime`` but are discarded by
``time.strptime``.

For :class:`.time` objects, the format codes for year, month, and day should not
be used, as :class:`!time` objects have no such values. If they're used anyway,
1900 is substituted for the year, and 1 for the month and day.

For :class:`date` objects, the format codes for hours, minutes, seconds, and
microseconds should not be used, as :class:`date` objects have no such
values. If they're used anyway, 0 is substituted for them.

For the same reason, handling of format strings containing Unicode code points
that can't be represented in the charset of the current locale is also
platform-dependent. On some platforms such code points are preserved intact in
the output, while on others ``strftime`` may raise :exc:`UnicodeError` or return
an empty string instead.

Notes:

(0)
   This format code is currently unsupported by :meth:`~.datetime.strptime`.

(1)
   Because the format depends on the current locale, care should be taken when
   making assumptions about the output value. Field orderings will vary (for
   example, "month/day/year" versus "day/month/year"), and the output may
   contain non-ASCII characters.

(2)
   The :meth:`~.datetime.strptime` method can parse years in the full [1, 9999] range, but
   years < 1000 must be zero-filled to 4-digit width.

   .. versionchanged:: 3.2
      In previous versions, :meth:`~.datetime.strftime` method was restricted to
      years >= 1900.

   .. versionchanged:: 3.3
      In version 3.2, :meth:`~.datetime.strftime` method was restricted to
      years >= 1000.

(3)
   When used with the :meth:`~.datetime.strptime` method, the ``%p`` directive only affects
   the output hour field if the ``%I`` directive is used to parse the hour.

(4)
   Unlike the :mod:`time` module, the :mod:`!datetime` module does not support
   leap seconds.

(5)
   When used with the :meth:`~.datetime.strptime` method, the ``%f`` directive
   accepts from one to six digits and zero pads on the right. ``%f`` is
   an extension to the set of format characters in the C standard (but
   implemented separately in datetime objects, and therefore always
   available).

(6)
   For a naive object, the ``%z``, ``%:z`` and ``%Z`` format codes are replaced
   by empty strings.

   For an aware object:

   ``%z``
      :meth:`~.datetime.utcoffset` is transformed into a string of the form
      ``±HHMM[SS[.ffffff]]``, where ``HH`` is a 2-digit string giving the number
      of UTC offset hours, ``MM`` is a 2-digit string giving the number of UTC
      offset minutes, ``SS`` is a 2-digit string giving the number of UTC offset
      seconds and ``ffffff`` is a 6-digit string giving the number of UTC
      offset microseconds. The ``ffffff`` part is omitted when the offset is a
      whole number of seconds and both the ``ffffff`` and the ``SS`` part is
      omitted when the offset is a whole number of minutes. For example, if
      :meth:`~.datetime.utcoffset` returns ``timedelta(hours=-3, minutes=-30)``, ``%z`` is
      replaced with the string ``'-0330'``.

   .. versionchanged:: 3.7
      The UTC offset is not restricted to a whole number of minutes.

   .. versionchanged:: 3.7
      When the ``%z`` directive is provided to the  :meth:`~.datetime.strptime` method,
      the UTC offsets can have a colon as a separator between hours, minutes
      and seconds.
      For example, both ``'+010000'`` and ``'+01:00:00'`` will be parsed as an offset
      of one hour. In addition, providing ``'Z'`` is identical to ``'+00:00'``.

   ``%:z``
      When used with :meth:`~.datetime.strftime`, behaves exactly as ``%z``,
      except that a colon separator is added between hours, minutes and seconds.

      When used with :meth:`~.datetime.strptime`, the UTC offset is *required*
      to have a colon as a separator between hours, minutes and seconds.
      For example, ``'+01:00:00'`` (but *not* ``'+010000'``) will be parsed as
      an offset of one hour. In addition, providing ``'Z'`` is identical to
      ``'+00:00'``.

   ``%Z``
      In :meth:`~.datetime.strftime`, ``%Z`` is replaced by an empty string if
      :meth:`~.datetime.tzname` returns ``None``; otherwise ``%Z`` is replaced by the
      returned value, which must be a string.

      :meth:`~.datetime.strptime` only accepts certain values for ``%Z``:

      1. any value in ``time.tzname`` for your machine's locale
      2. the hard-coded values ``UTC`` and ``GMT``

      So someone living in Japan may have ``JST``, ``UTC``, and ``GMT`` as
      valid values, but probably not ``EST``. It will raise ``ValueError`` for
      invalid values.

   .. versionchanged:: 3.2
      When the ``%z`` directive is provided to the :meth:`~.datetime.strptime` method, an
      aware :class:`.datetime` object will be produced. The ``tzinfo`` of the
      result will be set to a :class:`timezone` instance.

(7)
   When used with the :meth:`~.datetime.strptime` method, ``%U`` and ``%W`` are only used
   in calculations when the day of the week and the calendar year (``%Y``)
   are specified.

(8)
   Similar to ``%U`` and ``%W``, ``%V`` is only used in calculations when the
   day of the week and the ISO year (``%G``) are specified in a
   :meth:`~.datetime.strptime` format string. Also note that ``%G`` and ``%Y`` are not
   interchangeable.

(9)
   When used with the :meth:`~.datetime.strptime` method, the leading zero is optional
   for  formats ``%d``, ``%m``, ``%H``, ``%I``, ``%M``, ``%S``, ``%j``, ``%U``,
   ``%W``, and ``%V``. Format ``%y`` does require a leading zero.

(10)
   When parsing a month and day using :meth:`~.datetime.strptime`, always
   include a year in the format.  If the value you need to parse lacks a year,
   append an explicit dummy leap year.  Otherwise your code will raise an
   exception when it encounters leap day because the default year used by the
   parser (1900) is not a leap year.  Users run into that bug every leap year.

   .. doctest::

      >>> month_day = "02/29"
      >>> dt.datetime.strptime(f"{month_day};1984", "%m/%d;%Y")  # No leap year bug.
      datetime.datetime(1984, 2, 29, 0, 0)

   .. versionchanged:: 3.15
      Using ``%d`` without a year now raises :exc:`ValueError`.

   .. deprecated-removed:: 3.15 3.17
      :meth:`~.datetime.strptime` calls using a format string containing
      ``%e`` without a year now emit a :exc:`DeprecationWarning`.

.. rubric:: Footnotes

.. [#] If, that is, we ignore the effects of relativity.

.. [#] This matches the definition of the "proleptic Gregorian" calendar in
       Dershowitz and Reingold's book *Calendrical Calculations*,
       where it's the base calendar for all computations. See the book for
       algorithms for converting between proleptic Gregorian ordinals and
       many other calendar systems.

.. [#] See R. H. van Gent's `guide to the mathematics of the ISO 8601 calendar
       <https://web.archive.org/web/20220531051136/https://webspace.science.uu.nl/~gent0113/calendar/isocalendar.htm>`_
       for a good explanation.