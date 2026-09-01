import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# PYTHON MATPLOTLIB - FULL NOTES
# ==========================================================


# ----------------------------------------------------------
# Matplotlib Intro
# ----------------------------------------------------------
# - Matplotlib is a low-level graph plotting library in Python,
#   used as a visualization utility.
# - Created by John D. Hunter.
# - Open source and free to use.
# - Mostly written in Python, with some parts in C, Objective-C,
#   and JavaScript for platform compatibility.
# - Used to create static, animated, and interactive visualizations.
print("Matplotlib Intro - see comments above")


# ----------------------------------------------------------
# Matplotlib Get Started
# ----------------------------------------------------------
# - Install matplotlib using: pip install matplotlib
# - Import convention: import matplotlib.pyplot as plt
# - Check installed version below.
import matplotlib
print(matplotlib.__version__)


# ----------------------------------------------------------
# Matplotlib Pyplot
# ----------------------------------------------------------
# - pyplot is a sub-module of Matplotlib, used for plotting.
# - Most matplotlib utilities live under the pyplot submodule.
# - Standard import alias: import matplotlib.pyplot as plt
# - plt.plot() draws a line/points based on given x and y values.
# - plt.show() displays the figure.

# sub-point: basic plot with 2 points (draws a line between them)
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

# sub-point: plotting without x-points (x defaults to 0,1,2,3...)
ypoints2 = np.array([3, 8, 1, 10])
plt.plot(ypoints2)
plt.show()


# ----------------------------------------------------------
# Matplotlib Plotting
# ----------------------------------------------------------
# - plt.plot(x, y) is used to draw points (markers) or lines
#   in a diagram.
# - By default, plot() draws a line from point to point.
# - To plot only markers (no line), use a 3rd argument 'o'.

# sub-point: plotting x and y points
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)
plt.show()

# sub-point: plotting markers only (no line)
plt.plot(xpoints, ypoints, 'o')
plt.show()

# sub-point: plotting multiple points
xpoints3 = np.array([1, 2, 6, 8])
ypoints3 = np.array([3, 8, 1, 10])
plt.plot(xpoints3, ypoints3)
plt.show()


# ----------------------------------------------------------
# Matplotlib Markers
# ----------------------------------------------------------
# - Markers emphasize each individual point on a line plot.
# - Use keyword argument 'marker' to set marker type.
#
# ---- FULL Marker Reference ----
# 'o' Circle        '*' Star          '.' Point         ',' Pixel
# 'x' X             'X' X (filled)    '+' Plus          'P' Plus (filled)
# 's' Square        'D' Diamond       'd' Diamond (thin)
# 'p' Pentagon      'H' Hexagon       'h' Hexagon
# 'v' Triangle Down '^' Triangle Up   '<' Triangle Left '>' Triangle Right
# '1' Tri Down      '2' Tri Up        '3' Tri Left      '4' Tri Right
# '|' Vline         '_' Hline
#
# ---- Line Reference (for fmt string) ----
# '-' Solid   ':' Dotted   '--' Dashed   '-.' Dashed/dotted
# (leave out the line value to plot markers only, no line)
#
# ---- Color Reference (for fmt string) ----
# 'r' Red  'g' Green  'b' Blue  'c' Cyan
# 'm' Magenta  'y' Yellow  'k' Black  'w' White

ypoints4 = np.array([3, 8, 1, 10])
plt.plot(ypoints4, marker='o')      # sub-point: circle marker
plt.show()

plt.plot(ypoints4, marker='*')      # sub-point: star marker
plt.show()

# sub-point: a few more markers from the full reference table
plt.plot(ypoints4, marker='P')      # plus (filled)
plt.show()
plt.plot(ypoints4, marker='1')      # tri down
plt.show()
plt.plot(ypoints4, marker='|')      # vline
plt.show()

# sub-point: fmt shorthand format string 'marker|line|color'
plt.plot(ypoints4, 'o:r')   # circle marker, dotted line, red color
plt.show()

