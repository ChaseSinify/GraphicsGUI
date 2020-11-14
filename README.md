# GraphicsGUI
Python and QT

General Info:
	The shortcut for this documentation is "Cntrl+D"
	Almost every item has a "hover" function that displays a tool tip!
	The tool box is on a floatable dock widget on the left.
	The left window is for drawing vertices, or simply painting.
	The right window renders the graphics polygons as true 2d objects.
	At any time, you can clear either window (drawing, graphics) by
		pressing the "clear" buttons on the bottom left of the tool dock.
	With this program, you can:
		* Draw arbitrary creations with the "paint" tool;
		* Create custom polygons with the "vertex" tool;
		* Modify (translate, transform, scale and rotate) 2d graphics objects;
			
Drawing Polygons:
	1. Select the "Vertex" tool from the left toolbar dock (enabled by default)
	2. In the drawing area (left pane), click to place vertices (these are displayed
		in red). Once you have a sufficient amount to draw a polygon (3+) and
		are happy, press "return" to draw the polygon in the graphics view
		on the right (right pane).
	3. The polygon appears in the right graphics view, where it can be modified
		(more on this below)

Customizing Polygons:	
		On the left side of the application, we have a tool bar with many 
	different settings. In the middle of the toolbar, there is a tab section with 
	specific settings for the pen and the brush. These settings determine the 
	colors, size, opacity, line style, textures, etc. of the drawings and shapes 
	created.
		Specifically, the PEN directly impacts the drawing area paint tool, as well
	as the BORDER of the 2d graphics polygons on the right (which are created 
	by drawing vertices on the left). The BRUSH directly impacts the FILL of the 
	2d graphics polygons on the right.
		Inside the tool box on the left dock, modify the colors, alpha, pen style,
	brush texture, etc. to produce a different color/style of polygon. At any given
	time, the color/alpha in RGBA is displayed on the colored sqaure within the
	pen or brush tab that is active.

Transforming Polygons:
		Polygon transformations occur in the graphics window (right pane). 
	These item are true 2d graphics objects, and support transformations. 
	To modify one, start by selecting it (click on the polygon).
	*ROTATION: Hover the polygon and use mouse scroll wheel
		or the arrow keys (more precise, but slow).
	*SCALING: Select a polygon and use the up and down arrows.
	*TRANSLATION: Click and drag a polygon.

Drawing:
		On the left window, with the paint tool selected from the tool dock, 
	click and drag to paint the current PEN settings onto the drawing area.

Coming Soon:
	*3D objects with QOpenGl
	*Significantly cleaner UI design and colors
	*Ability to upload custom images and texture maps
	*Saving/Opening projects and items
	*Significantly more customization and control
	*Easter eggs and small bug fixes (what bugs? :) )