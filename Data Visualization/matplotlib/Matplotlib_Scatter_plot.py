"""
    The idea of scatter plots is usually to compare two variables, or three if you are plotting
    in 3 dimensions, looking for correlation or groups.
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label= 'skitscat', s=25, marker= "o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph')
plt.legend()
plt.show()

"""
    The plt.scatter allows us to not only plot on x and y, but it also lets us decide
    on the color, size, and type of marker we use.
"""