# sub-point: fmt with no line value -> markers only, no connecting line
plt.plot(ypoints4, 'o')
plt.show()

# sub-point: marker size using markersize (or ms)
plt.plot(ypoints4, marker='o', ms=20)
plt.show()

# sub-point: marker edge color using markeredgecolor (or mec)
plt.plot(ypoints4, marker='o', ms=20, mec='r')
plt.show()

# sub-point: marker face color using markerfacecolor (or mfc)
plt.plot(ypoints4, marker='o', ms=20, mfc='r')
plt.show()

# sub-point: both mec and mfc together colors the whole marker
plt.plot(ypoints4, marker='o', ms=20, mec='r', mfc='r')
plt.show()

# sub-point: using hex color values for edge and face
plt.plot(ypoints4, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')
plt.show()

# sub-point: using any of the 140 supported named colors (e.g. hotpink)
plt.plot(ypoints4, marker='o', ms=20, mec='hotpink', mfc='hotpink')
plt.show()


# ----------------------------------------------------------
# Matplotlib Line
# ----------------------------------------------------------
# - Use keyword argument 'linestyle' (or 'ls') to change line style.
# - Styles: 'solid'/'-', 'dotted'/':', 'dashed'/'--', 'dashdot'/'-.',
#   'None'/'' (no line at all).
# - Use 'color' (or 'c') to set line color.
# - Use 'linewidth' (or 'lw') to set line width.
# - plt.plot() can plot multiple lines by using multiple
#   plt.plot() calls before plt.show(), or by passing pairs of
#   x,y arrays.

ypoints5 = np.array([3, 8, 1, 10])
plt.plot(ypoints5, linestyle='dotted')    # sub-point: dotted line
plt.show()

plt.plot(ypoints5, ls='-.')                # sub-point: dashdot shorthand
plt.show()

plt.plot(ypoints5, ls='None', marker='o')   # sub-point: no line, markers only
plt.show()

plt.plot(ypoints5, color='r')               # sub-point: line color
plt.show()

plt.plot(ypoints5, c='#4CAF50')              # sub-point: hex line color
plt.show()

plt.plot(ypoints5, linewidth='20.5')          # sub-point: line width
plt.show()

# sub-point: multiple lines with two separate plot() calls
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()

# sub-point: multiple lines by passing x1,y1,x2,y2
x1 = np.array([0, 1, 2, 3])
y1b = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2b = np.array([6, 2, 7, 11])
plt.plot(x1, y1b, x2, y2b)
plt.show()


# ----------------------------------------------------------
# Matplotlib Labels
# ----------------------------------------------------------
# - plt.title() sets the title of the plot.
# - plt.xlabel() and plt.ylabel() set axis labels.
# - fontdict parameter customizes label/title font.
# - loc parameter in title() positions the title ('left','right','center').

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")     # sub-point: title
plt.xlabel("Average Pulse")         # sub-point: x-axis label
plt.ylabel("Calorie Burnage")        # sub-point: y-axis label
plt.show()

# sub-point: styling title/labels with fontdict
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
plt.plot(x, y)
plt.title("Sports Watch Data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.show()

# sub-point: positioning the title with loc
plt.plot(x, y)
plt.title("Sports Watch Data", loc='left')
plt.show()


# ----------------------------------------------------------
# Matplotlib Grid
# ----------------------------------------------------------
# - plt.grid() adds gridlines to the plot.
# - axis parameter controls which grid lines: 'x', 'y', or 'both' (default).
# - Additional kwargs (color, linestyle, linewidth) style the grid.

plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid()               # sub-point: default grid (both axes)
plt.show()

plt.plot(x, y)
plt.grid(axis='x')       # sub-point: grid lines for x-axis only
plt.show()

plt.plot(x, y)
plt.grid(axis='y')       # sub-point: grid lines for y-axis only
plt.show()

plt.plot(x, y)
plt.grid(color='green', linestyle='--', linewidth=0.5)  # sub-point: styled grid
plt.show()


# ----------------------------------------------------------
# Matplotlib Subplot
# ----------------------------------------------------------
# - plt.subplot(rows, columns, index) lets you draw multiple
#   plots in one figure.
# - plt.suptitle() sets a title for the whole figure (all subplots).
# - subplot() index starts at 1 (not 0).

x1s = np.array([0, 1, 2, 3])
y1s = np.array([3, 8, 1, 10])
x2s = np.array([0, 1, 2, 3])
y2s = np.array([10, 20, 30, 40])

# sub-point: 1 row, 2 columns - first plot
plt.subplot(1, 2, 1)
plt.plot(x1s, y1s)
plt.title("Plot 1")

# sub-point: 1 row, 2 columns - second plot
plt.subplot(1, 2, 2)
plt.plot(x2s, y2s)
plt.title("Plot 2")
plt.show()

# sub-point: 2 rows, 1 column - grid of subplots (vertical stack)
plt.subplot(2, 1, 1)
plt.plot(x1s, y1s)
plt.subplot(2, 1, 2)
plt.plot(x2s, y2s)
plt.suptitle("My Subplots")   # sub-point: overall figure title
plt.show()

# sub-point: 2x2 grid of subplots
x3s = np.array([0, 1, 2, 3])
y3s = np.array([3, 8, 1, 10])
plt.subplot(2, 2, 1)
plt.plot(x1s, y1s)
plt.title("Plot 1")
plt.subplot(2, 2, 2)
plt.plot(x2s, y2s)
plt.title("Plot 2")
plt.subplot(2, 2, 3)
plt.plot(x3s, y3s)
plt.title("Plot 3")
plt.subplot(2, 2, 4)
plt.plot(x2s, y1s)
plt.title("Plot 4")
plt.show()


# ----------------------------------------------------------
# Matplotlib Scatter
# ----------------------------------------------------------
# - plt.scatter(x, y) draws a scatter plot (dots for each observation).
# - color parameter can set a single color or an array of colors per point.
# - colormap ('cmap') can color points based on values, use with 'c'.
# - plt.colorbar() shows the colormap scale.
# - 's' parameter sets sizes of dots (can be an array for varying sizes).
# - 'alpha' parameter sets transparency (0 to 1).

x_sc = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y_sc = np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x_sc, y_sc)   # sub-point: basic scatter plot
plt.show()

# sub-point: compare two scatter plots (different datasets, colors)
x1_sc = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y1_sc = np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86])
x2_sc = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y2_sc = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x1_sc, y1_sc, color='hotpink')
plt.scatter(x2_sc, y2_sc, color='#88c999')
plt.show()

