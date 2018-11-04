# Easy Visual.py

# Note Visual Python's technique:
# 1. Create a plot object
# 2. Add points to the object, one by one
# reference: http://vpython.org/contents/docs/graph.html
# added in: must import visual or vis first before visual.graph...
from visual import *

from visual.graph import *	# import graphing features

# New: Added gdisplay for this first curve...
graph1 = gdisplay( 
	title = 'Visual 2D Curve', xtitle = 'x ', ytitle='5 cos(2x) e^(-0.4x)',\
	foreground = color.white, background = color.black )

# gcurve(): conntected curve based on points... 
plotsky1 = gcurve(color = color.white) # gcurve method

for x in arange(0.0, 8.1, 0.1):
     plotsky1.plot(pos=(x,5*cos(2*x)*exp(-0.4*x))) # Plot points

PI=3.14159

# Use gdisplay plotting object before you create a
# gcurve graph object to set size, position, title,
# title for x-axis, title for y-axis, max and mins, etc.
graph2 = gdisplay( width = 600, height = 550,\
	title = 'Visual 2D Plot', xtitle = 'x ', ytitle='cos(x)',\
	foreground = color.black, background = color.white,\
        xmin = -6.0, xmax = 6.0, ymin = -2, ymax = 2)

# gdots(): only points are plotted
plotsky2 = gdots( color = color.black )  # Dots 

for x in arange( -5.0 , +5.0, 0.1 ):
	plotsky2.plot( pos = (x, cos(x)))
