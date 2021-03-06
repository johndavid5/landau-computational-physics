from visual import *
from visual.graph import *

s_title = "red: sin(x), blue: cos(x), magenta: sin(x)*cos(x)"
graph1 = gdisplay(title=s_title, xtitle='x', ytitle='y', ymin = -2, ymax = 2)

y1 = gcurve(color=color.red) #curve
y2 = gcurve(color=color.blue) 
y3 = gcurve(color=color.magenta) 

for x in arange(-5, 5, 0.1):
	y1.plot( pos = (x, sin(x)) )
	y2.plot( pos = (x, cos(x)) )
	y3.plot( pos = (x, sin(x)*cos(x)) )