# sub-point: color each dot using an array of colors
colors = np.array(["red", "green", "blue", "yellow", "pink",
                    "black", "orange", "purple", "beige", "brown",
                    "gray", "cyan", "magenta"])
plt.scatter(x_sc, y_sc, c=colors)
plt.show()

# sub-point: colormap - color dots by value using cmap + colorbar
colors2 = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x_sc, y_sc, c=colors2, cmap='viridis')
plt.colorbar()
plt.show()

# sub-point: size of the dots using 's' (array of sizes)
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
plt.scatter(x_sc, y_sc, s=sizes)
plt.show()

# sub-point: transparency using 'alpha'
plt.scatter(x_sc, y_sc, s=sizes, alpha=0.5)
plt.show()


# ----------------------------------------------------------
# Matplotlib Bars
# ----------------------------------------------------------
# - plt.bar(x, y) creates a vertical bar chart.
# - plt.barh(x, y) creates a horizontal bar chart.
# - 'color' sets bar color(s).
# - 'width' sets bar width (bar() only, default 0.8).
# - 'height' sets bar height (barh() only, default 0.8).

x_bar = np.array(["A", "B", "C", "D"])
y_bar = np.array([3, 8, 1, 10])
plt.bar(x_bar, y_bar)    # sub-point: vertical bar chart
plt.show()

