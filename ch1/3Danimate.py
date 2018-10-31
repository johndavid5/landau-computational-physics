""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# 3Danimate.py:  3-D animation of circular polarized EM Wave 

from visual import *                           # import graphics routines

xmax = 201                                      # number of x,y points
scene = display(x=0, y=0, width= 500, height= 500, title= 'sin(6pi*x/201-t)',
              background=(1.,1.,1.0), forward=(-0.6,-0.5,-1), range=400)    
sinWave = curve(color=color.yellow, radius=4.5)
cosWave = curve(color=color.red, radius=4.5)
Xaxis   = curve(pos=[(-300,0,0),(300,0,0)], color=color.blue)  
t = 0                             # initial time
dt = 0.02                           
arr = arrow(color=color.orange)    # arrows for electric field
arr2 = arrow(color=color.orange)
arr3 = arrow(color=color.orange)
x1 = pi/3                           # arrow1 x position
x2 = 5*pi/6                         
x3 = pi/7                           # arrow3 x position
while True:
    rate(10)                       # limit < 200 iterations/s
    x = arange(0, pi, pi/xmax)       
    xp = 200*x-300                  # screen coordinates
    yp = 100*sin(6*x-t)         
    zp = 100*cos(6*x-t) 
    sinWave.x = xp                   
    sinWave.y = yp                  
    cosWave.x = xp                   
    cosWave.z = zp                   
    x1p = x1*200-300            # linear transformation for arrow pos.
    x2p = x2*200-300                  
    x3p = x3*200-300
    arr.pos = vector(x1p,0,0) 
    arr2.pos = vector(x2p,0,0)
    arr3.pos = vector(x3p,0,0)
    arr.axis = vector(0,100*sin(6*x1-t),100*cos(6*x1-t))  # arrow axis
    arr2.axis = vector(0,100*sin(6*x2-t),100*cos(6*x2-t))
    arr3.axis = vector(0,100*sin(6*x3-t),100*cos(6*x3-t))
    t += dt                         
