# Easy Visual.py

# reference: http://vpython.org/contents/docs/graph.html
# added in: must import visual or vis first before visual.graph...
from visual import *

from visual.graph import *	# import graphing features

plotsky1 = gcurve(color = color.white) # gcurve method

for x in arange(0.0, 8.1, 0.1):
     plotsky1.plot(pos=(x,5*cos(2*x)*exp(-0.4*x))) # Plot points

PI=3.14159

# Use gdisplay plotting object before you create a
# gcurve graph object to set size, position, title,
# title for x-axis, title for y-axis, max and mins, etc.
graph2 = gdisplay( width = 600, height = 450,\
	title = 'Visual 2D Plot', xtitle = 'x ', ytitle='cos(x)',\
	foreground = color.black, background = color.white )

plotsky2 = gdots( color = color.black )  # Dots 

for x in arange( -5.0 , +5.0, 0.1 ):
	plotsky2.plot( pos = (x, cos(x)))