plt.barh(x_bar, y_bar)   # sub-point: horizontal bar chart
plt.show()

plt.bar(x_bar, y_bar, color='red')   # sub-point: bar color
plt.show()

plt.bar(x_bar, y_bar, width=0.1)      # sub-point: bar width (vertical)
plt.show()

plt.barh(x_bar, y_bar, height=0.1)     # sub-point: bar height (horizontal)
plt.show()


# ----------------------------------------------------------
# Matplotlib Histograms
# ----------------------------------------------------------
# - A histogram is a graph showing frequency distributions.
# - plt.hist() creates a histogram; it uses np.histogram() internally.
# - Each bar groups numbers into ranges ("bins").
# - Bars are taller where there are more data points in that range.

x_hist = np.random.normal(170, 10, 250)   # random normal distribution
plt.hist(x_hist)   # sub-point: basic histogram
plt.show()

# sub-point: controlling number of bins
plt.hist(x_hist, bins=5)
plt.show()

# sub-point: adding a title to a histogram
plt.hist(x_hist)
plt.title("Normal Data Distribution")
plt.show()


# ----------------------------------------------------------
# Matplotlib Pie Charts
# ----------------------------------------------------------
# - plt.pie(y) creates a pie chart from an array of values.
# - By default, first wedge starts at the x-axis and moves counterclockwise.
# - 'labels' parameter names each wedge.
# - 'startangle' rotates the starting point of the first wedge.
# - 'explode' pulls a wedge out from the pie for emphasis.
# - 'shadow' adds a shadow effect.
# - 'colors' sets custom colors for wedges.
# - plt.legend() shows a legend for the wedges.

y_pie = np.array([35, 25, 25, 15])
plt.pie(y_pie)   # sub-point: basic pie chart
plt.show()

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y_pie, labels=mylabels)   # sub-point: labels
plt.show()

plt.pie(y_pie, labels=mylabels, startangle=90)   # sub-point: start angle
plt.show()

myexplode = [0.2, 0, 0, 0]
plt.pie(y_pie, labels=mylabels, explode=myexplode)   # sub-point: explode a wedge
plt.show()

plt.pie(y_pie, labels=mylabels, explode=myexplode, shadow=True)  # sub-point: shadow
plt.show()

mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y_pie, labels=mylabels, colors=mycolors)   # sub-point: custom colors
plt.show()

plt.pie(y_pie, labels=mylabels)
plt.legend(title="Four Fruits:")   # sub-point: legend with title
plt.show()


# ==========================================================
# EXTRA TOPICS (BONUS - beyond the official tutorial)
# ==========================================================

# ----------------------------------------------------------
# Matplotlib Figure & Axes (Object-Oriented API)
# ----------------------------------------------------------
# - plt.plot() style is called the "pyplot" (state-based) interface.
# - The Object-Oriented (OO) interface uses explicit Figure and Axes
#   objects, which gives more control - recommended for complex plots.
# - plt.subplots() returns a (Figure, Axes) tuple.

fig, ax = plt.subplots()             # sub-point: create Figure and single Axes
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title("OO API Example")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()

fig, axs = plt.subplots(2, 2)         # sub-point: create Figure with 2x2 Axes grid
axs[0, 0].plot([1, 2, 3], [1, 2, 3])
axs[0, 1].plot([1, 2, 3], [3, 2, 1])
axs[1, 0].plot([1, 2, 3], [1, 4, 9])
axs[1, 1].plot([1, 2, 3], [9, 4, 1])
plt.show()

fig2 = plt.figure(figsize=(8, 4))      # sub-point: set figure size (width, height in inches)
ax2 = fig2.add_subplot(111)             # sub-point: add_subplot alternative to subplot()
ax2.plot([1, 2, 3])
plt.show()


