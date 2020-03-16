import staticAlgorithm as algorithm
import numpy as np
from inputs.config import initialParameters

eosPath="./inputs/EoS/apr.dat"
outputPath = "./tables/static"
algorithm.staticTOV(initialParameters, outputPath, eosPath)