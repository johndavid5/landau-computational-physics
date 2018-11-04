# Easy Visual.py

# http://vpython.org/contents/docs/graph.html
from visual import * # must import visual or vis first (Prof. Landau forgot to do this.)
from visual.graph import *	# import graphing features

plotsky1 = gcurve(color = color.white) # gcurve method

for x in arange(0.0, 8.1, 0.1):
     plotsky1.plot(pos=(x,5*cos(2*x)*exp(-0.4*x))) # Plot points


graph1 = gdisplay( width = 600, height = 450,\
	title = 'Visual 2D Plot', xtitle = 'x ', ytitle='f(x)',\
	foreground = color.black, background = color.white ) 

plotsky2 = gdots( color = color.black )  # Dots 

for x in arange( -5.0 , +5.0, 0.1 ):
	plotsky2.plot( pos = (x, cos(x)))
