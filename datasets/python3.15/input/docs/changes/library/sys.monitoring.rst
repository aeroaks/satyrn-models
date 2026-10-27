Other events
''''''''''''

Other events are not necessarily tied to a specific location in the
program and cannot be individually disabled per location.

The other events that can be monitored are:

* :monitoring-event:`PY_THROW`
* :monitoring-event:`PY_UNWIND`
* :monitoring-event:`RAISE`
* :monitoring-event:`EXCEPTION_HANDLED`
* :monitoring-event:`RERAISE`

.. versionchanged:: 3.15
   Other events can now be turned on and disabled on a per code object
   basis. Returning :data:`DISABLE` from a callback disables the event
   for the entire code object (for the current tool).

