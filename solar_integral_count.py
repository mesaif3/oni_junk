from cmath import pi
import numpy as np
import sympy as sy

l44 = 0.5907
u44 = 2.5508
avg = 44.56
excess = 23.23

T = sy.Symbol("T")

def light(x):
    return 80*sy.sin(x)

def integrate(f,x, lower, upper):
    return sy.integrate(f(x), (x, lower, upper))

def average(lower, uppersin, upperrange, f=light, x=T):
    return integrate(f,x, lower, uppersin)/(upperrange-lower)



print((average(u44, pi, pi)*(pi-u44)+average(0, l44, l44)*(l44))/(pi-u44+(pi*(1/0.875-1))+l44))