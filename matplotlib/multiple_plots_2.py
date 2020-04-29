# Adding mulitple plots by superimposition
# Good for plot sharing similar x, y limits
# differnt than mulitple_plots_1 and much preferred


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.cos(x)

# Values for making ticks in x and y axis
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)

plt.plot(x, y, color='r', label='sin')
plt.plot(x, z, color='g', label='cos')
plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.title("Plot of trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend()
plt.grid()
plt.axis([0, 6.5, -1.1, 1.1])
plt.show()