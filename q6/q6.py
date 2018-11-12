import numpy

sample = [1.87, 1.29, 2.01, 0.93, 1.02, 2.78, 2.33, 1.65, 0.50, 0.99]

x = numpy.mean(sample)
s = numpy.sqrt(numpy.var(sample))

print(x)
print(s)

t = ((x - 1.5) * numpy.sqrt(10))/s
print(t)
