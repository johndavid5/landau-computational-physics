from visual import * # must import visual or vis first
from visual.graph import *	# import graphing features 

f1 = gcurve(color=color.cyan)	# a graphics curve

for x in arange(0, 8.05, 0.1):	# x goes from 0 to 8
    f1.plot(pos=(x,5*cos(2*x)*exp(-0.2*x)))	# plot
