""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""                                                       

# EasyMatPlot.py:                 Simple use of matplotlib's plot command 
from pylab import *           # Load Matplotlib

Xmin = -5.0;        Xmax = +5.0;      Npoints= 500
DelX= (Xmax-Xmin)/Npoints                                      # Delta x
x = arange(Xmin, Xmax, DelX)      # Form x array in range with increment 
y =  sin(x)*sin(x*x)              # y array = function of x array

print ('arange => x[0], x[1],x[499]=%8.2f %8.2f %8.2f' %(x[0],x[1],x[499]))
print ('arange => y[0], y[1],y[499]=%8.2f %8.2f %8.2f' %(y[0],y[1],y[499]))
print ("\n Now doing the plotting thing, look for Figure 1 on desktop" )                                                                                       
xlabel('x');      ylabel('f(x)');     title(' f(x) vs x')        # labels
text(-1.85,  0.75, 'MatPlotLib Example')                     # Text on plot
plot(x, y, '-', lw=2)                                                      
grid(True)                                                    # Form grid
show()                                                 # Make screen plot
