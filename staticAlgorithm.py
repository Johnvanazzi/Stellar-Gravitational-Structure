import math_methods as meth
import numpy as np
import gr_Functions.nonRotational as static

def staticTOV(initialParameters, outputPath, eosPath):  
  r = [initialParameters.get("radius")]
  m = [initialParameters.get("mass")]
  eps = [initialParameters.get("eps")]
  potential = [initialParameters.get("potential")]
  step = initialParameters.get("step")
  eosData = np.loadtxt(eosPath, delimiter=" ")
  
  p = [meth.logInterpolation(eps[0], eosData[:,0], eosData[:,1])]

  file = open(outputPath, "w+")
  i = 0

  while (p[i] > 0.0):
    m.append(meth.rungeKutta(step, r[i], m[i], static.mass, [eps[i]], type=0))
    p.append(meth.rungeKutta(step, r[i], p[i], static.pressure, [eps[i], m[i]], type=1))
    potential.append(meth.rungeKutta(step, r[i], potential[i], static.potential, [p[i], m[i]], type=0))    
    eps.append(meth.logInterpolation(p[i], eosData[:,1], eosData[:,0]))
    r.append(r[i] + step)

    file.write("{:f}\t {:f}\t {:f}\t {:f}\t {:f}\n".format(r[i], m[i], p[i], eps[i], potential[i]))
    i += 1
  
  file.close()