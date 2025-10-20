import matplotlib.pyplot as plt

xValues = [1, 2, 3, 4]
yValues1 = [1, 2, 3, 4]

plt.plot(xValues, yValues1, 'b-', label = 'First plot')
            
yValues2 = [1, 7, 3, 5]
            
plt.plot(xValues, yValues2, 'r--', label = 'Second plot')

plt.legend()

plt.show()
