"""
    Seaborn is a wrapper around Maplolib that makes creating stastical plots easy.
    The list of supported plots includes univariate and bivariate distribution plots,
    regression plots, and a number of methods for plotting categorical variables.

    Creating a graph in seaborn is as simple as calling the appropriate graphing function.
    Here is an example of creating histogram, kernel density estimation, and rug plot for
    randomly generated data.
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate normally distributed data
data = np.random.randn(1000)

# Plot a histogram with both a rugplot and kde graph superimposed
sns.set_style('dark')
sns.distplot(data, kde= True, rug= True)
plt.xlabel("This is x-axis")
plt.ylabel("This is y-axis")
plt.show()