.. method:: xmlparser.SetBillionLaughsAttackProtectionActivationThreshold(threshold, /)

   Sets the number of output bytes needed to activate protection against
   `billion laughs`_ attacks.

   The number of output bytes includes amplification from entity expansion
   and reading DTD files.

   Parser objects usually have a protection activation threshold of 8 MiB,
   but the actual default value depends on the underlying Expat library.

   An :exc:`ExpatError` is raised if this method is called on a
   |xml-non-root-parser| parser.
   The corresponding :attr:`~ExpatError.lineno` and :attr:`~ExpatError.offset`
   should not be used as they may have no special meaning.

   :meth:`!SetBillionLaughsAttackProtectionActivationThreshold`
   has been backported to some prior releases of CPython as a security fix.
   Check for availability using :func:`hasattr` if used in code running
   across a variety of Python versions.

   .. note::

      Activation thresholds below 4 MiB are known to break support for DITA 1.3
      payload and are hence not recommended.

   .. versionadded:: 3.15


----

.. method:: xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification(max_factor, /)

   Sets the maximum tolerated amplification factor for protection against
   `billion laughs`_ attacks.

   The amplification factor is calculated as ``(direct + indirect) / direct``
   while parsing, where ``direct`` is the number of bytes read from
   the primary document in parsing and ``indirect`` is the number of
   bytes added by expanding entities and reading of external DTD files.

   The *max_factor* value must be a non-NaN :class:`float` value greater than
   or equal to 1.0. Peak amplifications of factor 15,000 for the entire payload
   and of factor 30,000 in the middle of parsing have been observed with small
   benign files in practice. In particular, the activation threshold should be
   carefully chosen to avoid false positives.

   Parser objects usually have a maximum amplification factor of 100,
   but the actual default value depends on the underlying Expat library.

   An :exc:`ExpatError` is raised if this method is called on a
   |xml-non-root-parser| parser or if *max_factor* is outside the valid range.
   The corresponding :attr:`~ExpatError.lineno` and :attr:`~ExpatError.offset`
   should not be used as they may have no special meaning.

   :meth:`!SetBillionLaughsAttackProtectionMaximumAmplification`
   has been backported to some prior releases of CPython as a security fix.
   Check for availability using :func:`hasattr` if used in code running
   across a variety of Python versions.

   .. note::

      The maximum amplification factor is only considered if the threshold
      that can be adjusted by :meth:`.SetBillionLaughsAttackProtectionActivationThreshold`
      is exceeded.

   .. versionadded:: 3.15


----

.. method:: xmlparser.SetAllocTrackerActivationThreshold(threshold, /)

   Sets the number of allocated bytes of dynamic memory needed to activate
   protection against disproportionate use of RAM.

   Parser objects usually have an allocation activation threshold of 64 MiB,
   but the actual default value depends on the underlying Expat library.

   An :exc:`ExpatError` is raised if this method is called on a
   |xml-non-root-parser| parser.
   The corresponding :attr:`~ExpatError.lineno` and :attr:`~ExpatError.offset`
   should not be used as they may have no special meaning.

   :meth:`!SetAllocTrackerActivationThreshold`
   has been backported to some prior releases of CPython as a security fix.
   Check for availability using :func:`hasattr` if used in code running
   across a variety of Python versions.

   .. versionadded:: 3.15


----

.. method:: xmlparser.SetAllocTrackerMaximumAmplification(max_factor, /)

   Sets the maximum amplification factor between direct input and bytes
   of dynamic memory allocated.

   The amplification factor is calculated as ``allocated / direct``
   while parsing, where ``direct`` is the number of bytes read from
   the primary document in parsing and ``allocated`` is the number
   of bytes of dynamic memory allocated in the parser hierarchy.

   The *max_factor* value must be a non-NaN :class:`float` value greater than
   or equal to 1.0. Amplification factors greater than 100.0 can be observed
   near the start of parsing even with benign files in practice. In particular,
   the activation threshold should be carefully chosen to avoid false positives.

   Parser objects usually have a maximum amplification factor of 100,
   but the actual default value depends on the underlying Expat library.

   An :exc:`ExpatError` is raised if this method is called on a
   |xml-non-root-parser| parser or if *max_factor* is outside the valid range.
   The corresponding :attr:`~ExpatError.lineno` and :attr:`~ExpatError.offset`
   should not be used as they may have no special meaning.

   :meth:`!SetAllocTrackerMaximumAmplification`
   has been backported to some prior releases of CPython as a security fix.
   Check for availability using :func:`hasattr` if used in code running
   across a variety of Python versions.

   .. note::

      The maximum amplification factor is only considered if the threshold
      that can be adjusted by :meth:`.SetAllocTrackerActivationThreshold`
      is exceeded.

   .. versionadded:: 3.15

