import numpy as np

sampleX = np.genfromtxt("q7_X.dat", dtype="double", delimiter="\n")
sampleY = np.genfromtxt("q7_Y.dat", dtype="double", delimiter="\n")

sampleD = [sampleY[i] - sampleX[i] for i in range(len(sampleY) - 1)]
meanD = np.mean(sampleD)
print("Sample mean: ", meanD)

varD = np.var(sampleD)
print("Sample variance: ", varD)

T = (meanD)/np.sqrt(varD/1000)
print("T = ", T)