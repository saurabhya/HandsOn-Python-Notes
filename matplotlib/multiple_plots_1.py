# Adding mulitple plots by superimposition
# Good for plot sharing similar x, y limits


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.cos(x)

# Values for making ticks in x and y axis
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)

plt.plot(x, y, 'r', x, z, 'g')
plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.title("Plot of trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend(['sine','cosine'])
plt.grid()
plt.axis([0, 6.5, -1.1, 1.1])
plt.show()