# ----------------------------------------------------------
# Matplotlib Legend
# ----------------------------------------------------------
# - plt.legend() shows a legend describing each plotted line/series.
# - 'label' parameter in plot() names the series for the legend.
# - 'loc' parameter positions the legend.

x_leg = np.array([0, 1, 2, 3])
plt.plot(x_leg, x_leg**2, label='y = x^2')     # sub-point: labeled line
plt.plot(x_leg, x_leg**3, label='y = x^3')      # sub-point: another labeled line
plt.legend()                                      # sub-point: basic legend
plt.show()

plt.plot(x_leg, x_leg**2, label='y = x^2')
plt.legend(loc='upper left')                      # sub-point: legend position
plt.show()

plt.plot(x_leg, x_leg**2, label='y = x^2')
plt.legend(title="Functions", fontsize=10)         # sub-point: legend title + fontsize
plt.show()


# ----------------------------------------------------------
# Matplotlib Saving Figures
# ----------------------------------------------------------
# - plt.savefig() saves the current figure to a file.
# - Common formats: .png, .jpg, .pdf, .svg
# - 'dpi' controls resolution; 'bbox_inches="tight"' trims whitespace.

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Saved Figure Example")
plt.savefig('my_plot.png')                  # sub-point: save as PNG
plt.savefig('my_plot.pdf')                   # sub-point: save as PDF
plt.savefig('my_plot_hd.png', dpi=300)        # sub-point: high resolution
plt.savefig('my_plot_tight.png', bbox_inches='tight')  # sub-point: trim whitespace
plt.show()


# ----------------------------------------------------------
# Matplotlib Text & Annotations
# ----------------------------------------------------------
# - plt.text(x, y, s) places arbitrary text at a data coordinate.
# - plt.annotate() adds text with an optional arrow pointing to a point.

x_ann = np.array([1, 2, 3, 4])
y_ann = np.array([10, 20, 25, 30])
plt.plot(x_ann, y_ann)
plt.text(2, 20, "Midpoint")                # sub-point: simple text label
plt.show()

