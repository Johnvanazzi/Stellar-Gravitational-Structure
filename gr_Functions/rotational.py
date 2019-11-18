import numpy as np
import math
import gr_Functions.nonRotational as nonRot

def lenseThirring (r, j, jPrime, omBar, omBarPrime):
  return - (4*j*omBarPrime + (r*omBarPrime + 4*omBar)*jPrime)/(r*j)

def m_0Prime(r, j, m, eps, p, obp, p0, ob, dedp):
  return 4*np.pi*(r**2)*(eps + p)*(dedp)*p0 + (r**4)*(obp*j)**2/12 + 8*np.pi*(r**5)*(eps + p)*(ob*j)**2/(3*r-6*m)

def p_0Prime(r, j, jPrime, m, eps, p, ob, obp, p0, m0):
  return -(1 + 8*np.pi*(r**2)*p)*m0/(r - 2*m)**2 - 4*np.pi*r*r*p0*(eps + p)/(r-2*m) + (r**4)*(j*obp)**2/(12*r-24*m)+ (3*j*ob	+ 2*r*jPrime*ob + 2*r*j*obp + r*j*ob*(8*np.pi*eps-1)/(r-2*m))*r*r*j*ob/(3*r-6*m)

def v_2Prime(r, j, jPrime, m, p, obp, ob, h2):
  phiprm = nonRot.potential(r, p, m)
  return - 2*phiprm*h2 + (1/r + phiprm)*((j*obp)**2*(r**4)/6 - 2*j*jPrime*(ob**2)*r**3/3)

def h_2Prime(r, j, jprim, m, eps, p, obp, ob, h2, v2):
  phiprm = nonRot.potential(r, p, m)
  return h2*( -2*phiprm + (4*np.pi*r*r*r*(eps+p)- 2*m)/(r*r*phiprm*(r-2*m))) - 2*v2/(phiprm*(r*r-2*m*r)) + (r*phiprm - 1/(2*phiprm*(r-2*m)))*j*j*obp*obp*r*r*r/6 - (r*phiprm + 1/(2*phiprm*(r-2*m)))*2*j*jprim*ob*ob*r*r/3	

def jota(r, phi, m):
  return math.exp(-phi)*math.sqrt(1.0-2*m/r)

def jota_Prime(r, phi, m, eps, p):
  return - 4*np.pi*r*math.exp(-phi)*(eps + p)/math.sqrt(1.0-2*m/r)
	