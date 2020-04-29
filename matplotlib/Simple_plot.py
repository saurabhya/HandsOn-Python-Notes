# Launching a simple plot

import numpy as np
import matplotlib.pyplot as plt

# angle varying between 0 and 2*np.pi
x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)

plt.plot(x, y)
plt.show()