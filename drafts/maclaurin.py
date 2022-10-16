from math import e, factorial
import numpy as np


fac = np.vectorize(factorial)

def e_x(x, terms):
    n = np.arange(terms)
    return (sum(x**n/fac(n)))
    
if __name__=='__main__':
    terms = 10
    x = 3
    print('Calculating e^{x} via Maclaurin Series'.format(x=x))
    print('Actual result: {}'.format(e**x))
    print('Maclaurin result: {}'.format(e_x(x,terms)))
    
    
    