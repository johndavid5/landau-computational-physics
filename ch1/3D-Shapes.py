from visual import *
# from visual.graph import *

graph1 = display( width = 500, height = 500, \
	title = "VPython 3D Shapes", range = 10 \
	)

sphere( pos = (0,0,0), radius = 1, color = color.cyan )
sphere( pos = (0,1,-3), radius = 1.5, color = color.red )

arrow( pos = (3,2,2), axis = (3,1,1), color = color.green )

cylinder( pos = (-3,-2,3), axis = (6,-1,5), color = color.yellow )

cone( pos = (-6,-6,0), axis = (-2, 1, -0.5), radius = 2, color = (0.5, 0, 0.5 ) )

helix( pos = (-5,5,-2), axis = (5,0,0), radius = 2, thickness = 0.4, color = color.orange )

ring( pos=(-6, 1, 0), axis=(1,1,1), radius = 2, thickness = 0.3, \
  color = (0.3, 0.4, 0.6) )

box( pos = (5,-2,2), length = 5, width = 4, height = 1, color = (0.4, 0.8, 0.2) )

pyramid( pos = (2,5,2), size=(4,3,2), color=(0.7,0.7,0.2))
