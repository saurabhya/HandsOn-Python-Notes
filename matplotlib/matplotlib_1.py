"""
    Plots wih Common X-axis but different Y-axis using twinx()
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.sinh(x)

# Separate the figure object and the axes object from the plotting object
fig, ax1 = plt.subplots()

# Duplicate the axes with a different y axis and the same x axis
ax2 = ax1.twinx() # ax2, ax1 will have common x axis and different y axis

# plot the curves on axes 1, and 2, and get the curve handles
curve1, = ax1.plot(x, y, label="sin", color='r')
curve2, = ax2.plot(x, z, label="sinh", color='b')

# make a curves list to access the pararmeters in the curves
curves = [curve1, curve2]

# add legend via axes 1 or axes 2 object
# ax1.legend() will not show the legend of ax2
# ax2.legend() will not show the legend of ax1
ax1.legend(curves, [curve.get_label() for curve in curves])

# Global figure configuration
plt.title("PLot of sine and hyperbolic sine")
plt.show()