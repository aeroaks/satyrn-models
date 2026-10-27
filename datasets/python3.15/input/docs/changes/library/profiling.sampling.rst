:mod:`!profiling.sampling` --- Statistical profiler
***************************************************

.. module:: profiling.sampling
   :synopsis: Statistical sampling profiler for Python processes.

.. versionadded:: 3.15

**Source code:** :source:`Lib/profiling/sampling/`

.. program:: profiling.sampling

--------------

.. image:: ../../Lib/profiling/sampling/_assets/tachyon-logo.png
   :alt: Tachyon logo
   :align: center
   :width: 300px

The :mod:`!profiling.sampling` module, named **Tachyon**, provides statistical
profiling of Python programs through periodic stack sampling. Tachyon can
run scripts directly or attach to any running Python process without requiring
code changes or restarts. Because sampling occurs externally to the target
process, overhead is virtually zero, making Tachyon suitable for both
development and production environments.


What is statistical profiling?
==============================

Statistical profiling builds a picture of program behavior by periodically
capturing snapshots of the call stack. Rather than instrumenting every function
call and return as deterministic profilers do, Tachyon reads the call stack at
regular intervals to record what code is currently running.

This approach rests on a simple principle: functions that consume significant
CPU time will appear frequently in the collected samples. By gathering thousands
of samples over a profiling session, Tachyon constructs an accurate statistical
estimate of where time is spent. The more samples collected, the
more precise this estimate becomes.

.. only:: html

   The following interactive visualization demonstrates how sampling profiling
   works. Press **Play** to watch a Python program execute, and observe how the
   profiler periodically captures snapshots of the call stack. Adjust the
   **sample interval** to see how sampling frequency affects the results.

   .. raw:: html
      :file: profiling-sampling-visualization.html

.. only:: not html

   .. note::

      An interactive visualization of sampling profiling is available in the
      HTML version of this documentation.


How time is estimated
---------------------

The time values shown in Tachyon's output are **estimates derived from sample
counts**, not direct measurements. Tachyon counts how many times each function
appears in the collected samples, then multiplies by the sampling interval to
estimate time.

For example, with a 10 kHz sampling rate over a 10-second profile,
Tachyon collects approximately 100,000 samples. If a function appears in 5,000
samples (5% of total), Tachyon estimates it consumed 5% of the 10-second
duration, or about 500 milliseconds. This is a statistical estimate, not a
precise measurement.

The accuracy of these estimates depends on sample count. With 100,000 samples,
a function showing 5% has a margin of error of roughly ±0.5%. With only 1,000
samples, the same 5% measurement could actually represent anywhere from 3% to
7% of real time.

This is why longer profiling durations and shorter sampling intervals produce
more reliable results---they collect more samples. For most performance
analysis, the default settings provide sufficient accuracy to identify
bottlenecks and guide optimization efforts.

Because sampling is statistical, results will vary slightly between runs. A
function showing 12% in one run might show 11% or 13% in the next. This is
normal and expected. Focus on the overall pattern rather than exact percentages,
and don't worry about small variations between runs.


When to use a different approach
--------------------------------

Statistical sampling is not ideal for every situation.

For very short scripts that complete in under one second, the profiler may not
collect enough samples for reliable results. Use :mod:`profiling.tracing`
instead, or run the script in a loop to extend profiling time.

When you need exact call counts, sampling cannot provide them. Sampling
estimates frequency from snapshots, so if you need to know precisely how many
times a function was called, use :mod:`profiling.tracing`.

When comparing two implementations where the difference might be only 1-2%,
sampling noise can obscure real differences. Use :mod:`timeit` for
micro-benchmarks or :mod:`profiling.tracing` for precise measurements.
