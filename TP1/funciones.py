import math

def funcion1(x):
    return x*x-2

def funcion2(x):
    return x*x*x*x*x-6.6*x*x*x*x+5.12*x*x*x+21.312*x*x-38.016*x+17.28

def funcion3(x):
    return (x-1.5)*math.exp(-4*(x-1.5)*(x-1.5))

def derivada1Funcion1(x):
    return 2*x

def derivada1Funcion2(x):
    return 5*x*x*x*x-26.4*x*x*x+15.36*x*x+42.624*x-38.016

def derivada1Funcion3(x):
    return (-8*x+12.0)*(x-1.5)*math.exp(-4*(x-1.5)*(x-1.5))+math.exp(-4*(x-1.5)*(x-1.5))

def derivada2Funcion1(x):
    return 2

def derivada2Funcion2(x):
    return 20*x*x*x-79.9*x*x+30.72*x+42.624

def derivada2Funcion3(x):
    return (-24*x+(x-1.5)*(8*x-12.0)*(8*x-12.0)+36.0)*math.exp(-4*(x-1.5)*(x-1.5))
    
funcion={1:funcion1,2:funcion2,3:funcion3}
derivada1Funcion={1:derivada1Funcion1,2:derivada1Funcion2,3:derivada1Funcion3}
derivada2Funcion={1:derivada2Funcion1,2:derivada2Funcion2,3:derivada2Funcion3}
