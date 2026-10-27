.. function:: get_stats()

   Return a list of three per-generation dictionaries containing collection
   statistics since interpreter start.  The number of keys may change
   in the future, but currently each dictionary will contain the following
   items:

   * ``collections`` is the number of times this generation was collected;

   * ``collected`` is the total number of objects collected inside this
     generation;

   * ``uncollectable`` is the total number of objects which were found
     to be uncollectable (and were therefore moved to the :data:`garbage`
     list) inside this generation;

   * ``candidates`` is the total number of objects in this generation which were
     considered for collection and traversed;

   * ``duration`` is the total time in seconds spent in collections for this
     generation.

   .. versionadded:: 3.4

   .. versionchanged:: 3.15
      Add ``duration`` and ``candidates``.



----

.. data:: callbacks

   A list of callbacks that will be invoked by the garbage collector before and
   after collection.  The callbacks will be called with two arguments,
   *phase* and *info*.

   *phase* can be one of two values:

      "start": The garbage collection is about to start.

      "stop": The garbage collection has finished.

   *info* is a dict providing more information for the callback.  The following
   keys are currently defined:

      "generation": The oldest generation being collected.

      "collected": When *phase* is "stop", the number of objects
      successfully collected.

      "uncollectable": When *phase* is "stop", the number of objects
      that could not be collected and were put in :data:`garbage`.

      "candidates": When *phase* is "stop", the total number of objects in this
      generation which were considered for collection and traversed.

      "duration": When *phase* is "stop", the time in seconds spent in the
      collection.

   Applications can add their own callbacks to this list.  The primary
   use cases are:

      Gathering statistics about garbage collection, such as how often
      various generations are collected, and how long the collection
      takes.

      Allowing applications to identify and clear their own uncollectable
      types when they appear in :data:`garbage`.

   .. versionadded:: 3.3

   .. versionchanged:: 3.15
      Add "duration" and "candidates".

