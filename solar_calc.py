import numpy as np
from sympy import sin, cos, pi, symbols, integrate, N
from sympy.plotting import plot

#theta = t/(2*pi)

period = [-pi, pi]
intercepts = [num*3.5/8 for num in period]
order = range(1,10)
def f(theta, coeff=80, nth=1, shift=pi/2):
    period = 7/4
    freq = 1/period
    return coeff*sin((freq*nth*theta) + shift)

theta = symbols('theta')
n = symbols('n')
t = symbols('t')

fourier = integrate((2/(period[1]-period[0])*f(theta)*cos(n*theta)), (theta, intercepts[0], intercepts[1]))

Light = N(fourier.subs(n, 0))/2

for k in order:
    coeff = N(fourier.subs(n, k))
    Light += f(theta, coeff, k)

plot(Light.subs(theta, (t*(2*pi))), (t, 0, 6))
# for k in order:
#     kcoeff = N(fourier.subs(n, k))
#     if abs(kcoeff) > 0.5:
#         print(f'{k}: {kcoeff}')