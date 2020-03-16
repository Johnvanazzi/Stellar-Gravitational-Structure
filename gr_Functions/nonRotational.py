import numpy as np

def mass(radius, energyDensity):
	return 4*np.pi*energyDensity*(radius**2)

def pressure(radius, pressure, energyDensity, mass):
	return -(energyDensity + pressure)*(mass + 4*np.pi*(radius**3)*pressure)/(radius**2-2*mass*radius)

def potential(radius, pressure, mass):
	return (mass+4*np.pi*(radius**3)*pressure)/(radius**2-2*mass*radius)
