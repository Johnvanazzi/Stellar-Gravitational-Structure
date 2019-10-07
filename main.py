import math_methods as mathmeth
import physical_functions as phys

eps = []
r = []
m = []
p = []

eps.insert(0, 0.1)
r.insert(0, 0.2)
m.insert(0, 0.01)
p.insert(0, 0)
delta = 0.2

for i in range(0, 10):

  m.append(mathmeth.rungeKutta(delta, r[i], m[i], phys.mass, [eps[i]], type=0))
  p.append(mathmeth.rungeKutta(delta, r[i], p[i], phys.pressure, [eps[i], m[i]], type=1))

  r.append(r[i] + delta)
  eps.append(phys.EoS(p[i+1]))

  print("{:f} {:f} {:f} {:f}".format(r[i], m[i], p[i], eps[i]))