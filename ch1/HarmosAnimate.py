# http://physics.oregonstate.edu/~landaur/Books/CPbook/Codes/PythonCodes/HarmosAnimate.py
""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# HarmosAnimate: Soltn of t-dependent Sch Eqt fro HO with animation

from visual import *

# initialize wave function, probability, potential
dx = 0.04;    dx2 = dx*dx;  k0 = 5.5*pi;  dt = dx2/20.0;  xmax = 6.0
xs = arange(-xmax,xmax+dx/2,dx)                    # array of x positions

g = display(width=500, height=250, title='Wave packet in HO Well')
PlotObj = curve(x=xs, color=color.yellow, radius=0.1)
g.center = (0,2,0)                                      # center of scene
                                         # initial condition; wave packet
psr = exp(-0.5*(xs/0.5)**2) * cos(k0*xs)           # Re wave function Psi
psi = exp(-0.5*(xs/0.5)**2) * sin(k0*xs)           # Im wave function Psi
v   = 15.0*xs**2

while True:
   rate(500)
   psr[1:-1] = psr[1:-1]-(dt/dx2)*(psi[2:]+psi[:-2]-2*psi[1:-1])+dt*v[1:-1]*psi[1:-1]
   psi[1:-1] = psi[1:-1]+(dt/dx2)*(psr[2:]+psr[:-2]-2*psr[1:-1])-dt*v[1:-1]*psr[1:-1]
   PlotObj.y = 4*(psr**2 + psi**2)