plt.plot(x_ann, y_ann)
plt.annotate('Peak', xy=(4, 30), xytext=(2, 28),   # sub-point: annotate with arrow
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()


# ----------------------------------------------------------
# Matplotlib Axis Scale (Log Scale)
# ----------------------------------------------------------
# - plt.xscale() / plt.yscale() change the axis scale.
# - Useful for data spanning several orders of magnitude.

x_log = np.linspace(1, 1000, 100)
y_log = x_log ** 2
plt.plot(x_log, y_log)
plt.yscale('log')     # sub-point: logarithmic y-axis
plt.title("Log Scale Y-Axis")
plt.show()

plt.plot(x_log, y_log)
plt.xscale('log')      # sub-point: logarithmic x-axis
plt.yscale('log')       # sub-point: logarithmic both axes
plt.show()


# ----------------------------------------------------------
# Matplotlib Twin Axes (Dual Y-Axis)
# ----------------------------------------------------------
# - ax.twinx() creates a second y-axis sharing the same x-axis.
# - Useful for comparing two different scales on one plot.

fig3, ax1 = plt.subplots()
x_tw = np.arange(0, 10, 1)
ax1.plot(x_tw, x_tw, 'g-')
ax1.set_ylabel('Linear (green)', color='g')

ax1b = ax1.twinx()                          # sub-point: create twin axis
ax1b.plot(x_tw, x_tw**2, 'b-')
ax1b.set_ylabel('Squared (blue)', color='b')
plt.show()


# ----------------------------------------------------------
# Matplotlib Style Sheets
# ----------------------------------------------------------
# - plt.style.use() applies a built-in visual theme to all plots.
# - plt.style.available lists all available styles.

print(plt.style.available[:5])   # sub-point: view some available styles

plt.style.use('ggplot')           # sub-point: apply the 'ggplot' style
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("ggplot Style")
plt.show()

plt.style.use('default')           # sub-point: reset back to default style


# ----------------------------------------------------------
# Matplotlib Colormaps
# ----------------------------------------------------------
# - Colormaps map numeric values to colors, used with 'cmap' parameter.
# - Common colormaps: 'viridis', 'plasma', 'coolwarm', 'jet', 'gray'.

data_cmap = np.random.rand(10, 10)
plt.imshow(data_cmap, cmap='viridis')   # sub-point: heatmap-style image with colormap
plt.colorbar()
plt.title("Colormap Example")
plt.show()


# ----------------------------------------------------------
# Matplotlib Heatmaps
# ----------------------------------------------------------
# - plt.imshow() displays 2D data as a color-coded grid (heatmap).

heat_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
plt.imshow(heat_data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Simple Heatmap")
plt.show()


# ----------------------------------------------------------
# Matplotlib Box Plots
# ----------------------------------------------------------
# - plt.boxplot() shows the distribution of data via quartiles (box-and-whisker).

box_data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(box_data, labels=['Std=1', 'Std=2', 'Std=3'])
plt.title("Box Plot Example")
plt.show()


# ----------------------------------------------------------
# Matplotlib Stack Plots
# ----------------------------------------------------------
# - plt.stackplot() shows multiple series stacked on top of each other.

x_stack = [1, 2, 3, 4, 5]
y1_stack = [1, 2, 3, 4, 5]
y2_stack = [2, 3, 4, 5, 6]
y3_stack = [1, 1, 2, 2, 3]
plt.stackplot(x_stack, y1_stack, y2_stack, y3_stack, labels=['A', 'B', 'C'])
plt.legend(loc='upper left')
plt.title("Stack Plot Example")
plt.show()


# ----------------------------------------------------------
# Matplotlib Error Bars
# ----------------------------------------------------------
# - plt.errorbar() plots data points with uncertainty/error ranges.

x_err = np.arange(0, 5, 1)
y_err = np.array([1, 2, 1.5, 3, 2.5])
error = np.array([0.2, 0.4, 0.3, 0.5, 0.2])
plt.errorbar(x_err, y_err, yerr=error, fmt='o-', capsize=5)
plt.title("Error Bar Example")
plt.show()


# ----------------------------------------------------------
# Matplotlib Polar Plots
# ----------------------------------------------------------
# - Polar plots use angle and radius instead of x and y.
# - Created via plt.subplot(projection='polar').

theta = np.linspace(0, 2 * np.pi, 100)
r = np.abs(np.sin(2 * theta))
plt.subplot(projection='polar')
plt.plot(theta, r)
plt.title("Polar Plot Example")
plt.show()


# ----------------------------------------------------------
# Matplotlib 3D Plotting
# ----------------------------------------------------------
# - The mplot3d toolkit enables 3D plots via projection='3d'.

from mpl_toolkits.mplot3d import Axes3D   # sub-point: required import for 3D plotting

fig4 = plt.figure()
ax3d = fig4.add_subplot(projection='3d')    # sub-point: create 3D axes
x3 = np.random.standard_normal(100)
y3 = np.random.standard_normal(100)
z3 = np.random.standard_normal(100)
ax3d.scatter(x3, y3, z3)                     # sub-point: 3D scatter plot
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')
plt.title("3D Scatter Plot")
plt.show()

fig5 = plt.figure()
ax3d2 = fig5.add_subplot(projection='3d')
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)
z_line = np.cos(x_line)
ax3d2.plot(x_line, y_line, z_line)            # sub-point: 3D line plot
plt.title("3D Line Plot")
plt.show()


# ----------------------------------------------------------
# Matplotlib More Plot Types
# ----------------------------------------------------------

# --- Violin Plot ---
# - plt.violinplot() shows the full distribution shape (like a
#   smoothed, mirrored histogram) instead of just quartiles like boxplot.
violin_data = [np.random.normal(0, std, 200) for std in range(1, 4)]
plt.violinplot(violin_data, showmeans=True, showmedians=True)
plt.title("Violin Plot Example")
plt.show()

# --- Hexbin Plot ---
# - plt.hexbin() bins 2D points into hexagons, colored by density.
# - Useful for scatter plots with too many overlapping points.
x_hex = np.random.normal(0, 1, 5000)
y_hex = np.random.normal(0, 1, 5000)
plt.hexbin(x_hex, y_hex, gridsize=30, cmap='Blues')
plt.colorbar(label='count in bin')
plt.title("Hexbin Plot Example")
plt.show()

# --- Contour Plot ---
# - plt.contour() / plt.contourf() draw contour lines/filled regions
#   for a function of two variables (like a topographic map).
x_c = np.linspace(-5, 5, 100)
y_c = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_c, y_c)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z, cmap='viridis')       # sub-point: contour lines only
plt.title("Contour Plot Example")
plt.show()

