from visual import *
from visual.graph import *

string = "blue: sin^2(x), white: cos^2(x), red: sin(x)*cos(x)"
graph1 = gdisplay(title=string, xtitle='x', ytitle='y')

y1 = gcurve(color=color.blue, delta = 3) #curve
y2 = gvbars(color=color.white) #vertical bars
y3 = gdots( color=color.red, delta = 3) #dots

for x in arange(-5, 5, 0.1):
	y1.plot( pos = (x, sin(x)*sin(x)) )
	y2.plot( pos = (x, cos(x)*cos(x)/3.0) )
	y3.plot( pos = (x, sin(x)*cos(x)) )
