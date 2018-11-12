import numpy as np

sampleX = np.genfromtxt("q7_X.dat", dtype="double", delimiter="\n")
sampleY = np.genfromtxt("q7_Y.dat", dtype="double", delimiter="\n")

meanX = np.mean(sampleX)
meanY = np.mean(sampleY)
print("Sample mean: ", meanX, meanY)

varX = np.var(sampleX)
varY = np.var(sampleY)
print("Sample variance: ", varX, varY)

W = (meanX - meanY)/np.sqrt((varX + varY)/1000)
print("W = ", W)