import staticAlgorithm as algorithm
import numpy as np
from inputs.config import initialParameters

filename="./inputs/EoS/apr.dat"
data = np.loadtxt(filename, delimiter=" ")

filePath = "./tables/static"
algorithm.staticTOV(initialParameters, filePath)