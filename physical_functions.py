import numpy as np

def mass(r, eps):
	return 4*np.pi*eps*r*r

def pressure(r, p, eps, m):
	return -(eps+p)*(m+4*np.pi*r*r*r*p)/(r*r-2*m*r)

def EoS(p):
	return 3*p 