import math_methods as mathmeth
import gr_Functions.nonRotational as static

def staticTOV(initialParameters, filePath):  
  r = [initialParameters.get("radius")]
  m = [initialParameters.get("mass")]
  eps = [initialParameters.get("eps")]
  p = [initialParameters.get("pressure")]
  potential = [initialParameters.get("potential")]
  step = initialParameters.get("step")

  file = open(filePath, "w+")

  i = 0
  while (p[i] > 1e-4):
    m.append(mathmeth.rungeKutta(step, r[i], m[i], static.mass, [eps[i]], type=0))
    p.append(mathmeth.rungeKutta(step, r[i], p[i], static.pressure, [eps[i], m[i]], type=1))
    potential.append(mathmeth.rungeKutta(step, r[i], potential[i], static.potential, [p[i], m[i]], type=0))
    
    r.append(r[i] + step)
    eps.append(static.EoS(p[i+1]))

    file.write("{:f}\t {:f}\t {:f}\t {:f}\t {:f}\n".format(r[i], m[i], p[i], eps[i], potential[i]))
    i += 1
  
  file.close()