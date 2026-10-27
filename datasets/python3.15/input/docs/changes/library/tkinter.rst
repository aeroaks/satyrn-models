   .. method:: grid_content(row=None, column=None)

      Same as :meth:`grid_slaves`: return the child widgets managed in this
      container's grid, optionally restricted to a given *row* or *column*.

      .. versionadded:: 3.15



----

   .. method:: pack_content()

      Same as :meth:`pack_slaves`: return the child widgets managed by this
      container with the pack geometry manager, in packing order.

      :meth:`content` is an alias of :meth:`!pack_content`.

      .. versionadded:: 3.15



----

   .. method:: place_content()

      Same as :meth:`place_slaves`: return the child widgets managed by this
      container with the place geometry manager.

      .. versionadded:: 3.15


----

   .. method:: pack_content()

      Same as :meth:`Misc.pack_content`.
      :meth:`content` is an alias of :meth:`!pack_content`.

      .. versionadded:: 3.15


.. class:: Place()

   Geometry manager that places widgets at explicit positions and sizes within
   their container.
   The :class:`!Place` mix-in is inherited by all widgets (through
   :class:`Widget`).
   See also :ref:`tkinter-geometry-management`.

   .. method:: configure(cnf={}, **kw)
      :no-typesetting:

   .. method:: config(cnf={}, **kw)
      :no-typesetting:

   .. method:: place_configure(cnf={}, **kw)
               place(cnf={}, **kw)

      Place the widget inside its container at an absolute or relative
      position.
      The supported options are:

      *x*, *y*
         The absolute horizontal and vertical position of the widget's anchor
         point, as a screen distance (default ``0``).

      *relx*, *rely*
         The horizontal and vertical position of the widget's anchor point as a
         fraction of the container's width and height, where ``0.0`` is the
         left or top edge and ``1.0`` is the right or bottom edge.
         If both the absolute and the relative option are given, their values
         are summed.

      *anchor*
         Which point of the widget is placed at the given position: an anchor
         such as ``'n'`` or ``'se'`` (default ``'nw'``).

      *width*, *height*
         The absolute width and height of the widget, as a screen distance.
         By default the widget's requested size is used.

      *relwidth*, *relheight*
         The width and height of the widget as a fraction of the container's
         width and height.
         If both the absolute and the relative option are given, their values
         are summed.

      *bordermode*
         How the container's border affects placement: ``'inside'`` (the
         default) measures the area inside the border, ``'outside'`` measures
         the area including the border, and ``'ignore'`` uses the official X
         area.

      *in_*
         The container relative to which the widget is placed; it must be the
         widget's parent or a descendant of the parent, and defaults to the
         parent.

      :meth:`place`, :meth:`configure` and :meth:`config` are aliases of
      :meth:`!place_configure`.

   .. method:: forget()
      :no-typesetting:

   .. method:: place_forget()

      Unmap the widget and remove it from the placement, forgetting its place
      options.

   .. method:: info()
      :no-typesetting:

   .. method:: place_info()

      Return a dictionary of the widget's current place options.

   .. method:: slaves()
      :no-typesetting:

   .. method:: place_slaves()

      Same as :meth:`Misc.place_slaves`: return the list of widgets placed in
      this widget.

   .. method:: content()
      :no-typesetting:

   .. method:: place_content()

      Same as :meth:`Misc.place_content`.

      .. versionadded:: 3.15


.. class:: Grid()

   Geometry manager that arranges widgets in a two-dimensional grid of rows and
   columns within their container.
   The :class:`!Grid` mix-in is inherited by all widgets (through
   :class:`Widget`).
   See also :ref:`tkinter-geometry-management`.

   .. method:: configure(cnf={}, **kw)
      :no-typesetting:

   .. method:: config(cnf={}, **kw)
      :no-typesetting:

   .. method:: grid_configure(cnf={}, **kw)
               grid(cnf={}, **kw)

      Position the widget in a cell of its container's grid.

      Not to be confused with :meth:`Wm.grid`.

      The supported options are:

      *row*, *column*
         The row and column of the cell to place the widget in, counting from
         ``0``.
         *column* defaults to the column after the previous widget placed in
         the same :meth:`!grid_configure` call (or ``0``), and *row* defaults
         to the next empty row.

      *rowspan*, *columnspan*
         The number of rows and columns the widget should span (default ``1``).

      *sticky*
         How to position or stretch the widget when its cell is larger than the
         widget: a string containing zero or more of the characters ``'n'``,
         ``'s'``, ``'e'`` and ``'w'``, naming the cell sides the widget sticks
         to.
         Specifying both ``'n'`` and ``'s'`` (or ``'e'`` and ``'w'``) stretches
         the widget to fill the height (or width) of the cell.
         The default is ``''``, which centers the widget at its requested size.

      *ipadx*, *ipady*
         Internal padding added on the left and right (*ipadx*) or top and
         bottom (*ipady*) of the widget, as a screen distance (default ``0``).

      *padx*, *pady*
         External padding left on the left and right (*padx*) or top and bottom
         (*pady*) of the widget, as a screen distance or a pair of two
         distances for the two sides (default ``0``).

      *in_*
         The container in whose grid to place the widget; it defaults to the
         parent widget.

      :meth:`grid`, :meth:`configure` and :meth:`config` are aliases of
      :meth:`!grid_configure`.

   .. method:: forget()
      :no-typesetting:

   .. method:: grid_forget()

      Unmap the widget and remove it from the grid, forgetting its grid
      options.

   .. method:: grid_remove()

      Unmap the widget and remove it from the grid, but remember its grid
      options so that it is restored to the same cell if it is gridded again.

   .. method:: info()
      :no-typesetting:

   .. method:: grid_info()

      Return a dictionary of the widget's current grid options.

   .. method:: bbox(column=None, row=None, col2=None, row2=None)
      :no-typesetting:

   .. method:: grid_bbox(column=None, row=None, col2=None, row2=None)

      Same as :meth:`Misc.grid_bbox`.
      :meth:`bbox` is an alias of :meth:`!grid_bbox`,
      except on :class:`Canvas`, :class:`Listbox`, :class:`Spinbox`,
      :class:`Text`, :class:`ttk.Entry <tkinter.ttk.Entry>` and
      :class:`ttk.Treeview <tkinter.ttk.Treeview>`,
      which provide their own :meth:`!bbox` method.

   .. method:: columnconfigure(index, cnf={}, **kw)
      :no-typesetting:

   .. method:: grid_columnconfigure(index, cnf={}, **kw)

      Same as :meth:`Misc.grid_columnconfigure`: query or set the options (such
      as *weight*, *minsize*, *pad* and *uniform*) of a grid column.
      :meth:`columnconfigure` is an alias of :meth:`!grid_columnconfigure`.

   .. method:: rowconfigure(index, cnf={}, **kw)
      :no-typesetting:

   .. method:: grid_rowconfigure(index, cnf={}, **kw)

      Same as :meth:`Misc.grid_rowconfigure`: query or set the options of a
      grid row.
      :meth:`rowconfigure` is an alias of :meth:`!grid_rowconfigure`.

   .. method:: location(x, y)
      :no-typesetting:

   .. method:: grid_location(x, y)

      Same as :meth:`Misc.grid_location`: return the ``(column, row)`` of the
      cell that covers the pixel at *x*, *y*.
      :meth:`location` is an alias of :meth:`!grid_location`.

   .. method:: size()
      :no-typesetting:

   .. method:: grid_size()

      Same as :meth:`Misc.grid_size`: return a ``(columns, rows)`` tuple giving
      the size of the grid.
      :meth:`size` is an alias of :meth:`!grid_size`,
      except on the :class:`Listbox` widget,
      which provides its own :meth:`!size` method.

   .. method:: propagate()
               propagate(flag)
      :no-typesetting:

   .. method:: grid_propagate()
               grid_propagate(flag)

      Same as :meth:`Misc.grid_propagate`.

   .. method:: slaves(row=None, column=None)
      :no-typesetting:

   .. method:: grid_slaves(row=None, column=None)

      Same as :meth:`Misc.grid_slaves`: return the widgets managed in the grid,
      optionally restricted to a *row* and/or *column*.

   .. method:: content(row=None, column=None)
      :no-typesetting:

   .. method:: grid_content(row=None, column=None)

      Same as :meth:`Misc.grid_content`.

      .. versionadded:: 3.15


.. class:: XView()

   Mix-in providing the horizontal-scrolling interface shared by widgets such
   as :class:`Entry`, :class:`Canvas`, :class:`Listbox`, :class:`Text` and
   :class:`Spinbox`.
   A widget's :meth:`xview` method is registered as the *command* of a
   horizontal :class:`Scrollbar`.

   .. method:: xview(*args)

      Query or change the horizontal position of the view.
      With no arguments, return a tuple ``(first, last)`` of two fractions
      between 0 and 1 giving the portion of the document that is currently
      visible.
      Otherwise the arguments are passed to the Tk ``xview`` widget command and
      are usually generated by a scrollbar; :meth:`xview_moveto` and
      :meth:`xview_scroll` provide a more convenient interface.

   .. method:: xview_moveto(fraction)

      Adjust the view so that *fraction* of the total width of the document is
      off-screen to the left.
      *fraction* is a number between 0 and 1.

   .. method:: xview_scroll(number, what)

      Shift the view left or right by *number* units.
      *what* is either ``'units'`` or ``'pages'``; a negative *number* scrolls
      left and a positive one scrolls right.
      The :class:`Text` widget accepts also ``'pixels'``,
      and then *number* can be a screen distance, such as ``'1i'``.


.. class:: YView()

   Mix-in providing the vertical-scrolling interface shared by widgets such as
   :class:`Canvas`, :class:`Listbox` and :class:`Text`.
   A widget's :meth:`yview` method is registered as the *command* of a vertical
   :class:`Scrollbar`.

   .. method:: yview(*args)

      Query or change the vertical position of the view.
      With no arguments, return a tuple ``(first, last)`` of two fractions
      between 0 and 1 giving the portion of the document that is currently
      visible.
      Otherwise the arguments are passed to the Tk ``yview`` widget command,
      usually generated by a scrollbar; :meth:`yview_moveto` and
      :meth:`yview_scroll` provide a more convenient interface.

   .. method:: yview_moveto(fraction)

      Adjust the view so that *fraction* of the total height of the document is
      off-screen above the top.
      *fraction* is a number between 0 and 1.

   .. method:: yview_scroll(number, what)

      Shift the view up or down by *number* units.
      *what* is either ``'units'`` or ``'pages'``; a negative *number* scrolls
      up and a positive one scrolls down.
      The :class:`Text` widget accepts also ``'pixels'``,
      and then *number* can be a screen distance, such as ``'1i'``.


.. class:: BaseWidget(master, widgetName, cnf={}, kw={}, extra=())

   Internal base class for all widgets.
   It inherits from :class:`Misc` and adds the machinery that creates the
   underlying Tk widget; application code normally uses :class:`Widget` or a
   concrete widget class rather than instantiating :class:`!BaseWidget`
   directly.

   .. method:: destroy()

      Destroy this widget and all of its children, removing the corresponding
      Tk widgets and deleting the associated Tcl commands.


.. class:: Widget(master, widgetName, cnf={}, kw={}, extra=())

   Internal base class for the standard widgets.
   It combines :class:`BaseWidget` with the geometry-manager mix-ins
   :class:`Pack`, :class:`Place` and :class:`Grid`, so that every widget can be
   managed by any of the three geometry managers.
   The concrete widget classes (:class:`Button`, :class:`Label`, and so on)
   derive from :class:`!Widget`.


Toplevel widgets
^^^^^^^^^^^^^^^^

.. class:: Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)

   Construct a toplevel Tk widget, which is usually the main window of an
   application, and initialize a Tcl interpreter for this widget.  Each
   instance has its own associated Tcl interpreter.
   Inherits from :class:`Misc` and :class:`Wm`.

   To create a Tcl interpreter without initializing the Tk subsystem, use the
   :func:`Tcl` factory function instead.

   The :class:`Tk` class is typically instantiated using all default values.
   However, the following keyword arguments are currently recognized:

   *screenName*
      When given (as a string), sets the :envvar:`DISPLAY` environment
      variable. (X11 only)
   *baseName*
      Name of the profile file.  By default, *baseName* is derived from the
      program name (``sys.argv[0]``).
   *className*
      Name of the widget class.  Used as a profile file and also as the name
      with which Tcl is invoked (*argv0* in *interp*).
   *useTk*
      If ``True``, initialize the Tk subsystem.  The :func:`tkinter.Tcl() <Tcl>`
      function sets this to ``False``.
   *sync*
      If ``True``, execute all X server commands synchronously, so that errors
      are reported immediately.  Can be used for debugging. (X11 only)
   *use*
      Specifies the *id* of the window in which to embed the application,
      instead of it being created as an independent toplevel window. *id* must
      be specified in the same way as the value for the -use option for
      toplevel widgets (that is, it has a form like that returned by
      :meth:`~Misc.winfo_id`).

      Note that on some platforms this will only work correctly if *id* refers
      to a Tk frame or toplevel that has its -container option enabled.

   :class:`Tk` reads and interprets profile files, named
   :file:`.{className}.tcl` and :file:`.{baseName}.tcl`, into the Tcl
   interpreter and calls :func:`exec` on the contents of
   :file:`.{className}.py` and :file:`.{baseName}.py`.  The path for the
   profile files is the :envvar:`HOME` environment variable or, if that
   isn't defined, then :data:`os.curdir`.

   .. note::

      On Windows, creating a Tcl interpreter (by instantiating :class:`Tk` or
      calling :func:`Tcl`) sets the :envvar:`HOME` environment variable for
      the process, if it is not already set, to ``%HOMEDRIVE%%HOMEPATH%`` (or
      :envvar:`USERPROFILE`, or ``c:\``).  This is done by Tcl and can affect
      other code that reads :envvar:`HOME`.

   .. attribute:: tk

      The Tk application object created by instantiating :class:`Tk`.  This
      provides access to the Tcl interpreter.  Each widget that is attached
      the same instance of :class:`Tk` has the same value for its :attr:`tk`
      attribute.

   .. attribute:: master

      The widget object that contains this widget.
      For :class:`Tk`, the :attr:`!master` is :const:`None` because it is the
      main window.
      The terms *master* and *parent* are similar and sometimes used
      interchangeably as argument names; however, calling
      :meth:`~Misc.winfo_parent` returns a string of the widget name whereas
      :attr:`!master` returns the object.
      *parent*/*child* reflects the tree-like relationship while *master* (or
      *container*)/*content* reflects the container structure.

   .. attribute:: children

      The immediate descendants of this widget as a :class:`dict` with the
      child widget names as the keys and the child instance objects as the
      values.

   .. method:: destroy()

      Destroy this and all descendant widgets and, for the main window, end the
      connection to the underlying Tcl interpreter.

   .. method:: loadtk()

      Finish loading and initializing the Tk subsystem.
      This is needed only when the interpreter was created without Tk (for
      example through :func:`Tcl`); it is called automatically when *useTk* is
      true.

   .. method:: readprofile(baseName, className)

      Read and source the user's profile files :file:`.{className}.tcl` and
      :file:`.{baseName}.tcl` into the Tcl interpreter, and execute the
      corresponding :file:`.{className}.py` and :file:`.{baseName}.py` files.
      This is called during initialization; see the description of the
      constructor above.

   .. method:: report_callback_exception(exc, val, tb)

      Report a callback exception.
      This is called when an exception propagates out of a Tkinter callback;
      *exc*, *val* and *tb* are the exception type, value and traceback as
      returned by :func:`sys.exc_info`.
      The default implementation prints a traceback to :data:`sys.stderr`.
      It can be overridden to customize error handling, for example to display
      the traceback in a dialog.


.. class:: Toplevel(master=None, cnf={}, **kw)

   A :class:`!Toplevel` widget is a top-level window, similar to a
   :class:`Frame` except that its X parent is the root window of a screen
   rather than its logical parent.
   Its primary purpose is to serve as a container for dialog boxes and other
   collections of widgets; its only visible features are its background and an
   optional 3-D border.
   Notable options include *menu*, which installs a :class:`Menu` as the
   window's menubar.
   Inherits from :class:`BaseWidget` and :class:`Wm`, so a toplevel is managed
   by the window manager.
   Refer to the Tk ``toplevel`` manual page for the full list of options.


Widget classes
^^^^^^^^^^^^^^

.. class:: Button(master=None, cnf={}, **kw)

   A :class:`!Button` widget displays a textual string, bitmap or image and
   invokes a command when the user presses it (by clicking mouse button 1 over
   the button or, when the button has focus, by pressing the space key).
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a button accepts the options
   documented in the Tk ``button`` manual page, such as *command* (the callback
   invoked when the button is pressed), *textvariable*, *state* and *default*.

   .. method:: invoke()

      Invoke the command associated with the button, if there is one, and
      return its result, or an empty string if no command is associated with
      the button.
      This is ignored if the button's state is ``disabled``.

   .. method:: flash()

      Flash the button by redisplaying it several times, alternating between
      the active and normal colors.
      At the end of the flash the button is left in the same normal or active
      state as when the method was called.
      This is ignored if the button's state is ``disabled``.


.. class:: Canvas(master=None, cnf={}, **kw)

   A :class:`!Canvas` widget implements structured graphics.
   It displays any number of *items*, such as arcs, lines, ovals, polygons,
   rectangles, text, bitmaps, images and embedded windows, which may be drawn,
   moved, re-colored and bound to events.
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``canvas`` manual page for the full list of widget and item
   options.

   Each item has a unique integer *id*, assigned when it is created, and zero
   or more string *tags*.
   A tag is an arbitrary string that does not have the form of an integer; the
   same tag may be shared by many items, which makes tags convenient for
   grouping items.
   The special tag ``'all'`` matches every item in the canvas, and
   ``'current'`` matches the topmost item under the mouse pointer.
   Most methods take a *tagOrId* argument that may be an integer id naming a
   single item, or a tag naming zero or more items; as described in the Tk
   ``canvas`` manual page, a tag may also be a logical expression of tags
   combined with the operators ``&&``, ``||``, ``^``, ``!`` and parentheses.
   When a method that operates on a single item is given a *tagOrId* matching
   several items, it normally uses the lowest matching item in the display
   list.

   The items are kept in a *display list* that determines drawing order: items
   later in the list are drawn on top of earlier ones.
   A newly created item is placed at the top of the list; the order can be
   changed with :meth:`tag_raise` and :meth:`tag_lower`.

   .. method:: create_arc(*args, **kw)
               create_bitmap(*args, **kw)
               create_image(*args, **kw)
               create_line(*args, **kw)
               create_oval(*args, **kw)
               create_polygon(*args, **kw)
               create_rectangle(*args, **kw)
               create_text(*args, **kw)
               create_window(*args, **kw)

      Create a new item of the corresponding type and return its integer id.
      Each method is called as ``create_TYPE(coord..., **options)``: the
      leading positional arguments give the coordinates that define the item
      (as separate numbers, as a single sequence of numbers, or as coordinate
      pairs), and the keyword arguments set item-specific options.
      Coordinates and screen distances may be given as numbers (interpreted as
      pixels) or as strings with a unit suffix (``'m'``, ``'c'``, ``'i'`` or
      ``'p'`` for millimetres, centimetres, inches or printer's points), but
      are always stored and returned in pixels.

      The item types are: ``arc`` (an arc-shaped region that is a section of an
      oval, defined by two diagonally opposite corners ``x1, y1, x2, y2`` of
      the enclosing rectangle); ``bitmap`` (a two-color bitmap positioned at a
      point ``x, y``); ``image`` (a Tk image positioned at a point ``x, y``);
      ``line`` (a line or curve through the points ``x1, y1, ..., xn, yn``);
      ``oval`` (a circle or ellipse inscribed in the rectangle
      ``x1, y1, x2, y2``); ``polygon`` (a closed polygon through the points
      ``x1, y1, ..., xn, yn``); ``rectangle`` (a rectangle with corners
      ``x1, y1, x2, y2``); ``text`` (a string of text positioned at a point
      ``x, y``); and ``window`` (a child widget embedded in the canvas at a
      point ``x, y``, specified with the *window* option).

      Most item types accept a common set of *standard item options*, plus a
      few options specific to each type.
      Option names are passed as keyword arguments, without the leading
      hyphen.

      The standard item options are:

      *fill*
         The color used to fill the item's interior, or to draw a *line*
         item or the characters of a *text* item.
         An empty string (the default for all types except *line* and *text*)
         leaves the item unfilled.

      *outline*
         The color used to draw the item's outline.
         An empty string draws no outline.

      *width*
         The width of the outline, defaulting to ``1.0``.
         Has no effect if *outline* is empty.

      *dash*
         A dash pattern for the outline, given either as a sequence of
         segment lengths in pixels or as a string of the characters
         ``'.'``, ``','``, ``'-'``, ``'_'`` and space.
         An empty pattern (the default) draws a solid outline.

      *dashoffset*
         The starting offset in pixels into the *dash* pattern.
         Ignored if there is no *dash* pattern.

      *stipple*
         A bitmap used as a stipple pattern when filling the item.
         Only well supported on X11.

      *outlinestipple*
         A bitmap used as a stipple pattern when drawing the outline.
         Has no effect if *outline* is empty.

      *offset*, *outlineoffset*
         The offset of the fill and outline stipple patterns, given as
         ``'x,y'`` or as a side such as ``'n'``, ``'se'`` or ``'center'``.
         Stipple offsets are only supported on X11.

      *state*
         Overrides the canvas state for this item; one of ``'normal'``,
         ``'disabled'`` or ``'hidden'``.

      *tags*
         A single tag or a sequence of tags to associate with the item,
         replacing any existing tags.

      Many of these options have *active...* and *disabled...* variants
      (such as *activefill*, *disabledfill*, *activewidth*, *disableddash*,
      *activeoutline*, *disabledstipple*) that override the base option when
      the item is the active item (under the mouse pointer) or is in the
      disabled state.

      The following item types support additional options.

      For ``arc`` items:

      *start*
         The start of the arc's angular range, in degrees measured
         counter-clockwise from the 3-o'clock position.

      *extent*
         The size of the angular range, in degrees counter-clockwise from
         *start*.

      *style*
         How the arc is drawn: ``'pieslice'`` (the default), ``'chord'`` or
         ``'arc'``.

      For ``line`` items:

      *arrow*
         Where to draw arrowheads: ``'none'`` (the default), ``'first'``,
         ``'last'`` or ``'both'``.

      *arrowshape*
         A sequence of three distances describing the shape of the
         arrowheads.

      *capstyle*
         How line ends are drawn: ``'butt'`` (the default), ``'projecting'``
         or ``'round'``.

      *joinstyle*
         How line vertices are drawn: ``'round'`` (the default), ``'bevel'``
         or ``'miter'``.

      *smooth*
         The smoothing method: a false value (the default) for no smoothing,
         or ``'true'``/``'bezier'`` or ``'raw'`` to draw the line as a curve.

      *splinesteps*
         The number of line segments approximating each spline when
         *smooth* is enabled.

      For ``polygon`` items:

      *joinstyle*, *smooth*, *splinesteps*
         As for ``line`` items, applied to the polygon's outline.

      For ``text`` items:

      *text*
         The string to display; newline characters start new lines.

      *font*
         The font used for the text.

      *justify*
         How lines are justified: ``'left'`` (the default), ``'right'`` or
         ``'center'``.

      *anchor*
         How the text is positioned relative to its point, defaulting to
         ``'center'``.

      *width*
         The maximum line length; if non-zero, lines are wrapped at spaces.

      *angle*
         How many degrees to rotate the text counter-clockwise about its
         positioning point, from ``0.0`` to ``360.0`` (default ``0.0``).

      *underline*
         The index of a character to underline, or ``-1`` for none.

      For ``bitmap`` items:

      *bitmap*
         The bitmap to display.

      *anchor*
         How the bitmap is positioned relative to its point.

      *background*, *foreground*
         The colors used for the bitmap's ``0`` and ``1`` pixels; an empty
         *background* makes the ``0`` pixels transparent.
         Both have *active...* and *disabled...* variants, and *bitmap* has
         *activebitmap* and *disabledbitmap* variants.

      For ``image`` items:

      *image*
         The Tk image to display, previously created with the image
         protocols.

      *anchor*
         How the image is positioned relative to its point.

      Both options have *active...* and *disabled...* variants
      (*activeimage*, *disabledimage*) used in the active and disabled
      states.

      For ``window`` items:

      *window*
         The widget to embed; it must be a child of the canvas or of one of
         its ancestors, and may not be a top-level window.

      *anchor*
         How the window is positioned relative to its point.

      *width*, *height*
         The size to assign to the window; if zero (the default), the window
         is given its requested size.

      ``oval`` and ``rectangle`` items have no type-specific options; they
      use only the standard item options.

      .. note::

         Tk 8.6 added the *angle* option for ``text`` items.

   .. method:: coords(tagOrId)
               coords(tagOrId, coordList, /)
               coords(tagOrId, /, *coordList)

      Query or modify the coordinates of an item.
      With only *tagOrId*, return a list of the floating-point coordinates of
      the item given by *tagOrId* (the first matching item if it matches
      several).
      Given new coordinates, replace the coordinates of that item with them;
      like the ``create_*`` methods, the coordinates may be given as separate
      numbers, as a single sequence, or as coordinate pairs.
      The returned coordinates are always in pixels, regardless of the units
      used to specify them; for rectangles, ovals and arcs they are ordered
      left, top, right, bottom.

      .. versionchanged:: 3.12
         The arguments are now flattened: the coordinates may be given as
         separate arguments, as a single sequence, or grouped in pairs, like
         the ``create_*`` methods.


   .. method:: move(tagOrId, xAmount, yAmount, /)

      Move each of the items given by *tagOrId* in the canvas coordinate space
      by adding *xAmount* to every x-coordinate and *yAmount* to every
      y-coordinate of the item.

   .. method:: moveto(tagOrId, x='', y='')

      Move the items given by *tagOrId* so that the first coordinate pair (the
      upper-left corner of the bounding box) of the lowest matching item is at
      position (*x*, *y*).
      *x* or *y* may be an empty string, in which case the corresponding
      coordinate is unchanged.
      All matching items keep their positions relative to each other.

      .. versionadded:: 3.8


   .. method:: scale(tagOrId, xOrigin, yOrigin, xScale, yScale, /)

      Rescale the coordinates of all items given by *tagOrId* in canvas
      coordinate space.
      Each x-coordinate is adjusted so that its distance from *xOrigin* changes
      by a factor of *xScale*, and each y-coordinate so that its distance from
      *yOrigin* changes by a factor of *yScale* (a factor of ``1.0`` leaves the
      coordinate unchanged).

   .. method:: delete(*tagOrIds)

      Delete each of the items given by the *tagOrIds* arguments.

   .. method:: dchars(tagOrId, first, /)
               dchars(tagOrId, first, last, /)

      Delete from each of the items given by *tagOrId* the characters (for text
      items) or coordinates (for line and polygon items) in the range from
      *first* to *last* inclusive; *last* defaults to *first*.
      Items that do not support indexing ignore this operation.

   .. method:: insert(tagOrId, beforeThis, string, /)

      Insert *string* into each of the items given by *tagOrId* just before the
      character or coordinate whose index is *beforeThis*.
      For line and polygon items *string* must be a valid sequence of
      coordinates.

   .. method:: itemcget(tagOrId, option)

      Return the current value of the configuration option *option* for the
      item given by *tagOrId* (the lowest matching item if it matches several).
      This is like :meth:`~Misc.cget` but applies to an individual item.

   .. method:: itemconfig(tagOrId, cnf=None, **kw)
      :no-typesetting:

   .. method:: itemconfigure(tagOrId, cnf=None, **kw)

      Query or modify the configuration options of the items given by
      *tagOrId*.
      This mirrors :meth:`~Misc.configure`, except that it applies to
      individual items rather than to the canvas as a whole.
      With no options, it returns a dictionary describing the current options
      of the first matching item; otherwise it sets the given options on every
      matching item.
      The legal options are those accepted by the corresponding ``create_*``
      method.
      :meth:`itemconfig` is an alias of :meth:`!itemconfigure`.

   .. method:: type(tagOrId)

      Return the type of the item given by *tagOrId* (the first matching item
      if it matches several), such as ``'rectangle'`` or ``'text'``, or
      ``None`` if *tagOrId* does not match any item.

   .. method:: gettags(tagOrId, /)

      Return a tuple of the tags associated with the item given by *tagOrId*
      (the first matching item in display-list order if it matches several).
      Return an empty tuple if no item matches or the item has no tags.

   .. method:: dtag(tagOrId, /)
               dtag(tagOrId, tagToDelete, /)

      Remove the tag *tagToDelete* (which defaults to *tagOrId*) from each of
      the items given by *tagOrId*.
      Items that do not have that tag are unaffected.

   .. method:: addtag(newtag, searchSpec, /, *args)

      Add the tag *newtag* to each item selected by the search specification
      *searchSpec* (and any further *args*).
      *searchSpec* is one of ``'above'``, ``'all'``, ``'below'``,
      ``'closest'``, ``'enclosed'``, ``'overlapping'`` or ``'withtag'``; the
      ``addtag_*`` methods below are convenient wrappers that supply each of
      these forms.

   .. method:: addtag_above(newtag, tagOrId)

      Add the tag *newtag* to the item just above (after) *tagOrId* in the
      display list.

   .. method:: addtag_all(newtag)

      Add the tag *newtag* to all items in the canvas.

   .. method:: addtag_below(newtag, tagOrId)

      Add the tag *newtag* to the item just below (before) *tagOrId* in the
      display list.

   .. method:: addtag_closest(newtag, x, y, halo=None, start=None)

      Add the tag *newtag* to the item closest to the point (*x*, *y*).
      If *halo* is given, any item within that distance of the point is treated
      as overlapping it.
      If *start* is given (a tag or id), select the topmost closest item that
      lies below *start* in the display list, which can be used to step through
      all the closest items.

   .. method:: addtag_enclosed(newtag, x1, y1, x2, y2)

      Add the tag *newtag* to every item completely enclosed within the
      rectangle (*x1*, *y1*, *x2*, *y2*), where *x1* <= *x2* and *y1* <= *y2*.

   .. method:: addtag_overlapping(newtag, x1, y1, x2, y2)

      Add the tag *newtag* to every item that overlaps or is enclosed within
      the rectangle (*x1*, *y1*, *x2*, *y2*), where *x1* <= *x2* and *y1* <=
      *y2*.

   .. method:: addtag_withtag(newtag, tagOrId)

      Add the tag *newtag* to every item given by *tagOrId*.

   .. method:: find(searchSpec, /, *args)

      Return a tuple of the ids of all items selected by the search
      specification *searchSpec* (and any further *args*), in stacking order
      with the lowest item first.
      The search specification has any of the forms accepted by :meth:`addtag`.
      The ``find_*`` methods below are more convenient wrappers around it.

   .. method:: find_above(tagOrId)

      Return a tuple containing the id of the item just above *tagOrId* in the
      display list.

   .. method:: find_all()

      Return a tuple of the ids of all items in the canvas, in stacking order.

   .. method:: find_below(tagOrId)

      Return a tuple containing the id of the item just below *tagOrId* in the
      display list.

   .. method:: find_closest(x, y, halo=None, start=None)

      Return a tuple containing the id of the item closest to the point (*x*,
      *y*).
      *halo* and *start* are interpreted as for :meth:`addtag_closest`.

   .. method:: find_enclosed(x1, y1, x2, y2)

      Return a tuple of the ids of all items completely enclosed within the
      rectangle (*x1*, *y1*, *x2*, *y2*).

   .. method:: find_overlapping(x1, y1, x2, y2)

      Return a tuple of the ids of all items that overlap or are enclosed
      within the rectangle (*x1*, *y1*, *x2*, *y2*).

   .. method:: find_withtag(tagOrId)

      Return a tuple of the ids of all items given by *tagOrId*.

   .. method:: lift(tagOrId, aboveThis=None, /)
      :no-typesetting:

   .. method:: tkraise(tagOrId, aboveThis=None, /)
      :no-typesetting:

   .. method:: tag_raise(tagOrId, aboveThis=None, /)

      Move all items given by *tagOrId* to a new position in the display list
      just above the item given by *aboveThis*, or to the top of the display
      list if *aboveThis* is omitted.
      When several items are moved their relative order is preserved.
      This has no effect on embedded window items, whose stacking order is
      controlled by :meth:`Misc.tkraise` and :meth:`Misc.lower` instead.
      :meth:`lift` and :meth:`tkraise` are aliases of :meth:`!tag_raise`.

   .. method:: lower(tagOrId, belowThis=None, /)
      :no-typesetting:

   .. method:: tag_lower(tagOrId, belowThis=None, /)

      Move all items given by *tagOrId* to a new position in the display list
      just below the item given by *belowThis*, or to the bottom of the display
      list if *belowThis* is omitted.
      When several items are moved their relative order is preserved.
      This has no effect on embedded window items.
      :meth:`lower` is an alias of :meth:`!tag_lower`.

      .. note::

         On a :class:`Canvas`, :meth:`tkraise`/:meth:`lift` and :meth:`lower`
         restack canvas items,
         shadowing the inherited :meth:`Misc.tkraise`/:meth:`Misc.lift` and
         :meth:`Misc.lower` methods that restack the widget itself,
         which are therefore not available.

   .. method:: tag_bind(tagOrId, sequence=None, func=None, add=None)

      Bind the callback *func* to the event *sequence* for all items given by
      *tagOrId*, so that *func* is invoked whenever that event occurs for one
      of the items.
      This is like :meth:`Widget.bind <Misc.bind>` but operates on canvas items
      rather than on whole widgets; only mouse, keyboard and virtual events may
      be bound.
      Mouse events are directed to the current item and keyboard events to the
      focus item (see :meth:`focus`).
      If *add* is true the new binding is added to any existing bindings for
      the same sequence, rather than replacing them.
      Return the identifier of the bound function, which can be passed to
      :meth:`tag_unbind`.

   .. method:: tag_unbind(tagOrId, sequence, funcid=None)

      Remove for all items given by *tagOrId* the binding for the event
      *sequence*.
      If *funcid* is given, only that callback (as returned by
      :meth:`tag_bind`) is unbound and deregistered.

      .. versionchanged:: 3.13
         If *funcid* is given, only that callback is unbound.


   .. method:: bbox(tagOrId, /, *tagOrIds)

      Return a 4-tuple ``(x1, y1, x2, y2)`` giving an approximate bounding box,
      in pixels, that encloses all the items given by *tagOrId* and any further
      *tagOrIds*.
      The result may overestimate the true bounding box by a few pixels.
      Return ``None`` if no item matches or the matching items have nothing to
      display.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: canvasx(screenx, gridspacing=None)

      Given a window x-coordinate *screenx*, return the canvas x-coordinate
      displayed at that location.
      If *gridspacing* is given, the result is rounded to the nearest multiple
      of *gridspacing* units.

   .. method:: canvasy(screeny, gridspacing=None)

      Given a window y-coordinate *screeny*, return the canvas y-coordinate
      displayed at that location.
      If *gridspacing* is given, the result is rounded to the nearest multiple
      of *gridspacing* units.

   .. method:: focus()
               focus(tagOrId, /)

      With *tagOrId*, set the keyboard focus for the canvas to the first item
      given by *tagOrId* that supports the insertion cursor; the focus is left
      unchanged if no such item exists.
      If *tagOrId* is an empty string, reset the focus so that no item has it.
      With no argument, return the id of the item that currently has the focus,
      or an empty string if none does.
      An item only displays the insertion cursor when both it is the focus item
      and its canvas has the input focus.

      This shadows the inherited :meth:`!Misc.focus`;
      use :meth:`~Misc.focus_set` to focus the widget itself.

   .. method:: icursor(tagOrId, index, /)

      Set the insertion cursor of the items given by *tagOrId* to just before
      the character given by *index*.
      Items that do not support an insertion cursor are unaffected.
      The cursor is only displayed when the item has the focus, but its
      position may be set at any time.

   .. method:: index(tagOrId, index, /)

      Return as an integer the numerical index within *tagOrId* corresponding
      to *index*, which is a textual description of a position (for text items
      an index into the characters, for line and polygon items an index into
      the coordinates).
      If *tagOrId* matches several items, the first one that supports indexing
      is used.

   .. method:: select_adjust(tagOrId, index)

      Adjust the end of the selection in *tagOrId* nearest to *index* so that
      it is at *index*, and make the other end the anchor point for future
      :meth:`select_to` calls.
      If the selection is not currently in *tagOrId*, this behaves like
      :meth:`select_to`.

   .. method:: select_clear()

      Clear the selection if it is in this canvas; otherwise do nothing.

   .. method:: select_from(tagOrId, index)

      Set the selection anchor point to just before the character given by
      *index* in the item given by *tagOrId*.
      This does not change the selection itself; it sets the fixed end for
      future :meth:`select_to` calls.

   .. method:: select_item()

      Return the id of the item that holds the selection, or ``None`` if the
      selection is not in this canvas.
      Unlike :meth:`find` and the ``find_*`` methods, this returns the id as a
      string rather than an integer.

   .. method:: select_to(tagOrId, index)

      Set the selection to the characters of *tagOrId* between the selection
      anchor point and *index*, inclusive of *index*.
      The anchor point is the one set by the most recent :meth:`select_adjust`
      or :meth:`select_from` call.

   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y, gain=10)

      Scroll the canvas by *gain* times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events in the widget, producing
      the effect of dragging the canvas at high speed through its window.

   .. method:: postscript(cnf={}, **kw)

      Generate a PostScript (Encapsulated PostScript, version 3.0)
      representation of part or all of the canvas.
      If the *file* or *channel* option is given, the PostScript is written
      there and an empty string is returned; otherwise it is returned as a
      string.
      By default only the area currently visible in the window is generated, so
      it is usually necessary either to call :meth:`~Misc.update` first or to
      use the *width* and *height* options.
      Supported options include *colormap*, *colormode*, *file*, *fontmap*,
      *height*, *pageanchor*, *pageheight*, *pagewidth*, *pagex*, *pagey*,
      *rotate*, *width*, *x* and *y*.


.. class:: Checkbutton(master=None, cnf={}, **kw)

   A :class:`!Checkbutton` widget displays a textual string, bitmap or image
   together with a square indicator, and toggles a boolean selection when
   pressed.
   It has all the behavior of a simple button and, in addition, can be
   selected: when selected the indicator is drawn with a check mark and the
   associated variable is set to the ``onvalue``, and when deselected the
   indicator is drawn empty and the variable is set to the ``offvalue``.
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a checkbutton accepts the
   options documented in the Tk ``checkbutton`` manual page, such as
   *variable*, *onvalue*, *offvalue* and *command*.

   .. method:: invoke()

      Do just what would happen if the user pressed the checkbutton with the
      mouse: toggle the selection state of the button and invoke the associated
      command, if there is one.
      Return the result of the command, or an empty string if no command is
      associated with the checkbutton.
      This is ignored if the checkbutton's state is ``disabled``.

   .. method:: select()

      Select the checkbutton and set the associated variable to its
      ``onvalue``.

   .. method:: deselect()

      Deselect the checkbutton and set the associated variable to its
      ``offvalue``.

   .. method:: toggle()

      Toggle the selection state of the button, redisplaying it and modifying
      its associated variable to reflect the new state.

   .. method:: flash()

      Flash the checkbutton by redisplaying it several times, alternating
      between the active and normal colors.
      At the end of the flash the checkbutton is left in the same normal or
      active state as when the method was called.
      This is ignored if the checkbutton's state is ``disabled``.


.. class:: Entry(master=None, cnf={}, **kw)

   An :class:`!Entry` widget displays a single line of text and lets the user
   edit it.
   Inherits from :class:`Widget` and :class:`XView`; since entries can hold
   strings too long to fit in the window, they support horizontal scrolling
   through :meth:`~XView.xview`.

   In addition to the standard widget options, an entry accepts the options
   documented in the Tk ``entry`` manual page.
   Notable ones are *textvariable* (the name of a variable kept in sync with
   the entry's contents), *show* (if set, each character is displayed as the
   given character rather than its true value, useful for password entry),
   *validate* and *validatecommand* (which together let a callback accept or
   reject edits), and *state* (one of ``'normal'``, ``'disabled'`` or
   ``'readonly'``).

   Many of the methods below take an *index* argument that selects a character
   in the entry's string.
   As described in the Tk ``entry`` manual page, *index* may be a number
   (counting from 0), ``'insert'`` (the character just after the insertion
   cursor), ``'end'`` (just after the last character), ``'anchor'`` (the
   selection anchor point), ``'sel.first'`` and ``'sel.last'`` (the ends of the
   selection), or ``@x`` (the character covering pixel x-coordinate *x* in the
   window).
   Out-of-range indices are rounded to the nearest legal value.

   .. method:: delete(first, last=None)

      Delete the characters from index *first* up to but not including index
      *last*.
      If *last* is omitted, only the single character at *first* is deleted.

   .. method:: get()

      Return the entry's current string.

   .. method:: insert(index, string)

      Insert *string* just before the character given by *index*.

   .. method:: icursor(index)

      Arrange for the insertion cursor to be displayed just before the
      character given by *index*.

   .. method:: index(index)

      Return the numerical index corresponding to *index*.

   .. method:: select_adjust(index)
      :no-typesetting:

   .. method:: selection_adjust(index)

      Locate the end of the selection nearest to the character given by
      *index*, and adjust that end to be at *index* (including but not going
      beyond it); the other end becomes the anchor point for future
      :meth:`selection_to` calls.
      If there is no selection in the entry, a new one is created between
      *index* and the most recent anchor point, inclusive.
      :meth:`select_adjust` is an alias of :meth:`!selection_adjust`.

   .. method:: select_clear()
      :no-typesetting:

   .. method:: selection_clear()

      Clear the selection if it is currently in this widget.
      If the selection is not in this widget the method has no effect.
      :meth:`select_clear` is an alias of :meth:`!selection_clear`.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on an :class:`Entry`.

   .. method:: select_from(index)
      :no-typesetting:

   .. method:: selection_from(index)

      Set the selection anchor point to just before the character given by
      *index*, without changing the selection.
      :meth:`select_from` is an alias of :meth:`!selection_from`.

   .. method:: select_present()
      :no-typesetting:

   .. method:: selection_present()

      Return ``True`` if there are characters selected in the entry, ``False``
      otherwise.
      :meth:`select_present` is an alias of :meth:`!selection_present`.

   .. method:: select_range(start, end)
      :no-typesetting:

   .. method:: selection_range(start, end)

      Set the selection to include the characters starting with the one indexed
      by *start* and ending with the one just before *end*.
      If *end* refers to the same character as *start* or an earlier one, the
      selection is cleared.
      :meth:`select_range` is an alias of :meth:`!selection_range`.

   .. method:: select_to(index)
      :no-typesetting:

   .. method:: selection_to(index)

      Set the selection between the anchor point and *index*: if *index* is
      before the anchor point, the selection runs from *index* up to but not
      including the anchor; if *index* is after it, from the anchor up to but
      not including *index*; if they coincide, nothing happens.
      The anchor point is the one set by the most recent :meth:`selection_from`
      or :meth:`selection_adjust` call.
      If there is no selection in the entry, a new one is created using the
      most recent anchor point.
      :meth:`select_to` is an alias of :meth:`!selection_to`.

   .. method:: scan_mark(x)

      Record *x* and the current view in the entry window, for use with later
      :meth:`scan_dragto` calls.
      Typically associated with a mouse button press in the widget.

   .. method:: scan_dragto(x)

      Compute the difference between *x* and the *x* given to the last
      :meth:`scan_mark` call, and adjust the view left or right by 10 times
      that difference.
      Typically associated with mouse motion events, to produce the effect of
      dragging the entry at high speed through the window.


.. class:: Frame(master=None, cnf={}, **kw)

   A :class:`!Frame` widget is a simple container.
   Its primary purpose is to act as a spacer or container for complex window
   layouts; its only features are its background and an optional 3-D border to
   make the frame appear raised or sunken.
   Inherits from :class:`Widget`.
   Refer to the Tk ``frame`` manual page for the full list of options.


.. class:: Label(master=None, cnf={}, **kw)

   A :class:`!Label` widget displays a non-interactive textual string, bitmap
   or image.
   The displayed text is set with the *text* option or linked to a variable
   through *textvariable*, and an image can be shown using the *image* option.
   Text must all be in a single font but may occupy multiple lines, and one
   character may be underlined with the *underline* option.
   Inherits from :class:`Widget`.
   Refer to the Tk ``label`` manual page for the full list of options.


.. class:: LabelFrame(master=None, cnf={}, **kw)

   A :class:`!LabelFrame` widget is a container that has the features of a
   :class:`Frame` plus the ability to display a label.
   The label text is set with the *text* option and positioned with
   *labelanchor*, or an arbitrary widget may be used as the label by giving it
   as the *labelwidget* option.
   Inherits from :class:`Widget`.
   Refer to the Tk ``labelframe`` manual page for the full list of options.


.. class:: Listbox(master=None, cnf={}, **kw)

   A :class:`!Listbox` widget displays a list of single-line text items, one
   per line, of which the user can select one or more.
   The way the selection behaves is governed by the *selectmode* option, which
   is one of ``browse`` (the default; at most one item, which may be dragged
   with the mouse), ``single`` (at most one item), ``multiple`` (any number of
   items, toggled individually), or ``extended`` (any number of items,
   including discontiguous ranges, selected by clicking and dragging).
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``listbox`` manual page for the full list of options.

   Many of the methods take an *index* argument identifying a particular item.
   As described in the Tk ``listbox`` manual page, *index* may be a numeric
   index (counting from 0 at the top), ``'active'`` (the item with the location
   cursor, set with :meth:`activate`), ``'anchor'`` (the selection anchor, set
   with :meth:`selection_anchor`), ``'end'`` (the last item, or for
   :meth:`index` and :meth:`insert` the position just after it), or ``@x,y``
   (the item covering pixel coordinates *x*, *y* in the listbox window).
   Arguments named *first* and *last* are indices of the same forms.

   .. method:: insert(index, *elements)

      Insert the given *elements* as new items just before the item given by
      *index*.
      If *index* is ``'end'``, the new items are appended to the end of the
      list.

   .. method:: delete(first, last=None)

      Delete the items in the range from *first* to *last* inclusive.
      If *last* is omitted, it defaults to *first*, so that a single item is
      deleted.

   .. method:: get(first, last=None)

      If *last* is omitted, return the contents of the item given by *first*,
      or an empty string if *first* refers to a non-existent item.
      If *last* is given, return a tuple of all the items in the range from
      *first* to *last* inclusive.

   .. method:: size()

      Return the total number of items in the listbox.

      This shadows the inherited :meth:`!Misc.size`;
      use :meth:`~Misc.grid_size` for the grid size.

   .. method:: index(index)

      Return the integer index value corresponding to *index*, or ``None`` if
      *index* is out of range.
      If *index* is ``'end'``, the result is a count of the number of items in
      the listbox (not the index of the last item).

   .. method:: bbox(index)

      Return a tuple ``(x, y, width, height)`` describing the bounding box, in
      pixels relative to the widget, of the text of the item given by *index*.
      Return ``None`` if no part of that item is visible on the screen, or if
      *index* refers to a non-existent item; if the item is only partly
      visible, the result still gives the full area of the item, including the
      parts that are not visible.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: nearest(y)

      Given a y-coordinate within the listbox window, return the index of the
      visible item nearest to that y-coordinate.

   .. method:: see(index)

      Adjust the view so that the item given by *index* is visible.
      If the item is already visible the method has no effect; if it is near an
      edge of the window the listbox scrolls just enough to bring it into view
      at that edge, otherwise the listbox scrolls to center the item.

   .. method:: activate(index)

      Set the active item to the one given by *index*.
      If *index* is outside the range of items, the closest item is activated
      instead.
      The active item is drawn as specified by the *activestyle* option when
      the widget has the input focus, and its index may be retrieved with the
      ``'active'`` index.

   .. method:: curselection()

      Return a tuple containing the numerical indices of all of the items that
      are currently selected, or an empty tuple if no items are selected.

   .. method:: select_anchor(index)
      :no-typesetting:

   .. method:: selection_anchor(index)

      Set the selection anchor to the item given by *index*.
      If *index* refers to a non-existent item, the closest item is used.
      The selection anchor is the end of the selection that is fixed while
      dragging out a selection with the mouse, and may afterwards be referred
      to with the ``'anchor'`` index.
      :meth:`select_anchor` is an alias of :meth:`!selection_anchor`.

   .. method:: select_clear(first, last=None)
      :no-typesetting:

   .. method:: selection_clear(first, last=None)

      Deselect any of the items in the range from *first* to *last* inclusive
      that are selected.
      The selection state of items outside this range is not changed.
      :meth:`select_clear` is an alias of :meth:`!selection_clear`.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on a :class:`Listbox`.

   .. method:: select_includes(index)
      :no-typesetting:

   .. method:: selection_includes(index)

      Return ``True`` if the item given by *index* is currently selected,
      ``False`` otherwise.
      :meth:`select_includes` is an alias of :meth:`!selection_includes`.

   .. method:: select_set(first, last=None)
      :no-typesetting:

   .. method:: selection_set(first, last=None)

      Select all of the items in the range from *first* to *last* inclusive,
      without affecting the selection state of items outside that range.
      :meth:`select_set` is an alias of :meth:`!selection_set`.

   .. method:: itemcget(index, option)

      Return the current value of the configuration option *option* for the
      item given by *index*.

   .. method:: itemconfig(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: itemconfigure(index, cnf=None, **kw)

      Query or modify the configuration options of the item given by *index*.
      This mirrors :meth:`~Misc.configure`, except that it applies to an
      individual item rather than to the listbox as a whole.
      With no options, it returns a dictionary describing the current options
      of the item; otherwise it sets the given options.
      The supported item options are *background*, *foreground*,
      *selectbackground* and *selectforeground*.
      :meth:`itemconfig` is an alias of :meth:`!itemconfigure`.

   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y)

      Scroll the listbox by 10 times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events in the widget, producing
      the effect of dragging the list at high speed through the window.


.. class:: Menu(master=None, cnf={}, **kw)

   A :class:`!Menu` widget displays a column of entries, each of which may be a
   command, a checkbutton, a radiobutton, a cascade (which posts an associated
   submenu) or a separator.
   Menus are used as the menubar of a toplevel window, as pulldown menus posted
   from a cascade entry or menubutton, and as popup menus.
   Inherits from :class:`Widget`.

   Many of the entry methods take an *index* argument that selects which entry
   to operate on.
   As described in the Tk ``menu`` manual page, *index* may be a numeric index
   (counting from 0 at the top), ``'active'`` (the currently active entry),
   ``'end'`` or ``'last'`` (the bottommost entry), ``'none'`` (no entry at all,
   written ``{}`` in Tcl), ``@y`` (the entry covering pixel y-coordinate *y* in
   the menu window), or a pattern matched against the labels of the entries
   from the top down.

   .. method:: add(itemType, cnf={}, **kw)

      Add a new entry to the bottom of the menu.
      *itemType* is one of ``'command'``, ``'cascade'``, ``'checkbutton'``,
      ``'radiobutton'`` or ``'separator'`` and determines the type of the new
      entry; the remaining options configure it.
      The :meth:`!add_command`, :meth:`!add_cascade`, :meth:`!add_checkbutton`,
      :meth:`!add_radiobutton` and :meth:`!add_separator` convenience methods
      call this method with the corresponding *itemType*.

      The entry is configured by the following options, although not every
      option applies to every entry type (a separator accepts none of them):

      *label*
         The text to display in the entry.

      *command*
         The function to call when the entry is invoked (command, checkbutton
         and radiobutton entries).

      *accelerator*
         A string displayed at the right of the entry to advertise an
         accelerator keystroke; it does not itself create the binding.

      *underline*
         The index of a character in the label to underline for keyboard
         traversal.

      *state*
         One of ``'normal'``, ``'active'`` or ``'disabled'``.

      *image*
         An image to display instead of, or together with, the text label.

      *compound*
         Where to show the image relative to the text: ``'none'`` (the
         default), ``'text'``, ``'image'``, ``'top'``, ``'bottom'``, ``'left'``
         or ``'right'``.

      *bitmap*
         A bitmap to display instead of the text label.

      *font*
         The font to use for the text.

      *background*, *foreground*
         The entry's background and foreground colors in its normal state
         (ignored on macOS).

      *activebackground*, *activeforeground*
         The background and foreground colors used when the entry is active
         (ignored on macOS).

      *columnbreak*
         If true, the entry starts a new column instead of being placed below
         the previous entry.

      *hidemargin*
         If true, the standard margin around the entry is omitted, which is
         useful when a menu is used as a palette.

      *menu*
         The submenu posted by a cascade entry; it must be a child of this
         menu.

      *variable*
         The variable associated with a checkbutton or radiobutton entry.

      *onvalue*, *offvalue*
         The values stored in *variable* when a checkbutton entry is selected
         or cleared.

      *value*
         The value stored in *variable* when a radiobutton entry is selected.

      *indicatoron*
         Whether to display the indicator of a checkbutton or radiobutton
         entry.

      *selectcolor*
         The color of the indicator of a checkbutton or radiobutton entry when
         it is selected.

      *selectimage*
         The image displayed when a checkbutton or radiobutton entry is
         selected and *image* is also given.

   .. method:: add_cascade(cnf={}, **kw)

      Add a new cascade entry to the bottom of the menu.
      A cascade entry has an associated submenu, given by its *menu* option,
      which must be a child of this menu; posting the entry posts the submenu
      next to it.

   .. method:: add_checkbutton(cnf={}, **kw)

      Add a new checkbutton entry to the bottom of the menu.
      When invoked, a checkbutton entry toggles between its *onvalue* and
      *offvalue*, storing the result in its associated *variable*, and displays
      an indicator showing whether it is selected.

   .. method:: add_command(cnf={}, **kw)

      Add a new command entry to the bottom of the menu.
      A command entry behaves much like a button: when it is invoked, the
      callback given by its *command* option is called.

   .. method:: add_radiobutton(cnf={}, **kw)

      Add a new radiobutton entry to the bottom of the menu.
      Radiobutton entries sharing the same *variable* form a group of which
      only one may be selected at a time; selecting an entry stores its *value*
      in the variable.

   .. method:: add_separator(cnf={}, **kw)

      Add a separator to the bottom of the menu.
      A separator is displayed as a horizontal dividing line and cannot be
      activated or invoked.

   .. method:: insert(index, itemType, cnf={}, **kw)

      Same as :meth:`add`, except that the new entry is inserted just before
      the entry given by *index* instead of being appended to the end of the
      menu.
      *itemType* is one of ``'command'``, ``'cascade'``, ``'checkbutton'``,
      ``'radiobutton'`` or ``'separator'``.
      The :meth:`!insert_command`, :meth:`!insert_cascade`,
      :meth:`!insert_checkbutton`, :meth:`!insert_radiobutton` and
      :meth:`!insert_separator` convenience methods call this method with the
      corresponding *itemType*.

   .. method:: insert_cascade(index, cnf={}, **kw)

      Insert a new cascade entry before the entry given by *index* (see
      :meth:`add_cascade`).

   .. method:: insert_checkbutton(index, cnf={}, **kw)

      Insert a new checkbutton entry before the entry given by *index* (see
      :meth:`add_checkbutton`).

   .. method:: insert_command(index, cnf={}, **kw)

      Insert a new command entry before the entry given by *index* (see
      :meth:`add_command`).

   .. method:: insert_radiobutton(index, cnf={}, **kw)

      Insert a new radiobutton entry before the entry given by *index* (see
      :meth:`add_radiobutton`).

   .. method:: insert_separator(index, cnf={}, **kw)

      Insert a separator before the entry given by *index* (see
      :meth:`add_separator`).

   .. method:: delete(index1, index2=None)

      Delete all of the menu entries between *index1* and *index2* inclusive.
      If *index2* is omitted, it defaults to *index1*, so that a single entry
      is deleted.
      Attempts to delete a tear-off entry are ignored; remove it by changing
      the *tearoff* option instead.

   .. method:: entrycget(index, option)

      Return the current value of the configuration option *option* for the
      entry given by *index*.

   .. method:: entryconfig(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: entryconfigure(index, cnf=None, **kw)

      Query or modify the configuration options of the entry given by *index*.
      This mirrors :meth:`~Misc.configure`, except that it applies to an
      individual entry rather than to the menu as a whole.
      With no options, it returns a dictionary describing the current options
      of the entry; otherwise it sets the given options.
      The supported options are those accepted by :meth:`add` for the entry's
      type.
      :meth:`entryconfig` is an alias of :meth:`!entryconfigure`.

   .. method:: index(index)

      Return the numerical index corresponding to *index*, or ``None`` if
      *index* selects no entry.

   .. method:: type(index)

      Return the type of the entry given by *index*: one of ``'command'``,
      ``'cascade'``, ``'checkbutton'``, ``'radiobutton'``, ``'separator'`` or
      ``'tearoff'`` (for the tear-off entry).

   .. method:: activate(index)

      Make the entry given by *index* the active entry, redisplaying it with
      its active colors, and deactivate any previously active entry.
      If *index* selects no entry, or the selected entry is disabled, the menu
      ends up with no active entry.

   .. method:: invoke(index)

      Invoke the action of the entry given by *index*, as if it had been
      clicked.
      Nothing happens if the entry is disabled.
      If the entry has a *command* associated with it, the result of that
      command is returned; otherwise the result is an empty string.

   .. method:: post(x, y)

      Display the menu on the screen at the root-window coordinates *x* and
      *y*, adjusting them if necessary so that the whole menu is visible.
      If the *postcommand* option has been specified, it is evaluated before
      the menu is posted.

   .. method:: tk_popup(x, y, entry='')

      Post the menu as a popup at the root-window coordinates *x* and *y*.
      If *entry* is given, the menu is positioned so that this entry is
      displayed under the pointer.

   .. method:: unpost()

      Unmap the menu so that it is no longer displayed, also unposting any
      posted lower-level cascaded submenu.
      This has no effect on Windows and macOS, which manage the unposting of
      menus themselves.

   .. method:: xposition(index)

      Return the x-coordinate, within the menu window, of the leftmost pixel of
      the entry given by *index*.

      .. versionadded:: 3.3

   .. method:: yposition(index)

      Return the y-coordinate, within the menu window, of the topmost pixel of
      the entry given by *index*.


.. class:: Menubutton(master=None, cnf={}, **kw)

   A :class:`!Menubutton` widget displays a textual string, bitmap or image and
   posts an associated :class:`Menu`, given by its *menu* option, when the user
   presses it.
   Like a :class:`Label` it can show *text*, a *textvariable*, or an *image*,
   and the *direction* option controls where the menu appears relative to the
   button.
   Inherits from :class:`Widget`.
   Refer to the Tk ``menubutton`` manual page for the full list of options.


.. class:: Message(master=None, cnf={}, **kw)

   A :class:`!Message` widget displays a non-interactive textual string, given
   by the *text* option or linked to a variable through *textvariable*.
   Unlike a :class:`Label`, it breaks the string into multiple lines in order
   to produce a given aspect ratio, choosing line breaks at word boundaries,
   and it can justify the text left, centered or right.
   Inherits from :class:`Widget`.
   Refer to the Tk ``message`` manual page for the full list of options.


.. class:: OptionMenu(master, variable, value, *values, **kwargs)

   A helper subclass of :class:`Menubutton` that displays a pop-up menu of
   mutually exclusive choices.
   *variable* is a :class:`Variable` kept in sync with the selection, *value*
   is the initial choice, and *values* are the remaining menu entries.
   The keyword argument *command* may be given a callback that is invoked with
   the selected value, and the keyword argument *name* sets the Tk widget name.

   .. method:: destroy()

      Destroy the widget, also cleaning up the associated pop-up menu.

   .. versionchanged:: 3.14
      Added support for the *name* keyword argument.



.. class:: PanedWindow(master=None, cnf={}, **kw)

   A :class:`!PanedWindow` is a geometry-manager widget that arranges any
   number of child *panes* in a row (when *orient* is ``'horizontal'``) or a
   column (when *orient* is ``'vertical'``).
   Each pane holds one widget, and each pair of adjacent panes is separated by
   a movable *sash* that the user can drag with the mouse to resize the widgets
   on either side of it.
   Inherits from :class:`Widget`.

   The *orient* option selects the layout direction, *sashwidth* sets the width
   of each sash and *sashrelief* its relief.
   When *showhandle* is true a small handle is drawn on each sash that the user
   can grab to drag it.
   Refer to the Tk ``panedwindow`` manual page for the full list of options.

   .. method:: add(child, **kw)

      Add *child* to the panedwindow as a new pane, placed after any existing
      panes.
      The keyword arguments specify per-pane management options for *child*;
      they may be any of the options accepted by :meth:`paneconfigure`.

   .. method:: forget(child)
      :no-typesetting:

   .. method:: remove(child)

      Remove the pane containing *child* from the panedwindow.
      All geometry management options for *child* are forgotten.
      :meth:`forget` is an alias of :meth:`!remove`.
      This shadows the inherited geometry-manager :meth:`!forget`;
      use :meth:`~Pack.pack_forget`, :meth:`~Grid.grid_forget` or
      :meth:`~Place.place_forget` to remove the widget itself from its manager.

   .. method:: panes()

      Return a tuple of the widgets managed by the panedwindow, one per pane,
      in order.

   .. method:: panecget(child, option)

      Return the current value of the management option *option* for the pane
      containing *child*.
      *option* may be any value allowed by :meth:`paneconfigure`.

   .. method:: paneconfig(tagOrId, cnf=None, **kw)
      :no-typesetting:

   .. method:: paneconfigure(tagOrId, cnf=None, **kw)

      Query or modify the management options of the pane containing the widget
      *tagOrId*.
      With no options, it returns a dictionary describing all of the available
      options for the pane; given a single option name as a string, it returns
      a description of that one option; otherwise it sets the given options.
      The supported options include *after* and *before* (insert the pane after
      or before another managed window), *height* and *width* (the outer
      dimensions of the window, including any border), *minsize* (the minimum
      size in the paned dimension), *padx* and *pady* (extra space to leave on
      each side of the window), *sticky* (position or stretch the window within
      an oversized pane, using a string of the characters ``n``, ``s``, ``e``
      and ``w``), *hide* (hide the pane while keeping it in the list of panes)
      and *stretch* (how extra space is allocated to the pane: one of
      ``'always'``, ``'first'``, ``'last'``, ``'middle'`` or ``'never'``).
      :meth:`paneconfig` is an alias of :meth:`!paneconfigure`.

   .. method:: identify(x, y)

      Identify the panedwindow component underneath the point given by *x* and
      *y*, in window coordinates.
      If the point is over a sash or a sash handle, the result is a two-element
      tuple containing the index of the sash or handle and a word indicating
      whether it is over a sash or a handle, such as ``(0, 'sash')`` or
      ``(2, 'handle')``.
      If the point is over any other part of the panedwindow, the result is an
      empty string.

   .. method:: sash(*args)

      Query or change the position of the sashes in the panedwindow.
      This is a thin wrapper around the Tk ``sash`` subcommand; the convenience
      methods :meth:`sash_coord`, :meth:`sash_mark` and :meth:`sash_place`
      should normally be used instead.

   .. method:: sash_coord(index)

      Return the current x and y coordinate pair for the sash given by *index*,
      which must be an integer between 0 and one less than the number of panes
      in the panedwindow.
      The coordinates returned are those of the top left corner of the region
      containing the sash.

   .. method:: sash_mark(index)

      Record the current mouse position for the sash given by *index*, for use
      together with later sash-drag operations to move the sash.

   .. method:: sash_place(index, x, y)

      Place the sash given by *index* at the coordinates *x* and *y*.

   .. method:: proxy(*args)

      Query or change the position of the sash proxy, the "ghost" sash shown
      while a sash is being dragged with non-opaque resizing.
      This is a thin wrapper around the Tk ``proxy`` subcommand; the
      convenience methods :meth:`proxy_coord`, :meth:`proxy_forget` and
      :meth:`proxy_place` should normally be used instead.

   .. method:: proxy_coord()

      Return a tuple containing the x and y coordinates of the most recent
      proxy location.

   .. method:: proxy_forget()

      Remove the proxy from the display.

   .. method:: proxy_place(x, y)

      Place the proxy at the coordinates *x* and *y*.


.. class:: Radiobutton(master=None, cnf={}, **kw)

   A :class:`!Radiobutton` widget displays a textual string, bitmap or image
   together with a diamond or circular indicator, and selects one choice out of
   several.
   It has all the behavior of a simple button and, in addition, can be
   selected: typically several radiobuttons share a single *variable*, and
   selecting one sets that variable to the radiobutton's *value*; each
   radiobutton also monitors the variable and automatically selects or
   deselects itself when the variable changes.
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a radiobutton accepts the
   options documented in the Tk ``radiobutton`` manual page, such as
   *variable*, *value* and *command*.

   .. method:: invoke()

      Do just what would happen if the user pressed the radiobutton with the
      mouse: select the button and invoke the associated command, if there is
      one.
      Return the result of the command, or an empty string if no command is
      associated with the radiobutton.
      This is ignored if the radiobutton's state is ``disabled``.

   .. method:: select()

      Select the radiobutton and set the associated variable to the value
      corresponding to this widget.

   .. method:: deselect()

      Deselect the radiobutton and set the associated variable to an empty
      string.
      If this radiobutton was not currently selected, this has no effect.

   .. method:: flash()

      Flash the radiobutton by redisplaying it several times, alternating
      between the active and normal colors.
      At the end of the flash the radiobutton is left in the same normal or
      active state as when the method was called.
      This is ignored if the radiobutton's state is ``disabled``.


.. class:: Scale(master=None, cnf={}, **kw)

   A :class:`!Scale` widget lets the user select a numerical value by moving a
   slider along a trough.
   It can be oriented vertically or horizontally and can optionally display a
   label and the current value.
   Inherits from :class:`Widget`.

   In addition to the standard widget options, a scale accepts the options
   documented in the Tk ``scale`` manual page, such as *from_*, *to*,
   *resolution*, *orient*, *tickinterval*, *variable* and *command*.
   As elsewhere in :mod:`!tkinter`, the leading ``-`` of the Tk option name is
   dropped; *from* is spelled ``from_`` because :keyword:`from` is a Python
   keyword.

   With a non-integer *resolution*, see :ref:`numeric values and the locale
   <tkinter-numeric-locale>`.

   .. method:: get()

      Return the current value of the scale.
      The result is an integer if the scale's *resolution* yields whole
      numbers, and a float otherwise.

   .. method:: set(value)

      Set the scale to *value*, moving the slider accordingly.
      This has no effect if the scale is disabled.

   .. method:: coords(value=None)

      Return a tuple ``(x, y)`` giving the pixel coordinates, relative to the
      widget, of the point on the centerline of the trough that corresponds to
      *value*.
      If *value* is omitted, the scale's current value is used.

   .. method:: identify(x, y)

      Return a string describing the part of the scale at the pixel coordinates
      *x*, *y*: ``'slider'``, ``'trough1'`` (the part of the trough above or to
      the left of the slider), ``'trough2'`` (below or to the right of the
      slider), or an empty string if the point is not over any of these
      elements.


.. class:: Scrollbar(master=None, cnf={}, **kw)

   A :class:`!Scrollbar` widget displays a slider and two arrows that let the
   user scroll an associated widget, such as a :class:`Listbox`, :class:`Text`,
   :class:`Canvas` or :class:`Entry`.
   It is connected to the scrolled widget by setting that widget's
   *xscrollcommand* or *yscrollcommand* option to the scrollbar's :meth:`set`
   method, and the scrollbar's *command* option to the scrolled widget's
   :meth:`~XView.xview` or :meth:`~YView.yview` method.
   Inherits from :class:`Widget`.

   .. method:: get()

      Return the current scrollbar settings as a tuple ``(first, last)`` of two
      fractions between 0 and 1, describing the portion of the document that is
      currently visible, as last passed to :meth:`set`.

   .. method:: set(first, last)

      Set the scrollbar.
      *first* and *last* are fractions between 0 and 1 giving the positions of
      the start and end of the visible portion of the associated document.
      This method is normally registered as the scrolled widget's
      *xscrollcommand* or *yscrollcommand* and called by that widget.

   .. method:: activate(index=None)

      Mark the element *index* (one of ``'arrow1'``, ``'slider'`` or
      ``'arrow2'``) as active, displaying it according to the
      *activebackground* and *activerelief* options.
      If *index* is omitted, return the name of the currently active element,
      or ``None`` if no element is active.

      .. versionchanged:: 3.5
         The *index* argument is now optional.

   .. method:: delta(deltax, deltay)

      Return a float indicating the fractional change in the scrollbar setting
      that corresponds to moving the slider by *deltax* pixels horizontally
      (for horizontal scrollbars) or *deltay* pixels vertically (for vertical
      scrollbars).

   .. method:: fraction(x, y)

      Return a float between 0 and 1 indicating where the point at pixel
      coordinates *x*, *y* lies in the trough: 0 corresponds to the top or left
      of the trough and 1 to the bottom or right.

   .. method:: identify(x, y)

      Return the name of the element under the pixel coordinates *x*, *y* (such
      as ``'arrow1'``), or an empty string if the point does not lie in any
      element of the scrollbar.


.. class:: Spinbox(master=None, cnf={}, **kw)

   A :class:`!Spinbox` widget is an :class:`Entry`-like widget with a pair of
   up/down arrow buttons that let the user step through a range of values in
   addition to editing the value directly.
   The set of values may be a numeric range given by the *from_*, *to* and
   *increment* options, or an explicit list of strings given by the *values*
   option (which takes precedence over the range).
   Each time an arrow is invoked the *command* callback, if any, is called; the
   boolean *wrap* option controls whether stepping past either end of the range
   wraps around to the other end;
   the *format* option specifies how numeric values are formatted;
   and the *validate* option enables validation of the entered text.
   Inherits from :class:`Widget` and :class:`XView`.

   With a non-integer *increment*, see :ref:`numeric values and the locale
   <tkinter-numeric-locale>`.

   Many of the methods take an *index* argument identifying a character in the
   spinbox's string.
   As described in the Tk ``spinbox`` manual page, *index* may be a numeric
   index (counting from 0), ``'anchor'`` (the selection anchor point),
   ``'end'`` (just after the last character), ``'insert'`` (the character just
   after the insertion cursor), ``'sel.first'`` or ``'sel.last'`` (the ends of
   the selection), or ``@x`` (the character covering pixel x-coordinate *x* in
   the window).

   .. method:: get()

      Return the spinbox's string.

   .. method:: insert(index, s)

      Insert the characters of the string *s* just before the character given
      by *index*.

   .. method:: delete(first, last=None)

      Delete one or more characters of the spinbox.
      *first* is the index of the first character to delete, and *last* is the
      index of the character just after the last one to delete.
      If *last* is omitted, a single character at *first* is deleted.

   .. method:: icursor(index)

      Arrange for the insertion cursor to be displayed just before the
      character given by *index*.

   .. method:: index(index)

      Return the numerical index corresponding to *index*, as a string.

   .. method:: bbox(index)

      Return a tuple of four integers ``(x, y, width, height)`` describing the
      bounding box of the character given by *index*.
      *x* and *y* are the pixel coordinates of the upper-left corner of the
      character relative to the widget, and *width* and *height* are its size
      in pixels.
      The bounding box may refer to a region outside the visible area of the
      window.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: identify(x, y)

      Return the name of the window element at the pixel coordinates *x*, *y*:
      one of ``'buttondown'``, ``'buttonup'``, ``'entry'`` or ``'none'``.

   .. method:: invoke(element)

      Invoke the spin button given by *element*, either ``'buttonup'`` or
      ``'buttondown'``, triggering the action associated with it.

   .. method:: scan(*args)

      A thin wrapper around the Tk ``scan`` widget subcommand, used to
      implement fast dragging of the view: ``scan('mark', x)`` records *x* and
      the current view, and ``scan('dragto', x)`` adjusts the view relative to
      that mark.
      The :meth:`scan_mark` and :meth:`scan_dragto` methods wrap the two forms.

   .. method:: scan_mark(x)

      Record *x* and the current view in the spinbox window, for use with a
      later :meth:`scan_dragto` call.
      This is typically associated with a mouse button press in the widget.

   .. method:: scan_dragto(x)

      Adjust the view by 10 times the difference between *x* and the *x* passed
      to the last :meth:`scan_mark` call.
      This is typically associated with mouse motion events, producing the
      effect of dragging the spinbox at high speed through the window.

   .. method:: selection(*args)

      A thin wrapper around the Tk ``selection`` widget subcommand, used to
      adjust the selection within the spinbox.
      It has several forms depending on the first argument, such as
      ``selection('adjust', index)``, ``selection('clear')``,
      ``selection('element', ?elem?)``, ``selection('from', index)``,
      ``selection('present')``, ``selection('range', start, end)`` and
      ``selection('to', index)``.
      The :meth:`selection_adjust`, :meth:`selection_clear`,
      :meth:`selection_element`, :meth:`selection_from`,
      :meth:`selection_present`, :meth:`selection_range` and
      :meth:`selection_to` methods wrap these forms.

   .. method:: selection_adjust(index)

      Locate the end of the selection nearest to the character given by *index*
      and adjust that end of the selection to be at *index* (including but not
      going beyond *index*).
      The other end becomes the anchor point for future :meth:`selection_to`
      calls.
      If the selection is not currently in the spinbox, a new selection is
      created to include the characters between *index* and the most recent
      anchor point, inclusive.

   .. method:: selection_clear()

      Clear the selection if it is currently in this widget.
      If the selection is not in this widget, the method has no effect.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on a :class:`Spinbox`.

   .. method:: selection_element(element=None)

      Set or get the currently selected element.
      If *element* (one of ``'buttonup'``, ``'buttondown'`` or ``'none'``) is
      given, that spin button is selected and displayed depressed; otherwise
      the name of the currently selected element is returned.

   .. method:: selection_from(index)

      Set the selection anchor point to just before the character given by
      *index*, without changing the selection itself.

      .. versionadded:: 3.8


   .. method:: selection_present()

      Return ``True`` if there are characters selected in the spinbox,
      ``False`` otherwise.

      .. versionadded:: 3.8


   .. method:: selection_range(start, end)

      Set the selection to include the characters starting with the one indexed
      by *start* and ending with the one just before *end*.
      If *end* refers to the same character as *start* or an earlier one, the
      selection is cleared.

      .. versionadded:: 3.8


   .. method:: selection_to(index)

      Set the selection between *index* and the anchor point.
      If *index* is before the anchor point, the selection runs from *index* up
      to but not including the anchor point; if it is after, the selection runs
      from the anchor point up to but not including *index*; if it is the same,
      nothing happens.
      The anchor point is the one set by the most recent :meth:`selection_from`
      or :meth:`selection_adjust` call.
      If the selection is not in this widget, a new selection is created using
      the most recent anchor point.

      .. versionadded:: 3.8



.. class:: Text(master=None, cnf={}, **kw)

   A :class:`!Text` widget displays and edits multi-line text.
   Portions of the text may be styled with **tags**, particular positions may
   be annotated with floating **marks**, and arbitrary images and other widgets
   may be embedded in the text.
   The widget also provides an unlimited undo/redo mechanism and supports peer
   widgets that share the same underlying data.
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``text`` manual page for the full list of options.

   Most of the methods take one or more *index* arguments that identify a
   position within the text.
   As described in the Tk ``text`` manual page, an index is a string consisting
   of a base, optionally followed by one or more modifiers.
   The base may be ``'line.char'`` (line *line*, character *char*, where lines
   are counted from 1 and characters within a line from 0; ``'line.end'``
   refers to the newline ending the line), ``'end'`` (the position just after
   the last newline), the name of a mark, ``'tag.first'`` or ``'tag.last'``
   (the first character tagged with *tag*, or the position just after the last
   such character), the name of an embedded image or window, or ``@x,y`` (the
   character covering pixel coordinates *x*, *y* in the widget).
   A modifier such as ``'+5 chars'``, ``'-3 lines'``, ``'linestart'``,
   ``'lineend'``, ``'wordstart'`` or ``'wordend'`` adjusts the index relative
   to its base; several modifiers may be combined and are applied from left to
   right, for example ``'insert wordstart - 1 c'``.

   .. method:: insert(index, chars, *args)

      Insert the string *chars* just before the character at *index* (if
      *index* is ``'end'``, just before the final newline).
      By default the new text inherits any tags present on both sides of the
      insertion point.
      If *args* is given, it consists of alternating *tagList*, *chars* values:
      the preceding *chars* receives exactly the tags listed (a tag list may be
      a single tag name or a sequence of names), overriding the surrounding
      tags.

   .. method:: delete(index1, index2=None)

      Delete the range of characters from *index1* up to but not including
      *index2*.
      If *index2* is omitted, the single character at *index1* is deleted.
      The widget always keeps a newline as its last character, so a deletion
      that would remove it is adjusted accordingly.

   .. method:: replace(index1, index2, chars, *args)

      Replace the range of characters from *index1* up to but not including
      *index2* with *chars*.
      This is equivalent to a :meth:`delete` followed by an :meth:`insert` at
      *index1*; *args* is interpreted as for :meth:`insert`.

      .. versionadded:: 3.3

   .. method:: get(index1, index2=None)

      Return the text from *index1* up to but not including *index2* as a
      string.
      If *index2* is omitted, return the single character at *index1*.
      Embedded images and windows are omitted from the result.

   .. method:: index(index)

      Return the position corresponding to *index* in the canonical
      ``'line.char'`` form.

   .. method:: compare(index1, op, index2)

      Compare the positions of *index1* and *index2* using the relational
      operator *op*, which must be one of ``'<'``, ``'<='``, ``'=='``,
      ``'>='``, ``'>'`` or ``'!='``, and return the boolean result.

   .. method:: count(index1, index2, *options, return_ints=False)

      Count the number of items of the requested kinds between *index1* and
      *index2*; the count is negative if *index1* is after *index2*.
      Each of *options* names a kind of item to count: ``'chars'``,
      ``'displaychars'``, ``'displayindices'``, ``'displaylines'``,
      ``'indices'``, ``'lines'``, ``'xpixels'`` or ``'ypixels'`` (the default,
      used when no option is given, is ``'indices'``).
      The pseudo-option ``'update'`` forces any out-of-date layout information
      to be recalculated before the following options are evaluated.
      When *return_ints* is true and a single counting option is given, return
      a plain integer; otherwise return a tuple with one integer per counting
      option (or ``None`` if the result is empty).

      .. versionadded:: 3.3

      .. versionchanged:: 3.13
         Added the *return_ints* parameter.


   .. method:: see(index)

      Adjust the view so that the character given by *index* is visible.
      If it is already visible the method has no effect; if it is a short
      distance out of view the widget scrolls just enough to bring it to the
      nearest edge, otherwise it scrolls to center *index* in the window.

   .. method:: bbox(index)

      Return a tuple ``(x, y, width, height)`` giving the bounding box, in
      pixels, of the visible part of the character at *index*, or ``None`` if
      that character is not visible on the screen.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: dlineinfo(index)

      Return a tuple ``(x, y, width, height, baseline)`` describing the display
      line that contains *index*: the first four values give the bounding box
      of the line in pixels and *baseline* gives the offset of the baseline
      measured down from the top of the area.
      Return ``None`` if that display line is not visible on the screen.

   .. method:: mark_set(markName, index)

      Set the mark named *markName* to the position just before the character
      at *index*, creating the mark if it does not already exist.
      A mark created this way has right gravity by default.

   .. method:: mark_unset(*markNames)

      Remove each of the marks named in *markNames*.
      The special ``insert`` and ``current`` marks may not be removed.

   .. method:: mark_names()

      Return a tuple of the names of all marks currently set in the widget.

   .. method:: mark_gravity(markName, direction=None)

      If *direction* is omitted, return the gravity of mark *markName*, either
      ``'left'`` or ``'right'``.
      Otherwise set its gravity to *direction*.
      The gravity determines on which side of the mark text inserted at the
      mark's position appears: a mark with right gravity (the default) stays to
      the right of such text.

   .. method:: mark_next(index)

      Return the name of the first mark at or after *index*, or ``None`` if
      there is none.
      When *index* is the name of a mark, the search starts just after that
      mark.

   .. method:: mark_previous(index)

      Return the name of the last mark at or before *index*, or ``None`` if
      there is none.
      When *index* is the name of a mark, the search starts just before that
      mark.

   .. method:: tag_add(tagName, index1, *args)

      Add the tag *tagName* to the range of characters from *index1* up to but
      not including the next index in *args*.
      Further pairs of indices may follow in *args* to tag additional ranges; a
      trailing single index tags just the character at that index.

   .. method:: tag_remove(tagName, index1, index2=None)

      Remove the tag *tagName* from the characters from *index1* up to but not
      including *index2* (or from the single character at *index1* if *index2*
      is omitted).
      The tag itself continues to exist even if no characters carry it.

   .. method:: tag_delete(*tagNames)

      Delete each of the tags named in *tagNames*, removing them from all
      characters and discarding their options and bindings.

   .. method:: tag_config(tagName, cnf=None, **kw)
      :no-typesetting:

   .. method:: tag_configure(tagName, cnf=None, **kw)

      Query or modify the configuration options of the tag *tagName*.
      This mirrors :meth:`~Misc.configure`, except that it applies to a tag
      rather than to the widget as a whole: with no options it returns a
      dictionary describing the current options, otherwise it sets the given
      options.
      Defining a tag this way also gives it a priority higher than any existing
      tag.

      The supported tag options, all controlling the appearance of the tagged
      text, are:

      *font*
         The font to use for the text.

      *foreground*
         The color to use for the text.

      *background*
         The color to use for the area behind the text.

      *fgstipple*, *bgstipple*
         Bitmaps used to stipple the foreground (text) and the background;
         only well supported on X11.

      *borderwidth*
         The width of the border drawn around the text according to *relief*
         (default ``0``).

      *relief*
         The 3-D appearance of the text's border: ``'flat'`` (the default),
         ``'raised'``, ``'sunken'``, ``'ridge'``, ``'groove'`` or ``'solid'``.

      *offset*
         How far the text is raised above (or, if negative, lowered below) the
         baseline, for superscripts and subscripts.

      *underline*
         Whether to underline the text (a boolean).

      *underlinefg*
         The color of the underline; it defaults to the text color.

      *overstrike*
         Whether to draw a line through the middle of the text.

      *overstrikefg*
         The color of the overstrike line; it defaults to the text color.

      *elide*
         Whether the text is elided (hidden).

      *justify*
         How to justify the first character of a display line: ``'left'`` (the
         default), ``'right'`` or ``'center'``.

      *wrap*
         How to wrap lines that are too long: ``'char'``, ``'word'`` or
         ``'none'``.

      *lmargin1*, *lmargin2*
         The indentation, in pixels, of the first display line of a logical
         line and of the remaining display lines.

      *lmargincolor*
         The color of the left margin area.

      *rmargin*
         The right-hand margin, in pixels.

      *rmargincolor*
         The color of the right margin area.

      *spacing1*, *spacing2*, *spacing3*
         Extra space, in pixels, above the first display line of a logical
         line, between its display lines, and below its last display line.

      *tabs*
         The set of tab stops, in the same form as the widget's *tabs* option.

      *tabstyle*
         How tab stops are interpreted: ``'tabular'`` or ``'wordprocessor'``.

      *selectbackground*, *selectforeground*
         The background and foreground colors used for the text while it is
         selected.

      .. note::

         Tk 8.6 added the *lmargincolor*, *overstrikefg*, *rmargincolor*,
         *selectbackground*, *selectforeground* and *underlinefg* options.

      :meth:`tag_config` is an alias of :meth:`!tag_configure`.

   .. method:: tag_cget(tagName, option)

      Return the current value of the configuration option *option* for the tag
      *tagName*.

   .. method:: tag_names(index=None)

      If *index* is omitted, return a tuple of the names of all tags defined in
      the widget; otherwise return only the names of the tags applied to the
      character at *index*.
      The names are ordered from lowest to highest priority.

   .. method:: tag_ranges(tagName)

      Return a tuple of indices describing all ranges of text tagged with
      *tagName*.
      The result alternates start and end indices, so that elements ``2*i`` and
      ``2*i+1`` bound the *i*-th range.

   .. method:: tag_nextrange(tagName, index1, index2=None)

      Search forward from *index1* (up to *index2* if given) for the first
      range of characters tagged with *tagName*, and return a two-element tuple
      of its start and end indices, or an empty tuple if there is no such
      range.

   .. method:: tag_prevrange(tagName, index1, index2=None)

      Search backward from *index1* (down to *index2* if given) for the nearest
      preceding range of characters tagged with *tagName*, and return a
      two-element tuple of its start and end indices, or an empty tuple if
      there is no such range.

   .. method:: tag_raise(tagName, aboveThis=None)

      Raise the priority of tag *tagName* so that it is just above the priority
      of *aboveThis*, or to the highest priority of all tags if *aboveThis* is
      omitted.
      When the display options of overlapping tags conflict, the
      higher-priority tag wins.

   .. method:: tag_lower(tagName, belowThis=None)

      Lower the priority of tag *tagName* so that it is just below the priority
      of *belowThis*, or to the lowest priority of all tags if *belowThis* is
      omitted.

   .. method:: tag_bind(tagName, sequence, func, add=None)

      Bind the event *sequence* on characters tagged with *tagName* to the
      callback *func*, so that *func* is invoked when that event occurs over
      such a character.
      If *add* is true the binding is added alongside any existing bindings for
      *sequence*, otherwise it replaces them.
      Works like :meth:`~Misc.bind` and returns the identifier of the new
      binding.

   .. method:: tag_unbind(tagName, sequence, funcid=None)

      Remove the bindings of the event *sequence* on characters tagged with
      *tagName*.
      If *funcid* is given, only that binding (as returned by :meth:`tag_bind`)
      is removed and its callback is unregistered.

      .. versionchanged:: 3.13
         If *funcid* is given, only that callback is unbound.


   .. method:: image_create(index, cnf={}, **kw)

      Embed an image at *index* and return the name assigned to this image
      instance, which may then be used as an index or passed to the other
      ``image_*`` methods.
      The options, given in *cnf* and *kw*, include *image* (the Tk image to
      display), *name* (a base name for the instance), *align*, *padx* and
      *pady*.

   .. method:: image_cget(index, option)

      Return the current value of the configuration option *option* for the
      embedded image at *index*.

   .. method:: image_configure(index, cnf=None, **kw)

      Query or modify the configuration options of the embedded image at
      *index*, like :meth:`~Misc.configure` but applied to that image.

   .. method:: image_names()

      Return a tuple of the names of all images embedded in the widget.

      .. note::

         This shadows the inherited :meth:`Misc.image_names`,
         which returns the names of all images in the Tcl interpreter;
         that method is not available on a :class:`Text`.

   .. method:: window_create(index, cnf={}, **kw)

      Embed a window (any widget) at *index*.
      The options, given in *cnf* and *kw*, include *window* (the widget to
      embed), *create* (a callback that creates the widget on demand), *align*,
      the boolean *stretch* (whether the widget is stretched vertically to the
      height of the line), *padx* and *pady*.
      The embedded widget must be a descendant of the text widget's parent.

   .. method:: window_cget(index, option)

      Return the current value of the configuration option *option* for the
      embedded window at *index*.

   .. method:: window_config(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: window_configure(index, cnf=None, **kw)

      Query or modify the configuration options of the embedded window at
      *index*, like :meth:`~Misc.configure` but applied to that window.

      :meth:`window_config` is an alias of :meth:`!window_configure`.

   .. method:: window_names()

      Return a tuple of the names of all windows embedded in the widget.

   .. method:: edit(*args)

      Low-level wrapper around the Tk ``edit`` widget command that controls the
      undo/redo mechanism and the modified flag; *args* is the ``edit``
      subcommand and its arguments.
      The :meth:`!edit_\*` methods below are thin wrappers around it and are
      usually more convenient.

   .. method:: edit_modified(arg=None)

      If *arg* is omitted, return the current state of the modified flag as
      true or false; the flag is set automatically whenever the text is
      inserted or deleted.
      Otherwise set the flag to the boolean *arg*.

   .. method:: edit_undo()

      Undo the most recent edit action, that is, all the inserts and deletes
      recorded on the undo stack since the previous separator, and move it to
      the redo stack.
      Raises :exc:`TclError` if the undo stack is empty.
      Has no effect unless the *undo* option is true.
      Since Tk 9.0, returns a tuple of indices delimiting the ranges of text
      that were changed.

   .. method:: edit_redo()

      Reapply the most recently undone edit action, provided no further edits
      have been made since, and move it back to the undo stack.
      Raises :exc:`TclError` if the redo stack is empty.
      Has no effect unless the *undo* option is true.
      Since Tk 9.0, returns a tuple of indices delimiting the ranges of text
      that were changed.

   .. method:: edit_reset()

      Clear the undo and redo stacks.

   .. method:: edit_separator()

      Push a separator onto the undo stack, marking a boundary between edit
      actions for undo and redo.
      Has no effect unless the *undo* option is true.
      Separators are inserted automatically when the *autoseparators* option is
      true.

   .. method:: search(pattern, index, stopindex=None, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, *, nolinestop=None, strictlimits=None)

      Search for *pattern* starting at *index* and return the index of the
      first character of the first match, or an empty string if there is no
      match.
      Searching stops at *stopindex* if given; otherwise it wraps around the
      ends of the text until the starting position is reached again.
      The following boolean keyword flags control the search: *forwards* or
      *backwards* select the direction (forward is the default); *exact* (the
      default) or *regexp* select literal or regular-expression matching;
      *nocase* makes the match case-insensitive; *elide* causes hidden text to
      be searched as well; *nolinestop* (regexp only) lets ``.`` and ``[^``
      match newlines; and *strictlimits* requires the whole match to lie within
      *index* and *stopindex*.
      If *count* is a :class:`Variable`, the number of index positions in the
      match is stored in it.

      .. versionchanged:: 3.15
         Added the *nolinestop* and *strictlimits* parameters.


   .. method:: search_all(pattern, index, stopindex=None, *, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, nolinestop=None, overlap=None, strictlimits=None)

      Like :meth:`search`, but find every match in the searched range and
      return a tuple of the starting indices of all matches (empty if there are
      none).
      By default overlapping matches are not reported; passing a true *overlap*
      returns every match that is not wholly contained in another.
      If *count* is a :class:`Variable`, it receives a list with one element
      per match.

      .. versionadded:: 3.15


   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y)

      Scroll the widget by 10 times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events, producing the effect of
      dragging the text at high speed through the window.

   .. method:: debug(boolean=None)

      If *boolean* is omitted, return whether internal consistency checks of
      the B-tree data structure are enabled.
      Otherwise enable or disable them.
      The setting is shared by all text widgets and may noticeably slow down
      widgets holding large amounts of text.

   .. method:: dump(index1, index2=None, command=None, **kw)

      Return the contents of the widget from *index1* up to but not including
      *index2* (or just the segment at *index1* if *index2* is omitted),
      including text and information about marks, tags, images and windows.
      The result is a list of ``(key, value, index)`` triples, where *key* is
      one of ``'text'``, ``'mark'``, ``'tagon'``, ``'tagoff'``, ``'image'`` or
      ``'window'``.
      By default all kinds are reported; passing any of the keyword arguments
      *all*, *text*, *mark*, *tag*, *image* or *window* as true restricts the
      dump to the selected kinds.
      If *command* is given, it is called once per triple with the three values
      as arguments and nothing is returned.

   .. method:: peer_create(newPathName, cnf={}, **kw)

      Create a peer text widget with the path name *newPathName* that shares
      this widget's underlying data (text, marks, tags, images and the undo
      stack).
      Changes made through any peer are reflected in all of them.
      By default the peer covers the same lines as this widget; standard text
      options, including *startline* and *endline*, may be given to override
      this.

      .. versionadded:: 3.3

   .. method:: peer_names()

      Return a tuple of the path names of this widget's peers, not including
      the widget itself.

      .. versionadded:: 3.3

   .. method:: yview_pickplace(*what)

      Adjust the view so that the location given by *what* is visible.
      This is an obsolete equivalent of :meth:`see`, which should be used
      instead.


Variable classes
^^^^^^^^^^^^^^^^

.. class:: Variable(master=None, value=None, name=None)

   The base class for the Tk variable wrappers.
   A Tk variable is a value stored in the Tcl interpreter that can be linked to
   widgets through their *variable* or *textvariable* options (see
   :ref:`coupling-widget-variables`), so that changes propagate both ways:
   updating the variable updates every widget bound to it, and a user editing
   such a widget updates the variable.

   *master* is the widget whose Tcl interpreter owns the variable; if omitted,
   the default root window is used.
   *value* is the initial value; if omitted, a type-specific default is used.
   *name* is the name of the variable in the Tcl interpreter; if omitted, a
   unique name of the form ``'PY_VARnum'`` is generated.
   If *name* matches an existing variable and *value* is omitted, the existing
   value is retained.

   In most cases you should use one of the typed subclasses below --
   :class:`StringVar`, :class:`IntVar`, :class:`DoubleVar` or
   :class:`BooleanVar` -- rather than :class:`!Variable` directly.

   .. note::

      When a :class:`!Variable` is garbage collected, its Tcl variable is unset.
      Keep a reference to it for as long as a widget is linked to it, for example
      by storing it as an attribute rather than in a local variable.
      Otherwise Tk recreates the Tcl variable to keep the widget working, but it
      is never unset again, leaking one Tcl variable per dropped wrapper.

   .. versionchanged:: 3.10
      Two variables now compare equal (``==``) only when they have the same
      name, are of the same class, and belong to the same Tcl interpreter.

   .. method:: get()

      Return the current value of the variable.
      For the base class the value is returned as a string; the typed
      subclasses convert it to the appropriate Python type.

   .. method:: initialize(value)
      :no-typesetting:

   .. method:: set(value)

      Set the variable to *value*.
      :meth:`initialize` is an alias of :meth:`!set`.

      .. versionadded:: 3.3
         The *initialize* spelling.

   .. method:: trace_add(mode, callback)

      Register *callback* to be called when the variable is accessed according
      to *mode*.
      *mode* is one of the strings ``'array'``, ``'read'``, ``'write'`` or
      ``'unset'``, or a list or tuple of such strings.

      When triggered, *callback* is called with three arguments: the name of
      the Tcl variable, an index (or an empty string if the variable is not an
      element of an array), and the *mode* that triggered the call.

      Return the internal name of the registered callback, which can be passed
      to :meth:`trace_remove`.

      .. versionadded:: 3.6

   .. method:: trace_remove(mode, cbname)

      Remove a trace callback from the variable.
      *mode* must match the *mode* that was passed to :meth:`trace_add`, and
      *cbname* is the callback name returned by :meth:`trace_add`.

      .. versionadded:: 3.6

   .. method:: trace_info()

      Return a list of ``(modes, cbname)`` pairs describing all traces
      currently set on the variable, where *modes* is a tuple of mode strings
      and *cbname* is the internal callback name.

      .. versionadded:: 3.6

   .. method:: trace(mode, callback)
      :no-typesetting:

   .. method:: trace_variable(mode, callback)

      Register *callback* to be called when the variable is accessed according
      to *mode*.
      *mode* is one of the strings ``'r'``, ``'w'`` or ``'u'``, for read, write
      or unset.
      Return the internal name of the registered callback.
      :meth:`trace` is an alias of :meth:`!trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_add` instead.  This method wraps a Tcl feature that
         was removed in Tcl 9.0.

   .. method:: trace_vdelete(mode, cbname)

      Remove the trace callback named *cbname* registered for *mode* with
      :meth:`trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_remove` instead.  This method wraps a Tcl feature
         that was removed in Tcl 9.0.

   .. method:: trace_vinfo()

      Return a list of ``(mode, cbname)`` pairs for all traces set on the
      variable with :meth:`trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_info` instead.  This method wraps a Tcl feature that
         was removed in Tcl 9.0.


.. class:: StringVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a string.
   The default value is ``''``.

   .. method:: get()

      Return the value of the variable as a :class:`str`.


.. class:: IntVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds an integer.
   The default value is ``0``.

   .. method:: get()

      Return the value of the variable as an :class:`int`.


.. class:: DoubleVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a float.
   The default value is ``0.0``.

   .. method:: get()

      Return the value of the variable as a :class:`float`.

   .. _tkinter-numeric-locale:

   .. note::

      A floating-point value is always parsed with a period (``.``) as the
      decimal separator, but :class:`Spinbox`, :class:`Scale` and
      :class:`ttk.Spinbox <tkinter.ttk.Spinbox>` format it according to the
      ``LC_NUMERIC`` locale.  Under a locale that uses a comma they produce a
      value that :meth:`get` cannot read, raising :exc:`TclError`.  Set
      ``LC_NUMERIC`` to a locale that uses a period (such as ``'C'``) to avoid
      this.


.. class:: BooleanVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a boolean.
   The default value is ``False``.

   .. method:: get()

      Return the value of the variable as a :class:`bool`.
      Raise a :exc:`ValueError` if the value cannot be interpreted as a
      boolean.

   .. method:: initialize(value)
      :no-typesetting:

   .. method:: set(value)

      Set the variable to *value*, converting it to a boolean.
      :meth:`initialize` is an alias of :meth:`!set`.

      .. versionadded:: 3.3
         The *initialize* spelling.


Image classes
^^^^^^^^^^^^^

.. class:: Image(imgtype, name=None, cnf={}, master=None, **kw)

   Base class for Tk images.
   *imgtype* is the Tk image type, one of ``'photo'`` or ``'bitmap'``.
   An image is a named object that can be displayed by widgets through their
   *image* option; deleting all references to the :class:`!Image` object
   deletes the underlying Tk image.
   Usually you create a :class:`PhotoImage` or :class:`BitmapImage` rather than
   an :class:`!Image` directly.

   The image's configuration options are given by *cnf* and *kw* and may be
   queried and changed later with the mapping protocol (using ``image[key]``)
   or with the :meth:`configure` method.

   .. method:: config(**kw)
      :no-typesetting:

   .. method:: configure(**kw)

      Modify one or more configuration options of the image.
      The valid options depend on the image type; see :class:`PhotoImage` and
      :class:`BitmapImage`.
      :meth:`config` is an alias of :meth:`!configure`.

   .. method:: height()

      Return the height of the image, in pixels.

   .. method:: width()

      Return the width of the image, in pixels.

   .. method:: type()

      Return the type of the image, that is the value of *imgtype* with which
      it was created (for example ``'photo'`` or ``'bitmap'``).


.. class:: PhotoImage(name=None, cnf={}, master=None, **kw)

   A full-color image (the Tk ``photo`` image type), stored internally with a
   varying degree of transparency per pixel.
   It can read and write GIF, PPM/PGM and (in Tk 8.6 and later) PNG files, read
   SVG files (in Tk 9.0 and later), and be drawn in widgets.
   Inherits from :class:`Image`.

   The configuration options include *data* (the image contents as a string),
   *file* (the name of a file to read the contents from), *format* (the name of
   the file format handler), *width* and *height* (the size of the image, used
   when building it up piece by piece), *gamma* and *palette*.

   .. method:: blank()

      Blank the image; that is, set the entire image to have no data, so that
      it is displayed as transparent and the background of whatever window it
      is displayed in shows through.

   .. method:: cget(option)

      Return the current value of the configuration option *option*.

   .. method:: copy(*, from_coords=None, zoom=None, subsample=None)

      Return a new :class:`PhotoImage` with a copy of this image.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      ``(x1, y1)`` and ``(x2, y2)`` specify diagonally opposite corners of the
      rectangle.
      If *x2* and *y2* are not specified, they default to the bottom-right
      corner of the source image.
      The pixels copied include the left and top edges of the rectangle but not
      the bottom or right edges.
      If *from_coords* is not given, the whole source image is copied.

      If *zoom* or *subsample* are specified, the image is transformed as in
      the :meth:`zoom` or :meth:`subsample` methods.
      The value must be a single integer or a pair of integers.

      .. versionchanged:: 3.13
         Added the *from_coords*, *zoom* and *subsample* parameters.


   .. method:: copy_replace(sourceImage, *, from_coords=None, to=None, \
                            shrink=False, zoom=None, subsample=None, \
                            compositingrule=None)

      Copy a region from *sourceImage* (which must be a :class:`PhotoImage`)
      into this image, possibly with pixel zooming and/or subsampling.
      If no options are specified, the whole of *sourceImage* is copied into
      this image, starting at coordinates ``(0, 0)``.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      *to* specifies a rectangular sub-region of the destination image to be
      affected.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If *x2* and *y2* are not specified, they default to ``(x1, y1)`` plus the
      size of the source region (after subsampling and zooming, if specified).
      If *x2* and *y2* are specified, the source region is replicated if
      necessary to fill the destination region in a tiled fashion.

      If *shrink* is true, the size of the destination image is reduced, if
      necessary, so that the region being copied into is at the bottom-right
      corner of the image.

      If *zoom* or *subsample* are specified, the image is transformed as in
      the :meth:`zoom` or :meth:`subsample` methods.
      The value must be a single integer or a pair of integers.

      *compositingrule* specifies how transparent pixels in the source image
      are combined with the destination image.
      With ``'overlay'`` (the default), the old contents of the destination
      image remain visible, as if the source image were printed on a piece of
      transparent film and placed over the top of the destination.
      With ``'set'``, the old contents of the destination image are discarded
      and the source image is used as-is.

      .. versionadded:: 3.13


   .. method:: data(format=None, *, from_coords=None, background=None, \
                    grayscale=False)

      Return the image data.

      *format* specifies the name of the image file format handler to use.
      If it is not given, the data is returned as a tuple (one element per row)
      of strings containing space-separated (one element per pixel/column)
      colors in ``#RRGGBB`` format.

      *from_coords* specifies a rectangular region of the image to be returned.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region, including ``(x1, y1)`` and excluding ``(x2, y2)``.
      If *from_coords* is not given, the whole image is returned.

      If *background* is specified, the data does not contain any transparency
      information; in all transparent pixels the color is replaced by the
      specified color.

      If *grayscale* is true, the data does not contain color information; all
      pixel data is transformed into grayscale.

      .. versionadded:: 3.13


   .. method:: get(x, y)

      Return the color of the pixel at coordinates (*x*, *y*) as an
      ``(r, g, b)`` tuple of three integers between 0 and 255, representing the
      red, green and blue components respectively.

   .. method:: put(data, to=None)

      Set pixels of the image to the colors given in *data*, which must be a
      string or a nested sequence of horizontal rows of pixel colors (for
      example ``"{red green} {blue yellow}"``).

      *to* specifies the coordinates of the region of the image into which the
      data are copied.
      It must be a tuple or a list of 2 or 4 integers ``(x1, y1)`` or
      ``(x1, y1, x2, y2)`` giving the top-left corner, and optionally the
      bottom-right corner, of the region.
      The default position is ``(0, 0)``.

   .. method:: read(filename, format=None, *, from_coords=None, to=None, \
                    shrink=False)

      Read image data from the file named *filename* into the image.

      *format* specifies the format of the image data in the file.

      *from_coords* specifies a rectangular sub-region of the image file data
      to be copied to the destination image.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image in the file.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region.
      If *from_coords* is not given, the whole of the image in the file is
      read.

      *to* specifies the coordinates of the top-left corner of the region of
      the image into which the data are read.
      The default is ``(0, 0)``.

      If *shrink* is true, the size of the image is reduced, if necessary, so
      that the region into which the file data are read is at the bottom-right
      corner of the image.

      .. versionadded:: 3.13


   .. method:: subsample(x, y='', *, from_coords=None)

      Return a new :class:`PhotoImage` based on this image but using only every
      *x*-th pixel in the X direction and every *y*-th pixel in the Y
      direction.
      If *y* is not given, it defaults to the same value as *x*.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      .. versionchanged:: 3.13
         Added the *from_coords* parameter.


   .. method:: transparency_get(x, y)

      Return ``True`` if the pixel at coordinates (*x*, *y*) is fully
      transparent, ``False`` otherwise.

      .. versionadded:: 3.8


   .. method:: transparency_set(x, y, boolean)

      Make the pixel at coordinates (*x*, *y*) fully transparent if *boolean*
      is true, fully opaque otherwise.

      .. versionadded:: 3.8


   .. method:: write(filename, format=None, from_coords=None, *, \
                     background=None, grayscale=False)

      Write image data from the image to the file named *filename*.

      *format* specifies the name of the image file format handler to use.
      If it is not given, the format is guessed from the file extension.

      *from_coords* specifies a rectangular region of the image to be written.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region.
      If *from_coords* is not given, the whole image is written.

      If *background* is specified, the data does not contain any transparency
      information; in all transparent pixels the color is replaced by the
      specified color.

      If *grayscale* is true, the data does not contain color information; all
      pixel data is transformed into grayscale.

      .. versionchanged:: 3.13
         Added the *background* and *grayscale* parameters.


   .. method:: zoom(x, y='', *, from_coords=None)

      Return a new :class:`PhotoImage` with this image magnified by a factor of
      *x* in the X direction and *y* in the Y direction.
      If *y* is not given, it defaults to the same value as *x*.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      .. versionchanged:: 3.13
         Added the *from_coords* parameter.



.. class:: BitmapImage(name=None, cnf={}, master=None, **kw)

   A two-color image (the Tk ``bitmap`` image type) created from an X11 bitmap.
   Each pixel displays a foreground color, a background color, or nothing
   (producing a transparent effect).
   Inherits from :class:`Image`.

   The configuration options are *data* or *file* (the source bitmap, given as
   a string in X11 bitmap format or as the name of a file in that format),
   *maskdata* or *maskfile* (the mask bitmap, in the same forms), and
   *foreground* and *background* (the two colors).
   For pixels where the mask is zero the image displays nothing; for other
   pixels it displays the foreground color where the source is one and the
   background color where the source is zero.
   If *background* is set to an empty string, the background pixels are
   transparent.

   :class:`!BitmapImage` has no methods of its own beyond those inherited from
   :class:`Image`.


Other classes
^^^^^^^^^^^^^

.. class:: Event()

   A container for the attributes of an event passed to a callback bound with
   :meth:`Misc.bind`.
   An :class:`!Event` instance has the following attributes, each corresponding
   to a field of the underlying Tk event; depending on the event type, some
   attributes may be set to the string ``'??'`` to indicate that they are not
   meaningful.
   See :ref:`bindings-and-events`.

   .. attribute:: serial

      The serial number of the event.

   .. attribute:: num

      The mouse button that was pressed or released (for button events).

   .. attribute:: focus

      Whether the window has the focus (for ``Enter`` and ``Leave`` events).

   .. attribute:: height
                  width

      The new height and width of the window (for ``Configure`` and ``Expose``
      events).

   .. attribute:: keycode

      The keycode of the key that was pressed or released.

   .. attribute:: state

      The state of the event, as a number (for most events) or a string (for
      ``Visibility`` events).

   .. attribute:: time

      The timestamp of the event, in milliseconds.

   .. attribute:: x
                  y

      The pointer position relative to the widget, in pixels.

   .. attribute:: x_root
                  y_root

      The pointer position relative to the top-left corner of the screen, in
      pixels.

   .. attribute:: char

      The character typed, as a string (for key events).

   .. attribute:: send_event

      ``True`` if the event was sent by another application.

   .. attribute:: keysym

      The symbolic name of the key that was pressed or released.

   .. attribute:: keysym_num

      The numeric value of :attr:`keysym`.

   .. attribute:: type

      The :class:`EventType` of the event.

   .. attribute:: widget

      The widget on which the event occurred.

   .. attribute:: delta

      The amount the mouse wheel was rotated (for ``MouseWheel`` events).

   .. attribute:: user_data

      The data string of a virtual event, as passed to the *data* option of
      :meth:`Misc.event_generate`.
      It is ``'??'`` for non-virtual events.

      .. versionadded:: 3.15

   .. attribute:: detail

      A fixed detail string for ``Enter``, ``Leave``, ``FocusIn``, ``FocusOut``
      and ``ConfigureRequest`` events (see the Tcl/Tk documentation).
      It is ``'??'`` for other events.

      .. versionadded:: 3.15


.. class:: EventType(*values)

   An :class:`enum.StrEnum` enumerating the Tk event types, used as the value
   of :attr:`Event.type`.
   Its members include, among others, ``KeyPress``, ``KeyRelease``,
   ``ButtonPress``, ``ButtonRelease``, ``Motion``, ``Enter``, ``Leave``,
   ``FocusIn``, ``FocusOut``, ``Configure``, ``Map``, ``Unmap``, ``Expose``,
   ``Destroy`` and ``MouseWheel``.

   .. versionadded:: 3.6



.. class:: CallWrapper(func, subst, widget)

   Internal helper that wraps a Python callback so that it can be invoked from
   Tcl.
   *func* is the Python function, *subst* is an optional function that
   pre-processes the Tcl arguments, and *widget* is the widget used for error
   reporting.
   Instances are created automatically by :meth:`Misc.register`; this class is
   not normally used directly.


Module-level functions
^^^^^^^^^^^^^^^^^^^^^^

.. function:: Tcl(screenName=None, baseName=None, className='Tk', useTk=False)

   The :func:`Tcl` function is a factory function which creates an object much
   like that created by the :class:`Tk` class, except that it does not
   initialize the Tk subsystem.
   This is most often useful when driving the Tcl interpreter in an environment
   where one doesn't want to create extraneous toplevel windows, or where one
   cannot (such as Unix/Linux systems without an X server).
   An object created by the :func:`Tcl` object can have a Toplevel window
   created (and the Tk subsystem initialized) by calling its :meth:`~Tk.loadtk`
   method.

.. function:: NoDefaultRoot()

   Inhibit the creation of an implicit default root window.
   Afterwards :mod:`!tkinter` no longer creates a shared default root
   automatically, and operations that rely on one --- such as constructing a
   widget without an explicit *master* --- raise a :exc:`RuntimeError`.
   Call this early in larger applications to make the root window explicit.

.. function:: mainloop(n=0)

   Run the Tk main event loop on the default root window until all windows are
   destroyed.
   Equivalent to calling :meth:`Misc.mainloop` on the default root.

.. function:: getboolean(s)

   Convert the Tcl boolean string *s* (one of ``'1'``, ``'true'``, ``'yes'``,
   ``'on'`` and similar, or their false counterparts) to a Python
   :class:`bool`.
   Raise :exc:`ValueError` for an invalid value.

.. function:: getdouble(s)

   Convert *s* to a floating-point number.
   This is the built-in :class:`float`.

.. function:: getint(s)

   Convert *s* to an integer.
   This is the built-in :class:`int`.

.. function:: image_names()

   Return the names of all existing images in the default root's interpreter.

.. function:: image_types()

   Return the available image types (such as ``'photo'`` and ``'bitmap'``) in
   the default root's interpreter.


.. _tkinter-file-handlers:

File handlers
^^^^^^^^^^^^^

Tk allows you to register and unregister a callback function which will be
called from the Tk mainloop when I/O is possible on a file descriptor.
Only one handler may be registered per file descriptor. Example code::

   import tkinter
   widget = tkinter.Tk()
   mask = tkinter.READABLE | tkinter.WRITABLE
   widget.tk.createfilehandler(file, mask, callback)
   ...
   widget.tk.deletefilehandler(file)

This feature is not available on Windows.

Since you don't know how many bytes are available for reading, you may not
want to use the :class:`~io.BufferedIOBase` or :class:`~io.TextIOBase`
:meth:`~io.BufferedIOBase.read` or :meth:`~io.IOBase.readline` methods,
since these will insist on reading a predefined number of bytes.
For sockets, the :meth:`~socket.socket.recv` or
:meth:`~socket.socket.recvfrom` methods will work fine; for other files,
use raw reads or ``os.read(file.fileno(), maxbytecount)``.


.. method:: Widget.tk.createfilehandler(file, mask, func)

   Registers the file handler callback function *func*. The *file* argument
   may either be an object with a :meth:`~io.IOBase.fileno` method (such as
   a file or socket object), or an integer file descriptor. The *mask*
   argument is an ORed combination of any of the three constants below.
   The callback is called as follows::

      callback(file, mask)


.. method:: Widget.tk.deletefilehandler(file)

   Unregisters a file handler.


.. data:: READABLE
          WRITABLE
          EXCEPTION

   Constants used in the *mask* arguments.


Constants
^^^^^^^^^

The following symbolic constants are available in both the :mod:`!tkinter`
and :mod:`!tkinter.constants` namespaces.

.. data:: TRUE
          YES
          ON

   Truthy values, all equal to the integer ``1``.

.. data:: FALSE
          NO
          OFF

   Falsy values, all equal to the integer ``0``.

.. data:: N
          S
          E
          W
          NE
          NW
          SE
          SW
          NS
          EW
          NSEW
          CENTER

   Compass directions (``'n'``, ``'s'``, ``'e'``, ``'w'`` and the diagonals and
   edges) plus ``CENTER`` (``'center'``), used as values for the *anchor* and
   *sticky* options and by methods such as :meth:`Misc.grid_anchor`.

.. data:: LEFT
          RIGHT
          TOP
          BOTTOM

   Sides for the *side* option of the packer (see :meth:`Pack.pack_configure`).

.. data:: X
          Y
          BOTH
          NONE

   Values for the *fill* option of the packer: ``'x'``, ``'y'``, ``'both'`` or
   ``'none'``.

.. data:: RAISED
          SUNKEN
          FLAT
          RIDGE
          GROOVE
          SOLID

   Values for the *relief* option, which controls a widget's 3-D border.

.. data:: HORIZONTAL
          VERTICAL

   Values for the *orient* option of widgets such as :class:`Scale`,
   :class:`Scrollbar` and :class:`PanedWindow`.

.. data:: CHAR
          WORD

   Values for the *wrap* option of the :class:`Text` widget, selecting line
   wrapping on character or word boundaries.

.. data:: BASELINE

   The text-alignment value ``'baseline'``.

.. data:: INSIDE
          OUTSIDE

   Values for the *bordermode* option of the placer (see
   :meth:`Place.place_configure`).

.. data:: INSERT
          CURRENT
          END
          ANCHOR
          SEL
          SEL_FIRST
          SEL_LAST

   Symbolic indices used by the :class:`Text`, :class:`Entry`, :class:`Listbox`
   and :class:`Canvas` widgets, such as ``'insert'`` (the insertion cursor),
   ``'current'``, ``'end'``, ``'anchor'`` and the bounds of the selection
   (``'sel.first'`` and ``'sel.last'``).

.. data:: ALL

   The special tag ``'all'``, which matches every item of a :class:`Canvas` or
   every character of a :class:`Text` (for example ``canvas.delete(ALL)``).

.. data:: NORMAL
          DISABLED
          ACTIVE
          HIDDEN

   Values for the *state* option of various widgets and items.

.. data:: CASCADE
          CHECKBUTTON
          COMMAND
          RADIOBUTTON
          SEPARATOR

   Menu entry types, used as the *itemType* argument of :meth:`Menu.add` and
   :meth:`Menu.insert`.

.. data:: SINGLE
          BROWSE
          MULTIPLE
          EXTENDED

   Values for the *selectmode* option of the :class:`Listbox` widget.

.. data:: PIESLICE
          CHORD
          ARC

   Values for the *style* option of :class:`Canvas` arc items.

.. data:: BUTT
          PROJECTING
          ROUND
          BEVEL
          MITER

   Values for the *capstyle* (``'butt'``, ``'projecting'``, ``'round'``) and
   *joinstyle* (``'round'``, ``'bevel'``, ``'miter'``) options of
   :class:`Canvas` line items.

.. data:: FIRST
          LAST

   Values for the *arrow* option of :class:`Canvas` line items, indicating
   which ends have arrowheads.

.. data:: MOVETO
          SCROLL

   The first argument passed by a :class:`Scrollbar` to the :meth:`XView.xview`
   or :meth:`YView.yview` method of the scrolled widget.

.. data:: UNITS
          PAGES

   Values for the *what* argument of :meth:`XView.xview_scroll` and
   :meth:`YView.yview_scroll`.

.. data:: UNDERLINE
          NUMERIC
          DOTBOX

   Other option values: ``'underline'``, ``'numeric'`` and ``'dotbox'``.

----

   .. method:: place_content()

      Same as :meth:`Misc.place_content`.

      .. versionadded:: 3.15


.. class:: Grid()

   Geometry manager that arranges widgets in a two-dimensional grid of rows and
   columns within their container.
   The :class:`!Grid` mix-in is inherited by all widgets (through
   :class:`Widget`).
   See also :ref:`tkinter-geometry-management`.

   .. method:: configure(cnf={}, **kw)
      :no-typesetting:

   .. method:: config(cnf={}, **kw)
      :no-typesetting:

   .. method:: grid_configure(cnf={}, **kw)
               grid(cnf={}, **kw)

      Position the widget in a cell of its container's grid.

      Not to be confused with :meth:`Wm.grid`.

      The supported options are:

      *row*, *column*
         The row and column of the cell to place the widget in, counting from
         ``0``.
         *column* defaults to the column after the previous widget placed in
         the same :meth:`!grid_configure` call (or ``0``), and *row* defaults
         to the next empty row.

      *rowspan*, *columnspan*
         The number of rows and columns the widget should span (default ``1``).

      *sticky*
         How to position or stretch the widget when its cell is larger than the
         widget: a string containing zero or more of the characters ``'n'``,
         ``'s'``, ``'e'`` and ``'w'``, naming the cell sides the widget sticks
         to.
         Specifying both ``'n'`` and ``'s'`` (or ``'e'`` and ``'w'``) stretches
         the widget to fill the height (or width) of the cell.
         The default is ``''``, which centers the widget at its requested size.

      *ipadx*, *ipady*
         Internal padding added on the left and right (*ipadx*) or top and
         bottom (*ipady*) of the widget, as a screen distance (default ``0``).

      *padx*, *pady*
         External padding left on the left and right (*padx*) or top and bottom
         (*pady*) of the widget, as a screen distance or a pair of two
         distances for the two sides (default ``0``).

      *in_*
         The container in whose grid to place the widget; it defaults to the
         parent widget.

      :meth:`grid`, :meth:`configure` and :meth:`config` are aliases of
      :meth:`!grid_configure`.

   .. method:: forget()
      :no-typesetting:

   .. method:: grid_forget()

      Unmap the widget and remove it from the grid, forgetting its grid
      options.

   .. method:: grid_remove()

      Unmap the widget and remove it from the grid, but remember its grid
      options so that it is restored to the same cell if it is gridded again.

   .. method:: info()
      :no-typesetting:

   .. method:: grid_info()

      Return a dictionary of the widget's current grid options.

   .. method:: bbox(column=None, row=None, col2=None, row2=None)
      :no-typesetting:

   .. method:: grid_bbox(column=None, row=None, col2=None, row2=None)

      Same as :meth:`Misc.grid_bbox`.
      :meth:`bbox` is an alias of :meth:`!grid_bbox`,
      except on :class:`Canvas`, :class:`Listbox`, :class:`Spinbox`,
      :class:`Text`, :class:`ttk.Entry <tkinter.ttk.Entry>` and
      :class:`ttk.Treeview <tkinter.ttk.Treeview>`,
      which provide their own :meth:`!bbox` method.

   .. method:: columnconfigure(index, cnf={}, **kw)
      :no-typesetting:

   .. method:: grid_columnconfigure(index, cnf={}, **kw)

      Same as :meth:`Misc.grid_columnconfigure`: query or set the options (such
      as *weight*, *minsize*, *pad* and *uniform*) of a grid column.
      :meth:`columnconfigure` is an alias of :meth:`!grid_columnconfigure`.

   .. method:: rowconfigure(index, cnf={}, **kw)
      :no-typesetting:

   .. method:: grid_rowconfigure(index, cnf={}, **kw)

      Same as :meth:`Misc.grid_rowconfigure`: query or set the options of a
      grid row.
      :meth:`rowconfigure` is an alias of :meth:`!grid_rowconfigure`.

   .. method:: location(x, y)
      :no-typesetting:

   .. method:: grid_location(x, y)

      Same as :meth:`Misc.grid_location`: return the ``(column, row)`` of the
      cell that covers the pixel at *x*, *y*.
      :meth:`location` is an alias of :meth:`!grid_location`.

   .. method:: size()
      :no-typesetting:

   .. method:: grid_size()

      Same as :meth:`Misc.grid_size`: return a ``(columns, rows)`` tuple giving
      the size of the grid.
      :meth:`size` is an alias of :meth:`!grid_size`,
      except on the :class:`Listbox` widget,
      which provides its own :meth:`!size` method.

   .. method:: propagate()
               propagate(flag)
      :no-typesetting:

   .. method:: grid_propagate()
               grid_propagate(flag)

      Same as :meth:`Misc.grid_propagate`.

   .. method:: slaves(row=None, column=None)
      :no-typesetting:

   .. method:: grid_slaves(row=None, column=None)

      Same as :meth:`Misc.grid_slaves`: return the widgets managed in the grid,
      optionally restricted to a *row* and/or *column*.

   .. method:: content(row=None, column=None)
      :no-typesetting:

   .. method:: grid_content(row=None, column=None)

      Same as :meth:`Misc.grid_content`.

      .. versionadded:: 3.15


.. class:: XView()

   Mix-in providing the horizontal-scrolling interface shared by widgets such
   as :class:`Entry`, :class:`Canvas`, :class:`Listbox`, :class:`Text` and
   :class:`Spinbox`.
   A widget's :meth:`xview` method is registered as the *command* of a
   horizontal :class:`Scrollbar`.

   .. method:: xview(*args)

      Query or change the horizontal position of the view.
      With no arguments, return a tuple ``(first, last)`` of two fractions
      between 0 and 1 giving the portion of the document that is currently
      visible.
      Otherwise the arguments are passed to the Tk ``xview`` widget command and
      are usually generated by a scrollbar; :meth:`xview_moveto` and
      :meth:`xview_scroll` provide a more convenient interface.

   .. method:: xview_moveto(fraction)

      Adjust the view so that *fraction* of the total width of the document is
      off-screen to the left.
      *fraction* is a number between 0 and 1.

   .. method:: xview_scroll(number, what)

      Shift the view left or right by *number* units.
      *what* is either ``'units'`` or ``'pages'``; a negative *number* scrolls
      left and a positive one scrolls right.
      The :class:`Text` widget accepts also ``'pixels'``,
      and then *number* can be a screen distance, such as ``'1i'``.


.. class:: YView()

   Mix-in providing the vertical-scrolling interface shared by widgets such as
   :class:`Canvas`, :class:`Listbox` and :class:`Text`.
   A widget's :meth:`yview` method is registered as the *command* of a vertical
   :class:`Scrollbar`.

   .. method:: yview(*args)

      Query or change the vertical position of the view.
      With no arguments, return a tuple ``(first, last)`` of two fractions
      between 0 and 1 giving the portion of the document that is currently
      visible.
      Otherwise the arguments are passed to the Tk ``yview`` widget command,
      usually generated by a scrollbar; :meth:`yview_moveto` and
      :meth:`yview_scroll` provide a more convenient interface.

   .. method:: yview_moveto(fraction)

      Adjust the view so that *fraction* of the total height of the document is
      off-screen above the top.
      *fraction* is a number between 0 and 1.

   .. method:: yview_scroll(number, what)

      Shift the view up or down by *number* units.
      *what* is either ``'units'`` or ``'pages'``; a negative *number* scrolls
      up and a positive one scrolls down.
      The :class:`Text` widget accepts also ``'pixels'``,
      and then *number* can be a screen distance, such as ``'1i'``.


.. class:: BaseWidget(master, widgetName, cnf={}, kw={}, extra=())

   Internal base class for all widgets.
   It inherits from :class:`Misc` and adds the machinery that creates the
   underlying Tk widget; application code normally uses :class:`Widget` or a
   concrete widget class rather than instantiating :class:`!BaseWidget`
   directly.

   .. method:: destroy()

      Destroy this widget and all of its children, removing the corresponding
      Tk widgets and deleting the associated Tcl commands.


.. class:: Widget(master, widgetName, cnf={}, kw={}, extra=())

   Internal base class for the standard widgets.
   It combines :class:`BaseWidget` with the geometry-manager mix-ins
   :class:`Pack`, :class:`Place` and :class:`Grid`, so that every widget can be
   managed by any of the three geometry managers.
   The concrete widget classes (:class:`Button`, :class:`Label`, and so on)
   derive from :class:`!Widget`.


Toplevel widgets
^^^^^^^^^^^^^^^^

.. class:: Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)

   Construct a toplevel Tk widget, which is usually the main window of an
   application, and initialize a Tcl interpreter for this widget.  Each
   instance has its own associated Tcl interpreter.
   Inherits from :class:`Misc` and :class:`Wm`.

   To create a Tcl interpreter without initializing the Tk subsystem, use the
   :func:`Tcl` factory function instead.

   The :class:`Tk` class is typically instantiated using all default values.
   However, the following keyword arguments are currently recognized:

   *screenName*
      When given (as a string), sets the :envvar:`DISPLAY` environment
      variable. (X11 only)
   *baseName*
      Name of the profile file.  By default, *baseName* is derived from the
      program name (``sys.argv[0]``).
   *className*
      Name of the widget class.  Used as a profile file and also as the name
      with which Tcl is invoked (*argv0* in *interp*).
   *useTk*
      If ``True``, initialize the Tk subsystem.  The :func:`tkinter.Tcl() <Tcl>`
      function sets this to ``False``.
   *sync*
      If ``True``, execute all X server commands synchronously, so that errors
      are reported immediately.  Can be used for debugging. (X11 only)
   *use*
      Specifies the *id* of the window in which to embed the application,
      instead of it being created as an independent toplevel window. *id* must
      be specified in the same way as the value for the -use option for
      toplevel widgets (that is, it has a form like that returned by
      :meth:`~Misc.winfo_id`).

      Note that on some platforms this will only work correctly if *id* refers
      to a Tk frame or toplevel that has its -container option enabled.

   :class:`Tk` reads and interprets profile files, named
   :file:`.{className}.tcl` and :file:`.{baseName}.tcl`, into the Tcl
   interpreter and calls :func:`exec` on the contents of
   :file:`.{className}.py` and :file:`.{baseName}.py`.  The path for the
   profile files is the :envvar:`HOME` environment variable or, if that
   isn't defined, then :data:`os.curdir`.

   .. note::

      On Windows, creating a Tcl interpreter (by instantiating :class:`Tk` or
      calling :func:`Tcl`) sets the :envvar:`HOME` environment variable for
      the process, if it is not already set, to ``%HOMEDRIVE%%HOMEPATH%`` (or
      :envvar:`USERPROFILE`, or ``c:\``).  This is done by Tcl and can affect
      other code that reads :envvar:`HOME`.

   .. attribute:: tk

      The Tk application object created by instantiating :class:`Tk`.  This
      provides access to the Tcl interpreter.  Each widget that is attached
      the same instance of :class:`Tk` has the same value for its :attr:`tk`
      attribute.

   .. attribute:: master

      The widget object that contains this widget.
      For :class:`Tk`, the :attr:`!master` is :const:`None` because it is the
      main window.
      The terms *master* and *parent* are similar and sometimes used
      interchangeably as argument names; however, calling
      :meth:`~Misc.winfo_parent` returns a string of the widget name whereas
      :attr:`!master` returns the object.
      *parent*/*child* reflects the tree-like relationship while *master* (or
      *container*)/*content* reflects the container structure.

   .. attribute:: children

      The immediate descendants of this widget as a :class:`dict` with the
      child widget names as the keys and the child instance objects as the
      values.

   .. method:: destroy()

      Destroy this and all descendant widgets and, for the main window, end the
      connection to the underlying Tcl interpreter.

   .. method:: loadtk()

      Finish loading and initializing the Tk subsystem.
      This is needed only when the interpreter was created without Tk (for
      example through :func:`Tcl`); it is called automatically when *useTk* is
      true.

   .. method:: readprofile(baseName, className)

      Read and source the user's profile files :file:`.{className}.tcl` and
      :file:`.{baseName}.tcl` into the Tcl interpreter, and execute the
      corresponding :file:`.{className}.py` and :file:`.{baseName}.py` files.
      This is called during initialization; see the description of the
      constructor above.

   .. method:: report_callback_exception(exc, val, tb)

      Report a callback exception.
      This is called when an exception propagates out of a Tkinter callback;
      *exc*, *val* and *tb* are the exception type, value and traceback as
      returned by :func:`sys.exc_info`.
      The default implementation prints a traceback to :data:`sys.stderr`.
      It can be overridden to customize error handling, for example to display
      the traceback in a dialog.


.. class:: Toplevel(master=None, cnf={}, **kw)

   A :class:`!Toplevel` widget is a top-level window, similar to a
   :class:`Frame` except that its X parent is the root window of a screen
   rather than its logical parent.
   Its primary purpose is to serve as a container for dialog boxes and other
   collections of widgets; its only visible features are its background and an
   optional 3-D border.
   Notable options include *menu*, which installs a :class:`Menu` as the
   window's menubar.
   Inherits from :class:`BaseWidget` and :class:`Wm`, so a toplevel is managed
   by the window manager.
   Refer to the Tk ``toplevel`` manual page for the full list of options.


Widget classes
^^^^^^^^^^^^^^

.. class:: Button(master=None, cnf={}, **kw)

   A :class:`!Button` widget displays a textual string, bitmap or image and
   invokes a command when the user presses it (by clicking mouse button 1 over
   the button or, when the button has focus, by pressing the space key).
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a button accepts the options
   documented in the Tk ``button`` manual page, such as *command* (the callback
   invoked when the button is pressed), *textvariable*, *state* and *default*.

   .. method:: invoke()

      Invoke the command associated with the button, if there is one, and
      return its result, or an empty string if no command is associated with
      the button.
      This is ignored if the button's state is ``disabled``.

   .. method:: flash()

      Flash the button by redisplaying it several times, alternating between
      the active and normal colors.
      At the end of the flash the button is left in the same normal or active
      state as when the method was called.
      This is ignored if the button's state is ``disabled``.


.. class:: Canvas(master=None, cnf={}, **kw)

   A :class:`!Canvas` widget implements structured graphics.
   It displays any number of *items*, such as arcs, lines, ovals, polygons,
   rectangles, text, bitmaps, images and embedded windows, which may be drawn,
   moved, re-colored and bound to events.
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``canvas`` manual page for the full list of widget and item
   options.

   Each item has a unique integer *id*, assigned when it is created, and zero
   or more string *tags*.
   A tag is an arbitrary string that does not have the form of an integer; the
   same tag may be shared by many items, which makes tags convenient for
   grouping items.
   The special tag ``'all'`` matches every item in the canvas, and
   ``'current'`` matches the topmost item under the mouse pointer.
   Most methods take a *tagOrId* argument that may be an integer id naming a
   single item, or a tag naming zero or more items; as described in the Tk
   ``canvas`` manual page, a tag may also be a logical expression of tags
   combined with the operators ``&&``, ``||``, ``^``, ``!`` and parentheses.
   When a method that operates on a single item is given a *tagOrId* matching
   several items, it normally uses the lowest matching item in the display
   list.

   The items are kept in a *display list* that determines drawing order: items
   later in the list are drawn on top of earlier ones.
   A newly created item is placed at the top of the list; the order can be
   changed with :meth:`tag_raise` and :meth:`tag_lower`.

   .. method:: create_arc(*args, **kw)
               create_bitmap(*args, **kw)
               create_image(*args, **kw)
               create_line(*args, **kw)
               create_oval(*args, **kw)
               create_polygon(*args, **kw)
               create_rectangle(*args, **kw)
               create_text(*args, **kw)
               create_window(*args, **kw)

      Create a new item of the corresponding type and return its integer id.
      Each method is called as ``create_TYPE(coord..., **options)``: the
      leading positional arguments give the coordinates that define the item
      (as separate numbers, as a single sequence of numbers, or as coordinate
      pairs), and the keyword arguments set item-specific options.
      Coordinates and screen distances may be given as numbers (interpreted as
      pixels) or as strings with a unit suffix (``'m'``, ``'c'``, ``'i'`` or
      ``'p'`` for millimetres, centimetres, inches or printer's points), but
      are always stored and returned in pixels.

      The item types are: ``arc`` (an arc-shaped region that is a section of an
      oval, defined by two diagonally opposite corners ``x1, y1, x2, y2`` of
      the enclosing rectangle); ``bitmap`` (a two-color bitmap positioned at a
      point ``x, y``); ``image`` (a Tk image positioned at a point ``x, y``);
      ``line`` (a line or curve through the points ``x1, y1, ..., xn, yn``);
      ``oval`` (a circle or ellipse inscribed in the rectangle
      ``x1, y1, x2, y2``); ``polygon`` (a closed polygon through the points
      ``x1, y1, ..., xn, yn``); ``rectangle`` (a rectangle with corners
      ``x1, y1, x2, y2``); ``text`` (a string of text positioned at a point
      ``x, y``); and ``window`` (a child widget embedded in the canvas at a
      point ``x, y``, specified with the *window* option).

      Most item types accept a common set of *standard item options*, plus a
      few options specific to each type.
      Option names are passed as keyword arguments, without the leading
      hyphen.

      The standard item options are:

      *fill*
         The color used to fill the item's interior, or to draw a *line*
         item or the characters of a *text* item.
         An empty string (the default for all types except *line* and *text*)
         leaves the item unfilled.

      *outline*
         The color used to draw the item's outline.
         An empty string draws no outline.

      *width*
         The width of the outline, defaulting to ``1.0``.
         Has no effect if *outline* is empty.

      *dash*
         A dash pattern for the outline, given either as a sequence of
         segment lengths in pixels or as a string of the characters
         ``'.'``, ``','``, ``'-'``, ``'_'`` and space.
         An empty pattern (the default) draws a solid outline.

      *dashoffset*
         The starting offset in pixels into the *dash* pattern.
         Ignored if there is no *dash* pattern.

      *stipple*
         A bitmap used as a stipple pattern when filling the item.
         Only well supported on X11.

      *outlinestipple*
         A bitmap used as a stipple pattern when drawing the outline.
         Has no effect if *outline* is empty.

      *offset*, *outlineoffset*
         The offset of the fill and outline stipple patterns, given as
         ``'x,y'`` or as a side such as ``'n'``, ``'se'`` or ``'center'``.
         Stipple offsets are only supported on X11.

      *state*
         Overrides the canvas state for this item; one of ``'normal'``,
         ``'disabled'`` or ``'hidden'``.

      *tags*
         A single tag or a sequence of tags to associate with the item,
         replacing any existing tags.

      Many of these options have *active...* and *disabled...* variants
      (such as *activefill*, *disabledfill*, *activewidth*, *disableddash*,
      *activeoutline*, *disabledstipple*) that override the base option when
      the item is the active item (under the mouse pointer) or is in the
      disabled state.

      The following item types support additional options.

      For ``arc`` items:

      *start*
         The start of the arc's angular range, in degrees measured
         counter-clockwise from the 3-o'clock position.

      *extent*
         The size of the angular range, in degrees counter-clockwise from
         *start*.

      *style*
         How the arc is drawn: ``'pieslice'`` (the default), ``'chord'`` or
         ``'arc'``.

      For ``line`` items:

      *arrow*
         Where to draw arrowheads: ``'none'`` (the default), ``'first'``,
         ``'last'`` or ``'both'``.

      *arrowshape*
         A sequence of three distances describing the shape of the
         arrowheads.

      *capstyle*
         How line ends are drawn: ``'butt'`` (the default), ``'projecting'``
         or ``'round'``.

      *joinstyle*
         How line vertices are drawn: ``'round'`` (the default), ``'bevel'``
         or ``'miter'``.

      *smooth*
         The smoothing method: a false value (the default) for no smoothing,
         or ``'true'``/``'bezier'`` or ``'raw'`` to draw the line as a curve.

      *splinesteps*
         The number of line segments approximating each spline when
         *smooth* is enabled.

      For ``polygon`` items:

      *joinstyle*, *smooth*, *splinesteps*
         As for ``line`` items, applied to the polygon's outline.

      For ``text`` items:

      *text*
         The string to display; newline characters start new lines.

      *font*
         The font used for the text.

      *justify*
         How lines are justified: ``'left'`` (the default), ``'right'`` or
         ``'center'``.

      *anchor*
         How the text is positioned relative to its point, defaulting to
         ``'center'``.

      *width*
         The maximum line length; if non-zero, lines are wrapped at spaces.

      *angle*
         How many degrees to rotate the text counter-clockwise about its
         positioning point, from ``0.0`` to ``360.0`` (default ``0.0``).

      *underline*
         The index of a character to underline, or ``-1`` for none.

      For ``bitmap`` items:

      *bitmap*
         The bitmap to display.

      *anchor*
         How the bitmap is positioned relative to its point.

      *background*, *foreground*
         The colors used for the bitmap's ``0`` and ``1`` pixels; an empty
         *background* makes the ``0`` pixels transparent.
         Both have *active...* and *disabled...* variants, and *bitmap* has
         *activebitmap* and *disabledbitmap* variants.

      For ``image`` items:

      *image*
         The Tk image to display, previously created with the image
         protocols.

      *anchor*
         How the image is positioned relative to its point.

      Both options have *active...* and *disabled...* variants
      (*activeimage*, *disabledimage*) used in the active and disabled
      states.

      For ``window`` items:

      *window*
         The widget to embed; it must be a child of the canvas or of one of
         its ancestors, and may not be a top-level window.

      *anchor*
         How the window is positioned relative to its point.

      *width*, *height*
         The size to assign to the window; if zero (the default), the window
         is given its requested size.

      ``oval`` and ``rectangle`` items have no type-specific options; they
      use only the standard item options.

      .. note::

         Tk 8.6 added the *angle* option for ``text`` items.

   .. method:: coords(tagOrId)
               coords(tagOrId, coordList, /)
               coords(tagOrId, /, *coordList)

      Query or modify the coordinates of an item.
      With only *tagOrId*, return a list of the floating-point coordinates of
      the item given by *tagOrId* (the first matching item if it matches
      several).
      Given new coordinates, replace the coordinates of that item with them;
      like the ``create_*`` methods, the coordinates may be given as separate
      numbers, as a single sequence, or as coordinate pairs.
      The returned coordinates are always in pixels, regardless of the units
      used to specify them; for rectangles, ovals and arcs they are ordered
      left, top, right, bottom.

      .. versionchanged:: 3.12
         The arguments are now flattened: the coordinates may be given as
         separate arguments, as a single sequence, or grouped in pairs, like
         the ``create_*`` methods.


   .. method:: move(tagOrId, xAmount, yAmount, /)

      Move each of the items given by *tagOrId* in the canvas coordinate space
      by adding *xAmount* to every x-coordinate and *yAmount* to every
      y-coordinate of the item.

   .. method:: moveto(tagOrId, x='', y='')

      Move the items given by *tagOrId* so that the first coordinate pair (the
      upper-left corner of the bounding box) of the lowest matching item is at
      position (*x*, *y*).
      *x* or *y* may be an empty string, in which case the corresponding
      coordinate is unchanged.
      All matching items keep their positions relative to each other.

      .. versionadded:: 3.8


   .. method:: scale(tagOrId, xOrigin, yOrigin, xScale, yScale, /)

      Rescale the coordinates of all items given by *tagOrId* in canvas
      coordinate space.
      Each x-coordinate is adjusted so that its distance from *xOrigin* changes
      by a factor of *xScale*, and each y-coordinate so that its distance from
      *yOrigin* changes by a factor of *yScale* (a factor of ``1.0`` leaves the
      coordinate unchanged).

   .. method:: delete(*tagOrIds)

      Delete each of the items given by the *tagOrIds* arguments.

   .. method:: dchars(tagOrId, first, /)
               dchars(tagOrId, first, last, /)

      Delete from each of the items given by *tagOrId* the characters (for text
      items) or coordinates (for line and polygon items) in the range from
      *first* to *last* inclusive; *last* defaults to *first*.
      Items that do not support indexing ignore this operation.

   .. method:: insert(tagOrId, beforeThis, string, /)

      Insert *string* into each of the items given by *tagOrId* just before the
      character or coordinate whose index is *beforeThis*.
      For line and polygon items *string* must be a valid sequence of
      coordinates.

   .. method:: itemcget(tagOrId, option)

      Return the current value of the configuration option *option* for the
      item given by *tagOrId* (the lowest matching item if it matches several).
      This is like :meth:`~Misc.cget` but applies to an individual item.

   .. method:: itemconfig(tagOrId, cnf=None, **kw)
      :no-typesetting:

   .. method:: itemconfigure(tagOrId, cnf=None, **kw)

      Query or modify the configuration options of the items given by
      *tagOrId*.
      This mirrors :meth:`~Misc.configure`, except that it applies to
      individual items rather than to the canvas as a whole.
      With no options, it returns a dictionary describing the current options
      of the first matching item; otherwise it sets the given options on every
      matching item.
      The legal options are those accepted by the corresponding ``create_*``
      method.
      :meth:`itemconfig` is an alias of :meth:`!itemconfigure`.

   .. method:: type(tagOrId)

      Return the type of the item given by *tagOrId* (the first matching item
      if it matches several), such as ``'rectangle'`` or ``'text'``, or
      ``None`` if *tagOrId* does not match any item.

   .. method:: gettags(tagOrId, /)

      Return a tuple of the tags associated with the item given by *tagOrId*
      (the first matching item in display-list order if it matches several).
      Return an empty tuple if no item matches or the item has no tags.

   .. method:: dtag(tagOrId, /)
               dtag(tagOrId, tagToDelete, /)

      Remove the tag *tagToDelete* (which defaults to *tagOrId*) from each of
      the items given by *tagOrId*.
      Items that do not have that tag are unaffected.

   .. method:: addtag(newtag, searchSpec, /, *args)

      Add the tag *newtag* to each item selected by the search specification
      *searchSpec* (and any further *args*).
      *searchSpec* is one of ``'above'``, ``'all'``, ``'below'``,
      ``'closest'``, ``'enclosed'``, ``'overlapping'`` or ``'withtag'``; the
      ``addtag_*`` methods below are convenient wrappers that supply each of
      these forms.

   .. method:: addtag_above(newtag, tagOrId)

      Add the tag *newtag* to the item just above (after) *tagOrId* in the
      display list.

   .. method:: addtag_all(newtag)

      Add the tag *newtag* to all items in the canvas.

   .. method:: addtag_below(newtag, tagOrId)

      Add the tag *newtag* to the item just below (before) *tagOrId* in the
      display list.

   .. method:: addtag_closest(newtag, x, y, halo=None, start=None)

      Add the tag *newtag* to the item closest to the point (*x*, *y*).
      If *halo* is given, any item within that distance of the point is treated
      as overlapping it.
      If *start* is given (a tag or id), select the topmost closest item that
      lies below *start* in the display list, which can be used to step through
      all the closest items.

   .. method:: addtag_enclosed(newtag, x1, y1, x2, y2)

      Add the tag *newtag* to every item completely enclosed within the
      rectangle (*x1*, *y1*, *x2*, *y2*), where *x1* <= *x2* and *y1* <= *y2*.

   .. method:: addtag_overlapping(newtag, x1, y1, x2, y2)

      Add the tag *newtag* to every item that overlaps or is enclosed within
      the rectangle (*x1*, *y1*, *x2*, *y2*), where *x1* <= *x2* and *y1* <=
      *y2*.

   .. method:: addtag_withtag(newtag, tagOrId)

      Add the tag *newtag* to every item given by *tagOrId*.

   .. method:: find(searchSpec, /, *args)

      Return a tuple of the ids of all items selected by the search
      specification *searchSpec* (and any further *args*), in stacking order
      with the lowest item first.
      The search specification has any of the forms accepted by :meth:`addtag`.
      The ``find_*`` methods below are more convenient wrappers around it.

   .. method:: find_above(tagOrId)

      Return a tuple containing the id of the item just above *tagOrId* in the
      display list.

   .. method:: find_all()

      Return a tuple of the ids of all items in the canvas, in stacking order.

   .. method:: find_below(tagOrId)

      Return a tuple containing the id of the item just below *tagOrId* in the
      display list.

   .. method:: find_closest(x, y, halo=None, start=None)

      Return a tuple containing the id of the item closest to the point (*x*,
      *y*).
      *halo* and *start* are interpreted as for :meth:`addtag_closest`.

   .. method:: find_enclosed(x1, y1, x2, y2)

      Return a tuple of the ids of all items completely enclosed within the
      rectangle (*x1*, *y1*, *x2*, *y2*).

   .. method:: find_overlapping(x1, y1, x2, y2)

      Return a tuple of the ids of all items that overlap or are enclosed
      within the rectangle (*x1*, *y1*, *x2*, *y2*).

   .. method:: find_withtag(tagOrId)

      Return a tuple of the ids of all items given by *tagOrId*.

   .. method:: lift(tagOrId, aboveThis=None, /)
      :no-typesetting:

   .. method:: tkraise(tagOrId, aboveThis=None, /)
      :no-typesetting:

   .. method:: tag_raise(tagOrId, aboveThis=None, /)

      Move all items given by *tagOrId* to a new position in the display list
      just above the item given by *aboveThis*, or to the top of the display
      list if *aboveThis* is omitted.
      When several items are moved their relative order is preserved.
      This has no effect on embedded window items, whose stacking order is
      controlled by :meth:`Misc.tkraise` and :meth:`Misc.lower` instead.
      :meth:`lift` and :meth:`tkraise` are aliases of :meth:`!tag_raise`.

   .. method:: lower(tagOrId, belowThis=None, /)
      :no-typesetting:

   .. method:: tag_lower(tagOrId, belowThis=None, /)

      Move all items given by *tagOrId* to a new position in the display list
      just below the item given by *belowThis*, or to the bottom of the display
      list if *belowThis* is omitted.
      When several items are moved their relative order is preserved.
      This has no effect on embedded window items.
      :meth:`lower` is an alias of :meth:`!tag_lower`.

      .. note::

         On a :class:`Canvas`, :meth:`tkraise`/:meth:`lift` and :meth:`lower`
         restack canvas items,
         shadowing the inherited :meth:`Misc.tkraise`/:meth:`Misc.lift` and
         :meth:`Misc.lower` methods that restack the widget itself,
         which are therefore not available.

   .. method:: tag_bind(tagOrId, sequence=None, func=None, add=None)

      Bind the callback *func* to the event *sequence* for all items given by
      *tagOrId*, so that *func* is invoked whenever that event occurs for one
      of the items.
      This is like :meth:`Widget.bind <Misc.bind>` but operates on canvas items
      rather than on whole widgets; only mouse, keyboard and virtual events may
      be bound.
      Mouse events are directed to the current item and keyboard events to the
      focus item (see :meth:`focus`).
      If *add* is true the new binding is added to any existing bindings for
      the same sequence, rather than replacing them.
      Return the identifier of the bound function, which can be passed to
      :meth:`tag_unbind`.

   .. method:: tag_unbind(tagOrId, sequence, funcid=None)

      Remove for all items given by *tagOrId* the binding for the event
      *sequence*.
      If *funcid* is given, only that callback (as returned by
      :meth:`tag_bind`) is unbound and deregistered.

      .. versionchanged:: 3.13
         If *funcid* is given, only that callback is unbound.


   .. method:: bbox(tagOrId, /, *tagOrIds)

      Return a 4-tuple ``(x1, y1, x2, y2)`` giving an approximate bounding box,
      in pixels, that encloses all the items given by *tagOrId* and any further
      *tagOrIds*.
      The result may overestimate the true bounding box by a few pixels.
      Return ``None`` if no item matches or the matching items have nothing to
      display.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: canvasx(screenx, gridspacing=None)

      Given a window x-coordinate *screenx*, return the canvas x-coordinate
      displayed at that location.
      If *gridspacing* is given, the result is rounded to the nearest multiple
      of *gridspacing* units.

   .. method:: canvasy(screeny, gridspacing=None)

      Given a window y-coordinate *screeny*, return the canvas y-coordinate
      displayed at that location.
      If *gridspacing* is given, the result is rounded to the nearest multiple
      of *gridspacing* units.

   .. method:: focus()
               focus(tagOrId, /)

      With *tagOrId*, set the keyboard focus for the canvas to the first item
      given by *tagOrId* that supports the insertion cursor; the focus is left
      unchanged if no such item exists.
      If *tagOrId* is an empty string, reset the focus so that no item has it.
      With no argument, return the id of the item that currently has the focus,
      or an empty string if none does.
      An item only displays the insertion cursor when both it is the focus item
      and its canvas has the input focus.

      This shadows the inherited :meth:`!Misc.focus`;
      use :meth:`~Misc.focus_set` to focus the widget itself.

   .. method:: icursor(tagOrId, index, /)

      Set the insertion cursor of the items given by *tagOrId* to just before
      the character given by *index*.
      Items that do not support an insertion cursor are unaffected.
      The cursor is only displayed when the item has the focus, but its
      position may be set at any time.

   .. method:: index(tagOrId, index, /)

      Return as an integer the numerical index within *tagOrId* corresponding
      to *index*, which is a textual description of a position (for text items
      an index into the characters, for line and polygon items an index into
      the coordinates).
      If *tagOrId* matches several items, the first one that supports indexing
      is used.

   .. method:: select_adjust(tagOrId, index)

      Adjust the end of the selection in *tagOrId* nearest to *index* so that
      it is at *index*, and make the other end the anchor point for future
      :meth:`select_to` calls.
      If the selection is not currently in *tagOrId*, this behaves like
      :meth:`select_to`.

   .. method:: select_clear()

      Clear the selection if it is in this canvas; otherwise do nothing.

   .. method:: select_from(tagOrId, index)

      Set the selection anchor point to just before the character given by
      *index* in the item given by *tagOrId*.
      This does not change the selection itself; it sets the fixed end for
      future :meth:`select_to` calls.

   .. method:: select_item()

      Return the id of the item that holds the selection, or ``None`` if the
      selection is not in this canvas.
      Unlike :meth:`find` and the ``find_*`` methods, this returns the id as a
      string rather than an integer.

   .. method:: select_to(tagOrId, index)

      Set the selection to the characters of *tagOrId* between the selection
      anchor point and *index*, inclusive of *index*.
      The anchor point is the one set by the most recent :meth:`select_adjust`
      or :meth:`select_from` call.

   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y, gain=10)

      Scroll the canvas by *gain* times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events in the widget, producing
      the effect of dragging the canvas at high speed through its window.

   .. method:: postscript(cnf={}, **kw)

      Generate a PostScript (Encapsulated PostScript, version 3.0)
      representation of part or all of the canvas.
      If the *file* or *channel* option is given, the PostScript is written
      there and an empty string is returned; otherwise it is returned as a
      string.
      By default only the area currently visible in the window is generated, so
      it is usually necessary either to call :meth:`~Misc.update` first or to
      use the *width* and *height* options.
      Supported options include *colormap*, *colormode*, *file*, *fontmap*,
      *height*, *pageanchor*, *pageheight*, *pagewidth*, *pagex*, *pagey*,
      *rotate*, *width*, *x* and *y*.


.. class:: Checkbutton(master=None, cnf={}, **kw)

   A :class:`!Checkbutton` widget displays a textual string, bitmap or image
   together with a square indicator, and toggles a boolean selection when
   pressed.
   It has all the behavior of a simple button and, in addition, can be
   selected: when selected the indicator is drawn with a check mark and the
   associated variable is set to the ``onvalue``, and when deselected the
   indicator is drawn empty and the variable is set to the ``offvalue``.
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a checkbutton accepts the
   options documented in the Tk ``checkbutton`` manual page, such as
   *variable*, *onvalue*, *offvalue* and *command*.

   .. method:: invoke()

      Do just what would happen if the user pressed the checkbutton with the
      mouse: toggle the selection state of the button and invoke the associated
      command, if there is one.
      Return the result of the command, or an empty string if no command is
      associated with the checkbutton.
      This is ignored if the checkbutton's state is ``disabled``.

   .. method:: select()

      Select the checkbutton and set the associated variable to its
      ``onvalue``.

   .. method:: deselect()

      Deselect the checkbutton and set the associated variable to its
      ``offvalue``.

   .. method:: toggle()

      Toggle the selection state of the button, redisplaying it and modifying
      its associated variable to reflect the new state.

   .. method:: flash()

      Flash the checkbutton by redisplaying it several times, alternating
      between the active and normal colors.
      At the end of the flash the checkbutton is left in the same normal or
      active state as when the method was called.
      This is ignored if the checkbutton's state is ``disabled``.


.. class:: Entry(master=None, cnf={}, **kw)

   An :class:`!Entry` widget displays a single line of text and lets the user
   edit it.
   Inherits from :class:`Widget` and :class:`XView`; since entries can hold
   strings too long to fit in the window, they support horizontal scrolling
   through :meth:`~XView.xview`.

   In addition to the standard widget options, an entry accepts the options
   documented in the Tk ``entry`` manual page.
   Notable ones are *textvariable* (the name of a variable kept in sync with
   the entry's contents), *show* (if set, each character is displayed as the
   given character rather than its true value, useful for password entry),
   *validate* and *validatecommand* (which together let a callback accept or
   reject edits), and *state* (one of ``'normal'``, ``'disabled'`` or
   ``'readonly'``).

   Many of the methods below take an *index* argument that selects a character
   in the entry's string.
   As described in the Tk ``entry`` manual page, *index* may be a number
   (counting from 0), ``'insert'`` (the character just after the insertion
   cursor), ``'end'`` (just after the last character), ``'anchor'`` (the
   selection anchor point), ``'sel.first'`` and ``'sel.last'`` (the ends of the
   selection), or ``@x`` (the character covering pixel x-coordinate *x* in the
   window).
   Out-of-range indices are rounded to the nearest legal value.

   .. method:: delete(first, last=None)

      Delete the characters from index *first* up to but not including index
      *last*.
      If *last* is omitted, only the single character at *first* is deleted.

   .. method:: get()

      Return the entry's current string.

   .. method:: insert(index, string)

      Insert *string* just before the character given by *index*.

   .. method:: icursor(index)

      Arrange for the insertion cursor to be displayed just before the
      character given by *index*.

   .. method:: index(index)

      Return the numerical index corresponding to *index*.

   .. method:: select_adjust(index)
      :no-typesetting:

   .. method:: selection_adjust(index)

      Locate the end of the selection nearest to the character given by
      *index*, and adjust that end to be at *index* (including but not going
      beyond it); the other end becomes the anchor point for future
      :meth:`selection_to` calls.
      If there is no selection in the entry, a new one is created between
      *index* and the most recent anchor point, inclusive.
      :meth:`select_adjust` is an alias of :meth:`!selection_adjust`.

   .. method:: select_clear()
      :no-typesetting:

   .. method:: selection_clear()

      Clear the selection if it is currently in this widget.
      If the selection is not in this widget the method has no effect.
      :meth:`select_clear` is an alias of :meth:`!selection_clear`.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on an :class:`Entry`.

   .. method:: select_from(index)
      :no-typesetting:

   .. method:: selection_from(index)

      Set the selection anchor point to just before the character given by
      *index*, without changing the selection.
      :meth:`select_from` is an alias of :meth:`!selection_from`.

   .. method:: select_present()
      :no-typesetting:

   .. method:: selection_present()

      Return ``True`` if there are characters selected in the entry, ``False``
      otherwise.
      :meth:`select_present` is an alias of :meth:`!selection_present`.

   .. method:: select_range(start, end)
      :no-typesetting:

   .. method:: selection_range(start, end)

      Set the selection to include the characters starting with the one indexed
      by *start* and ending with the one just before *end*.
      If *end* refers to the same character as *start* or an earlier one, the
      selection is cleared.
      :meth:`select_range` is an alias of :meth:`!selection_range`.

   .. method:: select_to(index)
      :no-typesetting:

   .. method:: selection_to(index)

      Set the selection between the anchor point and *index*: if *index* is
      before the anchor point, the selection runs from *index* up to but not
      including the anchor; if *index* is after it, from the anchor up to but
      not including *index*; if they coincide, nothing happens.
      The anchor point is the one set by the most recent :meth:`selection_from`
      or :meth:`selection_adjust` call.
      If there is no selection in the entry, a new one is created using the
      most recent anchor point.
      :meth:`select_to` is an alias of :meth:`!selection_to`.

   .. method:: scan_mark(x)

      Record *x* and the current view in the entry window, for use with later
      :meth:`scan_dragto` calls.
      Typically associated with a mouse button press in the widget.

   .. method:: scan_dragto(x)

      Compute the difference between *x* and the *x* given to the last
      :meth:`scan_mark` call, and adjust the view left or right by 10 times
      that difference.
      Typically associated with mouse motion events, to produce the effect of
      dragging the entry at high speed through the window.


.. class:: Frame(master=None, cnf={}, **kw)

   A :class:`!Frame` widget is a simple container.
   Its primary purpose is to act as a spacer or container for complex window
   layouts; its only features are its background and an optional 3-D border to
   make the frame appear raised or sunken.
   Inherits from :class:`Widget`.
   Refer to the Tk ``frame`` manual page for the full list of options.


.. class:: Label(master=None, cnf={}, **kw)

   A :class:`!Label` widget displays a non-interactive textual string, bitmap
   or image.
   The displayed text is set with the *text* option or linked to a variable
   through *textvariable*, and an image can be shown using the *image* option.
   Text must all be in a single font but may occupy multiple lines, and one
   character may be underlined with the *underline* option.
   Inherits from :class:`Widget`.
   Refer to the Tk ``label`` manual page for the full list of options.


.. class:: LabelFrame(master=None, cnf={}, **kw)

   A :class:`!LabelFrame` widget is a container that has the features of a
   :class:`Frame` plus the ability to display a label.
   The label text is set with the *text* option and positioned with
   *labelanchor*, or an arbitrary widget may be used as the label by giving it
   as the *labelwidget* option.
   Inherits from :class:`Widget`.
   Refer to the Tk ``labelframe`` manual page for the full list of options.


.. class:: Listbox(master=None, cnf={}, **kw)

   A :class:`!Listbox` widget displays a list of single-line text items, one
   per line, of which the user can select one or more.
   The way the selection behaves is governed by the *selectmode* option, which
   is one of ``browse`` (the default; at most one item, which may be dragged
   with the mouse), ``single`` (at most one item), ``multiple`` (any number of
   items, toggled individually), or ``extended`` (any number of items,
   including discontiguous ranges, selected by clicking and dragging).
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``listbox`` manual page for the full list of options.

   Many of the methods take an *index* argument identifying a particular item.
   As described in the Tk ``listbox`` manual page, *index* may be a numeric
   index (counting from 0 at the top), ``'active'`` (the item with the location
   cursor, set with :meth:`activate`), ``'anchor'`` (the selection anchor, set
   with :meth:`selection_anchor`), ``'end'`` (the last item, or for
   :meth:`index` and :meth:`insert` the position just after it), or ``@x,y``
   (the item covering pixel coordinates *x*, *y* in the listbox window).
   Arguments named *first* and *last* are indices of the same forms.

   .. method:: insert(index, *elements)

      Insert the given *elements* as new items just before the item given by
      *index*.
      If *index* is ``'end'``, the new items are appended to the end of the
      list.

   .. method:: delete(first, last=None)

      Delete the items in the range from *first* to *last* inclusive.
      If *last* is omitted, it defaults to *first*, so that a single item is
      deleted.

   .. method:: get(first, last=None)

      If *last* is omitted, return the contents of the item given by *first*,
      or an empty string if *first* refers to a non-existent item.
      If *last* is given, return a tuple of all the items in the range from
      *first* to *last* inclusive.

   .. method:: size()

      Return the total number of items in the listbox.

      This shadows the inherited :meth:`!Misc.size`;
      use :meth:`~Misc.grid_size` for the grid size.

   .. method:: index(index)

      Return the integer index value corresponding to *index*, or ``None`` if
      *index* is out of range.
      If *index* is ``'end'``, the result is a count of the number of items in
      the listbox (not the index of the last item).

   .. method:: bbox(index)

      Return a tuple ``(x, y, width, height)`` describing the bounding box, in
      pixels relative to the widget, of the text of the item given by *index*.
      Return ``None`` if no part of that item is visible on the screen, or if
      *index* refers to a non-existent item; if the item is only partly
      visible, the result still gives the full area of the item, including the
      parts that are not visible.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: nearest(y)

      Given a y-coordinate within the listbox window, return the index of the
      visible item nearest to that y-coordinate.

   .. method:: see(index)

      Adjust the view so that the item given by *index* is visible.
      If the item is already visible the method has no effect; if it is near an
      edge of the window the listbox scrolls just enough to bring it into view
      at that edge, otherwise the listbox scrolls to center the item.

   .. method:: activate(index)

      Set the active item to the one given by *index*.
      If *index* is outside the range of items, the closest item is activated
      instead.
      The active item is drawn as specified by the *activestyle* option when
      the widget has the input focus, and its index may be retrieved with the
      ``'active'`` index.

   .. method:: curselection()

      Return a tuple containing the numerical indices of all of the items that
      are currently selected, or an empty tuple if no items are selected.

   .. method:: select_anchor(index)
      :no-typesetting:

   .. method:: selection_anchor(index)

      Set the selection anchor to the item given by *index*.
      If *index* refers to a non-existent item, the closest item is used.
      The selection anchor is the end of the selection that is fixed while
      dragging out a selection with the mouse, and may afterwards be referred
      to with the ``'anchor'`` index.
      :meth:`select_anchor` is an alias of :meth:`!selection_anchor`.

   .. method:: select_clear(first, last=None)
      :no-typesetting:

   .. method:: selection_clear(first, last=None)

      Deselect any of the items in the range from *first* to *last* inclusive
      that are selected.
      The selection state of items outside this range is not changed.
      :meth:`select_clear` is an alias of :meth:`!selection_clear`.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on a :class:`Listbox`.

   .. method:: select_includes(index)
      :no-typesetting:

   .. method:: selection_includes(index)

      Return ``True`` if the item given by *index* is currently selected,
      ``False`` otherwise.
      :meth:`select_includes` is an alias of :meth:`!selection_includes`.

   .. method:: select_set(first, last=None)
      :no-typesetting:

   .. method:: selection_set(first, last=None)

      Select all of the items in the range from *first* to *last* inclusive,
      without affecting the selection state of items outside that range.
      :meth:`select_set` is an alias of :meth:`!selection_set`.

   .. method:: itemcget(index, option)

      Return the current value of the configuration option *option* for the
      item given by *index*.

   .. method:: itemconfig(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: itemconfigure(index, cnf=None, **kw)

      Query or modify the configuration options of the item given by *index*.
      This mirrors :meth:`~Misc.configure`, except that it applies to an
      individual item rather than to the listbox as a whole.
      With no options, it returns a dictionary describing the current options
      of the item; otherwise it sets the given options.
      The supported item options are *background*, *foreground*,
      *selectbackground* and *selectforeground*.
      :meth:`itemconfig` is an alias of :meth:`!itemconfigure`.

   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y)

      Scroll the listbox by 10 times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events in the widget, producing
      the effect of dragging the list at high speed through the window.


.. class:: Menu(master=None, cnf={}, **kw)

   A :class:`!Menu` widget displays a column of entries, each of which may be a
   command, a checkbutton, a radiobutton, a cascade (which posts an associated
   submenu) or a separator.
   Menus are used as the menubar of a toplevel window, as pulldown menus posted
   from a cascade entry or menubutton, and as popup menus.
   Inherits from :class:`Widget`.

   Many of the entry methods take an *index* argument that selects which entry
   to operate on.
   As described in the Tk ``menu`` manual page, *index* may be a numeric index
   (counting from 0 at the top), ``'active'`` (the currently active entry),
   ``'end'`` or ``'last'`` (the bottommost entry), ``'none'`` (no entry at all,
   written ``{}`` in Tcl), ``@y`` (the entry covering pixel y-coordinate *y* in
   the menu window), or a pattern matched against the labels of the entries
   from the top down.

   .. method:: add(itemType, cnf={}, **kw)

      Add a new entry to the bottom of the menu.
      *itemType* is one of ``'command'``, ``'cascade'``, ``'checkbutton'``,
      ``'radiobutton'`` or ``'separator'`` and determines the type of the new
      entry; the remaining options configure it.
      The :meth:`!add_command`, :meth:`!add_cascade`, :meth:`!add_checkbutton`,
      :meth:`!add_radiobutton` and :meth:`!add_separator` convenience methods
      call this method with the corresponding *itemType*.

      The entry is configured by the following options, although not every
      option applies to every entry type (a separator accepts none of them):

      *label*
         The text to display in the entry.

      *command*
         The function to call when the entry is invoked (command, checkbutton
         and radiobutton entries).

      *accelerator*
         A string displayed at the right of the entry to advertise an
         accelerator keystroke; it does not itself create the binding.

      *underline*
         The index of a character in the label to underline for keyboard
         traversal.

      *state*
         One of ``'normal'``, ``'active'`` or ``'disabled'``.

      *image*
         An image to display instead of, or together with, the text label.

      *compound*
         Where to show the image relative to the text: ``'none'`` (the
         default), ``'text'``, ``'image'``, ``'top'``, ``'bottom'``, ``'left'``
         or ``'right'``.

      *bitmap*
         A bitmap to display instead of the text label.

      *font*
         The font to use for the text.

      *background*, *foreground*
         The entry's background and foreground colors in its normal state
         (ignored on macOS).

      *activebackground*, *activeforeground*
         The background and foreground colors used when the entry is active
         (ignored on macOS).

      *columnbreak*
         If true, the entry starts a new column instead of being placed below
         the previous entry.

      *hidemargin*
         If true, the standard margin around the entry is omitted, which is
         useful when a menu is used as a palette.

      *menu*
         The submenu posted by a cascade entry; it must be a child of this
         menu.

      *variable*
         The variable associated with a checkbutton or radiobutton entry.

      *onvalue*, *offvalue*
         The values stored in *variable* when a checkbutton entry is selected
         or cleared.

      *value*
         The value stored in *variable* when a radiobutton entry is selected.

      *indicatoron*
         Whether to display the indicator of a checkbutton or radiobutton
         entry.

      *selectcolor*
         The color of the indicator of a checkbutton or radiobutton entry when
         it is selected.

      *selectimage*
         The image displayed when a checkbutton or radiobutton entry is
         selected and *image* is also given.

   .. method:: add_cascade(cnf={}, **kw)

      Add a new cascade entry to the bottom of the menu.
      A cascade entry has an associated submenu, given by its *menu* option,
      which must be a child of this menu; posting the entry posts the submenu
      next to it.

   .. method:: add_checkbutton(cnf={}, **kw)

      Add a new checkbutton entry to the bottom of the menu.
      When invoked, a checkbutton entry toggles between its *onvalue* and
      *offvalue*, storing the result in its associated *variable*, and displays
      an indicator showing whether it is selected.

   .. method:: add_command(cnf={}, **kw)

      Add a new command entry to the bottom of the menu.
      A command entry behaves much like a button: when it is invoked, the
      callback given by its *command* option is called.

   .. method:: add_radiobutton(cnf={}, **kw)

      Add a new radiobutton entry to the bottom of the menu.
      Radiobutton entries sharing the same *variable* form a group of which
      only one may be selected at a time; selecting an entry stores its *value*
      in the variable.

   .. method:: add_separator(cnf={}, **kw)

      Add a separator to the bottom of the menu.
      A separator is displayed as a horizontal dividing line and cannot be
      activated or invoked.

   .. method:: insert(index, itemType, cnf={}, **kw)

      Same as :meth:`add`, except that the new entry is inserted just before
      the entry given by *index* instead of being appended to the end of the
      menu.
      *itemType* is one of ``'command'``, ``'cascade'``, ``'checkbutton'``,
      ``'radiobutton'`` or ``'separator'``.
      The :meth:`!insert_command`, :meth:`!insert_cascade`,
      :meth:`!insert_checkbutton`, :meth:`!insert_radiobutton` and
      :meth:`!insert_separator` convenience methods call this method with the
      corresponding *itemType*.

   .. method:: insert_cascade(index, cnf={}, **kw)

      Insert a new cascade entry before the entry given by *index* (see
      :meth:`add_cascade`).

   .. method:: insert_checkbutton(index, cnf={}, **kw)

      Insert a new checkbutton entry before the entry given by *index* (see
      :meth:`add_checkbutton`).

   .. method:: insert_command(index, cnf={}, **kw)

      Insert a new command entry before the entry given by *index* (see
      :meth:`add_command`).

   .. method:: insert_radiobutton(index, cnf={}, **kw)

      Insert a new radiobutton entry before the entry given by *index* (see
      :meth:`add_radiobutton`).

   .. method:: insert_separator(index, cnf={}, **kw)

      Insert a separator before the entry given by *index* (see
      :meth:`add_separator`).

   .. method:: delete(index1, index2=None)

      Delete all of the menu entries between *index1* and *index2* inclusive.
      If *index2* is omitted, it defaults to *index1*, so that a single entry
      is deleted.
      Attempts to delete a tear-off entry are ignored; remove it by changing
      the *tearoff* option instead.

   .. method:: entrycget(index, option)

      Return the current value of the configuration option *option* for the
      entry given by *index*.

   .. method:: entryconfig(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: entryconfigure(index, cnf=None, **kw)

      Query or modify the configuration options of the entry given by *index*.
      This mirrors :meth:`~Misc.configure`, except that it applies to an
      individual entry rather than to the menu as a whole.
      With no options, it returns a dictionary describing the current options
      of the entry; otherwise it sets the given options.
      The supported options are those accepted by :meth:`add` for the entry's
      type.
      :meth:`entryconfig` is an alias of :meth:`!entryconfigure`.

   .. method:: index(index)

      Return the numerical index corresponding to *index*, or ``None`` if
      *index* selects no entry.

   .. method:: type(index)

      Return the type of the entry given by *index*: one of ``'command'``,
      ``'cascade'``, ``'checkbutton'``, ``'radiobutton'``, ``'separator'`` or
      ``'tearoff'`` (for the tear-off entry).

   .. method:: activate(index)

      Make the entry given by *index* the active entry, redisplaying it with
      its active colors, and deactivate any previously active entry.
      If *index* selects no entry, or the selected entry is disabled, the menu
      ends up with no active entry.

   .. method:: invoke(index)

      Invoke the action of the entry given by *index*, as if it had been
      clicked.
      Nothing happens if the entry is disabled.
      If the entry has a *command* associated with it, the result of that
      command is returned; otherwise the result is an empty string.

   .. method:: post(x, y)

      Display the menu on the screen at the root-window coordinates *x* and
      *y*, adjusting them if necessary so that the whole menu is visible.
      If the *postcommand* option has been specified, it is evaluated before
      the menu is posted.

   .. method:: tk_popup(x, y, entry='')

      Post the menu as a popup at the root-window coordinates *x* and *y*.
      If *entry* is given, the menu is positioned so that this entry is
      displayed under the pointer.

   .. method:: unpost()

      Unmap the menu so that it is no longer displayed, also unposting any
      posted lower-level cascaded submenu.
      This has no effect on Windows and macOS, which manage the unposting of
      menus themselves.

   .. method:: xposition(index)

      Return the x-coordinate, within the menu window, of the leftmost pixel of
      the entry given by *index*.

      .. versionadded:: 3.3

   .. method:: yposition(index)

      Return the y-coordinate, within the menu window, of the topmost pixel of
      the entry given by *index*.


.. class:: Menubutton(master=None, cnf={}, **kw)

   A :class:`!Menubutton` widget displays a textual string, bitmap or image and
   posts an associated :class:`Menu`, given by its *menu* option, when the user
   presses it.
   Like a :class:`Label` it can show *text*, a *textvariable*, or an *image*,
   and the *direction* option controls where the menu appears relative to the
   button.
   Inherits from :class:`Widget`.
   Refer to the Tk ``menubutton`` manual page for the full list of options.


.. class:: Message(master=None, cnf={}, **kw)

   A :class:`!Message` widget displays a non-interactive textual string, given
   by the *text* option or linked to a variable through *textvariable*.
   Unlike a :class:`Label`, it breaks the string into multiple lines in order
   to produce a given aspect ratio, choosing line breaks at word boundaries,
   and it can justify the text left, centered or right.
   Inherits from :class:`Widget`.
   Refer to the Tk ``message`` manual page for the full list of options.


.. class:: OptionMenu(master, variable, value, *values, **kwargs)

   A helper subclass of :class:`Menubutton` that displays a pop-up menu of
   mutually exclusive choices.
   *variable* is a :class:`Variable` kept in sync with the selection, *value*
   is the initial choice, and *values* are the remaining menu entries.
   The keyword argument *command* may be given a callback that is invoked with
   the selected value, and the keyword argument *name* sets the Tk widget name.

   .. method:: destroy()

      Destroy the widget, also cleaning up the associated pop-up menu.

   .. versionchanged:: 3.14
      Added support for the *name* keyword argument.



.. class:: PanedWindow(master=None, cnf={}, **kw)

   A :class:`!PanedWindow` is a geometry-manager widget that arranges any
   number of child *panes* in a row (when *orient* is ``'horizontal'``) or a
   column (when *orient* is ``'vertical'``).
   Each pane holds one widget, and each pair of adjacent panes is separated by
   a movable *sash* that the user can drag with the mouse to resize the widgets
   on either side of it.
   Inherits from :class:`Widget`.

   The *orient* option selects the layout direction, *sashwidth* sets the width
   of each sash and *sashrelief* its relief.
   When *showhandle* is true a small handle is drawn on each sash that the user
   can grab to drag it.
   Refer to the Tk ``panedwindow`` manual page for the full list of options.

   .. method:: add(child, **kw)

      Add *child* to the panedwindow as a new pane, placed after any existing
      panes.
      The keyword arguments specify per-pane management options for *child*;
      they may be any of the options accepted by :meth:`paneconfigure`.

   .. method:: forget(child)
      :no-typesetting:

   .. method:: remove(child)

      Remove the pane containing *child* from the panedwindow.
      All geometry management options for *child* are forgotten.
      :meth:`forget` is an alias of :meth:`!remove`.
      This shadows the inherited geometry-manager :meth:`!forget`;
      use :meth:`~Pack.pack_forget`, :meth:`~Grid.grid_forget` or
      :meth:`~Place.place_forget` to remove the widget itself from its manager.

   .. method:: panes()

      Return a tuple of the widgets managed by the panedwindow, one per pane,
      in order.

   .. method:: panecget(child, option)

      Return the current value of the management option *option* for the pane
      containing *child*.
      *option* may be any value allowed by :meth:`paneconfigure`.

   .. method:: paneconfig(tagOrId, cnf=None, **kw)
      :no-typesetting:

   .. method:: paneconfigure(tagOrId, cnf=None, **kw)

      Query or modify the management options of the pane containing the widget
      *tagOrId*.
      With no options, it returns a dictionary describing all of the available
      options for the pane; given a single option name as a string, it returns
      a description of that one option; otherwise it sets the given options.
      The supported options include *after* and *before* (insert the pane after
      or before another managed window), *height* and *width* (the outer
      dimensions of the window, including any border), *minsize* (the minimum
      size in the paned dimension), *padx* and *pady* (extra space to leave on
      each side of the window), *sticky* (position or stretch the window within
      an oversized pane, using a string of the characters ``n``, ``s``, ``e``
      and ``w``), *hide* (hide the pane while keeping it in the list of panes)
      and *stretch* (how extra space is allocated to the pane: one of
      ``'always'``, ``'first'``, ``'last'``, ``'middle'`` or ``'never'``).
      :meth:`paneconfig` is an alias of :meth:`!paneconfigure`.

   .. method:: identify(x, y)

      Identify the panedwindow component underneath the point given by *x* and
      *y*, in window coordinates.
      If the point is over a sash or a sash handle, the result is a two-element
      tuple containing the index of the sash or handle and a word indicating
      whether it is over a sash or a handle, such as ``(0, 'sash')`` or
      ``(2, 'handle')``.
      If the point is over any other part of the panedwindow, the result is an
      empty string.

   .. method:: sash(*args)

      Query or change the position of the sashes in the panedwindow.
      This is a thin wrapper around the Tk ``sash`` subcommand; the convenience
      methods :meth:`sash_coord`, :meth:`sash_mark` and :meth:`sash_place`
      should normally be used instead.

   .. method:: sash_coord(index)

      Return the current x and y coordinate pair for the sash given by *index*,
      which must be an integer between 0 and one less than the number of panes
      in the panedwindow.
      The coordinates returned are those of the top left corner of the region
      containing the sash.

   .. method:: sash_mark(index)

      Record the current mouse position for the sash given by *index*, for use
      together with later sash-drag operations to move the sash.

   .. method:: sash_place(index, x, y)

      Place the sash given by *index* at the coordinates *x* and *y*.

   .. method:: proxy(*args)

      Query or change the position of the sash proxy, the "ghost" sash shown
      while a sash is being dragged with non-opaque resizing.
      This is a thin wrapper around the Tk ``proxy`` subcommand; the
      convenience methods :meth:`proxy_coord`, :meth:`proxy_forget` and
      :meth:`proxy_place` should normally be used instead.

   .. method:: proxy_coord()

      Return a tuple containing the x and y coordinates of the most recent
      proxy location.

   .. method:: proxy_forget()

      Remove the proxy from the display.

   .. method:: proxy_place(x, y)

      Place the proxy at the coordinates *x* and *y*.


.. class:: Radiobutton(master=None, cnf={}, **kw)

   A :class:`!Radiobutton` widget displays a textual string, bitmap or image
   together with a diamond or circular indicator, and selects one choice out of
   several.
   It has all the behavior of a simple button and, in addition, can be
   selected: typically several radiobuttons share a single *variable*, and
   selecting one sets that variable to the radiobutton's *value*; each
   radiobutton also monitors the variable and automatically selects or
   deselects itself when the variable changes.
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a radiobutton accepts the
   options documented in the Tk ``radiobutton`` manual page, such as
   *variable*, *value* and *command*.

   .. method:: invoke()

      Do just what would happen if the user pressed the radiobutton with the
      mouse: select the button and invoke the associated command, if there is
      one.
      Return the result of the command, or an empty string if no command is
      associated with the radiobutton.
      This is ignored if the radiobutton's state is ``disabled``.

   .. method:: select()

      Select the radiobutton and set the associated variable to the value
      corresponding to this widget.

   .. method:: deselect()

      Deselect the radiobutton and set the associated variable to an empty
      string.
      If this radiobutton was not currently selected, this has no effect.

   .. method:: flash()

      Flash the radiobutton by redisplaying it several times, alternating
      between the active and normal colors.
      At the end of the flash the radiobutton is left in the same normal or
      active state as when the method was called.
      This is ignored if the radiobutton's state is ``disabled``.


.. class:: Scale(master=None, cnf={}, **kw)

   A :class:`!Scale` widget lets the user select a numerical value by moving a
   slider along a trough.
   It can be oriented vertically or horizontally and can optionally display a
   label and the current value.
   Inherits from :class:`Widget`.

   In addition to the standard widget options, a scale accepts the options
   documented in the Tk ``scale`` manual page, such as *from_*, *to*,
   *resolution*, *orient*, *tickinterval*, *variable* and *command*.
   As elsewhere in :mod:`!tkinter`, the leading ``-`` of the Tk option name is
   dropped; *from* is spelled ``from_`` because :keyword:`from` is a Python
   keyword.

   With a non-integer *resolution*, see :ref:`numeric values and the locale
   <tkinter-numeric-locale>`.

   .. method:: get()

      Return the current value of the scale.
      The result is an integer if the scale's *resolution* yields whole
      numbers, and a float otherwise.

   .. method:: set(value)

      Set the scale to *value*, moving the slider accordingly.
      This has no effect if the scale is disabled.

   .. method:: coords(value=None)

      Return a tuple ``(x, y)`` giving the pixel coordinates, relative to the
      widget, of the point on the centerline of the trough that corresponds to
      *value*.
      If *value* is omitted, the scale's current value is used.

   .. method:: identify(x, y)

      Return a string describing the part of the scale at the pixel coordinates
      *x*, *y*: ``'slider'``, ``'trough1'`` (the part of the trough above or to
      the left of the slider), ``'trough2'`` (below or to the right of the
      slider), or an empty string if the point is not over any of these
      elements.


.. class:: Scrollbar(master=None, cnf={}, **kw)

   A :class:`!Scrollbar` widget displays a slider and two arrows that let the
   user scroll an associated widget, such as a :class:`Listbox`, :class:`Text`,
   :class:`Canvas` or :class:`Entry`.
   It is connected to the scrolled widget by setting that widget's
   *xscrollcommand* or *yscrollcommand* option to the scrollbar's :meth:`set`
   method, and the scrollbar's *command* option to the scrolled widget's
   :meth:`~XView.xview` or :meth:`~YView.yview` method.
   Inherits from :class:`Widget`.

   .. method:: get()

      Return the current scrollbar settings as a tuple ``(first, last)`` of two
      fractions between 0 and 1, describing the portion of the document that is
      currently visible, as last passed to :meth:`set`.

   .. method:: set(first, last)

      Set the scrollbar.
      *first* and *last* are fractions between 0 and 1 giving the positions of
      the start and end of the visible portion of the associated document.
      This method is normally registered as the scrolled widget's
      *xscrollcommand* or *yscrollcommand* and called by that widget.

   .. method:: activate(index=None)

      Mark the element *index* (one of ``'arrow1'``, ``'slider'`` or
      ``'arrow2'``) as active, displaying it according to the
      *activebackground* and *activerelief* options.
      If *index* is omitted, return the name of the currently active element,
      or ``None`` if no element is active.

      .. versionchanged:: 3.5
         The *index* argument is now optional.

   .. method:: delta(deltax, deltay)

      Return a float indicating the fractional change in the scrollbar setting
      that corresponds to moving the slider by *deltax* pixels horizontally
      (for horizontal scrollbars) or *deltay* pixels vertically (for vertical
      scrollbars).

   .. method:: fraction(x, y)

      Return a float between 0 and 1 indicating where the point at pixel
      coordinates *x*, *y* lies in the trough: 0 corresponds to the top or left
      of the trough and 1 to the bottom or right.

   .. method:: identify(x, y)

      Return the name of the element under the pixel coordinates *x*, *y* (such
      as ``'arrow1'``), or an empty string if the point does not lie in any
      element of the scrollbar.


.. class:: Spinbox(master=None, cnf={}, **kw)

   A :class:`!Spinbox` widget is an :class:`Entry`-like widget with a pair of
   up/down arrow buttons that let the user step through a range of values in
   addition to editing the value directly.
   The set of values may be a numeric range given by the *from_*, *to* and
   *increment* options, or an explicit list of strings given by the *values*
   option (which takes precedence over the range).
   Each time an arrow is invoked the *command* callback, if any, is called; the
   boolean *wrap* option controls whether stepping past either end of the range
   wraps around to the other end;
   the *format* option specifies how numeric values are formatted;
   and the *validate* option enables validation of the entered text.
   Inherits from :class:`Widget` and :class:`XView`.

   With a non-integer *increment*, see :ref:`numeric values and the locale
   <tkinter-numeric-locale>`.

   Many of the methods take an *index* argument identifying a character in the
   spinbox's string.
   As described in the Tk ``spinbox`` manual page, *index* may be a numeric
   index (counting from 0), ``'anchor'`` (the selection anchor point),
   ``'end'`` (just after the last character), ``'insert'`` (the character just
   after the insertion cursor), ``'sel.first'`` or ``'sel.last'`` (the ends of
   the selection), or ``@x`` (the character covering pixel x-coordinate *x* in
   the window).

   .. method:: get()

      Return the spinbox's string.

   .. method:: insert(index, s)

      Insert the characters of the string *s* just before the character given
      by *index*.

   .. method:: delete(first, last=None)

      Delete one or more characters of the spinbox.
      *first* is the index of the first character to delete, and *last* is the
      index of the character just after the last one to delete.
      If *last* is omitted, a single character at *first* is deleted.

   .. method:: icursor(index)

      Arrange for the insertion cursor to be displayed just before the
      character given by *index*.

   .. method:: index(index)

      Return the numerical index corresponding to *index*, as a string.

   .. method:: bbox(index)

      Return a tuple of four integers ``(x, y, width, height)`` describing the
      bounding box of the character given by *index*.
      *x* and *y* are the pixel coordinates of the upper-left corner of the
      character relative to the widget, and *width* and *height* are its size
      in pixels.
      The bounding box may refer to a region outside the visible area of the
      window.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: identify(x, y)

      Return the name of the window element at the pixel coordinates *x*, *y*:
      one of ``'buttondown'``, ``'buttonup'``, ``'entry'`` or ``'none'``.

   .. method:: invoke(element)

      Invoke the spin button given by *element*, either ``'buttonup'`` or
      ``'buttondown'``, triggering the action associated with it.

   .. method:: scan(*args)

      A thin wrapper around the Tk ``scan`` widget subcommand, used to
      implement fast dragging of the view: ``scan('mark', x)`` records *x* and
      the current view, and ``scan('dragto', x)`` adjusts the view relative to
      that mark.
      The :meth:`scan_mark` and :meth:`scan_dragto` methods wrap the two forms.

   .. method:: scan_mark(x)

      Record *x* and the current view in the spinbox window, for use with a
      later :meth:`scan_dragto` call.
      This is typically associated with a mouse button press in the widget.

   .. method:: scan_dragto(x)

      Adjust the view by 10 times the difference between *x* and the *x* passed
      to the last :meth:`scan_mark` call.
      This is typically associated with mouse motion events, producing the
      effect of dragging the spinbox at high speed through the window.

   .. method:: selection(*args)

      A thin wrapper around the Tk ``selection`` widget subcommand, used to
      adjust the selection within the spinbox.
      It has several forms depending on the first argument, such as
      ``selection('adjust', index)``, ``selection('clear')``,
      ``selection('element', ?elem?)``, ``selection('from', index)``,
      ``selection('present')``, ``selection('range', start, end)`` and
      ``selection('to', index)``.
      The :meth:`selection_adjust`, :meth:`selection_clear`,
      :meth:`selection_element`, :meth:`selection_from`,
      :meth:`selection_present`, :meth:`selection_range` and
      :meth:`selection_to` methods wrap these forms.

   .. method:: selection_adjust(index)

      Locate the end of the selection nearest to the character given by *index*
      and adjust that end of the selection to be at *index* (including but not
      going beyond *index*).
      The other end becomes the anchor point for future :meth:`selection_to`
      calls.
      If the selection is not currently in the spinbox, a new selection is
      created to include the characters between *index* and the most recent
      anchor point, inclusive.

   .. method:: selection_clear()

      Clear the selection if it is currently in this widget.
      If the selection is not in this widget, the method has no effect.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on a :class:`Spinbox`.

   .. method:: selection_element(element=None)

      Set or get the currently selected element.
      If *element* (one of ``'buttonup'``, ``'buttondown'`` or ``'none'``) is
      given, that spin button is selected and displayed depressed; otherwise
      the name of the currently selected element is returned.

   .. method:: selection_from(index)

      Set the selection anchor point to just before the character given by
      *index*, without changing the selection itself.

      .. versionadded:: 3.8


   .. method:: selection_present()

      Return ``True`` if there are characters selected in the spinbox,
      ``False`` otherwise.

      .. versionadded:: 3.8


   .. method:: selection_range(start, end)

      Set the selection to include the characters starting with the one indexed
      by *start* and ending with the one just before *end*.
      If *end* refers to the same character as *start* or an earlier one, the
      selection is cleared.

      .. versionadded:: 3.8


   .. method:: selection_to(index)

      Set the selection between *index* and the anchor point.
      If *index* is before the anchor point, the selection runs from *index* up
      to but not including the anchor point; if it is after, the selection runs
      from the anchor point up to but not including *index*; if it is the same,
      nothing happens.
      The anchor point is the one set by the most recent :meth:`selection_from`
      or :meth:`selection_adjust` call.
      If the selection is not in this widget, a new selection is created using
      the most recent anchor point.

      .. versionadded:: 3.8



.. class:: Text(master=None, cnf={}, **kw)

   A :class:`!Text` widget displays and edits multi-line text.
   Portions of the text may be styled with **tags**, particular positions may
   be annotated with floating **marks**, and arbitrary images and other widgets
   may be embedded in the text.
   The widget also provides an unlimited undo/redo mechanism and supports peer
   widgets that share the same underlying data.
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``text`` manual page for the full list of options.

   Most of the methods take one or more *index* arguments that identify a
   position within the text.
   As described in the Tk ``text`` manual page, an index is a string consisting
   of a base, optionally followed by one or more modifiers.
   The base may be ``'line.char'`` (line *line*, character *char*, where lines
   are counted from 1 and characters within a line from 0; ``'line.end'``
   refers to the newline ending the line), ``'end'`` (the position just after
   the last newline), the name of a mark, ``'tag.first'`` or ``'tag.last'``
   (the first character tagged with *tag*, or the position just after the last
   such character), the name of an embedded image or window, or ``@x,y`` (the
   character covering pixel coordinates *x*, *y* in the widget).
   A modifier such as ``'+5 chars'``, ``'-3 lines'``, ``'linestart'``,
   ``'lineend'``, ``'wordstart'`` or ``'wordend'`` adjusts the index relative
   to its base; several modifiers may be combined and are applied from left to
   right, for example ``'insert wordstart - 1 c'``.

   .. method:: insert(index, chars, *args)

      Insert the string *chars* just before the character at *index* (if
      *index* is ``'end'``, just before the final newline).
      By default the new text inherits any tags present on both sides of the
      insertion point.
      If *args* is given, it consists of alternating *tagList*, *chars* values:
      the preceding *chars* receives exactly the tags listed (a tag list may be
      a single tag name or a sequence of names), overriding the surrounding
      tags.

   .. method:: delete(index1, index2=None)

      Delete the range of characters from *index1* up to but not including
      *index2*.
      If *index2* is omitted, the single character at *index1* is deleted.
      The widget always keeps a newline as its last character, so a deletion
      that would remove it is adjusted accordingly.

   .. method:: replace(index1, index2, chars, *args)

      Replace the range of characters from *index1* up to but not including
      *index2* with *chars*.
      This is equivalent to a :meth:`delete` followed by an :meth:`insert` at
      *index1*; *args* is interpreted as for :meth:`insert`.

      .. versionadded:: 3.3

   .. method:: get(index1, index2=None)

      Return the text from *index1* up to but not including *index2* as a
      string.
      If *index2* is omitted, return the single character at *index1*.
      Embedded images and windows are omitted from the result.

   .. method:: index(index)

      Return the position corresponding to *index* in the canonical
      ``'line.char'`` form.

   .. method:: compare(index1, op, index2)

      Compare the positions of *index1* and *index2* using the relational
      operator *op*, which must be one of ``'<'``, ``'<='``, ``'=='``,
      ``'>='``, ``'>'`` or ``'!='``, and return the boolean result.

   .. method:: count(index1, index2, *options, return_ints=False)

      Count the number of items of the requested kinds between *index1* and
      *index2*; the count is negative if *index1* is after *index2*.
      Each of *options* names a kind of item to count: ``'chars'``,
      ``'displaychars'``, ``'displayindices'``, ``'displaylines'``,
      ``'indices'``, ``'lines'``, ``'xpixels'`` or ``'ypixels'`` (the default,
      used when no option is given, is ``'indices'``).
      The pseudo-option ``'update'`` forces any out-of-date layout information
      to be recalculated before the following options are evaluated.
      When *return_ints* is true and a single counting option is given, return
      a plain integer; otherwise return a tuple with one integer per counting
      option (or ``None`` if the result is empty).

      .. versionadded:: 3.3

      .. versionchanged:: 3.13
         Added the *return_ints* parameter.


   .. method:: see(index)

      Adjust the view so that the character given by *index* is visible.
      If it is already visible the method has no effect; if it is a short
      distance out of view the widget scrolls just enough to bring it to the
      nearest edge, otherwise it scrolls to center *index* in the window.

   .. method:: bbox(index)

      Return a tuple ``(x, y, width, height)`` giving the bounding box, in
      pixels, of the visible part of the character at *index*, or ``None`` if
      that character is not visible on the screen.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: dlineinfo(index)

      Return a tuple ``(x, y, width, height, baseline)`` describing the display
      line that contains *index*: the first four values give the bounding box
      of the line in pixels and *baseline* gives the offset of the baseline
      measured down from the top of the area.
      Return ``None`` if that display line is not visible on the screen.

   .. method:: mark_set(markName, index)

      Set the mark named *markName* to the position just before the character
      at *index*, creating the mark if it does not already exist.
      A mark created this way has right gravity by default.

   .. method:: mark_unset(*markNames)

      Remove each of the marks named in *markNames*.
      The special ``insert`` and ``current`` marks may not be removed.

   .. method:: mark_names()

      Return a tuple of the names of all marks currently set in the widget.

   .. method:: mark_gravity(markName, direction=None)

      If *direction* is omitted, return the gravity of mark *markName*, either
      ``'left'`` or ``'right'``.
      Otherwise set its gravity to *direction*.
      The gravity determines on which side of the mark text inserted at the
      mark's position appears: a mark with right gravity (the default) stays to
      the right of such text.

   .. method:: mark_next(index)

      Return the name of the first mark at or after *index*, or ``None`` if
      there is none.
      When *index* is the name of a mark, the search starts just after that
      mark.

   .. method:: mark_previous(index)

      Return the name of the last mark at or before *index*, or ``None`` if
      there is none.
      When *index* is the name of a mark, the search starts just before that
      mark.

   .. method:: tag_add(tagName, index1, *args)

      Add the tag *tagName* to the range of characters from *index1* up to but
      not including the next index in *args*.
      Further pairs of indices may follow in *args* to tag additional ranges; a
      trailing single index tags just the character at that index.

   .. method:: tag_remove(tagName, index1, index2=None)

      Remove the tag *tagName* from the characters from *index1* up to but not
      including *index2* (or from the single character at *index1* if *index2*
      is omitted).
      The tag itself continues to exist even if no characters carry it.

   .. method:: tag_delete(*tagNames)

      Delete each of the tags named in *tagNames*, removing them from all
      characters and discarding their options and bindings.

   .. method:: tag_config(tagName, cnf=None, **kw)
      :no-typesetting:

   .. method:: tag_configure(tagName, cnf=None, **kw)

      Query or modify the configuration options of the tag *tagName*.
      This mirrors :meth:`~Misc.configure`, except that it applies to a tag
      rather than to the widget as a whole: with no options it returns a
      dictionary describing the current options, otherwise it sets the given
      options.
      Defining a tag this way also gives it a priority higher than any existing
      tag.

      The supported tag options, all controlling the appearance of the tagged
      text, are:

      *font*
         The font to use for the text.

      *foreground*
         The color to use for the text.

      *background*
         The color to use for the area behind the text.

      *fgstipple*, *bgstipple*
         Bitmaps used to stipple the foreground (text) and the background;
         only well supported on X11.

      *borderwidth*
         The width of the border drawn around the text according to *relief*
         (default ``0``).

      *relief*
         The 3-D appearance of the text's border: ``'flat'`` (the default),
         ``'raised'``, ``'sunken'``, ``'ridge'``, ``'groove'`` or ``'solid'``.

      *offset*
         How far the text is raised above (or, if negative, lowered below) the
         baseline, for superscripts and subscripts.

      *underline*
         Whether to underline the text (a boolean).

      *underlinefg*
         The color of the underline; it defaults to the text color.

      *overstrike*
         Whether to draw a line through the middle of the text.

      *overstrikefg*
         The color of the overstrike line; it defaults to the text color.

      *elide*
         Whether the text is elided (hidden).

      *justify*
         How to justify the first character of a display line: ``'left'`` (the
         default), ``'right'`` or ``'center'``.

      *wrap*
         How to wrap lines that are too long: ``'char'``, ``'word'`` or
         ``'none'``.

      *lmargin1*, *lmargin2*
         The indentation, in pixels, of the first display line of a logical
         line and of the remaining display lines.

      *lmargincolor*
         The color of the left margin area.

      *rmargin*
         The right-hand margin, in pixels.

      *rmargincolor*
         The color of the right margin area.

      *spacing1*, *spacing2*, *spacing3*
         Extra space, in pixels, above the first display line of a logical
         line, between its display lines, and below its last display line.

      *tabs*
         The set of tab stops, in the same form as the widget's *tabs* option.

      *tabstyle*
         How tab stops are interpreted: ``'tabular'`` or ``'wordprocessor'``.

      *selectbackground*, *selectforeground*
         The background and foreground colors used for the text while it is
         selected.

      .. note::

         Tk 8.6 added the *lmargincolor*, *overstrikefg*, *rmargincolor*,
         *selectbackground*, *selectforeground* and *underlinefg* options.

      :meth:`tag_config` is an alias of :meth:`!tag_configure`.

   .. method:: tag_cget(tagName, option)

      Return the current value of the configuration option *option* for the tag
      *tagName*.

   .. method:: tag_names(index=None)

      If *index* is omitted, return a tuple of the names of all tags defined in
      the widget; otherwise return only the names of the tags applied to the
      character at *index*.
      The names are ordered from lowest to highest priority.

   .. method:: tag_ranges(tagName)

      Return a tuple of indices describing all ranges of text tagged with
      *tagName*.
      The result alternates start and end indices, so that elements ``2*i`` and
      ``2*i+1`` bound the *i*-th range.

   .. method:: tag_nextrange(tagName, index1, index2=None)

      Search forward from *index1* (up to *index2* if given) for the first
      range of characters tagged with *tagName*, and return a two-element tuple
      of its start and end indices, or an empty tuple if there is no such
      range.

   .. method:: tag_prevrange(tagName, index1, index2=None)

      Search backward from *index1* (down to *index2* if given) for the nearest
      preceding range of characters tagged with *tagName*, and return a
      two-element tuple of its start and end indices, or an empty tuple if
      there is no such range.

   .. method:: tag_raise(tagName, aboveThis=None)

      Raise the priority of tag *tagName* so that it is just above the priority
      of *aboveThis*, or to the highest priority of all tags if *aboveThis* is
      omitted.
      When the display options of overlapping tags conflict, the
      higher-priority tag wins.

   .. method:: tag_lower(tagName, belowThis=None)

      Lower the priority of tag *tagName* so that it is just below the priority
      of *belowThis*, or to the lowest priority of all tags if *belowThis* is
      omitted.

   .. method:: tag_bind(tagName, sequence, func, add=None)

      Bind the event *sequence* on characters tagged with *tagName* to the
      callback *func*, so that *func* is invoked when that event occurs over
      such a character.
      If *add* is true the binding is added alongside any existing bindings for
      *sequence*, otherwise it replaces them.
      Works like :meth:`~Misc.bind` and returns the identifier of the new
      binding.

   .. method:: tag_unbind(tagName, sequence, funcid=None)

      Remove the bindings of the event *sequence* on characters tagged with
      *tagName*.
      If *funcid* is given, only that binding (as returned by :meth:`tag_bind`)
      is removed and its callback is unregistered.

      .. versionchanged:: 3.13
         If *funcid* is given, only that callback is unbound.


   .. method:: image_create(index, cnf={}, **kw)

      Embed an image at *index* and return the name assigned to this image
      instance, which may then be used as an index or passed to the other
      ``image_*`` methods.
      The options, given in *cnf* and *kw*, include *image* (the Tk image to
      display), *name* (a base name for the instance), *align*, *padx* and
      *pady*.

   .. method:: image_cget(index, option)

      Return the current value of the configuration option *option* for the
      embedded image at *index*.

   .. method:: image_configure(index, cnf=None, **kw)

      Query or modify the configuration options of the embedded image at
      *index*, like :meth:`~Misc.configure` but applied to that image.

   .. method:: image_names()

      Return a tuple of the names of all images embedded in the widget.

      .. note::

         This shadows the inherited :meth:`Misc.image_names`,
         which returns the names of all images in the Tcl interpreter;
         that method is not available on a :class:`Text`.

   .. method:: window_create(index, cnf={}, **kw)

      Embed a window (any widget) at *index*.
      The options, given in *cnf* and *kw*, include *window* (the widget to
      embed), *create* (a callback that creates the widget on demand), *align*,
      the boolean *stretch* (whether the widget is stretched vertically to the
      height of the line), *padx* and *pady*.
      The embedded widget must be a descendant of the text widget's parent.

   .. method:: window_cget(index, option)

      Return the current value of the configuration option *option* for the
      embedded window at *index*.

   .. method:: window_config(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: window_configure(index, cnf=None, **kw)

      Query or modify the configuration options of the embedded window at
      *index*, like :meth:`~Misc.configure` but applied to that window.

      :meth:`window_config` is an alias of :meth:`!window_configure`.

   .. method:: window_names()

      Return a tuple of the names of all windows embedded in the widget.

   .. method:: edit(*args)

      Low-level wrapper around the Tk ``edit`` widget command that controls the
      undo/redo mechanism and the modified flag; *args* is the ``edit``
      subcommand and its arguments.
      The :meth:`!edit_\*` methods below are thin wrappers around it and are
      usually more convenient.

   .. method:: edit_modified(arg=None)

      If *arg* is omitted, return the current state of the modified flag as
      true or false; the flag is set automatically whenever the text is
      inserted or deleted.
      Otherwise set the flag to the boolean *arg*.

   .. method:: edit_undo()

      Undo the most recent edit action, that is, all the inserts and deletes
      recorded on the undo stack since the previous separator, and move it to
      the redo stack.
      Raises :exc:`TclError` if the undo stack is empty.
      Has no effect unless the *undo* option is true.
      Since Tk 9.0, returns a tuple of indices delimiting the ranges of text
      that were changed.

   .. method:: edit_redo()

      Reapply the most recently undone edit action, provided no further edits
      have been made since, and move it back to the undo stack.
      Raises :exc:`TclError` if the redo stack is empty.
      Has no effect unless the *undo* option is true.
      Since Tk 9.0, returns a tuple of indices delimiting the ranges of text
      that were changed.

   .. method:: edit_reset()

      Clear the undo and redo stacks.

   .. method:: edit_separator()

      Push a separator onto the undo stack, marking a boundary between edit
      actions for undo and redo.
      Has no effect unless the *undo* option is true.
      Separators are inserted automatically when the *autoseparators* option is
      true.

   .. method:: search(pattern, index, stopindex=None, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, *, nolinestop=None, strictlimits=None)

      Search for *pattern* starting at *index* and return the index of the
      first character of the first match, or an empty string if there is no
      match.
      Searching stops at *stopindex* if given; otherwise it wraps around the
      ends of the text until the starting position is reached again.
      The following boolean keyword flags control the search: *forwards* or
      *backwards* select the direction (forward is the default); *exact* (the
      default) or *regexp* select literal or regular-expression matching;
      *nocase* makes the match case-insensitive; *elide* causes hidden text to
      be searched as well; *nolinestop* (regexp only) lets ``.`` and ``[^``
      match newlines; and *strictlimits* requires the whole match to lie within
      *index* and *stopindex*.
      If *count* is a :class:`Variable`, the number of index positions in the
      match is stored in it.

      .. versionchanged:: 3.15
         Added the *nolinestop* and *strictlimits* parameters.


   .. method:: search_all(pattern, index, stopindex=None, *, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, nolinestop=None, overlap=None, strictlimits=None)

      Like :meth:`search`, but find every match in the searched range and
      return a tuple of the starting indices of all matches (empty if there are
      none).
      By default overlapping matches are not reported; passing a true *overlap*
      returns every match that is not wholly contained in another.
      If *count* is a :class:`Variable`, it receives a list with one element
      per match.

      .. versionadded:: 3.15


   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y)

      Scroll the widget by 10 times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events, producing the effect of
      dragging the text at high speed through the window.

   .. method:: debug(boolean=None)

      If *boolean* is omitted, return whether internal consistency checks of
      the B-tree data structure are enabled.
      Otherwise enable or disable them.
      The setting is shared by all text widgets and may noticeably slow down
      widgets holding large amounts of text.

   .. method:: dump(index1, index2=None, command=None, **kw)

      Return the contents of the widget from *index1* up to but not including
      *index2* (or just the segment at *index1* if *index2* is omitted),
      including text and information about marks, tags, images and windows.
      The result is a list of ``(key, value, index)`` triples, where *key* is
      one of ``'text'``, ``'mark'``, ``'tagon'``, ``'tagoff'``, ``'image'`` or
      ``'window'``.
      By default all kinds are reported; passing any of the keyword arguments
      *all*, *text*, *mark*, *tag*, *image* or *window* as true restricts the
      dump to the selected kinds.
      If *command* is given, it is called once per triple with the three values
      as arguments and nothing is returned.

   .. method:: peer_create(newPathName, cnf={}, **kw)

      Create a peer text widget with the path name *newPathName* that shares
      this widget's underlying data (text, marks, tags, images and the undo
      stack).
      Changes made through any peer are reflected in all of them.
      By default the peer covers the same lines as this widget; standard text
      options, including *startline* and *endline*, may be given to override
      this.

      .. versionadded:: 3.3

   .. method:: peer_names()

      Return a tuple of the path names of this widget's peers, not including
      the widget itself.

      .. versionadded:: 3.3

   .. method:: yview_pickplace(*what)

      Adjust the view so that the location given by *what* is visible.
      This is an obsolete equivalent of :meth:`see`, which should be used
      instead.


Variable classes
^^^^^^^^^^^^^^^^

.. class:: Variable(master=None, value=None, name=None)

   The base class for the Tk variable wrappers.
   A Tk variable is a value stored in the Tcl interpreter that can be linked to
   widgets through their *variable* or *textvariable* options (see
   :ref:`coupling-widget-variables`), so that changes propagate both ways:
   updating the variable updates every widget bound to it, and a user editing
   such a widget updates the variable.

   *master* is the widget whose Tcl interpreter owns the variable; if omitted,
   the default root window is used.
   *value* is the initial value; if omitted, a type-specific default is used.
   *name* is the name of the variable in the Tcl interpreter; if omitted, a
   unique name of the form ``'PY_VARnum'`` is generated.
   If *name* matches an existing variable and *value* is omitted, the existing
   value is retained.

   In most cases you should use one of the typed subclasses below --
   :class:`StringVar`, :class:`IntVar`, :class:`DoubleVar` or
   :class:`BooleanVar` -- rather than :class:`!Variable` directly.

   .. note::

      When a :class:`!Variable` is garbage collected, its Tcl variable is unset.
      Keep a reference to it for as long as a widget is linked to it, for example
      by storing it as an attribute rather than in a local variable.
      Otherwise Tk recreates the Tcl variable to keep the widget working, but it
      is never unset again, leaking one Tcl variable per dropped wrapper.

   .. versionchanged:: 3.10
      Two variables now compare equal (``==``) only when they have the same
      name, are of the same class, and belong to the same Tcl interpreter.

   .. method:: get()

      Return the current value of the variable.
      For the base class the value is returned as a string; the typed
      subclasses convert it to the appropriate Python type.

   .. method:: initialize(value)
      :no-typesetting:

   .. method:: set(value)

      Set the variable to *value*.
      :meth:`initialize` is an alias of :meth:`!set`.

      .. versionadded:: 3.3
         The *initialize* spelling.

   .. method:: trace_add(mode, callback)

      Register *callback* to be called when the variable is accessed according
      to *mode*.
      *mode* is one of the strings ``'array'``, ``'read'``, ``'write'`` or
      ``'unset'``, or a list or tuple of such strings.

      When triggered, *callback* is called with three arguments: the name of
      the Tcl variable, an index (or an empty string if the variable is not an
      element of an array), and the *mode* that triggered the call.

      Return the internal name of the registered callback, which can be passed
      to :meth:`trace_remove`.

      .. versionadded:: 3.6

   .. method:: trace_remove(mode, cbname)

      Remove a trace callback from the variable.
      *mode* must match the *mode* that was passed to :meth:`trace_add`, and
      *cbname* is the callback name returned by :meth:`trace_add`.

      .. versionadded:: 3.6

   .. method:: trace_info()

      Return a list of ``(modes, cbname)`` pairs describing all traces
      currently set on the variable, where *modes* is a tuple of mode strings
      and *cbname* is the internal callback name.

      .. versionadded:: 3.6

   .. method:: trace(mode, callback)
      :no-typesetting:

   .. method:: trace_variable(mode, callback)

      Register *callback* to be called when the variable is accessed according
      to *mode*.
      *mode* is one of the strings ``'r'``, ``'w'`` or ``'u'``, for read, write
      or unset.
      Return the internal name of the registered callback.
      :meth:`trace` is an alias of :meth:`!trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_add` instead.  This method wraps a Tcl feature that
         was removed in Tcl 9.0.

   .. method:: trace_vdelete(mode, cbname)

      Remove the trace callback named *cbname* registered for *mode* with
      :meth:`trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_remove` instead.  This method wraps a Tcl feature
         that was removed in Tcl 9.0.

   .. method:: trace_vinfo()

      Return a list of ``(mode, cbname)`` pairs for all traces set on the
      variable with :meth:`trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_info` instead.  This method wraps a Tcl feature that
         was removed in Tcl 9.0.


.. class:: StringVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a string.
   The default value is ``''``.

   .. method:: get()

      Return the value of the variable as a :class:`str`.


.. class:: IntVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds an integer.
   The default value is ``0``.

   .. method:: get()

      Return the value of the variable as an :class:`int`.


.. class:: DoubleVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a float.
   The default value is ``0.0``.

   .. method:: get()

      Return the value of the variable as a :class:`float`.

   .. _tkinter-numeric-locale:

   .. note::

      A floating-point value is always parsed with a period (``.``) as the
      decimal separator, but :class:`Spinbox`, :class:`Scale` and
      :class:`ttk.Spinbox <tkinter.ttk.Spinbox>` format it according to the
      ``LC_NUMERIC`` locale.  Under a locale that uses a comma they produce a
      value that :meth:`get` cannot read, raising :exc:`TclError`.  Set
      ``LC_NUMERIC`` to a locale that uses a period (such as ``'C'``) to avoid
      this.


.. class:: BooleanVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a boolean.
   The default value is ``False``.

   .. method:: get()

      Return the value of the variable as a :class:`bool`.
      Raise a :exc:`ValueError` if the value cannot be interpreted as a
      boolean.

   .. method:: initialize(value)
      :no-typesetting:

   .. method:: set(value)

      Set the variable to *value*, converting it to a boolean.
      :meth:`initialize` is an alias of :meth:`!set`.

      .. versionadded:: 3.3
         The *initialize* spelling.


Image classes
^^^^^^^^^^^^^

.. class:: Image(imgtype, name=None, cnf={}, master=None, **kw)

   Base class for Tk images.
   *imgtype* is the Tk image type, one of ``'photo'`` or ``'bitmap'``.
   An image is a named object that can be displayed by widgets through their
   *image* option; deleting all references to the :class:`!Image` object
   deletes the underlying Tk image.
   Usually you create a :class:`PhotoImage` or :class:`BitmapImage` rather than
   an :class:`!Image` directly.

   The image's configuration options are given by *cnf* and *kw* and may be
   queried and changed later with the mapping protocol (using ``image[key]``)
   or with the :meth:`configure` method.

   .. method:: config(**kw)
      :no-typesetting:

   .. method:: configure(**kw)

      Modify one or more configuration options of the image.
      The valid options depend on the image type; see :class:`PhotoImage` and
      :class:`BitmapImage`.
      :meth:`config` is an alias of :meth:`!configure`.

   .. method:: height()

      Return the height of the image, in pixels.

   .. method:: width()

      Return the width of the image, in pixels.

   .. method:: type()

      Return the type of the image, that is the value of *imgtype* with which
      it was created (for example ``'photo'`` or ``'bitmap'``).


.. class:: PhotoImage(name=None, cnf={}, master=None, **kw)

   A full-color image (the Tk ``photo`` image type), stored internally with a
   varying degree of transparency per pixel.
   It can read and write GIF, PPM/PGM and (in Tk 8.6 and later) PNG files, read
   SVG files (in Tk 9.0 and later), and be drawn in widgets.
   Inherits from :class:`Image`.

   The configuration options include *data* (the image contents as a string),
   *file* (the name of a file to read the contents from), *format* (the name of
   the file format handler), *width* and *height* (the size of the image, used
   when building it up piece by piece), *gamma* and *palette*.

   .. method:: blank()

      Blank the image; that is, set the entire image to have no data, so that
      it is displayed as transparent and the background of whatever window it
      is displayed in shows through.

   .. method:: cget(option)

      Return the current value of the configuration option *option*.

   .. method:: copy(*, from_coords=None, zoom=None, subsample=None)

      Return a new :class:`PhotoImage` with a copy of this image.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      ``(x1, y1)`` and ``(x2, y2)`` specify diagonally opposite corners of the
      rectangle.
      If *x2* and *y2* are not specified, they default to the bottom-right
      corner of the source image.
      The pixels copied include the left and top edges of the rectangle but not
      the bottom or right edges.
      If *from_coords* is not given, the whole source image is copied.

      If *zoom* or *subsample* are specified, the image is transformed as in
      the :meth:`zoom` or :meth:`subsample` methods.
      The value must be a single integer or a pair of integers.

      .. versionchanged:: 3.13
         Added the *from_coords*, *zoom* and *subsample* parameters.


   .. method:: copy_replace(sourceImage, *, from_coords=None, to=None, \
                            shrink=False, zoom=None, subsample=None, \
                            compositingrule=None)

      Copy a region from *sourceImage* (which must be a :class:`PhotoImage`)
      into this image, possibly with pixel zooming and/or subsampling.
      If no options are specified, the whole of *sourceImage* is copied into
      this image, starting at coordinates ``(0, 0)``.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      *to* specifies a rectangular sub-region of the destination image to be
      affected.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If *x2* and *y2* are not specified, they default to ``(x1, y1)`` plus the
      size of the source region (after subsampling and zooming, if specified).
      If *x2* and *y2* are specified, the source region is replicated if
      necessary to fill the destination region in a tiled fashion.

      If *shrink* is true, the size of the destination image is reduced, if
      necessary, so that the region being copied into is at the bottom-right
      corner of the image.

      If *zoom* or *subsample* are specified, the image is transformed as in
      the :meth:`zoom` or :meth:`subsample` methods.
      The value must be a single integer or a pair of integers.

      *compositingrule* specifies how transparent pixels in the source image
      are combined with the destination image.
      With ``'overlay'`` (the default), the old contents of the destination
      image remain visible, as if the source image were printed on a piece of
      transparent film and placed over the top of the destination.
      With ``'set'``, the old contents of the destination image are discarded
      and the source image is used as-is.

      .. versionadded:: 3.13


   .. method:: data(format=None, *, from_coords=None, background=None, \
                    grayscale=False)

      Return the image data.

      *format* specifies the name of the image file format handler to use.
      If it is not given, the data is returned as a tuple (one element per row)
      of strings containing space-separated (one element per pixel/column)
      colors in ``#RRGGBB`` format.

      *from_coords* specifies a rectangular region of the image to be returned.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region, including ``(x1, y1)`` and excluding ``(x2, y2)``.
      If *from_coords* is not given, the whole image is returned.

      If *background* is specified, the data does not contain any transparency
      information; in all transparent pixels the color is replaced by the
      specified color.

      If *grayscale* is true, the data does not contain color information; all
      pixel data is transformed into grayscale.

      .. versionadded:: 3.13


   .. method:: get(x, y)

      Return the color of the pixel at coordinates (*x*, *y*) as an
      ``(r, g, b)`` tuple of three integers between 0 and 255, representing the
      red, green and blue components respectively.

   .. method:: put(data, to=None)

      Set pixels of the image to the colors given in *data*, which must be a
      string or a nested sequence of horizontal rows of pixel colors (for
      example ``"{red green} {blue yellow}"``).

      *to* specifies the coordinates of the region of the image into which the
      data are copied.
      It must be a tuple or a list of 2 or 4 integers ``(x1, y1)`` or
      ``(x1, y1, x2, y2)`` giving the top-left corner, and optionally the
      bottom-right corner, of the region.
      The default position is ``(0, 0)``.

   .. method:: read(filename, format=None, *, from_coords=None, to=None, \
                    shrink=False)

      Read image data from the file named *filename* into the image.

      *format* specifies the format of the image data in the file.

      *from_coords* specifies a rectangular sub-region of the image file data
      to be copied to the destination image.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image in the file.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region.
      If *from_coords* is not given, the whole of the image in the file is
      read.

      *to* specifies the coordinates of the top-left corner of the region of
      the image into which the data are read.
      The default is ``(0, 0)``.

      If *shrink* is true, the size of the image is reduced, if necessary, so
      that the region into which the file data are read is at the bottom-right
      corner of the image.

      .. versionadded:: 3.13


   .. method:: subsample(x, y='', *, from_coords=None)

      Return a new :class:`PhotoImage` based on this image but using only every
      *x*-th pixel in the X direction and every *y*-th pixel in the Y
      direction.
      If *y* is not given, it defaults to the same value as *x*.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      .. versionchanged:: 3.13
         Added the *from_coords* parameter.


   .. method:: transparency_get(x, y)

      Return ``True`` if the pixel at coordinates (*x*, *y*) is fully
      transparent, ``False`` otherwise.

      .. versionadded:: 3.8


   .. method:: transparency_set(x, y, boolean)

      Make the pixel at coordinates (*x*, *y*) fully transparent if *boolean*
      is true, fully opaque otherwise.

      .. versionadded:: 3.8


   .. method:: write(filename, format=None, from_coords=None, *, \
                     background=None, grayscale=False)

      Write image data from the image to the file named *filename*.

      *format* specifies the name of the image file format handler to use.
      If it is not given, the format is guessed from the file extension.

      *from_coords* specifies a rectangular region of the image to be written.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region.
      If *from_coords* is not given, the whole image is written.

      If *background* is specified, the data does not contain any transparency
      information; in all transparent pixels the color is replaced by the
      specified color.

      If *grayscale* is true, the data does not contain color information; all
      pixel data is transformed into grayscale.

      .. versionchanged:: 3.13
         Added the *background* and *grayscale* parameters.


   .. method:: zoom(x, y='', *, from_coords=None)

      Return a new :class:`PhotoImage` with this image magnified by a factor of
      *x* in the X direction and *y* in the Y direction.
      If *y* is not given, it defaults to the same value as *x*.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      .. versionchanged:: 3.13
         Added the *from_coords* parameter.



.. class:: BitmapImage(name=None, cnf={}, master=None, **kw)

   A two-color image (the Tk ``bitmap`` image type) created from an X11 bitmap.
   Each pixel displays a foreground color, a background color, or nothing
   (producing a transparent effect).
   Inherits from :class:`Image`.

   The configuration options are *data* or *file* (the source bitmap, given as
   a string in X11 bitmap format or as the name of a file in that format),
   *maskdata* or *maskfile* (the mask bitmap, in the same forms), and
   *foreground* and *background* (the two colors).
   For pixels where the mask is zero the image displays nothing; for other
   pixels it displays the foreground color where the source is one and the
   background color where the source is zero.
   If *background* is set to an empty string, the background pixels are
   transparent.

   :class:`!BitmapImage` has no methods of its own beyond those inherited from
   :class:`Image`.


Other classes
^^^^^^^^^^^^^

.. class:: Event()

   A container for the attributes of an event passed to a callback bound with
   :meth:`Misc.bind`.
   An :class:`!Event` instance has the following attributes, each corresponding
   to a field of the underlying Tk event; depending on the event type, some
   attributes may be set to the string ``'??'`` to indicate that they are not
   meaningful.
   See :ref:`bindings-and-events`.

   .. attribute:: serial

      The serial number of the event.

   .. attribute:: num

      The mouse button that was pressed or released (for button events).

   .. attribute:: focus

      Whether the window has the focus (for ``Enter`` and ``Leave`` events).

   .. attribute:: height
                  width

      The new height and width of the window (for ``Configure`` and ``Expose``
      events).

   .. attribute:: keycode

      The keycode of the key that was pressed or released.

   .. attribute:: state

      The state of the event, as a number (for most events) or a string (for
      ``Visibility`` events).

   .. attribute:: time

      The timestamp of the event, in milliseconds.

   .. attribute:: x
                  y

      The pointer position relative to the widget, in pixels.

   .. attribute:: x_root
                  y_root

      The pointer position relative to the top-left corner of the screen, in
      pixels.

   .. attribute:: char

      The character typed, as a string (for key events).

   .. attribute:: send_event

      ``True`` if the event was sent by another application.

   .. attribute:: keysym

      The symbolic name of the key that was pressed or released.

   .. attribute:: keysym_num

      The numeric value of :attr:`keysym`.

   .. attribute:: type

      The :class:`EventType` of the event.

   .. attribute:: widget

      The widget on which the event occurred.

   .. attribute:: delta

      The amount the mouse wheel was rotated (for ``MouseWheel`` events).

   .. attribute:: user_data

      The data string of a virtual event, as passed to the *data* option of
      :meth:`Misc.event_generate`.
      It is ``'??'`` for non-virtual events.

      .. versionadded:: 3.15

   .. attribute:: detail

      A fixed detail string for ``Enter``, ``Leave``, ``FocusIn``, ``FocusOut``
      and ``ConfigureRequest`` events (see the Tcl/Tk documentation).
      It is ``'??'`` for other events.

      .. versionadded:: 3.15


.. class:: EventType(*values)

   An :class:`enum.StrEnum` enumerating the Tk event types, used as the value
   of :attr:`Event.type`.
   Its members include, among others, ``KeyPress``, ``KeyRelease``,
   ``ButtonPress``, ``ButtonRelease``, ``Motion``, ``Enter``, ``Leave``,
   ``FocusIn``, ``FocusOut``, ``Configure``, ``Map``, ``Unmap``, ``Expose``,
   ``Destroy`` and ``MouseWheel``.

   .. versionadded:: 3.6



.. class:: CallWrapper(func, subst, widget)

   Internal helper that wraps a Python callback so that it can be invoked from
   Tcl.
   *func* is the Python function, *subst* is an optional function that
   pre-processes the Tcl arguments, and *widget* is the widget used for error
   reporting.
   Instances are created automatically by :meth:`Misc.register`; this class is
   not normally used directly.


Module-level functions
^^^^^^^^^^^^^^^^^^^^^^

.. function:: Tcl(screenName=None, baseName=None, className='Tk', useTk=False)

   The :func:`Tcl` function is a factory function which creates an object much
   like that created by the :class:`Tk` class, except that it does not
   initialize the Tk subsystem.
   This is most often useful when driving the Tcl interpreter in an environment
   where one doesn't want to create extraneous toplevel windows, or where one
   cannot (such as Unix/Linux systems without an X server).
   An object created by the :func:`Tcl` object can have a Toplevel window
   created (and the Tk subsystem initialized) by calling its :meth:`~Tk.loadtk`
   method.

.. function:: NoDefaultRoot()

   Inhibit the creation of an implicit default root window.
   Afterwards :mod:`!tkinter` no longer creates a shared default root
   automatically, and operations that rely on one --- such as constructing a
   widget without an explicit *master* --- raise a :exc:`RuntimeError`.
   Call this early in larger applications to make the root window explicit.

.. function:: mainloop(n=0)

   Run the Tk main event loop on the default root window until all windows are
   destroyed.
   Equivalent to calling :meth:`Misc.mainloop` on the default root.

.. function:: getboolean(s)

   Convert the Tcl boolean string *s* (one of ``'1'``, ``'true'``, ``'yes'``,
   ``'on'`` and similar, or their false counterparts) to a Python
   :class:`bool`.
   Raise :exc:`ValueError` for an invalid value.

.. function:: getdouble(s)

   Convert *s* to a floating-point number.
   This is the built-in :class:`float`.

.. function:: getint(s)

   Convert *s* to an integer.
   This is the built-in :class:`int`.

.. function:: image_names()

   Return the names of all existing images in the default root's interpreter.

.. function:: image_types()

   Return the available image types (such as ``'photo'`` and ``'bitmap'``) in
   the default root's interpreter.


.. _tkinter-file-handlers:

File handlers
^^^^^^^^^^^^^

Tk allows you to register and unregister a callback function which will be
called from the Tk mainloop when I/O is possible on a file descriptor.
Only one handler may be registered per file descriptor. Example code::

   import tkinter
   widget = tkinter.Tk()
   mask = tkinter.READABLE | tkinter.WRITABLE
   widget.tk.createfilehandler(file, mask, callback)
   ...
   widget.tk.deletefilehandler(file)

This feature is not available on Windows.

Since you don't know how many bytes are available for reading, you may not
want to use the :class:`~io.BufferedIOBase` or :class:`~io.TextIOBase`
:meth:`~io.BufferedIOBase.read` or :meth:`~io.IOBase.readline` methods,
since these will insist on reading a predefined number of bytes.
For sockets, the :meth:`~socket.socket.recv` or
:meth:`~socket.socket.recvfrom` methods will work fine; for other files,
use raw reads or ``os.read(file.fileno(), maxbytecount)``.


.. method:: Widget.tk.createfilehandler(file, mask, func)

   Registers the file handler callback function *func*. The *file* argument
   may either be an object with a :meth:`~io.IOBase.fileno` method (such as
   a file or socket object), or an integer file descriptor. The *mask*
   argument is an ORed combination of any of the three constants below.
   The callback is called as follows::

      callback(file, mask)


.. method:: Widget.tk.deletefilehandler(file)

   Unregisters a file handler.


.. data:: READABLE
          WRITABLE
          EXCEPTION

   Constants used in the *mask* arguments.


Constants
^^^^^^^^^

The following symbolic constants are available in both the :mod:`!tkinter`
and :mod:`!tkinter.constants` namespaces.

.. data:: TRUE
          YES
          ON

   Truthy values, all equal to the integer ``1``.

.. data:: FALSE
          NO
          OFF

   Falsy values, all equal to the integer ``0``.

.. data:: N
          S
          E
          W
          NE
          NW
          SE
          SW
          NS
          EW
          NSEW
          CENTER

   Compass directions (``'n'``, ``'s'``, ``'e'``, ``'w'`` and the diagonals and
   edges) plus ``CENTER`` (``'center'``), used as values for the *anchor* and
   *sticky* options and by methods such as :meth:`Misc.grid_anchor`.

.. data:: LEFT
          RIGHT
          TOP
          BOTTOM

   Sides for the *side* option of the packer (see :meth:`Pack.pack_configure`).

.. data:: X
          Y
          BOTH
          NONE

   Values for the *fill* option of the packer: ``'x'``, ``'y'``, ``'both'`` or
   ``'none'``.

.. data:: RAISED
          SUNKEN
          FLAT
          RIDGE
          GROOVE
          SOLID

   Values for the *relief* option, which controls a widget's 3-D border.

.. data:: HORIZONTAL
          VERTICAL

   Values for the *orient* option of widgets such as :class:`Scale`,
   :class:`Scrollbar` and :class:`PanedWindow`.

.. data:: CHAR
          WORD

   Values for the *wrap* option of the :class:`Text` widget, selecting line
   wrapping on character or word boundaries.

.. data:: BASELINE

   The text-alignment value ``'baseline'``.

.. data:: INSIDE
          OUTSIDE

   Values for the *bordermode* option of the placer (see
   :meth:`Place.place_configure`).

.. data:: INSERT
          CURRENT
          END
          ANCHOR
          SEL
          SEL_FIRST
          SEL_LAST

   Symbolic indices used by the :class:`Text`, :class:`Entry`, :class:`Listbox`
   and :class:`Canvas` widgets, such as ``'insert'`` (the insertion cursor),
   ``'current'``, ``'end'``, ``'anchor'`` and the bounds of the selection
   (``'sel.first'`` and ``'sel.last'``).

.. data:: ALL

   The special tag ``'all'``, which matches every item of a :class:`Canvas` or
   every character of a :class:`Text` (for example ``canvas.delete(ALL)``).

.. data:: NORMAL
          DISABLED
          ACTIVE
          HIDDEN

   Values for the *state* option of various widgets and items.

.. data:: CASCADE
          CHECKBUTTON
          COMMAND
          RADIOBUTTON
          SEPARATOR

   Menu entry types, used as the *itemType* argument of :meth:`Menu.add` and
   :meth:`Menu.insert`.

.. data:: SINGLE
          BROWSE
          MULTIPLE
          EXTENDED

   Values for the *selectmode* option of the :class:`Listbox` widget.

.. data:: PIESLICE
          CHORD
          ARC

   Values for the *style* option of :class:`Canvas` arc items.

.. data:: BUTT
          PROJECTING
          ROUND
          BEVEL
          MITER

   Values for the *capstyle* (``'butt'``, ``'projecting'``, ``'round'``) and
   *joinstyle* (``'round'``, ``'bevel'``, ``'miter'``) options of
   :class:`Canvas` line items.

.. data:: FIRST
          LAST

   Values for the *arrow* option of :class:`Canvas` line items, indicating
   which ends have arrowheads.

.. data:: MOVETO
          SCROLL

   The first argument passed by a :class:`Scrollbar` to the :meth:`XView.xview`
   or :meth:`YView.yview` method of the scrolled widget.

.. data:: UNITS
          PAGES

   Values for the *what* argument of :meth:`XView.xview_scroll` and
   :meth:`YView.yview_scroll`.

.. data:: UNDERLINE
          NUMERIC
          DOTBOX

   Other option values: ``'underline'``, ``'numeric'`` and ``'dotbox'``.

----

   .. method:: grid_content(row=None, column=None)

      Same as :meth:`Misc.grid_content`.

      .. versionadded:: 3.15


.. class:: XView()

   Mix-in providing the horizontal-scrolling interface shared by widgets such
   as :class:`Entry`, :class:`Canvas`, :class:`Listbox`, :class:`Text` and
   :class:`Spinbox`.
   A widget's :meth:`xview` method is registered as the *command* of a
   horizontal :class:`Scrollbar`.

   .. method:: xview(*args)

      Query or change the horizontal position of the view.
      With no arguments, return a tuple ``(first, last)`` of two fractions
      between 0 and 1 giving the portion of the document that is currently
      visible.
      Otherwise the arguments are passed to the Tk ``xview`` widget command and
      are usually generated by a scrollbar; :meth:`xview_moveto` and
      :meth:`xview_scroll` provide a more convenient interface.

   .. method:: xview_moveto(fraction)

      Adjust the view so that *fraction* of the total width of the document is
      off-screen to the left.
      *fraction* is a number between 0 and 1.

   .. method:: xview_scroll(number, what)

      Shift the view left or right by *number* units.
      *what* is either ``'units'`` or ``'pages'``; a negative *number* scrolls
      left and a positive one scrolls right.
      The :class:`Text` widget accepts also ``'pixels'``,
      and then *number* can be a screen distance, such as ``'1i'``.


.. class:: YView()

   Mix-in providing the vertical-scrolling interface shared by widgets such as
   :class:`Canvas`, :class:`Listbox` and :class:`Text`.
   A widget's :meth:`yview` method is registered as the *command* of a vertical
   :class:`Scrollbar`.

   .. method:: yview(*args)

      Query or change the vertical position of the view.
      With no arguments, return a tuple ``(first, last)`` of two fractions
      between 0 and 1 giving the portion of the document that is currently
      visible.
      Otherwise the arguments are passed to the Tk ``yview`` widget command,
      usually generated by a scrollbar; :meth:`yview_moveto` and
      :meth:`yview_scroll` provide a more convenient interface.

   .. method:: yview_moveto(fraction)

      Adjust the view so that *fraction* of the total height of the document is
      off-screen above the top.
      *fraction* is a number between 0 and 1.

   .. method:: yview_scroll(number, what)

      Shift the view up or down by *number* units.
      *what* is either ``'units'`` or ``'pages'``; a negative *number* scrolls
      up and a positive one scrolls down.
      The :class:`Text` widget accepts also ``'pixels'``,
      and then *number* can be a screen distance, such as ``'1i'``.


.. class:: BaseWidget(master, widgetName, cnf={}, kw={}, extra=())

   Internal base class for all widgets.
   It inherits from :class:`Misc` and adds the machinery that creates the
   underlying Tk widget; application code normally uses :class:`Widget` or a
   concrete widget class rather than instantiating :class:`!BaseWidget`
   directly.

   .. method:: destroy()

      Destroy this widget and all of its children, removing the corresponding
      Tk widgets and deleting the associated Tcl commands.


.. class:: Widget(master, widgetName, cnf={}, kw={}, extra=())

   Internal base class for the standard widgets.
   It combines :class:`BaseWidget` with the geometry-manager mix-ins
   :class:`Pack`, :class:`Place` and :class:`Grid`, so that every widget can be
   managed by any of the three geometry managers.
   The concrete widget classes (:class:`Button`, :class:`Label`, and so on)
   derive from :class:`!Widget`.


Toplevel widgets
^^^^^^^^^^^^^^^^

.. class:: Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)

   Construct a toplevel Tk widget, which is usually the main window of an
   application, and initialize a Tcl interpreter for this widget.  Each
   instance has its own associated Tcl interpreter.
   Inherits from :class:`Misc` and :class:`Wm`.

   To create a Tcl interpreter without initializing the Tk subsystem, use the
   :func:`Tcl` factory function instead.

   The :class:`Tk` class is typically instantiated using all default values.
   However, the following keyword arguments are currently recognized:

   *screenName*
      When given (as a string), sets the :envvar:`DISPLAY` environment
      variable. (X11 only)
   *baseName*
      Name of the profile file.  By default, *baseName* is derived from the
      program name (``sys.argv[0]``).
   *className*
      Name of the widget class.  Used as a profile file and also as the name
      with which Tcl is invoked (*argv0* in *interp*).
   *useTk*
      If ``True``, initialize the Tk subsystem.  The :func:`tkinter.Tcl() <Tcl>`
      function sets this to ``False``.
   *sync*
      If ``True``, execute all X server commands synchronously, so that errors
      are reported immediately.  Can be used for debugging. (X11 only)
   *use*
      Specifies the *id* of the window in which to embed the application,
      instead of it being created as an independent toplevel window. *id* must
      be specified in the same way as the value for the -use option for
      toplevel widgets (that is, it has a form like that returned by
      :meth:`~Misc.winfo_id`).

      Note that on some platforms this will only work correctly if *id* refers
      to a Tk frame or toplevel that has its -container option enabled.

   :class:`Tk` reads and interprets profile files, named
   :file:`.{className}.tcl` and :file:`.{baseName}.tcl`, into the Tcl
   interpreter and calls :func:`exec` on the contents of
   :file:`.{className}.py` and :file:`.{baseName}.py`.  The path for the
   profile files is the :envvar:`HOME` environment variable or, if that
   isn't defined, then :data:`os.curdir`.

   .. note::

      On Windows, creating a Tcl interpreter (by instantiating :class:`Tk` or
      calling :func:`Tcl`) sets the :envvar:`HOME` environment variable for
      the process, if it is not already set, to ``%HOMEDRIVE%%HOMEPATH%`` (or
      :envvar:`USERPROFILE`, or ``c:\``).  This is done by Tcl and can affect
      other code that reads :envvar:`HOME`.

   .. attribute:: tk

      The Tk application object created by instantiating :class:`Tk`.  This
      provides access to the Tcl interpreter.  Each widget that is attached
      the same instance of :class:`Tk` has the same value for its :attr:`tk`
      attribute.

   .. attribute:: master

      The widget object that contains this widget.
      For :class:`Tk`, the :attr:`!master` is :const:`None` because it is the
      main window.
      The terms *master* and *parent* are similar and sometimes used
      interchangeably as argument names; however, calling
      :meth:`~Misc.winfo_parent` returns a string of the widget name whereas
      :attr:`!master` returns the object.
      *parent*/*child* reflects the tree-like relationship while *master* (or
      *container*)/*content* reflects the container structure.

   .. attribute:: children

      The immediate descendants of this widget as a :class:`dict` with the
      child widget names as the keys and the child instance objects as the
      values.

   .. method:: destroy()

      Destroy this and all descendant widgets and, for the main window, end the
      connection to the underlying Tcl interpreter.

   .. method:: loadtk()

      Finish loading and initializing the Tk subsystem.
      This is needed only when the interpreter was created without Tk (for
      example through :func:`Tcl`); it is called automatically when *useTk* is
      true.

   .. method:: readprofile(baseName, className)

      Read and source the user's profile files :file:`.{className}.tcl` and
      :file:`.{baseName}.tcl` into the Tcl interpreter, and execute the
      corresponding :file:`.{className}.py` and :file:`.{baseName}.py` files.
      This is called during initialization; see the description of the
      constructor above.

   .. method:: report_callback_exception(exc, val, tb)

      Report a callback exception.
      This is called when an exception propagates out of a Tkinter callback;
      *exc*, *val* and *tb* are the exception type, value and traceback as
      returned by :func:`sys.exc_info`.
      The default implementation prints a traceback to :data:`sys.stderr`.
      It can be overridden to customize error handling, for example to display
      the traceback in a dialog.


.. class:: Toplevel(master=None, cnf={}, **kw)

   A :class:`!Toplevel` widget is a top-level window, similar to a
   :class:`Frame` except that its X parent is the root window of a screen
   rather than its logical parent.
   Its primary purpose is to serve as a container for dialog boxes and other
   collections of widgets; its only visible features are its background and an
   optional 3-D border.
   Notable options include *menu*, which installs a :class:`Menu` as the
   window's menubar.
   Inherits from :class:`BaseWidget` and :class:`Wm`, so a toplevel is managed
   by the window manager.
   Refer to the Tk ``toplevel`` manual page for the full list of options.


Widget classes
^^^^^^^^^^^^^^

.. class:: Button(master=None, cnf={}, **kw)

   A :class:`!Button` widget displays a textual string, bitmap or image and
   invokes a command when the user presses it (by clicking mouse button 1 over
   the button or, when the button has focus, by pressing the space key).
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a button accepts the options
   documented in the Tk ``button`` manual page, such as *command* (the callback
   invoked when the button is pressed), *textvariable*, *state* and *default*.

   .. method:: invoke()

      Invoke the command associated with the button, if there is one, and
      return its result, or an empty string if no command is associated with
      the button.
      This is ignored if the button's state is ``disabled``.

   .. method:: flash()

      Flash the button by redisplaying it several times, alternating between
      the active and normal colors.
      At the end of the flash the button is left in the same normal or active
      state as when the method was called.
      This is ignored if the button's state is ``disabled``.


.. class:: Canvas(master=None, cnf={}, **kw)

   A :class:`!Canvas` widget implements structured graphics.
   It displays any number of *items*, such as arcs, lines, ovals, polygons,
   rectangles, text, bitmaps, images and embedded windows, which may be drawn,
   moved, re-colored and bound to events.
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``canvas`` manual page for the full list of widget and item
   options.

   Each item has a unique integer *id*, assigned when it is created, and zero
   or more string *tags*.
   A tag is an arbitrary string that does not have the form of an integer; the
   same tag may be shared by many items, which makes tags convenient for
   grouping items.
   The special tag ``'all'`` matches every item in the canvas, and
   ``'current'`` matches the topmost item under the mouse pointer.
   Most methods take a *tagOrId* argument that may be an integer id naming a
   single item, or a tag naming zero or more items; as described in the Tk
   ``canvas`` manual page, a tag may also be a logical expression of tags
   combined with the operators ``&&``, ``||``, ``^``, ``!`` and parentheses.
   When a method that operates on a single item is given a *tagOrId* matching
   several items, it normally uses the lowest matching item in the display
   list.

   The items are kept in a *display list* that determines drawing order: items
   later in the list are drawn on top of earlier ones.
   A newly created item is placed at the top of the list; the order can be
   changed with :meth:`tag_raise` and :meth:`tag_lower`.

   .. method:: create_arc(*args, **kw)
               create_bitmap(*args, **kw)
               create_image(*args, **kw)
               create_line(*args, **kw)
               create_oval(*args, **kw)
               create_polygon(*args, **kw)
               create_rectangle(*args, **kw)
               create_text(*args, **kw)
               create_window(*args, **kw)

      Create a new item of the corresponding type and return its integer id.
      Each method is called as ``create_TYPE(coord..., **options)``: the
      leading positional arguments give the coordinates that define the item
      (as separate numbers, as a single sequence of numbers, or as coordinate
      pairs), and the keyword arguments set item-specific options.
      Coordinates and screen distances may be given as numbers (interpreted as
      pixels) or as strings with a unit suffix (``'m'``, ``'c'``, ``'i'`` or
      ``'p'`` for millimetres, centimetres, inches or printer's points), but
      are always stored and returned in pixels.

      The item types are: ``arc`` (an arc-shaped region that is a section of an
      oval, defined by two diagonally opposite corners ``x1, y1, x2, y2`` of
      the enclosing rectangle); ``bitmap`` (a two-color bitmap positioned at a
      point ``x, y``); ``image`` (a Tk image positioned at a point ``x, y``);
      ``line`` (a line or curve through the points ``x1, y1, ..., xn, yn``);
      ``oval`` (a circle or ellipse inscribed in the rectangle
      ``x1, y1, x2, y2``); ``polygon`` (a closed polygon through the points
      ``x1, y1, ..., xn, yn``); ``rectangle`` (a rectangle with corners
      ``x1, y1, x2, y2``); ``text`` (a string of text positioned at a point
      ``x, y``); and ``window`` (a child widget embedded in the canvas at a
      point ``x, y``, specified with the *window* option).

      Most item types accept a common set of *standard item options*, plus a
      few options specific to each type.
      Option names are passed as keyword arguments, without the leading
      hyphen.

      The standard item options are:

      *fill*
         The color used to fill the item's interior, or to draw a *line*
         item or the characters of a *text* item.
         An empty string (the default for all types except *line* and *text*)
         leaves the item unfilled.

      *outline*
         The color used to draw the item's outline.
         An empty string draws no outline.

      *width*
         The width of the outline, defaulting to ``1.0``.
         Has no effect if *outline* is empty.

      *dash*
         A dash pattern for the outline, given either as a sequence of
         segment lengths in pixels or as a string of the characters
         ``'.'``, ``','``, ``'-'``, ``'_'`` and space.
         An empty pattern (the default) draws a solid outline.

      *dashoffset*
         The starting offset in pixels into the *dash* pattern.
         Ignored if there is no *dash* pattern.

      *stipple*
         A bitmap used as a stipple pattern when filling the item.
         Only well supported on X11.

      *outlinestipple*
         A bitmap used as a stipple pattern when drawing the outline.
         Has no effect if *outline* is empty.

      *offset*, *outlineoffset*
         The offset of the fill and outline stipple patterns, given as
         ``'x,y'`` or as a side such as ``'n'``, ``'se'`` or ``'center'``.
         Stipple offsets are only supported on X11.

      *state*
         Overrides the canvas state for this item; one of ``'normal'``,
         ``'disabled'`` or ``'hidden'``.

      *tags*
         A single tag or a sequence of tags to associate with the item,
         replacing any existing tags.

      Many of these options have *active...* and *disabled...* variants
      (such as *activefill*, *disabledfill*, *activewidth*, *disableddash*,
      *activeoutline*, *disabledstipple*) that override the base option when
      the item is the active item (under the mouse pointer) or is in the
      disabled state.

      The following item types support additional options.

      For ``arc`` items:

      *start*
         The start of the arc's angular range, in degrees measured
         counter-clockwise from the 3-o'clock position.

      *extent*
         The size of the angular range, in degrees counter-clockwise from
         *start*.

      *style*
         How the arc is drawn: ``'pieslice'`` (the default), ``'chord'`` or
         ``'arc'``.

      For ``line`` items:

      *arrow*
         Where to draw arrowheads: ``'none'`` (the default), ``'first'``,
         ``'last'`` or ``'both'``.

      *arrowshape*
         A sequence of three distances describing the shape of the
         arrowheads.

      *capstyle*
         How line ends are drawn: ``'butt'`` (the default), ``'projecting'``
         or ``'round'``.

      *joinstyle*
         How line vertices are drawn: ``'round'`` (the default), ``'bevel'``
         or ``'miter'``.

      *smooth*
         The smoothing method: a false value (the default) for no smoothing,
         or ``'true'``/``'bezier'`` or ``'raw'`` to draw the line as a curve.

      *splinesteps*
         The number of line segments approximating each spline when
         *smooth* is enabled.

      For ``polygon`` items:

      *joinstyle*, *smooth*, *splinesteps*
         As for ``line`` items, applied to the polygon's outline.

      For ``text`` items:

      *text*
         The string to display; newline characters start new lines.

      *font*
         The font used for the text.

      *justify*
         How lines are justified: ``'left'`` (the default), ``'right'`` or
         ``'center'``.

      *anchor*
         How the text is positioned relative to its point, defaulting to
         ``'center'``.

      *width*
         The maximum line length; if non-zero, lines are wrapped at spaces.

      *angle*
         How many degrees to rotate the text counter-clockwise about its
         positioning point, from ``0.0`` to ``360.0`` (default ``0.0``).

      *underline*
         The index of a character to underline, or ``-1`` for none.

      For ``bitmap`` items:

      *bitmap*
         The bitmap to display.

      *anchor*
         How the bitmap is positioned relative to its point.

      *background*, *foreground*
         The colors used for the bitmap's ``0`` and ``1`` pixels; an empty
         *background* makes the ``0`` pixels transparent.
         Both have *active...* and *disabled...* variants, and *bitmap* has
         *activebitmap* and *disabledbitmap* variants.

      For ``image`` items:

      *image*
         The Tk image to display, previously created with the image
         protocols.

      *anchor*
         How the image is positioned relative to its point.

      Both options have *active...* and *disabled...* variants
      (*activeimage*, *disabledimage*) used in the active and disabled
      states.

      For ``window`` items:

      *window*
         The widget to embed; it must be a child of the canvas or of one of
         its ancestors, and may not be a top-level window.

      *anchor*
         How the window is positioned relative to its point.

      *width*, *height*
         The size to assign to the window; if zero (the default), the window
         is given its requested size.

      ``oval`` and ``rectangle`` items have no type-specific options; they
      use only the standard item options.

      .. note::

         Tk 8.6 added the *angle* option for ``text`` items.

   .. method:: coords(tagOrId)
               coords(tagOrId, coordList, /)
               coords(tagOrId, /, *coordList)

      Query or modify the coordinates of an item.
      With only *tagOrId*, return a list of the floating-point coordinates of
      the item given by *tagOrId* (the first matching item if it matches
      several).
      Given new coordinates, replace the coordinates of that item with them;
      like the ``create_*`` methods, the coordinates may be given as separate
      numbers, as a single sequence, or as coordinate pairs.
      The returned coordinates are always in pixels, regardless of the units
      used to specify them; for rectangles, ovals and arcs they are ordered
      left, top, right, bottom.

      .. versionchanged:: 3.12
         The arguments are now flattened: the coordinates may be given as
         separate arguments, as a single sequence, or grouped in pairs, like
         the ``create_*`` methods.


   .. method:: move(tagOrId, xAmount, yAmount, /)

      Move each of the items given by *tagOrId* in the canvas coordinate space
      by adding *xAmount* to every x-coordinate and *yAmount* to every
      y-coordinate of the item.

   .. method:: moveto(tagOrId, x='', y='')

      Move the items given by *tagOrId* so that the first coordinate pair (the
      upper-left corner of the bounding box) of the lowest matching item is at
      position (*x*, *y*).
      *x* or *y* may be an empty string, in which case the corresponding
      coordinate is unchanged.
      All matching items keep their positions relative to each other.

      .. versionadded:: 3.8


   .. method:: scale(tagOrId, xOrigin, yOrigin, xScale, yScale, /)

      Rescale the coordinates of all items given by *tagOrId* in canvas
      coordinate space.
      Each x-coordinate is adjusted so that its distance from *xOrigin* changes
      by a factor of *xScale*, and each y-coordinate so that its distance from
      *yOrigin* changes by a factor of *yScale* (a factor of ``1.0`` leaves the
      coordinate unchanged).

   .. method:: delete(*tagOrIds)

      Delete each of the items given by the *tagOrIds* arguments.

   .. method:: dchars(tagOrId, first, /)
               dchars(tagOrId, first, last, /)

      Delete from each of the items given by *tagOrId* the characters (for text
      items) or coordinates (for line and polygon items) in the range from
      *first* to *last* inclusive; *last* defaults to *first*.
      Items that do not support indexing ignore this operation.

   .. method:: insert(tagOrId, beforeThis, string, /)

      Insert *string* into each of the items given by *tagOrId* just before the
      character or coordinate whose index is *beforeThis*.
      For line and polygon items *string* must be a valid sequence of
      coordinates.

   .. method:: itemcget(tagOrId, option)

      Return the current value of the configuration option *option* for the
      item given by *tagOrId* (the lowest matching item if it matches several).
      This is like :meth:`~Misc.cget` but applies to an individual item.

   .. method:: itemconfig(tagOrId, cnf=None, **kw)
      :no-typesetting:

   .. method:: itemconfigure(tagOrId, cnf=None, **kw)

      Query or modify the configuration options of the items given by
      *tagOrId*.
      This mirrors :meth:`~Misc.configure`, except that it applies to
      individual items rather than to the canvas as a whole.
      With no options, it returns a dictionary describing the current options
      of the first matching item; otherwise it sets the given options on every
      matching item.
      The legal options are those accepted by the corresponding ``create_*``
      method.
      :meth:`itemconfig` is an alias of :meth:`!itemconfigure`.

   .. method:: type(tagOrId)

      Return the type of the item given by *tagOrId* (the first matching item
      if it matches several), such as ``'rectangle'`` or ``'text'``, or
      ``None`` if *tagOrId* does not match any item.

   .. method:: gettags(tagOrId, /)

      Return a tuple of the tags associated with the item given by *tagOrId*
      (the first matching item in display-list order if it matches several).
      Return an empty tuple if no item matches or the item has no tags.

   .. method:: dtag(tagOrId, /)
               dtag(tagOrId, tagToDelete, /)

      Remove the tag *tagToDelete* (which defaults to *tagOrId*) from each of
      the items given by *tagOrId*.
      Items that do not have that tag are unaffected.

   .. method:: addtag(newtag, searchSpec, /, *args)

      Add the tag *newtag* to each item selected by the search specification
      *searchSpec* (and any further *args*).
      *searchSpec* is one of ``'above'``, ``'all'``, ``'below'``,
      ``'closest'``, ``'enclosed'``, ``'overlapping'`` or ``'withtag'``; the
      ``addtag_*`` methods below are convenient wrappers that supply each of
      these forms.

   .. method:: addtag_above(newtag, tagOrId)

      Add the tag *newtag* to the item just above (after) *tagOrId* in the
      display list.

   .. method:: addtag_all(newtag)

      Add the tag *newtag* to all items in the canvas.

   .. method:: addtag_below(newtag, tagOrId)

      Add the tag *newtag* to the item just below (before) *tagOrId* in the
      display list.

   .. method:: addtag_closest(newtag, x, y, halo=None, start=None)

      Add the tag *newtag* to the item closest to the point (*x*, *y*).
      If *halo* is given, any item within that distance of the point is treated
      as overlapping it.
      If *start* is given (a tag or id), select the topmost closest item that
      lies below *start* in the display list, which can be used to step through
      all the closest items.

   .. method:: addtag_enclosed(newtag, x1, y1, x2, y2)

      Add the tag *newtag* to every item completely enclosed within the
      rectangle (*x1*, *y1*, *x2*, *y2*), where *x1* <= *x2* and *y1* <= *y2*.

   .. method:: addtag_overlapping(newtag, x1, y1, x2, y2)

      Add the tag *newtag* to every item that overlaps or is enclosed within
      the rectangle (*x1*, *y1*, *x2*, *y2*), where *x1* <= *x2* and *y1* <=
      *y2*.

   .. method:: addtag_withtag(newtag, tagOrId)

      Add the tag *newtag* to every item given by *tagOrId*.

   .. method:: find(searchSpec, /, *args)

      Return a tuple of the ids of all items selected by the search
      specification *searchSpec* (and any further *args*), in stacking order
      with the lowest item first.
      The search specification has any of the forms accepted by :meth:`addtag`.
      The ``find_*`` methods below are more convenient wrappers around it.

   .. method:: find_above(tagOrId)

      Return a tuple containing the id of the item just above *tagOrId* in the
      display list.

   .. method:: find_all()

      Return a tuple of the ids of all items in the canvas, in stacking order.

   .. method:: find_below(tagOrId)

      Return a tuple containing the id of the item just below *tagOrId* in the
      display list.

   .. method:: find_closest(x, y, halo=None, start=None)

      Return a tuple containing the id of the item closest to the point (*x*,
      *y*).
      *halo* and *start* are interpreted as for :meth:`addtag_closest`.

   .. method:: find_enclosed(x1, y1, x2, y2)

      Return a tuple of the ids of all items completely enclosed within the
      rectangle (*x1*, *y1*, *x2*, *y2*).

   .. method:: find_overlapping(x1, y1, x2, y2)

      Return a tuple of the ids of all items that overlap or are enclosed
      within the rectangle (*x1*, *y1*, *x2*, *y2*).

   .. method:: find_withtag(tagOrId)

      Return a tuple of the ids of all items given by *tagOrId*.

   .. method:: lift(tagOrId, aboveThis=None, /)
      :no-typesetting:

   .. method:: tkraise(tagOrId, aboveThis=None, /)
      :no-typesetting:

   .. method:: tag_raise(tagOrId, aboveThis=None, /)

      Move all items given by *tagOrId* to a new position in the display list
      just above the item given by *aboveThis*, or to the top of the display
      list if *aboveThis* is omitted.
      When several items are moved their relative order is preserved.
      This has no effect on embedded window items, whose stacking order is
      controlled by :meth:`Misc.tkraise` and :meth:`Misc.lower` instead.
      :meth:`lift` and :meth:`tkraise` are aliases of :meth:`!tag_raise`.

   .. method:: lower(tagOrId, belowThis=None, /)
      :no-typesetting:

   .. method:: tag_lower(tagOrId, belowThis=None, /)

      Move all items given by *tagOrId* to a new position in the display list
      just below the item given by *belowThis*, or to the bottom of the display
      list if *belowThis* is omitted.
      When several items are moved their relative order is preserved.
      This has no effect on embedded window items.
      :meth:`lower` is an alias of :meth:`!tag_lower`.

      .. note::

         On a :class:`Canvas`, :meth:`tkraise`/:meth:`lift` and :meth:`lower`
         restack canvas items,
         shadowing the inherited :meth:`Misc.tkraise`/:meth:`Misc.lift` and
         :meth:`Misc.lower` methods that restack the widget itself,
         which are therefore not available.

   .. method:: tag_bind(tagOrId, sequence=None, func=None, add=None)

      Bind the callback *func* to the event *sequence* for all items given by
      *tagOrId*, so that *func* is invoked whenever that event occurs for one
      of the items.
      This is like :meth:`Widget.bind <Misc.bind>` but operates on canvas items
      rather than on whole widgets; only mouse, keyboard and virtual events may
      be bound.
      Mouse events are directed to the current item and keyboard events to the
      focus item (see :meth:`focus`).
      If *add* is true the new binding is added to any existing bindings for
      the same sequence, rather than replacing them.
      Return the identifier of the bound function, which can be passed to
      :meth:`tag_unbind`.

   .. method:: tag_unbind(tagOrId, sequence, funcid=None)

      Remove for all items given by *tagOrId* the binding for the event
      *sequence*.
      If *funcid* is given, only that callback (as returned by
      :meth:`tag_bind`) is unbound and deregistered.

      .. versionchanged:: 3.13
         If *funcid* is given, only that callback is unbound.


   .. method:: bbox(tagOrId, /, *tagOrIds)

      Return a 4-tuple ``(x1, y1, x2, y2)`` giving an approximate bounding box,
      in pixels, that encloses all the items given by *tagOrId* and any further
      *tagOrIds*.
      The result may overestimate the true bounding box by a few pixels.
      Return ``None`` if no item matches or the matching items have nothing to
      display.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: canvasx(screenx, gridspacing=None)

      Given a window x-coordinate *screenx*, return the canvas x-coordinate
      displayed at that location.
      If *gridspacing* is given, the result is rounded to the nearest multiple
      of *gridspacing* units.

   .. method:: canvasy(screeny, gridspacing=None)

      Given a window y-coordinate *screeny*, return the canvas y-coordinate
      displayed at that location.
      If *gridspacing* is given, the result is rounded to the nearest multiple
      of *gridspacing* units.

   .. method:: focus()
               focus(tagOrId, /)

      With *tagOrId*, set the keyboard focus for the canvas to the first item
      given by *tagOrId* that supports the insertion cursor; the focus is left
      unchanged if no such item exists.
      If *tagOrId* is an empty string, reset the focus so that no item has it.
      With no argument, return the id of the item that currently has the focus,
      or an empty string if none does.
      An item only displays the insertion cursor when both it is the focus item
      and its canvas has the input focus.

      This shadows the inherited :meth:`!Misc.focus`;
      use :meth:`~Misc.focus_set` to focus the widget itself.

   .. method:: icursor(tagOrId, index, /)

      Set the insertion cursor of the items given by *tagOrId* to just before
      the character given by *index*.
      Items that do not support an insertion cursor are unaffected.
      The cursor is only displayed when the item has the focus, but its
      position may be set at any time.

   .. method:: index(tagOrId, index, /)

      Return as an integer the numerical index within *tagOrId* corresponding
      to *index*, which is a textual description of a position (for text items
      an index into the characters, for line and polygon items an index into
      the coordinates).
      If *tagOrId* matches several items, the first one that supports indexing
      is used.

   .. method:: select_adjust(tagOrId, index)

      Adjust the end of the selection in *tagOrId* nearest to *index* so that
      it is at *index*, and make the other end the anchor point for future
      :meth:`select_to` calls.
      If the selection is not currently in *tagOrId*, this behaves like
      :meth:`select_to`.

   .. method:: select_clear()

      Clear the selection if it is in this canvas; otherwise do nothing.

   .. method:: select_from(tagOrId, index)

      Set the selection anchor point to just before the character given by
      *index* in the item given by *tagOrId*.
      This does not change the selection itself; it sets the fixed end for
      future :meth:`select_to` calls.

   .. method:: select_item()

      Return the id of the item that holds the selection, or ``None`` if the
      selection is not in this canvas.
      Unlike :meth:`find` and the ``find_*`` methods, this returns the id as a
      string rather than an integer.

   .. method:: select_to(tagOrId, index)

      Set the selection to the characters of *tagOrId* between the selection
      anchor point and *index*, inclusive of *index*.
      The anchor point is the one set by the most recent :meth:`select_adjust`
      or :meth:`select_from` call.

   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y, gain=10)

      Scroll the canvas by *gain* times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events in the widget, producing
      the effect of dragging the canvas at high speed through its window.

   .. method:: postscript(cnf={}, **kw)

      Generate a PostScript (Encapsulated PostScript, version 3.0)
      representation of part or all of the canvas.
      If the *file* or *channel* option is given, the PostScript is written
      there and an empty string is returned; otherwise it is returned as a
      string.
      By default only the area currently visible in the window is generated, so
      it is usually necessary either to call :meth:`~Misc.update` first or to
      use the *width* and *height* options.
      Supported options include *colormap*, *colormode*, *file*, *fontmap*,
      *height*, *pageanchor*, *pageheight*, *pagewidth*, *pagex*, *pagey*,
      *rotate*, *width*, *x* and *y*.


.. class:: Checkbutton(master=None, cnf={}, **kw)

   A :class:`!Checkbutton` widget displays a textual string, bitmap or image
   together with a square indicator, and toggles a boolean selection when
   pressed.
   It has all the behavior of a simple button and, in addition, can be
   selected: when selected the indicator is drawn with a check mark and the
   associated variable is set to the ``onvalue``, and when deselected the
   indicator is drawn empty and the variable is set to the ``offvalue``.
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a checkbutton accepts the
   options documented in the Tk ``checkbutton`` manual page, such as
   *variable*, *onvalue*, *offvalue* and *command*.

   .. method:: invoke()

      Do just what would happen if the user pressed the checkbutton with the
      mouse: toggle the selection state of the button and invoke the associated
      command, if there is one.
      Return the result of the command, or an empty string if no command is
      associated with the checkbutton.
      This is ignored if the checkbutton's state is ``disabled``.

   .. method:: select()

      Select the checkbutton and set the associated variable to its
      ``onvalue``.

   .. method:: deselect()

      Deselect the checkbutton and set the associated variable to its
      ``offvalue``.

   .. method:: toggle()

      Toggle the selection state of the button, redisplaying it and modifying
      its associated variable to reflect the new state.

   .. method:: flash()

      Flash the checkbutton by redisplaying it several times, alternating
      between the active and normal colors.
      At the end of the flash the checkbutton is left in the same normal or
      active state as when the method was called.
      This is ignored if the checkbutton's state is ``disabled``.


.. class:: Entry(master=None, cnf={}, **kw)

   An :class:`!Entry` widget displays a single line of text and lets the user
   edit it.
   Inherits from :class:`Widget` and :class:`XView`; since entries can hold
   strings too long to fit in the window, they support horizontal scrolling
   through :meth:`~XView.xview`.

   In addition to the standard widget options, an entry accepts the options
   documented in the Tk ``entry`` manual page.
   Notable ones are *textvariable* (the name of a variable kept in sync with
   the entry's contents), *show* (if set, each character is displayed as the
   given character rather than its true value, useful for password entry),
   *validate* and *validatecommand* (which together let a callback accept or
   reject edits), and *state* (one of ``'normal'``, ``'disabled'`` or
   ``'readonly'``).

   Many of the methods below take an *index* argument that selects a character
   in the entry's string.
   As described in the Tk ``entry`` manual page, *index* may be a number
   (counting from 0), ``'insert'`` (the character just after the insertion
   cursor), ``'end'`` (just after the last character), ``'anchor'`` (the
   selection anchor point), ``'sel.first'`` and ``'sel.last'`` (the ends of the
   selection), or ``@x`` (the character covering pixel x-coordinate *x* in the
   window).
   Out-of-range indices are rounded to the nearest legal value.

   .. method:: delete(first, last=None)

      Delete the characters from index *first* up to but not including index
      *last*.
      If *last* is omitted, only the single character at *first* is deleted.

   .. method:: get()

      Return the entry's current string.

   .. method:: insert(index, string)

      Insert *string* just before the character given by *index*.

   .. method:: icursor(index)

      Arrange for the insertion cursor to be displayed just before the
      character given by *index*.

   .. method:: index(index)

      Return the numerical index corresponding to *index*.

   .. method:: select_adjust(index)
      :no-typesetting:

   .. method:: selection_adjust(index)

      Locate the end of the selection nearest to the character given by
      *index*, and adjust that end to be at *index* (including but not going
      beyond it); the other end becomes the anchor point for future
      :meth:`selection_to` calls.
      If there is no selection in the entry, a new one is created between
      *index* and the most recent anchor point, inclusive.
      :meth:`select_adjust` is an alias of :meth:`!selection_adjust`.

   .. method:: select_clear()
      :no-typesetting:

   .. method:: selection_clear()

      Clear the selection if it is currently in this widget.
      If the selection is not in this widget the method has no effect.
      :meth:`select_clear` is an alias of :meth:`!selection_clear`.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on an :class:`Entry`.

   .. method:: select_from(index)
      :no-typesetting:

   .. method:: selection_from(index)

      Set the selection anchor point to just before the character given by
      *index*, without changing the selection.
      :meth:`select_from` is an alias of :meth:`!selection_from`.

   .. method:: select_present()
      :no-typesetting:

   .. method:: selection_present()

      Return ``True`` if there are characters selected in the entry, ``False``
      otherwise.
      :meth:`select_present` is an alias of :meth:`!selection_present`.

   .. method:: select_range(start, end)
      :no-typesetting:

   .. method:: selection_range(start, end)

      Set the selection to include the characters starting with the one indexed
      by *start* and ending with the one just before *end*.
      If *end* refers to the same character as *start* or an earlier one, the
      selection is cleared.
      :meth:`select_range` is an alias of :meth:`!selection_range`.

   .. method:: select_to(index)
      :no-typesetting:

   .. method:: selection_to(index)

      Set the selection between the anchor point and *index*: if *index* is
      before the anchor point, the selection runs from *index* up to but not
      including the anchor; if *index* is after it, from the anchor up to but
      not including *index*; if they coincide, nothing happens.
      The anchor point is the one set by the most recent :meth:`selection_from`
      or :meth:`selection_adjust` call.
      If there is no selection in the entry, a new one is created using the
      most recent anchor point.
      :meth:`select_to` is an alias of :meth:`!selection_to`.

   .. method:: scan_mark(x)

      Record *x* and the current view in the entry window, for use with later
      :meth:`scan_dragto` calls.
      Typically associated with a mouse button press in the widget.

   .. method:: scan_dragto(x)

      Compute the difference between *x* and the *x* given to the last
      :meth:`scan_mark` call, and adjust the view left or right by 10 times
      that difference.
      Typically associated with mouse motion events, to produce the effect of
      dragging the entry at high speed through the window.


.. class:: Frame(master=None, cnf={}, **kw)

   A :class:`!Frame` widget is a simple container.
   Its primary purpose is to act as a spacer or container for complex window
   layouts; its only features are its background and an optional 3-D border to
   make the frame appear raised or sunken.
   Inherits from :class:`Widget`.
   Refer to the Tk ``frame`` manual page for the full list of options.


.. class:: Label(master=None, cnf={}, **kw)

   A :class:`!Label` widget displays a non-interactive textual string, bitmap
   or image.
   The displayed text is set with the *text* option or linked to a variable
   through *textvariable*, and an image can be shown using the *image* option.
   Text must all be in a single font but may occupy multiple lines, and one
   character may be underlined with the *underline* option.
   Inherits from :class:`Widget`.
   Refer to the Tk ``label`` manual page for the full list of options.


.. class:: LabelFrame(master=None, cnf={}, **kw)

   A :class:`!LabelFrame` widget is a container that has the features of a
   :class:`Frame` plus the ability to display a label.
   The label text is set with the *text* option and positioned with
   *labelanchor*, or an arbitrary widget may be used as the label by giving it
   as the *labelwidget* option.
   Inherits from :class:`Widget`.
   Refer to the Tk ``labelframe`` manual page for the full list of options.


.. class:: Listbox(master=None, cnf={}, **kw)

   A :class:`!Listbox` widget displays a list of single-line text items, one
   per line, of which the user can select one or more.
   The way the selection behaves is governed by the *selectmode* option, which
   is one of ``browse`` (the default; at most one item, which may be dragged
   with the mouse), ``single`` (at most one item), ``multiple`` (any number of
   items, toggled individually), or ``extended`` (any number of items,
   including discontiguous ranges, selected by clicking and dragging).
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``listbox`` manual page for the full list of options.

   Many of the methods take an *index* argument identifying a particular item.
   As described in the Tk ``listbox`` manual page, *index* may be a numeric
   index (counting from 0 at the top), ``'active'`` (the item with the location
   cursor, set with :meth:`activate`), ``'anchor'`` (the selection anchor, set
   with :meth:`selection_anchor`), ``'end'`` (the last item, or for
   :meth:`index` and :meth:`insert` the position just after it), or ``@x,y``
   (the item covering pixel coordinates *x*, *y* in the listbox window).
   Arguments named *first* and *last* are indices of the same forms.

   .. method:: insert(index, *elements)

      Insert the given *elements* as new items just before the item given by
      *index*.
      If *index* is ``'end'``, the new items are appended to the end of the
      list.

   .. method:: delete(first, last=None)

      Delete the items in the range from *first* to *last* inclusive.
      If *last* is omitted, it defaults to *first*, so that a single item is
      deleted.

   .. method:: get(first, last=None)

      If *last* is omitted, return the contents of the item given by *first*,
      or an empty string if *first* refers to a non-existent item.
      If *last* is given, return a tuple of all the items in the range from
      *first* to *last* inclusive.

   .. method:: size()

      Return the total number of items in the listbox.

      This shadows the inherited :meth:`!Misc.size`;
      use :meth:`~Misc.grid_size` for the grid size.

   .. method:: index(index)

      Return the integer index value corresponding to *index*, or ``None`` if
      *index* is out of range.
      If *index* is ``'end'``, the result is a count of the number of items in
      the listbox (not the index of the last item).

   .. method:: bbox(index)

      Return a tuple ``(x, y, width, height)`` describing the bounding box, in
      pixels relative to the widget, of the text of the item given by *index*.
      Return ``None`` if no part of that item is visible on the screen, or if
      *index* refers to a non-existent item; if the item is only partly
      visible, the result still gives the full area of the item, including the
      parts that are not visible.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: nearest(y)

      Given a y-coordinate within the listbox window, return the index of the
      visible item nearest to that y-coordinate.

   .. method:: see(index)

      Adjust the view so that the item given by *index* is visible.
      If the item is already visible the method has no effect; if it is near an
      edge of the window the listbox scrolls just enough to bring it into view
      at that edge, otherwise the listbox scrolls to center the item.

   .. method:: activate(index)

      Set the active item to the one given by *index*.
      If *index* is outside the range of items, the closest item is activated
      instead.
      The active item is drawn as specified by the *activestyle* option when
      the widget has the input focus, and its index may be retrieved with the
      ``'active'`` index.

   .. method:: curselection()

      Return a tuple containing the numerical indices of all of the items that
      are currently selected, or an empty tuple if no items are selected.

   .. method:: select_anchor(index)
      :no-typesetting:

   .. method:: selection_anchor(index)

      Set the selection anchor to the item given by *index*.
      If *index* refers to a non-existent item, the closest item is used.
      The selection anchor is the end of the selection that is fixed while
      dragging out a selection with the mouse, and may afterwards be referred
      to with the ``'anchor'`` index.
      :meth:`select_anchor` is an alias of :meth:`!selection_anchor`.

   .. method:: select_clear(first, last=None)
      :no-typesetting:

   .. method:: selection_clear(first, last=None)

      Deselect any of the items in the range from *first* to *last* inclusive
      that are selected.
      The selection state of items outside this range is not changed.
      :meth:`select_clear` is an alias of :meth:`!selection_clear`.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on a :class:`Listbox`.

   .. method:: select_includes(index)
      :no-typesetting:

   .. method:: selection_includes(index)

      Return ``True`` if the item given by *index* is currently selected,
      ``False`` otherwise.
      :meth:`select_includes` is an alias of :meth:`!selection_includes`.

   .. method:: select_set(first, last=None)
      :no-typesetting:

   .. method:: selection_set(first, last=None)

      Select all of the items in the range from *first* to *last* inclusive,
      without affecting the selection state of items outside that range.
      :meth:`select_set` is an alias of :meth:`!selection_set`.

   .. method:: itemcget(index, option)

      Return the current value of the configuration option *option* for the
      item given by *index*.

   .. method:: itemconfig(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: itemconfigure(index, cnf=None, **kw)

      Query or modify the configuration options of the item given by *index*.
      This mirrors :meth:`~Misc.configure`, except that it applies to an
      individual item rather than to the listbox as a whole.
      With no options, it returns a dictionary describing the current options
      of the item; otherwise it sets the given options.
      The supported item options are *background*, *foreground*,
      *selectbackground* and *selectforeground*.
      :meth:`itemconfig` is an alias of :meth:`!itemconfigure`.

   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y)

      Scroll the listbox by 10 times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events in the widget, producing
      the effect of dragging the list at high speed through the window.


.. class:: Menu(master=None, cnf={}, **kw)

   A :class:`!Menu` widget displays a column of entries, each of which may be a
   command, a checkbutton, a radiobutton, a cascade (which posts an associated
   submenu) or a separator.
   Menus are used as the menubar of a toplevel window, as pulldown menus posted
   from a cascade entry or menubutton, and as popup menus.
   Inherits from :class:`Widget`.

   Many of the entry methods take an *index* argument that selects which entry
   to operate on.
   As described in the Tk ``menu`` manual page, *index* may be a numeric index
   (counting from 0 at the top), ``'active'`` (the currently active entry),
   ``'end'`` or ``'last'`` (the bottommost entry), ``'none'`` (no entry at all,
   written ``{}`` in Tcl), ``@y`` (the entry covering pixel y-coordinate *y* in
   the menu window), or a pattern matched against the labels of the entries
   from the top down.

   .. method:: add(itemType, cnf={}, **kw)

      Add a new entry to the bottom of the menu.
      *itemType* is one of ``'command'``, ``'cascade'``, ``'checkbutton'``,
      ``'radiobutton'`` or ``'separator'`` and determines the type of the new
      entry; the remaining options configure it.
      The :meth:`!add_command`, :meth:`!add_cascade`, :meth:`!add_checkbutton`,
      :meth:`!add_radiobutton` and :meth:`!add_separator` convenience methods
      call this method with the corresponding *itemType*.

      The entry is configured by the following options, although not every
      option applies to every entry type (a separator accepts none of them):

      *label*
         The text to display in the entry.

      *command*
         The function to call when the entry is invoked (command, checkbutton
         and radiobutton entries).

      *accelerator*
         A string displayed at the right of the entry to advertise an
         accelerator keystroke; it does not itself create the binding.

      *underline*
         The index of a character in the label to underline for keyboard
         traversal.

      *state*
         One of ``'normal'``, ``'active'`` or ``'disabled'``.

      *image*
         An image to display instead of, or together with, the text label.

      *compound*
         Where to show the image relative to the text: ``'none'`` (the
         default), ``'text'``, ``'image'``, ``'top'``, ``'bottom'``, ``'left'``
         or ``'right'``.

      *bitmap*
         A bitmap to display instead of the text label.

      *font*
         The font to use for the text.

      *background*, *foreground*
         The entry's background and foreground colors in its normal state
         (ignored on macOS).

      *activebackground*, *activeforeground*
         The background and foreground colors used when the entry is active
         (ignored on macOS).

      *columnbreak*
         If true, the entry starts a new column instead of being placed below
         the previous entry.

      *hidemargin*
         If true, the standard margin around the entry is omitted, which is
         useful when a menu is used as a palette.

      *menu*
         The submenu posted by a cascade entry; it must be a child of this
         menu.

      *variable*
         The variable associated with a checkbutton or radiobutton entry.

      *onvalue*, *offvalue*
         The values stored in *variable* when a checkbutton entry is selected
         or cleared.

      *value*
         The value stored in *variable* when a radiobutton entry is selected.

      *indicatoron*
         Whether to display the indicator of a checkbutton or radiobutton
         entry.

      *selectcolor*
         The color of the indicator of a checkbutton or radiobutton entry when
         it is selected.

      *selectimage*
         The image displayed when a checkbutton or radiobutton entry is
         selected and *image* is also given.

   .. method:: add_cascade(cnf={}, **kw)

      Add a new cascade entry to the bottom of the menu.
      A cascade entry has an associated submenu, given by its *menu* option,
      which must be a child of this menu; posting the entry posts the submenu
      next to it.

   .. method:: add_checkbutton(cnf={}, **kw)

      Add a new checkbutton entry to the bottom of the menu.
      When invoked, a checkbutton entry toggles between its *onvalue* and
      *offvalue*, storing the result in its associated *variable*, and displays
      an indicator showing whether it is selected.

   .. method:: add_command(cnf={}, **kw)

      Add a new command entry to the bottom of the menu.
      A command entry behaves much like a button: when it is invoked, the
      callback given by its *command* option is called.

   .. method:: add_radiobutton(cnf={}, **kw)

      Add a new radiobutton entry to the bottom of the menu.
      Radiobutton entries sharing the same *variable* form a group of which
      only one may be selected at a time; selecting an entry stores its *value*
      in the variable.

   .. method:: add_separator(cnf={}, **kw)

      Add a separator to the bottom of the menu.
      A separator is displayed as a horizontal dividing line and cannot be
      activated or invoked.

   .. method:: insert(index, itemType, cnf={}, **kw)

      Same as :meth:`add`, except that the new entry is inserted just before
      the entry given by *index* instead of being appended to the end of the
      menu.
      *itemType* is one of ``'command'``, ``'cascade'``, ``'checkbutton'``,
      ``'radiobutton'`` or ``'separator'``.
      The :meth:`!insert_command`, :meth:`!insert_cascade`,
      :meth:`!insert_checkbutton`, :meth:`!insert_radiobutton` and
      :meth:`!insert_separator` convenience methods call this method with the
      corresponding *itemType*.

   .. method:: insert_cascade(index, cnf={}, **kw)

      Insert a new cascade entry before the entry given by *index* (see
      :meth:`add_cascade`).

   .. method:: insert_checkbutton(index, cnf={}, **kw)

      Insert a new checkbutton entry before the entry given by *index* (see
      :meth:`add_checkbutton`).

   .. method:: insert_command(index, cnf={}, **kw)

      Insert a new command entry before the entry given by *index* (see
      :meth:`add_command`).

   .. method:: insert_radiobutton(index, cnf={}, **kw)

      Insert a new radiobutton entry before the entry given by *index* (see
      :meth:`add_radiobutton`).

   .. method:: insert_separator(index, cnf={}, **kw)

      Insert a separator before the entry given by *index* (see
      :meth:`add_separator`).

   .. method:: delete(index1, index2=None)

      Delete all of the menu entries between *index1* and *index2* inclusive.
      If *index2* is omitted, it defaults to *index1*, so that a single entry
      is deleted.
      Attempts to delete a tear-off entry are ignored; remove it by changing
      the *tearoff* option instead.

   .. method:: entrycget(index, option)

      Return the current value of the configuration option *option* for the
      entry given by *index*.

   .. method:: entryconfig(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: entryconfigure(index, cnf=None, **kw)

      Query or modify the configuration options of the entry given by *index*.
      This mirrors :meth:`~Misc.configure`, except that it applies to an
      individual entry rather than to the menu as a whole.
      With no options, it returns a dictionary describing the current options
      of the entry; otherwise it sets the given options.
      The supported options are those accepted by :meth:`add` for the entry's
      type.
      :meth:`entryconfig` is an alias of :meth:`!entryconfigure`.

   .. method:: index(index)

      Return the numerical index corresponding to *index*, or ``None`` if
      *index* selects no entry.

   .. method:: type(index)

      Return the type of the entry given by *index*: one of ``'command'``,
      ``'cascade'``, ``'checkbutton'``, ``'radiobutton'``, ``'separator'`` or
      ``'tearoff'`` (for the tear-off entry).

   .. method:: activate(index)

      Make the entry given by *index* the active entry, redisplaying it with
      its active colors, and deactivate any previously active entry.
      If *index* selects no entry, or the selected entry is disabled, the menu
      ends up with no active entry.

   .. method:: invoke(index)

      Invoke the action of the entry given by *index*, as if it had been
      clicked.
      Nothing happens if the entry is disabled.
      If the entry has a *command* associated with it, the result of that
      command is returned; otherwise the result is an empty string.

   .. method:: post(x, y)

      Display the menu on the screen at the root-window coordinates *x* and
      *y*, adjusting them if necessary so that the whole menu is visible.
      If the *postcommand* option has been specified, it is evaluated before
      the menu is posted.

   .. method:: tk_popup(x, y, entry='')

      Post the menu as a popup at the root-window coordinates *x* and *y*.
      If *entry* is given, the menu is positioned so that this entry is
      displayed under the pointer.

   .. method:: unpost()

      Unmap the menu so that it is no longer displayed, also unposting any
      posted lower-level cascaded submenu.
      This has no effect on Windows and macOS, which manage the unposting of
      menus themselves.

   .. method:: xposition(index)

      Return the x-coordinate, within the menu window, of the leftmost pixel of
      the entry given by *index*.

      .. versionadded:: 3.3

   .. method:: yposition(index)

      Return the y-coordinate, within the menu window, of the topmost pixel of
      the entry given by *index*.


.. class:: Menubutton(master=None, cnf={}, **kw)

   A :class:`!Menubutton` widget displays a textual string, bitmap or image and
   posts an associated :class:`Menu`, given by its *menu* option, when the user
   presses it.
   Like a :class:`Label` it can show *text*, a *textvariable*, or an *image*,
   and the *direction* option controls where the menu appears relative to the
   button.
   Inherits from :class:`Widget`.
   Refer to the Tk ``menubutton`` manual page for the full list of options.


.. class:: Message(master=None, cnf={}, **kw)

   A :class:`!Message` widget displays a non-interactive textual string, given
   by the *text* option or linked to a variable through *textvariable*.
   Unlike a :class:`Label`, it breaks the string into multiple lines in order
   to produce a given aspect ratio, choosing line breaks at word boundaries,
   and it can justify the text left, centered or right.
   Inherits from :class:`Widget`.
   Refer to the Tk ``message`` manual page for the full list of options.


.. class:: OptionMenu(master, variable, value, *values, **kwargs)

   A helper subclass of :class:`Menubutton` that displays a pop-up menu of
   mutually exclusive choices.
   *variable* is a :class:`Variable` kept in sync with the selection, *value*
   is the initial choice, and *values* are the remaining menu entries.
   The keyword argument *command* may be given a callback that is invoked with
   the selected value, and the keyword argument *name* sets the Tk widget name.

   .. method:: destroy()

      Destroy the widget, also cleaning up the associated pop-up menu.

   .. versionchanged:: 3.14
      Added support for the *name* keyword argument.



.. class:: PanedWindow(master=None, cnf={}, **kw)

   A :class:`!PanedWindow` is a geometry-manager widget that arranges any
   number of child *panes* in a row (when *orient* is ``'horizontal'``) or a
   column (when *orient* is ``'vertical'``).
   Each pane holds one widget, and each pair of adjacent panes is separated by
   a movable *sash* that the user can drag with the mouse to resize the widgets
   on either side of it.
   Inherits from :class:`Widget`.

   The *orient* option selects the layout direction, *sashwidth* sets the width
   of each sash and *sashrelief* its relief.
   When *showhandle* is true a small handle is drawn on each sash that the user
   can grab to drag it.
   Refer to the Tk ``panedwindow`` manual page for the full list of options.

   .. method:: add(child, **kw)

      Add *child* to the panedwindow as a new pane, placed after any existing
      panes.
      The keyword arguments specify per-pane management options for *child*;
      they may be any of the options accepted by :meth:`paneconfigure`.

   .. method:: forget(child)
      :no-typesetting:

   .. method:: remove(child)

      Remove the pane containing *child* from the panedwindow.
      All geometry management options for *child* are forgotten.
      :meth:`forget` is an alias of :meth:`!remove`.
      This shadows the inherited geometry-manager :meth:`!forget`;
      use :meth:`~Pack.pack_forget`, :meth:`~Grid.grid_forget` or
      :meth:`~Place.place_forget` to remove the widget itself from its manager.

   .. method:: panes()

      Return a tuple of the widgets managed by the panedwindow, one per pane,
      in order.

   .. method:: panecget(child, option)

      Return the current value of the management option *option* for the pane
      containing *child*.
      *option* may be any value allowed by :meth:`paneconfigure`.

   .. method:: paneconfig(tagOrId, cnf=None, **kw)
      :no-typesetting:

   .. method:: paneconfigure(tagOrId, cnf=None, **kw)

      Query or modify the management options of the pane containing the widget
      *tagOrId*.
      With no options, it returns a dictionary describing all of the available
      options for the pane; given a single option name as a string, it returns
      a description of that one option; otherwise it sets the given options.
      The supported options include *after* and *before* (insert the pane after
      or before another managed window), *height* and *width* (the outer
      dimensions of the window, including any border), *minsize* (the minimum
      size in the paned dimension), *padx* and *pady* (extra space to leave on
      each side of the window), *sticky* (position or stretch the window within
      an oversized pane, using a string of the characters ``n``, ``s``, ``e``
      and ``w``), *hide* (hide the pane while keeping it in the list of panes)
      and *stretch* (how extra space is allocated to the pane: one of
      ``'always'``, ``'first'``, ``'last'``, ``'middle'`` or ``'never'``).
      :meth:`paneconfig` is an alias of :meth:`!paneconfigure`.

   .. method:: identify(x, y)

      Identify the panedwindow component underneath the point given by *x* and
      *y*, in window coordinates.
      If the point is over a sash or a sash handle, the result is a two-element
      tuple containing the index of the sash or handle and a word indicating
      whether it is over a sash or a handle, such as ``(0, 'sash')`` or
      ``(2, 'handle')``.
      If the point is over any other part of the panedwindow, the result is an
      empty string.

   .. method:: sash(*args)

      Query or change the position of the sashes in the panedwindow.
      This is a thin wrapper around the Tk ``sash`` subcommand; the convenience
      methods :meth:`sash_coord`, :meth:`sash_mark` and :meth:`sash_place`
      should normally be used instead.

   .. method:: sash_coord(index)

      Return the current x and y coordinate pair for the sash given by *index*,
      which must be an integer between 0 and one less than the number of panes
      in the panedwindow.
      The coordinates returned are those of the top left corner of the region
      containing the sash.

   .. method:: sash_mark(index)

      Record the current mouse position for the sash given by *index*, for use
      together with later sash-drag operations to move the sash.

   .. method:: sash_place(index, x, y)

      Place the sash given by *index* at the coordinates *x* and *y*.

   .. method:: proxy(*args)

      Query or change the position of the sash proxy, the "ghost" sash shown
      while a sash is being dragged with non-opaque resizing.
      This is a thin wrapper around the Tk ``proxy`` subcommand; the
      convenience methods :meth:`proxy_coord`, :meth:`proxy_forget` and
      :meth:`proxy_place` should normally be used instead.

   .. method:: proxy_coord()

      Return a tuple containing the x and y coordinates of the most recent
      proxy location.

   .. method:: proxy_forget()

      Remove the proxy from the display.

   .. method:: proxy_place(x, y)

      Place the proxy at the coordinates *x* and *y*.


.. class:: Radiobutton(master=None, cnf={}, **kw)

   A :class:`!Radiobutton` widget displays a textual string, bitmap or image
   together with a diamond or circular indicator, and selects one choice out of
   several.
   It has all the behavior of a simple button and, in addition, can be
   selected: typically several radiobuttons share a single *variable*, and
   selecting one sets that variable to the radiobutton's *value*; each
   radiobutton also monitors the variable and automatically selects or
   deselects itself when the variable changes.
   Inherits from :class:`Widget`.
   In addition to the standard widget options, a radiobutton accepts the
   options documented in the Tk ``radiobutton`` manual page, such as
   *variable*, *value* and *command*.

   .. method:: invoke()

      Do just what would happen if the user pressed the radiobutton with the
      mouse: select the button and invoke the associated command, if there is
      one.
      Return the result of the command, or an empty string if no command is
      associated with the radiobutton.
      This is ignored if the radiobutton's state is ``disabled``.

   .. method:: select()

      Select the radiobutton and set the associated variable to the value
      corresponding to this widget.

   .. method:: deselect()

      Deselect the radiobutton and set the associated variable to an empty
      string.
      If this radiobutton was not currently selected, this has no effect.

   .. method:: flash()

      Flash the radiobutton by redisplaying it several times, alternating
      between the active and normal colors.
      At the end of the flash the radiobutton is left in the same normal or
      active state as when the method was called.
      This is ignored if the radiobutton's state is ``disabled``.


.. class:: Scale(master=None, cnf={}, **kw)

   A :class:`!Scale` widget lets the user select a numerical value by moving a
   slider along a trough.
   It can be oriented vertically or horizontally and can optionally display a
   label and the current value.
   Inherits from :class:`Widget`.

   In addition to the standard widget options, a scale accepts the options
   documented in the Tk ``scale`` manual page, such as *from_*, *to*,
   *resolution*, *orient*, *tickinterval*, *variable* and *command*.
   As elsewhere in :mod:`!tkinter`, the leading ``-`` of the Tk option name is
   dropped; *from* is spelled ``from_`` because :keyword:`from` is a Python
   keyword.

   With a non-integer *resolution*, see :ref:`numeric values and the locale
   <tkinter-numeric-locale>`.

   .. method:: get()

      Return the current value of the scale.
      The result is an integer if the scale's *resolution* yields whole
      numbers, and a float otherwise.

   .. method:: set(value)

      Set the scale to *value*, moving the slider accordingly.
      This has no effect if the scale is disabled.

   .. method:: coords(value=None)

      Return a tuple ``(x, y)`` giving the pixel coordinates, relative to the
      widget, of the point on the centerline of the trough that corresponds to
      *value*.
      If *value* is omitted, the scale's current value is used.

   .. method:: identify(x, y)

      Return a string describing the part of the scale at the pixel coordinates
      *x*, *y*: ``'slider'``, ``'trough1'`` (the part of the trough above or to
      the left of the slider), ``'trough2'`` (below or to the right of the
      slider), or an empty string if the point is not over any of these
      elements.


.. class:: Scrollbar(master=None, cnf={}, **kw)

   A :class:`!Scrollbar` widget displays a slider and two arrows that let the
   user scroll an associated widget, such as a :class:`Listbox`, :class:`Text`,
   :class:`Canvas` or :class:`Entry`.
   It is connected to the scrolled widget by setting that widget's
   *xscrollcommand* or *yscrollcommand* option to the scrollbar's :meth:`set`
   method, and the scrollbar's *command* option to the scrolled widget's
   :meth:`~XView.xview` or :meth:`~YView.yview` method.
   Inherits from :class:`Widget`.

   .. method:: get()

      Return the current scrollbar settings as a tuple ``(first, last)`` of two
      fractions between 0 and 1, describing the portion of the document that is
      currently visible, as last passed to :meth:`set`.

   .. method:: set(first, last)

      Set the scrollbar.
      *first* and *last* are fractions between 0 and 1 giving the positions of
      the start and end of the visible portion of the associated document.
      This method is normally registered as the scrolled widget's
      *xscrollcommand* or *yscrollcommand* and called by that widget.

   .. method:: activate(index=None)

      Mark the element *index* (one of ``'arrow1'``, ``'slider'`` or
      ``'arrow2'``) as active, displaying it according to the
      *activebackground* and *activerelief* options.
      If *index* is omitted, return the name of the currently active element,
      or ``None`` if no element is active.

      .. versionchanged:: 3.5
         The *index* argument is now optional.

   .. method:: delta(deltax, deltay)

      Return a float indicating the fractional change in the scrollbar setting
      that corresponds to moving the slider by *deltax* pixels horizontally
      (for horizontal scrollbars) or *deltay* pixels vertically (for vertical
      scrollbars).

   .. method:: fraction(x, y)

      Return a float between 0 and 1 indicating where the point at pixel
      coordinates *x*, *y* lies in the trough: 0 corresponds to the top or left
      of the trough and 1 to the bottom or right.

   .. method:: identify(x, y)

      Return the name of the element under the pixel coordinates *x*, *y* (such
      as ``'arrow1'``), or an empty string if the point does not lie in any
      element of the scrollbar.


.. class:: Spinbox(master=None, cnf={}, **kw)

   A :class:`!Spinbox` widget is an :class:`Entry`-like widget with a pair of
   up/down arrow buttons that let the user step through a range of values in
   addition to editing the value directly.
   The set of values may be a numeric range given by the *from_*, *to* and
   *increment* options, or an explicit list of strings given by the *values*
   option (which takes precedence over the range).
   Each time an arrow is invoked the *command* callback, if any, is called; the
   boolean *wrap* option controls whether stepping past either end of the range
   wraps around to the other end;
   the *format* option specifies how numeric values are formatted;
   and the *validate* option enables validation of the entered text.
   Inherits from :class:`Widget` and :class:`XView`.

   With a non-integer *increment*, see :ref:`numeric values and the locale
   <tkinter-numeric-locale>`.

   Many of the methods take an *index* argument identifying a character in the
   spinbox's string.
   As described in the Tk ``spinbox`` manual page, *index* may be a numeric
   index (counting from 0), ``'anchor'`` (the selection anchor point),
   ``'end'`` (just after the last character), ``'insert'`` (the character just
   after the insertion cursor), ``'sel.first'`` or ``'sel.last'`` (the ends of
   the selection), or ``@x`` (the character covering pixel x-coordinate *x* in
   the window).

   .. method:: get()

      Return the spinbox's string.

   .. method:: insert(index, s)

      Insert the characters of the string *s* just before the character given
      by *index*.

   .. method:: delete(first, last=None)

      Delete one or more characters of the spinbox.
      *first* is the index of the first character to delete, and *last* is the
      index of the character just after the last one to delete.
      If *last* is omitted, a single character at *first* is deleted.

   .. method:: icursor(index)

      Arrange for the insertion cursor to be displayed just before the
      character given by *index*.

   .. method:: index(index)

      Return the numerical index corresponding to *index*, as a string.

   .. method:: bbox(index)

      Return a tuple of four integers ``(x, y, width, height)`` describing the
      bounding box of the character given by *index*.
      *x* and *y* are the pixel coordinates of the upper-left corner of the
      character relative to the widget, and *width* and *height* are its size
      in pixels.
      The bounding box may refer to a region outside the visible area of the
      window.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: identify(x, y)

      Return the name of the window element at the pixel coordinates *x*, *y*:
      one of ``'buttondown'``, ``'buttonup'``, ``'entry'`` or ``'none'``.

   .. method:: invoke(element)

      Invoke the spin button given by *element*, either ``'buttonup'`` or
      ``'buttondown'``, triggering the action associated with it.

   .. method:: scan(*args)

      A thin wrapper around the Tk ``scan`` widget subcommand, used to
      implement fast dragging of the view: ``scan('mark', x)`` records *x* and
      the current view, and ``scan('dragto', x)`` adjusts the view relative to
      that mark.
      The :meth:`scan_mark` and :meth:`scan_dragto` methods wrap the two forms.

   .. method:: scan_mark(x)

      Record *x* and the current view in the spinbox window, for use with a
      later :meth:`scan_dragto` call.
      This is typically associated with a mouse button press in the widget.

   .. method:: scan_dragto(x)

      Adjust the view by 10 times the difference between *x* and the *x* passed
      to the last :meth:`scan_mark` call.
      This is typically associated with mouse motion events, producing the
      effect of dragging the spinbox at high speed through the window.

   .. method:: selection(*args)

      A thin wrapper around the Tk ``selection`` widget subcommand, used to
      adjust the selection within the spinbox.
      It has several forms depending on the first argument, such as
      ``selection('adjust', index)``, ``selection('clear')``,
      ``selection('element', ?elem?)``, ``selection('from', index)``,
      ``selection('present')``, ``selection('range', start, end)`` and
      ``selection('to', index)``.
      The :meth:`selection_adjust`, :meth:`selection_clear`,
      :meth:`selection_element`, :meth:`selection_from`,
      :meth:`selection_present`, :meth:`selection_range` and
      :meth:`selection_to` methods wrap these forms.

   .. method:: selection_adjust(index)

      Locate the end of the selection nearest to the character given by *index*
      and adjust that end of the selection to be at *index* (including but not
      going beyond *index*).
      The other end becomes the anchor point for future :meth:`selection_to`
      calls.
      If the selection is not currently in the spinbox, a new selection is
      created to include the characters between *index* and the most recent
      anchor point, inclusive.

   .. method:: selection_clear()

      Clear the selection if it is currently in this widget.
      If the selection is not in this widget, the method has no effect.

      .. note::

         This shadows the inherited :meth:`Misc.selection_clear`,
         which clears the X selection;
         that method is not available on a :class:`Spinbox`.

   .. method:: selection_element(element=None)

      Set or get the currently selected element.
      If *element* (one of ``'buttonup'``, ``'buttondown'`` or ``'none'``) is
      given, that spin button is selected and displayed depressed; otherwise
      the name of the currently selected element is returned.

   .. method:: selection_from(index)

      Set the selection anchor point to just before the character given by
      *index*, without changing the selection itself.

      .. versionadded:: 3.8


   .. method:: selection_present()

      Return ``True`` if there are characters selected in the spinbox,
      ``False`` otherwise.

      .. versionadded:: 3.8


   .. method:: selection_range(start, end)

      Set the selection to include the characters starting with the one indexed
      by *start* and ending with the one just before *end*.
      If *end* refers to the same character as *start* or an earlier one, the
      selection is cleared.

      .. versionadded:: 3.8


   .. method:: selection_to(index)

      Set the selection between *index* and the anchor point.
      If *index* is before the anchor point, the selection runs from *index* up
      to but not including the anchor point; if it is after, the selection runs
      from the anchor point up to but not including *index*; if it is the same,
      nothing happens.
      The anchor point is the one set by the most recent :meth:`selection_from`
      or :meth:`selection_adjust` call.
      If the selection is not in this widget, a new selection is created using
      the most recent anchor point.

      .. versionadded:: 3.8



.. class:: Text(master=None, cnf={}, **kw)

   A :class:`!Text` widget displays and edits multi-line text.
   Portions of the text may be styled with **tags**, particular positions may
   be annotated with floating **marks**, and arbitrary images and other widgets
   may be embedded in the text.
   The widget also provides an unlimited undo/redo mechanism and supports peer
   widgets that share the same underlying data.
   Inherits from :class:`Widget`, :class:`XView` and :class:`YView`, so the
   view can be scrolled horizontally and vertically with :meth:`~XView.xview`
   and :meth:`~YView.yview`.
   Refer to the Tk ``text`` manual page for the full list of options.

   Most of the methods take one or more *index* arguments that identify a
   position within the text.
   As described in the Tk ``text`` manual page, an index is a string consisting
   of a base, optionally followed by one or more modifiers.
   The base may be ``'line.char'`` (line *line*, character *char*, where lines
   are counted from 1 and characters within a line from 0; ``'line.end'``
   refers to the newline ending the line), ``'end'`` (the position just after
   the last newline), the name of a mark, ``'tag.first'`` or ``'tag.last'``
   (the first character tagged with *tag*, or the position just after the last
   such character), the name of an embedded image or window, or ``@x,y`` (the
   character covering pixel coordinates *x*, *y* in the widget).
   A modifier such as ``'+5 chars'``, ``'-3 lines'``, ``'linestart'``,
   ``'lineend'``, ``'wordstart'`` or ``'wordend'`` adjusts the index relative
   to its base; several modifiers may be combined and are applied from left to
   right, for example ``'insert wordstart - 1 c'``.

   .. method:: insert(index, chars, *args)

      Insert the string *chars* just before the character at *index* (if
      *index* is ``'end'``, just before the final newline).
      By default the new text inherits any tags present on both sides of the
      insertion point.
      If *args* is given, it consists of alternating *tagList*, *chars* values:
      the preceding *chars* receives exactly the tags listed (a tag list may be
      a single tag name or a sequence of names), overriding the surrounding
      tags.

   .. method:: delete(index1, index2=None)

      Delete the range of characters from *index1* up to but not including
      *index2*.
      If *index2* is omitted, the single character at *index1* is deleted.
      The widget always keeps a newline as its last character, so a deletion
      that would remove it is adjusted accordingly.

   .. method:: replace(index1, index2, chars, *args)

      Replace the range of characters from *index1* up to but not including
      *index2* with *chars*.
      This is equivalent to a :meth:`delete` followed by an :meth:`insert` at
      *index1*; *args* is interpreted as for :meth:`insert`.

      .. versionadded:: 3.3

   .. method:: get(index1, index2=None)

      Return the text from *index1* up to but not including *index2* as a
      string.
      If *index2* is omitted, return the single character at *index1*.
      Embedded images and windows are omitted from the result.

   .. method:: index(index)

      Return the position corresponding to *index* in the canonical
      ``'line.char'`` form.

   .. method:: compare(index1, op, index2)

      Compare the positions of *index1* and *index2* using the relational
      operator *op*, which must be one of ``'<'``, ``'<='``, ``'=='``,
      ``'>='``, ``'>'`` or ``'!='``, and return the boolean result.

   .. method:: count(index1, index2, *options, return_ints=False)

      Count the number of items of the requested kinds between *index1* and
      *index2*; the count is negative if *index1* is after *index2*.
      Each of *options* names a kind of item to count: ``'chars'``,
      ``'displaychars'``, ``'displayindices'``, ``'displaylines'``,
      ``'indices'``, ``'lines'``, ``'xpixels'`` or ``'ypixels'`` (the default,
      used when no option is given, is ``'indices'``).
      The pseudo-option ``'update'`` forces any out-of-date layout information
      to be recalculated before the following options are evaluated.
      When *return_ints* is true and a single counting option is given, return
      a plain integer; otherwise return a tuple with one integer per counting
      option (or ``None`` if the result is empty).

      .. versionadded:: 3.3

      .. versionchanged:: 3.13
         Added the *return_ints* parameter.


   .. method:: see(index)

      Adjust the view so that the character given by *index* is visible.
      If it is already visible the method has no effect; if it is a short
      distance out of view the widget scrolls just enough to bring it to the
      nearest edge, otherwise it scrolls to center *index* in the window.

   .. method:: bbox(index)

      Return a tuple ``(x, y, width, height)`` giving the bounding box, in
      pixels, of the visible part of the character at *index*, or ``None`` if
      that character is not visible on the screen.

      This shadows the inherited :meth:`!Misc.bbox`;
      use :meth:`~Misc.grid_bbox` for the grid bounding box.

   .. method:: dlineinfo(index)

      Return a tuple ``(x, y, width, height, baseline)`` describing the display
      line that contains *index*: the first four values give the bounding box
      of the line in pixels and *baseline* gives the offset of the baseline
      measured down from the top of the area.
      Return ``None`` if that display line is not visible on the screen.

   .. method:: mark_set(markName, index)

      Set the mark named *markName* to the position just before the character
      at *index*, creating the mark if it does not already exist.
      A mark created this way has right gravity by default.

   .. method:: mark_unset(*markNames)

      Remove each of the marks named in *markNames*.
      The special ``insert`` and ``current`` marks may not be removed.

   .. method:: mark_names()

      Return a tuple of the names of all marks currently set in the widget.

   .. method:: mark_gravity(markName, direction=None)

      If *direction* is omitted, return the gravity of mark *markName*, either
      ``'left'`` or ``'right'``.
      Otherwise set its gravity to *direction*.
      The gravity determines on which side of the mark text inserted at the
      mark's position appears: a mark with right gravity (the default) stays to
      the right of such text.

   .. method:: mark_next(index)

      Return the name of the first mark at or after *index*, or ``None`` if
      there is none.
      When *index* is the name of a mark, the search starts just after that
      mark.

   .. method:: mark_previous(index)

      Return the name of the last mark at or before *index*, or ``None`` if
      there is none.
      When *index* is the name of a mark, the search starts just before that
      mark.

   .. method:: tag_add(tagName, index1, *args)

      Add the tag *tagName* to the range of characters from *index1* up to but
      not including the next index in *args*.
      Further pairs of indices may follow in *args* to tag additional ranges; a
      trailing single index tags just the character at that index.

   .. method:: tag_remove(tagName, index1, index2=None)

      Remove the tag *tagName* from the characters from *index1* up to but not
      including *index2* (or from the single character at *index1* if *index2*
      is omitted).
      The tag itself continues to exist even if no characters carry it.

   .. method:: tag_delete(*tagNames)

      Delete each of the tags named in *tagNames*, removing them from all
      characters and discarding their options and bindings.

   .. method:: tag_config(tagName, cnf=None, **kw)
      :no-typesetting:

   .. method:: tag_configure(tagName, cnf=None, **kw)

      Query or modify the configuration options of the tag *tagName*.
      This mirrors :meth:`~Misc.configure`, except that it applies to a tag
      rather than to the widget as a whole: with no options it returns a
      dictionary describing the current options, otherwise it sets the given
      options.
      Defining a tag this way also gives it a priority higher than any existing
      tag.

      The supported tag options, all controlling the appearance of the tagged
      text, are:

      *font*
         The font to use for the text.

      *foreground*
         The color to use for the text.

      *background*
         The color to use for the area behind the text.

      *fgstipple*, *bgstipple*
         Bitmaps used to stipple the foreground (text) and the background;
         only well supported on X11.

      *borderwidth*
         The width of the border drawn around the text according to *relief*
         (default ``0``).

      *relief*
         The 3-D appearance of the text's border: ``'flat'`` (the default),
         ``'raised'``, ``'sunken'``, ``'ridge'``, ``'groove'`` or ``'solid'``.

      *offset*
         How far the text is raised above (or, if negative, lowered below) the
         baseline, for superscripts and subscripts.

      *underline*
         Whether to underline the text (a boolean).

      *underlinefg*
         The color of the underline; it defaults to the text color.

      *overstrike*
         Whether to draw a line through the middle of the text.

      *overstrikefg*
         The color of the overstrike line; it defaults to the text color.

      *elide*
         Whether the text is elided (hidden).

      *justify*
         How to justify the first character of a display line: ``'left'`` (the
         default), ``'right'`` or ``'center'``.

      *wrap*
         How to wrap lines that are too long: ``'char'``, ``'word'`` or
         ``'none'``.

      *lmargin1*, *lmargin2*
         The indentation, in pixels, of the first display line of a logical
         line and of the remaining display lines.

      *lmargincolor*
         The color of the left margin area.

      *rmargin*
         The right-hand margin, in pixels.

      *rmargincolor*
         The color of the right margin area.

      *spacing1*, *spacing2*, *spacing3*
         Extra space, in pixels, above the first display line of a logical
         line, between its display lines, and below its last display line.

      *tabs*
         The set of tab stops, in the same form as the widget's *tabs* option.

      *tabstyle*
         How tab stops are interpreted: ``'tabular'`` or ``'wordprocessor'``.

      *selectbackground*, *selectforeground*
         The background and foreground colors used for the text while it is
         selected.

      .. note::

         Tk 8.6 added the *lmargincolor*, *overstrikefg*, *rmargincolor*,
         *selectbackground*, *selectforeground* and *underlinefg* options.

      :meth:`tag_config` is an alias of :meth:`!tag_configure`.

   .. method:: tag_cget(tagName, option)

      Return the current value of the configuration option *option* for the tag
      *tagName*.

   .. method:: tag_names(index=None)

      If *index* is omitted, return a tuple of the names of all tags defined in
      the widget; otherwise return only the names of the tags applied to the
      character at *index*.
      The names are ordered from lowest to highest priority.

   .. method:: tag_ranges(tagName)

      Return a tuple of indices describing all ranges of text tagged with
      *tagName*.
      The result alternates start and end indices, so that elements ``2*i`` and
      ``2*i+1`` bound the *i*-th range.

   .. method:: tag_nextrange(tagName, index1, index2=None)

      Search forward from *index1* (up to *index2* if given) for the first
      range of characters tagged with *tagName*, and return a two-element tuple
      of its start and end indices, or an empty tuple if there is no such
      range.

   .. method:: tag_prevrange(tagName, index1, index2=None)

      Search backward from *index1* (down to *index2* if given) for the nearest
      preceding range of characters tagged with *tagName*, and return a
      two-element tuple of its start and end indices, or an empty tuple if
      there is no such range.

   .. method:: tag_raise(tagName, aboveThis=None)

      Raise the priority of tag *tagName* so that it is just above the priority
      of *aboveThis*, or to the highest priority of all tags if *aboveThis* is
      omitted.
      When the display options of overlapping tags conflict, the
      higher-priority tag wins.

   .. method:: tag_lower(tagName, belowThis=None)

      Lower the priority of tag *tagName* so that it is just below the priority
      of *belowThis*, or to the lowest priority of all tags if *belowThis* is
      omitted.

   .. method:: tag_bind(tagName, sequence, func, add=None)

      Bind the event *sequence* on characters tagged with *tagName* to the
      callback *func*, so that *func* is invoked when that event occurs over
      such a character.
      If *add* is true the binding is added alongside any existing bindings for
      *sequence*, otherwise it replaces them.
      Works like :meth:`~Misc.bind` and returns the identifier of the new
      binding.

   .. method:: tag_unbind(tagName, sequence, funcid=None)

      Remove the bindings of the event *sequence* on characters tagged with
      *tagName*.
      If *funcid* is given, only that binding (as returned by :meth:`tag_bind`)
      is removed and its callback is unregistered.

      .. versionchanged:: 3.13
         If *funcid* is given, only that callback is unbound.


   .. method:: image_create(index, cnf={}, **kw)

      Embed an image at *index* and return the name assigned to this image
      instance, which may then be used as an index or passed to the other
      ``image_*`` methods.
      The options, given in *cnf* and *kw*, include *image* (the Tk image to
      display), *name* (a base name for the instance), *align*, *padx* and
      *pady*.

   .. method:: image_cget(index, option)

      Return the current value of the configuration option *option* for the
      embedded image at *index*.

   .. method:: image_configure(index, cnf=None, **kw)

      Query or modify the configuration options of the embedded image at
      *index*, like :meth:`~Misc.configure` but applied to that image.

   .. method:: image_names()

      Return a tuple of the names of all images embedded in the widget.

      .. note::

         This shadows the inherited :meth:`Misc.image_names`,
         which returns the names of all images in the Tcl interpreter;
         that method is not available on a :class:`Text`.

   .. method:: window_create(index, cnf={}, **kw)

      Embed a window (any widget) at *index*.
      The options, given in *cnf* and *kw*, include *window* (the widget to
      embed), *create* (a callback that creates the widget on demand), *align*,
      the boolean *stretch* (whether the widget is stretched vertically to the
      height of the line), *padx* and *pady*.
      The embedded widget must be a descendant of the text widget's parent.

   .. method:: window_cget(index, option)

      Return the current value of the configuration option *option* for the
      embedded window at *index*.

   .. method:: window_config(index, cnf=None, **kw)
      :no-typesetting:

   .. method:: window_configure(index, cnf=None, **kw)

      Query or modify the configuration options of the embedded window at
      *index*, like :meth:`~Misc.configure` but applied to that window.

      :meth:`window_config` is an alias of :meth:`!window_configure`.

   .. method:: window_names()

      Return a tuple of the names of all windows embedded in the widget.

   .. method:: edit(*args)

      Low-level wrapper around the Tk ``edit`` widget command that controls the
      undo/redo mechanism and the modified flag; *args* is the ``edit``
      subcommand and its arguments.
      The :meth:`!edit_\*` methods below are thin wrappers around it and are
      usually more convenient.

   .. method:: edit_modified(arg=None)

      If *arg* is omitted, return the current state of the modified flag as
      true or false; the flag is set automatically whenever the text is
      inserted or deleted.
      Otherwise set the flag to the boolean *arg*.

   .. method:: edit_undo()

      Undo the most recent edit action, that is, all the inserts and deletes
      recorded on the undo stack since the previous separator, and move it to
      the redo stack.
      Raises :exc:`TclError` if the undo stack is empty.
      Has no effect unless the *undo* option is true.
      Since Tk 9.0, returns a tuple of indices delimiting the ranges of text
      that were changed.

   .. method:: edit_redo()

      Reapply the most recently undone edit action, provided no further edits
      have been made since, and move it back to the undo stack.
      Raises :exc:`TclError` if the redo stack is empty.
      Has no effect unless the *undo* option is true.
      Since Tk 9.0, returns a tuple of indices delimiting the ranges of text
      that were changed.

   .. method:: edit_reset()

      Clear the undo and redo stacks.

   .. method:: edit_separator()

      Push a separator onto the undo stack, marking a boundary between edit
      actions for undo and redo.
      Has no effect unless the *undo* option is true.
      Separators are inserted automatically when the *autoseparators* option is
      true.

   .. method:: search(pattern, index, stopindex=None, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, *, nolinestop=None, strictlimits=None)

      Search for *pattern* starting at *index* and return the index of the
      first character of the first match, or an empty string if there is no
      match.
      Searching stops at *stopindex* if given; otherwise it wraps around the
      ends of the text until the starting position is reached again.
      The following boolean keyword flags control the search: *forwards* or
      *backwards* select the direction (forward is the default); *exact* (the
      default) or *regexp* select literal or regular-expression matching;
      *nocase* makes the match case-insensitive; *elide* causes hidden text to
      be searched as well; *nolinestop* (regexp only) lets ``.`` and ``[^``
      match newlines; and *strictlimits* requires the whole match to lie within
      *index* and *stopindex*.
      If *count* is a :class:`Variable`, the number of index positions in the
      match is stored in it.

      .. versionchanged:: 3.15
         Added the *nolinestop* and *strictlimits* parameters.


   .. method:: search_all(pattern, index, stopindex=None, *, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, nolinestop=None, overlap=None, strictlimits=None)

      Like :meth:`search`, but find every match in the searched range and
      return a tuple of the starting indices of all matches (empty if there are
      none).
      By default overlapping matches are not reported; passing a true *overlap*
      returns every match that is not wholly contained in another.
      If *count* is a :class:`Variable`, it receives a list with one element
      per match.

      .. versionadded:: 3.15


   .. method:: scan_mark(x, y)

      Record *x*, *y* and the current view, for use with later
      :meth:`scan_dragto` calls.
      This is typically bound to a mouse button press in the widget.

   .. method:: scan_dragto(x, y)

      Scroll the widget by 10 times the difference between *x*, *y* and the
      coordinates passed to the last :meth:`scan_mark` call.
      This is typically bound to mouse motion events, producing the effect of
      dragging the text at high speed through the window.

   .. method:: debug(boolean=None)

      If *boolean* is omitted, return whether internal consistency checks of
      the B-tree data structure are enabled.
      Otherwise enable or disable them.
      The setting is shared by all text widgets and may noticeably slow down
      widgets holding large amounts of text.

   .. method:: dump(index1, index2=None, command=None, **kw)

      Return the contents of the widget from *index1* up to but not including
      *index2* (or just the segment at *index1* if *index2* is omitted),
      including text and information about marks, tags, images and windows.
      The result is a list of ``(key, value, index)`` triples, where *key* is
      one of ``'text'``, ``'mark'``, ``'tagon'``, ``'tagoff'``, ``'image'`` or
      ``'window'``.
      By default all kinds are reported; passing any of the keyword arguments
      *all*, *text*, *mark*, *tag*, *image* or *window* as true restricts the
      dump to the selected kinds.
      If *command* is given, it is called once per triple with the three values
      as arguments and nothing is returned.

   .. method:: peer_create(newPathName, cnf={}, **kw)

      Create a peer text widget with the path name *newPathName* that shares
      this widget's underlying data (text, marks, tags, images and the undo
      stack).
      Changes made through any peer are reflected in all of them.
      By default the peer covers the same lines as this widget; standard text
      options, including *startline* and *endline*, may be given to override
      this.

      .. versionadded:: 3.3

   .. method:: peer_names()

      Return a tuple of the path names of this widget's peers, not including
      the widget itself.

      .. versionadded:: 3.3

   .. method:: yview_pickplace(*what)

      Adjust the view so that the location given by *what* is visible.
      This is an obsolete equivalent of :meth:`see`, which should be used
      instead.


Variable classes
^^^^^^^^^^^^^^^^

.. class:: Variable(master=None, value=None, name=None)

   The base class for the Tk variable wrappers.
   A Tk variable is a value stored in the Tcl interpreter that can be linked to
   widgets through their *variable* or *textvariable* options (see
   :ref:`coupling-widget-variables`), so that changes propagate both ways:
   updating the variable updates every widget bound to it, and a user editing
   such a widget updates the variable.

   *master* is the widget whose Tcl interpreter owns the variable; if omitted,
   the default root window is used.
   *value* is the initial value; if omitted, a type-specific default is used.
   *name* is the name of the variable in the Tcl interpreter; if omitted, a
   unique name of the form ``'PY_VARnum'`` is generated.
   If *name* matches an existing variable and *value* is omitted, the existing
   value is retained.

   In most cases you should use one of the typed subclasses below --
   :class:`StringVar`, :class:`IntVar`, :class:`DoubleVar` or
   :class:`BooleanVar` -- rather than :class:`!Variable` directly.

   .. note::

      When a :class:`!Variable` is garbage collected, its Tcl variable is unset.
      Keep a reference to it for as long as a widget is linked to it, for example
      by storing it as an attribute rather than in a local variable.
      Otherwise Tk recreates the Tcl variable to keep the widget working, but it
      is never unset again, leaking one Tcl variable per dropped wrapper.

   .. versionchanged:: 3.10
      Two variables now compare equal (``==``) only when they have the same
      name, are of the same class, and belong to the same Tcl interpreter.

   .. method:: get()

      Return the current value of the variable.
      For the base class the value is returned as a string; the typed
      subclasses convert it to the appropriate Python type.

   .. method:: initialize(value)
      :no-typesetting:

   .. method:: set(value)

      Set the variable to *value*.
      :meth:`initialize` is an alias of :meth:`!set`.

      .. versionadded:: 3.3
         The *initialize* spelling.

   .. method:: trace_add(mode, callback)

      Register *callback* to be called when the variable is accessed according
      to *mode*.
      *mode* is one of the strings ``'array'``, ``'read'``, ``'write'`` or
      ``'unset'``, or a list or tuple of such strings.

      When triggered, *callback* is called with three arguments: the name of
      the Tcl variable, an index (or an empty string if the variable is not an
      element of an array), and the *mode* that triggered the call.

      Return the internal name of the registered callback, which can be passed
      to :meth:`trace_remove`.

      .. versionadded:: 3.6

   .. method:: trace_remove(mode, cbname)

      Remove a trace callback from the variable.
      *mode* must match the *mode* that was passed to :meth:`trace_add`, and
      *cbname* is the callback name returned by :meth:`trace_add`.

      .. versionadded:: 3.6

   .. method:: trace_info()

      Return a list of ``(modes, cbname)`` pairs describing all traces
      currently set on the variable, where *modes* is a tuple of mode strings
      and *cbname* is the internal callback name.

      .. versionadded:: 3.6

   .. method:: trace(mode, callback)
      :no-typesetting:

   .. method:: trace_variable(mode, callback)

      Register *callback* to be called when the variable is accessed according
      to *mode*.
      *mode* is one of the strings ``'r'``, ``'w'`` or ``'u'``, for read, write
      or unset.
      Return the internal name of the registered callback.
      :meth:`trace` is an alias of :meth:`!trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_add` instead.  This method wraps a Tcl feature that
         was removed in Tcl 9.0.

   .. method:: trace_vdelete(mode, cbname)

      Remove the trace callback named *cbname* registered for *mode* with
      :meth:`trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_remove` instead.  This method wraps a Tcl feature
         that was removed in Tcl 9.0.

   .. method:: trace_vinfo()

      Return a list of ``(mode, cbname)`` pairs for all traces set on the
      variable with :meth:`trace_variable`.

      .. deprecated:: 3.6
         Use :meth:`trace_info` instead.  This method wraps a Tcl feature that
         was removed in Tcl 9.0.


.. class:: StringVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a string.
   The default value is ``''``.

   .. method:: get()

      Return the value of the variable as a :class:`str`.


.. class:: IntVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds an integer.
   The default value is ``0``.

   .. method:: get()

      Return the value of the variable as an :class:`int`.


.. class:: DoubleVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a float.
   The default value is ``0.0``.

   .. method:: get()

      Return the value of the variable as a :class:`float`.

   .. _tkinter-numeric-locale:

   .. note::

      A floating-point value is always parsed with a period (``.``) as the
      decimal separator, but :class:`Spinbox`, :class:`Scale` and
      :class:`ttk.Spinbox <tkinter.ttk.Spinbox>` format it according to the
      ``LC_NUMERIC`` locale.  Under a locale that uses a comma they produce a
      value that :meth:`get` cannot read, raising :exc:`TclError`.  Set
      ``LC_NUMERIC`` to a locale that uses a period (such as ``'C'``) to avoid
      this.


.. class:: BooleanVar(master=None, value=None, name=None)

   A :class:`Variable` subclass that holds a boolean.
   The default value is ``False``.

   .. method:: get()

      Return the value of the variable as a :class:`bool`.
      Raise a :exc:`ValueError` if the value cannot be interpreted as a
      boolean.

   .. method:: initialize(value)
      :no-typesetting:

   .. method:: set(value)

      Set the variable to *value*, converting it to a boolean.
      :meth:`initialize` is an alias of :meth:`!set`.

      .. versionadded:: 3.3
         The *initialize* spelling.


Image classes
^^^^^^^^^^^^^

.. class:: Image(imgtype, name=None, cnf={}, master=None, **kw)

   Base class for Tk images.
   *imgtype* is the Tk image type, one of ``'photo'`` or ``'bitmap'``.
   An image is a named object that can be displayed by widgets through their
   *image* option; deleting all references to the :class:`!Image` object
   deletes the underlying Tk image.
   Usually you create a :class:`PhotoImage` or :class:`BitmapImage` rather than
   an :class:`!Image` directly.

   The image's configuration options are given by *cnf* and *kw* and may be
   queried and changed later with the mapping protocol (using ``image[key]``)
   or with the :meth:`configure` method.

   .. method:: config(**kw)
      :no-typesetting:

   .. method:: configure(**kw)

      Modify one or more configuration options of the image.
      The valid options depend on the image type; see :class:`PhotoImage` and
      :class:`BitmapImage`.
      :meth:`config` is an alias of :meth:`!configure`.

   .. method:: height()

      Return the height of the image, in pixels.

   .. method:: width()

      Return the width of the image, in pixels.

   .. method:: type()

      Return the type of the image, that is the value of *imgtype* with which
      it was created (for example ``'photo'`` or ``'bitmap'``).


.. class:: PhotoImage(name=None, cnf={}, master=None, **kw)

   A full-color image (the Tk ``photo`` image type), stored internally with a
   varying degree of transparency per pixel.
   It can read and write GIF, PPM/PGM and (in Tk 8.6 and later) PNG files, read
   SVG files (in Tk 9.0 and later), and be drawn in widgets.
   Inherits from :class:`Image`.

   The configuration options include *data* (the image contents as a string),
   *file* (the name of a file to read the contents from), *format* (the name of
   the file format handler), *width* and *height* (the size of the image, used
   when building it up piece by piece), *gamma* and *palette*.

   .. method:: blank()

      Blank the image; that is, set the entire image to have no data, so that
      it is displayed as transparent and the background of whatever window it
      is displayed in shows through.

   .. method:: cget(option)

      Return the current value of the configuration option *option*.

   .. method:: copy(*, from_coords=None, zoom=None, subsample=None)

      Return a new :class:`PhotoImage` with a copy of this image.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      ``(x1, y1)`` and ``(x2, y2)`` specify diagonally opposite corners of the
      rectangle.
      If *x2* and *y2* are not specified, they default to the bottom-right
      corner of the source image.
      The pixels copied include the left and top edges of the rectangle but not
      the bottom or right edges.
      If *from_coords* is not given, the whole source image is copied.

      If *zoom* or *subsample* are specified, the image is transformed as in
      the :meth:`zoom` or :meth:`subsample` methods.
      The value must be a single integer or a pair of integers.

      .. versionchanged:: 3.13
         Added the *from_coords*, *zoom* and *subsample* parameters.


   .. method:: copy_replace(sourceImage, *, from_coords=None, to=None, \
                            shrink=False, zoom=None, subsample=None, \
                            compositingrule=None)

      Copy a region from *sourceImage* (which must be a :class:`PhotoImage`)
      into this image, possibly with pixel zooming and/or subsampling.
      If no options are specified, the whole of *sourceImage* is copied into
      this image, starting at coordinates ``(0, 0)``.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      *to* specifies a rectangular sub-region of the destination image to be
      affected.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If *x2* and *y2* are not specified, they default to ``(x1, y1)`` plus the
      size of the source region (after subsampling and zooming, if specified).
      If *x2* and *y2* are specified, the source region is replicated if
      necessary to fill the destination region in a tiled fashion.

      If *shrink* is true, the size of the destination image is reduced, if
      necessary, so that the region being copied into is at the bottom-right
      corner of the image.

      If *zoom* or *subsample* are specified, the image is transformed as in
      the :meth:`zoom` or :meth:`subsample` methods.
      The value must be a single integer or a pair of integers.

      *compositingrule* specifies how transparent pixels in the source image
      are combined with the destination image.
      With ``'overlay'`` (the default), the old contents of the destination
      image remain visible, as if the source image were printed on a piece of
      transparent film and placed over the top of the destination.
      With ``'set'``, the old contents of the destination image are discarded
      and the source image is used as-is.

      .. versionadded:: 3.13


   .. method:: data(format=None, *, from_coords=None, background=None, \
                    grayscale=False)

      Return the image data.

      *format* specifies the name of the image file format handler to use.
      If it is not given, the data is returned as a tuple (one element per row)
      of strings containing space-separated (one element per pixel/column)
      colors in ``#RRGGBB`` format.

      *from_coords* specifies a rectangular region of the image to be returned.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region, including ``(x1, y1)`` and excluding ``(x2, y2)``.
      If *from_coords* is not given, the whole image is returned.

      If *background* is specified, the data does not contain any transparency
      information; in all transparent pixels the color is replaced by the
      specified color.

      If *grayscale* is true, the data does not contain color information; all
      pixel data is transformed into grayscale.

      .. versionadded:: 3.13


   .. method:: get(x, y)

      Return the color of the pixel at coordinates (*x*, *y*) as an
      ``(r, g, b)`` tuple of three integers between 0 and 255, representing the
      red, green and blue components respectively.

   .. method:: put(data, to=None)

      Set pixels of the image to the colors given in *data*, which must be a
      string or a nested sequence of horizontal rows of pixel colors (for
      example ``"{red green} {blue yellow}"``).

      *to* specifies the coordinates of the region of the image into which the
      data are copied.
      It must be a tuple or a list of 2 or 4 integers ``(x1, y1)`` or
      ``(x1, y1, x2, y2)`` giving the top-left corner, and optionally the
      bottom-right corner, of the region.
      The default position is ``(0, 0)``.

   .. method:: read(filename, format=None, *, from_coords=None, to=None, \
                    shrink=False)

      Read image data from the file named *filename* into the image.

      *format* specifies the format of the image data in the file.

      *from_coords* specifies a rectangular sub-region of the image file data
      to be copied to the destination image.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image in the file.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region.
      If *from_coords* is not given, the whole of the image in the file is
      read.

      *to* specifies the coordinates of the top-left corner of the region of
      the image into which the data are read.
      The default is ``(0, 0)``.

      If *shrink* is true, the size of the image is reduced, if necessary, so
      that the region into which the file data are read is at the bottom-right
      corner of the image.

      .. versionadded:: 3.13


   .. method:: subsample(x, y='', *, from_coords=None)

      Return a new :class:`PhotoImage` based on this image but using only every
      *x*-th pixel in the X direction and every *y*-th pixel in the Y
      direction.
      If *y* is not given, it defaults to the same value as *x*.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      .. versionchanged:: 3.13
         Added the *from_coords* parameter.


   .. method:: transparency_get(x, y)

      Return ``True`` if the pixel at coordinates (*x*, *y*) is fully
      transparent, ``False`` otherwise.

      .. versionadded:: 3.8


   .. method:: transparency_set(x, y, boolean)

      Make the pixel at coordinates (*x*, *y*) fully transparent if *boolean*
      is true, fully opaque otherwise.

      .. versionadded:: 3.8


   .. method:: write(filename, format=None, from_coords=None, *, \
                     background=None, grayscale=False)

      Write image data from the image to the file named *filename*.

      *format* specifies the name of the image file format handler to use.
      If it is not given, the format is guessed from the file extension.

      *from_coords* specifies a rectangular region of the image to be written.
      It must be a tuple or a list of 1 to 4 integers ``(x1, y1, x2, y2)``.
      If only *x1* and *y1* are specified, the region extends from ``(x1, y1)``
      to the bottom-right corner of the image.
      If all four coordinates are given, they specify diagonally opposite
      corners of the region.
      If *from_coords* is not given, the whole image is written.

      If *background* is specified, the data does not contain any transparency
      information; in all transparent pixels the color is replaced by the
      specified color.

      If *grayscale* is true, the data does not contain color information; all
      pixel data is transformed into grayscale.

      .. versionchanged:: 3.13
         Added the *background* and *grayscale* parameters.


   .. method:: zoom(x, y='', *, from_coords=None)

      Return a new :class:`PhotoImage` with this image magnified by a factor of
      *x* in the X direction and *y* in the Y direction.
      If *y* is not given, it defaults to the same value as *x*.

      *from_coords* specifies a rectangular sub-region of the source image to
      be copied, as in the :meth:`copy` method.

      .. versionchanged:: 3.13
         Added the *from_coords* parameter.



.. class:: BitmapImage(name=None, cnf={}, master=None, **kw)

   A two-color image (the Tk ``bitmap`` image type) created from an X11 bitmap.
   Each pixel displays a foreground color, a background color, or nothing
   (producing a transparent effect).
   Inherits from :class:`Image`.

   The configuration options are *data* or *file* (the source bitmap, given as
   a string in X11 bitmap format or as the name of a file in that format),
   *maskdata* or *maskfile* (the mask bitmap, in the same forms), and
   *foreground* and *background* (the two colors).
   For pixels where the mask is zero the image displays nothing; for other
   pixels it displays the foreground color where the source is one and the
   background color where the source is zero.
   If *background* is set to an empty string, the background pixels are
   transparent.

   :class:`!BitmapImage` has no methods of its own beyond those inherited from
   :class:`Image`.


Other classes
^^^^^^^^^^^^^

.. class:: Event()

   A container for the attributes of an event passed to a callback bound with
   :meth:`Misc.bind`.
   An :class:`!Event` instance has the following attributes, each corresponding
   to a field of the underlying Tk event; depending on the event type, some
   attributes may be set to the string ``'??'`` to indicate that they are not
   meaningful.
   See :ref:`bindings-and-events`.

   .. attribute:: serial

      The serial number of the event.

   .. attribute:: num

      The mouse button that was pressed or released (for button events).

   .. attribute:: focus

      Whether the window has the focus (for ``Enter`` and ``Leave`` events).

   .. attribute:: height
                  width

      The new height and width of the window (for ``Configure`` and ``Expose``
      events).

   .. attribute:: keycode

      The keycode of the key that was pressed or released.

   .. attribute:: state

      The state of the event, as a number (for most events) or a string (for
      ``Visibility`` events).

   .. attribute:: time

      The timestamp of the event, in milliseconds.

   .. attribute:: x
                  y

      The pointer position relative to the widget, in pixels.

   .. attribute:: x_root
                  y_root

      The pointer position relative to the top-left corner of the screen, in
      pixels.

   .. attribute:: char

      The character typed, as a string (for key events).

   .. attribute:: send_event

      ``True`` if the event was sent by another application.

   .. attribute:: keysym

      The symbolic name of the key that was pressed or released.

   .. attribute:: keysym_num

      The numeric value of :attr:`keysym`.

   .. attribute:: type

      The :class:`EventType` of the event.

   .. attribute:: widget

      The widget on which the event occurred.

   .. attribute:: delta

      The amount the mouse wheel was rotated (for ``MouseWheel`` events).

   .. attribute:: user_data

      The data string of a virtual event, as passed to the *data* option of
      :meth:`Misc.event_generate`.
      It is ``'??'`` for non-virtual events.

      .. versionadded:: 3.15

   .. attribute:: detail

      A fixed detail string for ``Enter``, ``Leave``, ``FocusIn``, ``FocusOut``
      and ``ConfigureRequest`` events (see the Tcl/Tk documentation).
      It is ``'??'`` for other events.

      .. versionadded:: 3.15


.. class:: EventType(*values)

   An :class:`enum.StrEnum` enumerating the Tk event types, used as the value
   of :attr:`Event.type`.
   Its members include, among others, ``KeyPress``, ``KeyRelease``,
   ``ButtonPress``, ``ButtonRelease``, ``Motion``, ``Enter``, ``Leave``,
   ``FocusIn``, ``FocusOut``, ``Configure``, ``Map``, ``Unmap``, ``Expose``,
   ``Destroy`` and ``MouseWheel``.

   .. versionadded:: 3.6



.. class:: CallWrapper(func, subst, widget)

   Internal helper that wraps a Python callback so that it can be invoked from
   Tcl.
   *func* is the Python function, *subst* is an optional function that
   pre-processes the Tcl arguments, and *widget* is the widget used for error
   reporting.
   Instances are created automatically by :meth:`Misc.register`; this class is
   not normally used directly.


Module-level functions
^^^^^^^^^^^^^^^^^^^^^^

.. function:: Tcl(screenName=None, baseName=None, className='Tk', useTk=False)

   The :func:`Tcl` function is a factory function which creates an object much
   like that created by the :class:`Tk` class, except that it does not
   initialize the Tk subsystem.
   This is most often useful when driving the Tcl interpreter in an environment
   where one doesn't want to create extraneous toplevel windows, or where one
   cannot (such as Unix/Linux systems without an X server).
   An object created by the :func:`Tcl` object can have a Toplevel window
   created (and the Tk subsystem initialized) by calling its :meth:`~Tk.loadtk`
   method.

.. function:: NoDefaultRoot()

   Inhibit the creation of an implicit default root window.
   Afterwards :mod:`!tkinter` no longer creates a shared default root
   automatically, and operations that rely on one --- such as constructing a
   widget without an explicit *master* --- raise a :exc:`RuntimeError`.
   Call this early in larger applications to make the root window explicit.

.. function:: mainloop(n=0)

   Run the Tk main event loop on the default root window until all windows are
   destroyed.
   Equivalent to calling :meth:`Misc.mainloop` on the default root.

.. function:: getboolean(s)

   Convert the Tcl boolean string *s* (one of ``'1'``, ``'true'``, ``'yes'``,
   ``'on'`` and similar, or their false counterparts) to a Python
   :class:`bool`.
   Raise :exc:`ValueError` for an invalid value.

.. function:: getdouble(s)

   Convert *s* to a floating-point number.
   This is the built-in :class:`float`.

.. function:: getint(s)

   Convert *s* to an integer.
   This is the built-in :class:`int`.

.. function:: image_names()

   Return the names of all existing images in the default root's interpreter.

.. function:: image_types()

   Return the available image types (such as ``'photo'`` and ``'bitmap'``) in
   the default root's interpreter.


.. _tkinter-file-handlers:

File handlers
^^^^^^^^^^^^^

Tk allows you to register and unregister a callback function which will be
called from the Tk mainloop when I/O is possible on a file descriptor.
Only one handler may be registered per file descriptor. Example code::

   import tkinter
   widget = tkinter.Tk()
   mask = tkinter.READABLE | tkinter.WRITABLE
   widget.tk.createfilehandler(file, mask, callback)
   ...
   widget.tk.deletefilehandler(file)

This feature is not available on Windows.

Since you don't know how many bytes are available for reading, you may not
want to use the :class:`~io.BufferedIOBase` or :class:`~io.TextIOBase`
:meth:`~io.BufferedIOBase.read` or :meth:`~io.IOBase.readline` methods,
since these will insist on reading a predefined number of bytes.
For sockets, the :meth:`~socket.socket.recv` or
:meth:`~socket.socket.recvfrom` methods will work fine; for other files,
use raw reads or ``os.read(file.fileno(), maxbytecount)``.


.. method:: Widget.tk.createfilehandler(file, mask, func)

   Registers the file handler callback function *func*. The *file* argument
   may either be an object with a :meth:`~io.IOBase.fileno` method (such as
   a file or socket object), or an integer file descriptor. The *mask*
   argument is an ORed combination of any of the three constants below.
   The callback is called as follows::

      callback(file, mask)


.. method:: Widget.tk.deletefilehandler(file)

   Unregisters a file handler.


.. data:: READABLE
          WRITABLE
          EXCEPTION

   Constants used in the *mask* arguments.


Constants
^^^^^^^^^

The following symbolic constants are available in both the :mod:`!tkinter`
and :mod:`!tkinter.constants` namespaces.

.. data:: TRUE
          YES
          ON

   Truthy values, all equal to the integer ``1``.

.. data:: FALSE
          NO
          OFF

   Falsy values, all equal to the integer ``0``.

.. data:: N
          S
          E
          W
          NE
          NW
          SE
          SW
          NS
          EW
          NSEW
          CENTER

   Compass directions (``'n'``, ``'s'``, ``'e'``, ``'w'`` and the diagonals and
   edges) plus ``CENTER`` (``'center'``), used as values for the *anchor* and
   *sticky* options and by methods such as :meth:`Misc.grid_anchor`.

.. data:: LEFT
          RIGHT
          TOP
          BOTTOM

   Sides for the *side* option of the packer (see :meth:`Pack.pack_configure`).

.. data:: X
          Y
          BOTH
          NONE

   Values for the *fill* option of the packer: ``'x'``, ``'y'``, ``'both'`` or
   ``'none'``.

.. data:: RAISED
          SUNKEN
          FLAT
          RIDGE
          GROOVE
          SOLID

   Values for the *relief* option, which controls a widget's 3-D border.

.. data:: HORIZONTAL
          VERTICAL

   Values for the *orient* option of widgets such as :class:`Scale`,
   :class:`Scrollbar` and :class:`PanedWindow`.

.. data:: CHAR
          WORD

   Values for the *wrap* option of the :class:`Text` widget, selecting line
   wrapping on character or word boundaries.

.. data:: BASELINE

   The text-alignment value ``'baseline'``.

.. data:: INSIDE
          OUTSIDE

   Values for the *bordermode* option of the placer (see
   :meth:`Place.place_configure`).

.. data:: INSERT
          CURRENT
          END
          ANCHOR
          SEL
          SEL_FIRST
          SEL_LAST

   Symbolic indices used by the :class:`Text`, :class:`Entry`, :class:`Listbox`
   and :class:`Canvas` widgets, such as ``'insert'`` (the insertion cursor),
   ``'current'``, ``'end'``, ``'anchor'`` and the bounds of the selection
   (``'sel.first'`` and ``'sel.last'``).

.. data:: ALL

   The special tag ``'all'``, which matches every item of a :class:`Canvas` or
   every character of a :class:`Text` (for example ``canvas.delete(ALL)``).

.. data:: NORMAL
          DISABLED
          ACTIVE
          HIDDEN

   Values for the *state* option of various widgets and items.

.. data:: CASCADE
          CHECKBUTTON
          COMMAND
          RADIOBUTTON
          SEPARATOR

   Menu entry types, used as the *itemType* argument of :meth:`Menu.add` and
   :meth:`Menu.insert`.

.. data:: SINGLE
          BROWSE
          MULTIPLE
          EXTENDED

   Values for the *selectmode* option of the :class:`Listbox` widget.

.. data:: PIESLICE
          CHORD
          ARC

   Values for the *style* option of :class:`Canvas` arc items.

.. data:: BUTT
          PROJECTING
          ROUND
          BEVEL
          MITER

   Values for the *capstyle* (``'butt'``, ``'projecting'``, ``'round'``) and
   *joinstyle* (``'round'``, ``'bevel'``, ``'miter'``) options of
   :class:`Canvas` line items.

.. data:: FIRST
          LAST

   Values for the *arrow* option of :class:`Canvas` line items, indicating
   which ends have arrowheads.

.. data:: MOVETO
          SCROLL

   The first argument passed by a :class:`Scrollbar` to the :meth:`XView.xview`
   or :meth:`YView.yview` method of the scrolled widget.

.. data:: UNITS
          PAGES

   Values for the *what* argument of :meth:`XView.xview_scroll` and
   :meth:`YView.yview_scroll`.

.. data:: UNDERLINE
          NUMERIC
          DOTBOX

   Other option values: ``'underline'``, ``'numeric'`` and ``'dotbox'``.

----

   .. method:: search(pattern, index, stopindex=None, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, *, nolinestop=None, strictlimits=None)

      Search for *pattern* starting at *index* and return the index of the
      first character of the first match, or an empty string if there is no
      match.
      Searching stops at *stopindex* if given; otherwise it wraps around the
      ends of the text until the starting position is reached again.
      The following boolean keyword flags control the search: *forwards* or
      *backwards* select the direction (forward is the default); *exact* (the
      default) or *regexp* select literal or regular-expression matching;
      *nocase* makes the match case-insensitive; *elide* causes hidden text to
      be searched as well; *nolinestop* (regexp only) lets ``.`` and ``[^``
      match newlines; and *strictlimits* requires the whole match to lie within
      *index* and *stopindex*.
      If *count* is a :class:`Variable`, the number of index positions in the
      match is stored in it.

      .. versionchanged:: 3.15
         Added the *nolinestop* and *strictlimits* parameters.



----

   .. method:: search_all(pattern, index, stopindex=None, *, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None, nolinestop=None, overlap=None, strictlimits=None)

      Like :meth:`search`, but find every match in the searched range and
      return a tuple of the starting indices of all matches (empty if there are
      none).
      By default overlapping matches are not reported; passing a true *overlap*
      returns every match that is not wholly contained in another.
      If *count* is a :class:`Variable`, it receives a list with one element
      per match.

      .. versionadded:: 3.15



----

   .. attribute:: user_data

      The data string of a virtual event, as passed to the *data* option of
      :meth:`Misc.event_generate`.
      It is ``'??'`` for non-virtual events.

      .. versionadded:: 3.15


----

   .. attribute:: detail

      A fixed detail string for ``Enter``, ``Leave``, ``FocusIn``, ``FocusOut``
      and ``ConfigureRequest`` events (see the Tcl/Tk documentation).
      It is ``'??'`` for other events.

      .. versionadded:: 3.15


.. class:: EventType(*values)

   An :class:`enum.StrEnum` enumerating the Tk event types, used as the value
   of :attr:`Event.type`.
   Its members include, among others, ``KeyPress``, ``KeyRelease``,
   ``ButtonPress``, ``ButtonRelease``, ``Motion``, ``Enter``, ``Leave``,
   ``FocusIn``, ``FocusOut``, ``Configure``, ``Map``, ``Unmap``, ``Expose``,
   ``Destroy`` and ``MouseWheel``.

   .. versionadded:: 3.6



.. class:: CallWrapper(func, subst, widget)

   Internal helper that wraps a Python callback so that it can be invoked from
   Tcl.
   *func* is the Python function, *subst* is an optional function that
   pre-processes the Tcl arguments, and *widget* is the widget used for error
   reporting.
   Instances are created automatically by :meth:`Misc.register`; this class is
   not normally used directly.


Module-level functions
^^^^^^^^^^^^^^^^^^^^^^

.. function:: Tcl(screenName=None, baseName=None, className='Tk', useTk=False)

   The :func:`Tcl` function is a factory function which creates an object much
   like that created by the :class:`Tk` class, except that it does not
   initialize the Tk subsystem.
   This is most often useful when driving the Tcl interpreter in an environment
   where one doesn't want to create extraneous toplevel windows, or where one
   cannot (such as Unix/Linux systems without an X server).
   An object created by the :func:`Tcl` object can have a Toplevel window
   created (and the Tk subsystem initialized) by calling its :meth:`~Tk.loadtk`
   method.

.. function:: NoDefaultRoot()

   Inhibit the creation of an implicit default root window.
   Afterwards :mod:`!tkinter` no longer creates a shared default root
   automatically, and operations that rely on one --- such as constructing a
   widget without an explicit *master* --- raise a :exc:`RuntimeError`.
   Call this early in larger applications to make the root window explicit.

.. function:: mainloop(n=0)

   Run the Tk main event loop on the default root window until all windows are
   destroyed.
   Equivalent to calling :meth:`Misc.mainloop` on the default root.

.. function:: getboolean(s)

   Convert the Tcl boolean string *s* (one of ``'1'``, ``'true'``, ``'yes'``,
   ``'on'`` and similar, or their false counterparts) to a Python
   :class:`bool`.
   Raise :exc:`ValueError` for an invalid value.

.. function:: getdouble(s)

   Convert *s* to a floating-point number.
   This is the built-in :class:`float`.

.. function:: getint(s)

   Convert *s* to an integer.
   This is the built-in :class:`int`.

.. function:: image_names()

   Return the names of all existing images in the default root's interpreter.

.. function:: image_types()

   Return the available image types (such as ``'photo'`` and ``'bitmap'``) in
   the default root's interpreter.


.. _tkinter-file-handlers:

File handlers
^^^^^^^^^^^^^

Tk allows you to register and unregister a callback function which will be
called from the Tk mainloop when I/O is possible on a file descriptor.
Only one handler may be registered per file descriptor. Example code::

   import tkinter
   widget = tkinter.Tk()
   mask = tkinter.READABLE | tkinter.WRITABLE
   widget.tk.createfilehandler(file, mask, callback)
   ...
   widget.tk.deletefilehandler(file)

This feature is not available on Windows.

Since you don't know how many bytes are available for reading, you may not
want to use the :class:`~io.BufferedIOBase` or :class:`~io.TextIOBase`
:meth:`~io.BufferedIOBase.read` or :meth:`~io.IOBase.readline` methods,
since these will insist on reading a predefined number of bytes.
For sockets, the :meth:`~socket.socket.recv` or
:meth:`~socket.socket.recvfrom` methods will work fine; for other files,
use raw reads or ``os.read(file.fileno(), maxbytecount)``.


.. method:: Widget.tk.createfilehandler(file, mask, func)

   Registers the file handler callback function *func*. The *file* argument
   may either be an object with a :meth:`~io.IOBase.fileno` method (such as
   a file or socket object), or an integer file descriptor. The *mask*
   argument is an ORed combination of any of the three constants below.
   The callback is called as follows::

      callback(file, mask)


.. method:: Widget.tk.deletefilehandler(file)

   Unregisters a file handler.


.. data:: READABLE
          WRITABLE
          EXCEPTION

   Constants used in the *mask* arguments.


Constants
^^^^^^^^^

The following symbolic constants are available in both the :mod:`!tkinter`
and :mod:`!tkinter.constants` namespaces.

.. data:: TRUE
          YES
          ON

   Truthy values, all equal to the integer ``1``.

.. data:: FALSE
          NO
          OFF

   Falsy values, all equal to the integer ``0``.

.. data:: N
          S
          E
          W
          NE
          NW
          SE
          SW
          NS
          EW
          NSEW
          CENTER

   Compass directions (``'n'``, ``'s'``, ``'e'``, ``'w'`` and the diagonals and
   edges) plus ``CENTER`` (``'center'``), used as values for the *anchor* and
   *sticky* options and by methods such as :meth:`Misc.grid_anchor`.

.. data:: LEFT
          RIGHT
          TOP
          BOTTOM

   Sides for the *side* option of the packer (see :meth:`Pack.pack_configure`).

.. data:: X
          Y
          BOTH
          NONE

   Values for the *fill* option of the packer: ``'x'``, ``'y'``, ``'both'`` or
   ``'none'``.

.. data:: RAISED
          SUNKEN
          FLAT
          RIDGE
          GROOVE
          SOLID

   Values for the *relief* option, which controls a widget's 3-D border.

.. data:: HORIZONTAL
          VERTICAL

   Values for the *orient* option of widgets such as :class:`Scale`,
   :class:`Scrollbar` and :class:`PanedWindow`.

.. data:: CHAR
          WORD

   Values for the *wrap* option of the :class:`Text` widget, selecting line
   wrapping on character or word boundaries.

.. data:: BASELINE

   The text-alignment value ``'baseline'``.

.. data:: INSIDE
          OUTSIDE

   Values for the *bordermode* option of the placer (see
   :meth:`Place.place_configure`).

.. data:: INSERT
          CURRENT
          END
          ANCHOR
          SEL
          SEL_FIRST
          SEL_LAST

   Symbolic indices used by the :class:`Text`, :class:`Entry`, :class:`Listbox`
   and :class:`Canvas` widgets, such as ``'insert'`` (the insertion cursor),
   ``'current'``, ``'end'``, ``'anchor'`` and the bounds of the selection
   (``'sel.first'`` and ``'sel.last'``).

.. data:: ALL

   The special tag ``'all'``, which matches every item of a :class:`Canvas` or
   every character of a :class:`Text` (for example ``canvas.delete(ALL)``).

.. data:: NORMAL
          DISABLED
          ACTIVE
          HIDDEN

   Values for the *state* option of various widgets and items.

.. data:: CASCADE
          CHECKBUTTON
          COMMAND
          RADIOBUTTON
          SEPARATOR

   Menu entry types, used as the *itemType* argument of :meth:`Menu.add` and
   :meth:`Menu.insert`.

.. data:: SINGLE
          BROWSE
          MULTIPLE
          EXTENDED

   Values for the *selectmode* option of the :class:`Listbox` widget.

.. data:: PIESLICE
          CHORD
          ARC

   Values for the *style* option of :class:`Canvas` arc items.

.. data:: BUTT
          PROJECTING
          ROUND
          BEVEL
          MITER

   Values for the *capstyle* (``'butt'``, ``'projecting'``, ``'round'``) and
   *joinstyle* (``'round'``, ``'bevel'``, ``'miter'``) options of
   :class:`Canvas` line items.

.. data:: FIRST
          LAST

   Values for the *arrow* option of :class:`Canvas` line items, indicating
   which ends have arrowheads.

.. data:: MOVETO
          SCROLL

   The first argument passed by a :class:`Scrollbar` to the :meth:`XView.xview`
   or :meth:`YView.yview` method of the scrolled widget.

.. data:: UNITS
          PAGES

   Values for the *what* argument of :meth:`XView.xview_scroll` and
   :meth:`YView.yview_scroll`.

.. data:: UNDERLINE
          NUMERIC
          DOTBOX

   Other option values: ``'underline'``, ``'numeric'`` and ``'dotbox'``.