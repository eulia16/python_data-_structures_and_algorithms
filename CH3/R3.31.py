#plotting the functions 8n, 4nlogn, 2n^2, n^3, and 2^n
import pylab
import math
import matplotlib.pyplot as plt
eightN = [i * 8 for i in range(10)]
logN = [4 * i * math.log(i) for i in range(10) if i >=1]
twoN = [2 * i ** 2 for i in range(10)]
threeN = [i**3 for i in range(10)]
exponential = [2 ** i for i in range(10)]

fig = plt.figure()
ax = fig.add_subplot(2,1,1)

ax.set_yscale("log")
ax.set_xscale("log")
ax.plot(eightN)
ax.plot(logN)
ax.plot(twoN)
ax.plot(threeN)
ax.plot(exponential)

pylab.show()