plt.contourf(X, Y, Z, cmap='viridis')       # sub-point: filled contour
plt.colorbar()
plt.title("Filled Contour Plot Example")
plt.show()

# --- Quiver Plot (Vector Field) ---
# - plt.quiver() draws arrows representing vector direction/magnitude.
x_q, y_q = np.meshgrid(np.arange(0, 5, 1), np.arange(0, 5, 1))
u_q = np.cos(x_q)
v_q = np.sin(y_q)
plt.quiver(x_q, y_q, u_q, v_q)
plt.title("Quiver Plot Example")
plt.show()

# --- Streamplot (Flow Lines) ---
# - plt.streamplot() draws continuous flow lines through a vector field.
x_s = np.linspace(-3, 3, 100)
y_s = np.linspace(-3, 3, 100)
X_s, Y_s = np.meshgrid(x_s, y_s)
U_s = -Y_s
V_s = X_s
plt.streamplot(X_s, Y_s, U_s, V_s, density=1.2)
plt.title("Streamplot Example")
plt.show()

# --- Stem Plot ---
# - plt.stem() draws discrete data points connected to a baseline
#   with vertical lines (used for discrete/digital signals).
x_stem = np.arange(0, 10, 1)
y_stem = np.sin(x_stem)
plt.stem(x_stem, y_stem)
plt.title("Stem Plot Example")
plt.show()

# --- Step Plot ---
# - plt.step() draws data as a series of horizontal steps instead
#   of connecting points with straight diagonal lines.
x_step = np.arange(0, 10, 1)
y_step = np.array([2, 3, 5, 4, 6, 5, 7, 8, 6, 9])
plt.step(x_step, y_step, where='mid')
plt.title("Step Plot Example")
plt.show()

# --- Fill Between (Area Plot) ---
# - plt.fill_between() fills the area between a curve and a baseline
#   (or between two curves) - useful for highlighting a range.
x_fb = np.linspace(0, 10, 100)
y_fb = np.sin(x_fb)
plt.plot(x_fb, y_fb)
plt.fill_between(x_fb, y_fb, 0, alpha=0.3)   # sub-point: fill under curve
plt.title("Fill Between Example")
plt.show()

y_fb2 = np.cos(x_fb)
plt.plot(x_fb, y_fb, x_fb, y_fb2)
plt.fill_between(x_fb, y_fb, y_fb2, alpha=0.3)   # sub-point: fill between 2 curves
plt.title("Fill Between Two Curves")
plt.show()

# --- pcolormesh (Pseudocolor Mesh) ---
# - plt.pcolormesh() draws a 2D grid of colored cells based on values,
#   similar to imshow but works well with non-uniform/irregular grids.
Z_pc = np.random.rand(10, 10)
plt.pcolormesh(Z_pc, cmap='coolwarm')
plt.colorbar()
plt.title("Pcolormesh Example")
plt.show()


# ==========================================================
# END OF NOTES
# ==========================================================