
# integration by another form

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps,quad

def f(x):
    return (n/np.pi)*(1.0/(1+(n**2)*(x**2)))
def g(x):
    return f(1.0/x)*x**(-2)
n=10
x=np.linspace(-1.0,1.0,1000000)
print(simps(f(x),x)+simps(f(1/x)*x**(-2.0),x))
print(quad(f,-1,+1)[0]+quad(g,-1,+1,points=(0,))[0])
