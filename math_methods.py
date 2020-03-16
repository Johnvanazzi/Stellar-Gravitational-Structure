import numpy as np
from math import pow, log10

def rungeKutta(step, radius, mainQty, externFunction, args, **kwargs):
  methodStructure = kwargs.get('type')

  if (methodStructure == 0):
    q1 = externFunction(radius, *args)
    q2 = externFunction(radius + 0.5*step, *args)
    q3 = externFunction(radius + 0.5*step, *args)
    q4 = externFunction(radius + step, *args)

  if (methodStructure == 1):
    q1 = externFunction(radius, mainQty, *args)
    q2 = externFunction(radius + 0.5*step, mainQty + 0.5*q1, *args)
    q3 = externFunction(radius + 0.5*step, mainQty + 0.5*q2, *args)
    q4 = externFunction(radius + step, mainQty + 0.5*q3, *args)

  return mainQty + step*(q1 + 2*q2 + 2*q3 + q4)/6

def logInterpolation(x, xArray, yArray):
  i = np.searchsorted(xArray, x)  
  yLog10 = (log10(yArray[i]/yArray[i-1]))*(log10(x/xArray[i-1]))/(log10(xArray[i]/xArray[i-1])) + log10(yArray[i-1])

  return pow(10, yLog10)