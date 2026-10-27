Installing free-threaded binaries
---------------------------------

.. versionadded:: 3.13

.. versionchanged:: 3.15
   Free-threading support is now installed by default.

The ``python.org`` :ref:`Python for macOS <getting-and-installing-macpython>`
installer package installs, by default, an additional build of
Python |version| that supports :term:`free threading`
(running with the :term:`global interpreter lock` disabled).
Check the release page on ``python.org`` for possible updated information.

The free-threaded mode is working and continues to be improved, but
there is some additional overhead in single-threaded workloads compared
to the regular build. Additionally, third-party packages, in particular ones
with an :term:`extension module`, may not be ready for use in a
free-threaded build, and will re-enable the :term:`GIL`.
As of Python 3.15, free-threading support is installed by default.
It is packaged as a separate install option, which can be deselected
by clicking the **Customize** button on the **Installation Type**
step of the installer as described above.

.. image:: mac_installer_09_custom_install_free_threaded.png

If the box next to the **Free-threaded Python** package name is checked
(as it is by default),
a separate :file:`PythonT.framework` will also be installed
alongside the normal :file:`Python.framework` in :file:`/Library/Frameworks`.
This configuration allows a free-threaded Python |version| build to co-exist
on your system with a traditional (GIL only) Python |version| build with
minimal risk while installing or testing. This installation layout may
change in future releases.

Known cautions and limitations:

- The **UNIX command-line tools** package, which is selected by default,
  will install links in :file:`/usr/local/bin` for |python_x_dot_y_t_literal|,
  the free-threaded interpreter, and |python_x_dot_y_t_literal_config|,
  a configuration utility which may be useful for package builders.
  Since :file:`/usr/local/bin` is typically included in your shell ``PATH``,
  in most cases no changes to your ``PATH`` environment variable should
  be needed to use |python_x_dot_y_t_literal|.

- For this release, the **Shell profile updater** package and the
  :file:`Update Shell Profile.command` in |applications_python_version_literal|
  do not support the free-threaded package.

- The free-threaded build and the traditional build have separate search
  paths and separate :file:`site-packages` directories so, by default,
  if you need a package available in both builds, it may need to be installed in both.
  The free-threaded package will install a separate instance of :program:`pip` for use
  with |python_x_dot_y_t_literal|.

  - To install a package using :command:`pip` without a :command:`venv`:

    .. parsed-literal::

       python\ |version|\ t -m pip install <package_name>

- When working with multiple Python environments, it is usually safest and easiest
  to :ref:`create and use virtual environments <tut-venv>`.
  This can avoid possible command name conflicts and confusion about which Python is in use:

  .. parsed-literal::

     python\ |version|\ t -m venv <venv_name>


  then :command:`activate`.

- To run a free-threaded version of IDLE:

  .. parsed-literal::

     python\ |version|\ t -m idlelib


- The interpreters in both builds respond to the same
  :ref:`PYTHON environment variables <using-on-envvars>`
  which may have unexpected results, for example, if you have ``PYTHONPATH``
  set in a shell profile. If necessary, there are
  :ref:`command line options <using-on-interface-options>` like ``-E``
  to ignore these environment variables.

- The free-threaded build links to the third-party shared libraries,
  such as ``OpenSSL`` and ``Tk``, installed in the traditional framework.
  This means that both builds also share one set of trust certificates
  as installed by the :command:`Install Certificates.command` script,
  thus it only needs to be run once.

- If you cannot depend on the link in ``/usr/local/bin`` pointing to the
  ``python.org`` free-threaded |python_x_dot_y_t_literal| (for example, if you want
  to install your own version there or some other distribution does),
  you can explicitly set your shell ``PATH`` environment variable to
  include the ``PythonT`` framework ``bin`` directory:

  .. parsed-literal::

     export PATH="/Library/Frameworks/PythonT.framework/Versions/\ |version|\ /bin":"$PATH"

  The traditional framework installation by default does something similar,
  except for :file:`Python.framework`. Be aware that having both framework ``bin``
  directories in ``PATH`` can lead to confusion if there are duplicate names
  like |python_x_dot_y_literal| in both; which one is actually used depends on the order
  they appear in ``PATH``. The ``which python3.x`` or ``which python3.xt``
  commands can show which path is being used. Using virtual environments
  can help avoid such ambiguities. Another option might be to create
  a shell :command:`alias` to the desired interpreter, like:

  .. parsed-literal::

     alias py\ |version|\ ="/Library/Frameworks/Python.framework/Versions/\ |version|\ /bin/python\ |version|\ "
     alias py\ |version|\ t="/Library/Frameworks/PythonT.framework/Versions/\ |version|\ /bin/python\ |version|\ t"
