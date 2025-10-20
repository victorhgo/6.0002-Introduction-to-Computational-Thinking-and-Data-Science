import pylab

xValues = [1, 2, 3, 4]
yValues1 = [1, 2, 3, 4]
yValues2 = [1, 7, 3, 5]

pylab.plot(xValues, yValues1, 'b-', label = 'First Plot')
pylab.plot(xValues, yValues2, 'r--', label = 'Second Plot')
pylab.legend()

pylab.show()