    .. method:: ensure_directories(env_dir)

        Creates the environment directory and all necessary subdirectories that
        don't already exist, and returns a context object.  This context object
        is just a holder for attributes (such as paths) for use by the other
        methods.  If the :class:`EnvBuilder` is created with the arg
        ``clear=True``, contents of the environment directory will be cleared
        and then all necessary subdirectories will be recreated.

        The returned context object is a :class:`types.SimpleNamespace` with the
        following attributes:

        * ``env_dir`` - The location of the virtual environment. Used for
          ``__VENV_DIR__`` in activation scripts (see :meth:`install_scripts`).

        * ``env_name`` - The name of the virtual environment. Used for
          ``__VENV_NAME__`` in activation scripts (see :meth:`install_scripts`).

        * ``prompt`` - The prompt to be used by the activation scripts. Used for
          ``__VENV_PROMPT__`` in activation scripts (see :meth:`install_scripts`).

        * ``executable`` - The underlying Python executable used by the virtual
          environment. This takes into account the case where a virtual environment
          is created from another virtual environment.

        * ``inc_path`` - The include path for the virtual environment.

        * ``lib_path`` - The purelib path for the virtual environment.

        * ``platlib_path`` - The platlib path for the virtual environment.

        * ``bin_path`` - The script path for the virtual environment.

        * ``bin_name`` - The name of the script path relative to the virtual
          environment location. Used for ``__VENV_BIN_NAME__`` in activation
          scripts (see :meth:`install_scripts`).

        * ``env_exe`` - The name of the Python interpreter in the virtual
          environment. Used for ``__VENV_PYTHON__`` in activation scripts
          (see :meth:`install_scripts`).

        * ``env_exec_cmd`` - The name of the Python interpreter, taking into
          account filesystem redirections. This can be used to run Python in
          the virtual environment.


        .. versionchanged:: 3.11
           The *venv*
           :ref:`sysconfig installation scheme <installation_paths>`
           is used to construct the paths of the created directories.

        .. versionchanged:: 3.12
           The attribute ``lib_path`` was added to the context, and the context
           object was documented.

        .. versionchanged:: 3.15
           The attribute ``platlib_path`` was added to the context.
