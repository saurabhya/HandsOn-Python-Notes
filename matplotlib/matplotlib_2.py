"""
    Plots with common Y-axis and different X-axis using twiny()
"""

import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(0, 2.0*np.pi, 101)
x1 = np.sin(y)
x2 = np.sinh(y)

# values for making ticks in x and y axis
ynumbers = np.linspace(0, 7, 15)
xnumbers1 = np.linspace(-1, 1, 11)
xnumbers2 = np.linspace(0, 300, 7)

# Separate the figure from the figure object and axes object from the plotting object
fig, ax1 = plt.subplots()

# Duplicate the axes with a different x axis and the same y axis
ax2 = ax1.twiny()

# plo the curves on axes 1 and 2, and get the axes handlers
curve1, = ax1.plot(x1, y, label="sin", color='r')
curve2, = ax2.plot(x2, y, label="sinh", color='b')

# Make a curves listto access the parameters in the curves
curves= [curve1, curve2]

# add legend via ax1 or ax2 object
ax2.legend(curves, [curve.get_label() for curve in curves])

# x axis labels via the axes
ax1.set_xlabel("Magnitude", color=curve1.get_color())
ax2.set_xlabel("Magnitude", color=curve2.get_color())

# y axis label via the axes
ax1.set_ylabel("Angle/Value", color=curve1.get_color())
# for ax2, it does not work because ax2 has no property  control over y axis

#y ticks - make them colored as well
ax1.tick_params(axis='y', colors=curve1.get_color())

# x axis ticks via the axes
ax1.tick_params(axis='x', colors=curve1.get_color())
ax2.tick_params(axis='x', colors=curve2.get_color())

# set x ticks
ax1.set_xticks(xnumbers1)
ax2.set_xticks(xnumbers2)

# set y ticks
ax1.set_yticks(ynumbers)

# To make grids using axes 2
ax1.grid(color=curve2.get_color())
ax2.grid(color=curve2.get_color())
ax1.xaxis.grid(False)

# Global figure properties
plt.title("Plot of sine and hyperbolic sine")
plt.show()