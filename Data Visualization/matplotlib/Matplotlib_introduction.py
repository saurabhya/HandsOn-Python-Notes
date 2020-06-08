import matplotlib.pyplot as plt

"""
    This line imports the integral pyplot, which we're going to use throughout this entire series.
    we import pyplot as plt, and this is a tradition standard for python programs using pyplot.
"""
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14, 12]


plt.plot(x, y, label = 'First Line')
plt.plot(x2, y2, label= 'Second Line')

"""
    Next, we invoke the .plot method of pyplot to plot some coordinates. This .plot takes many parameters,
    but the first wo here are 'x' and 'y' coordinates, which we've placed lists into.
    This means, we have 3 coordinates according to these lists: 1,5,2,7 and 3,4.

    The plt.plot will "draw" this plot in the background, but we need to bring it to the screen when we're
    ready, after graphing everything we intend to.

    Parameter 'label' allows us to assign a name to the line, which we can later show in the legened.

"""

plt.xlabel('Plot Number')
plt.ylabel('Importnat var')
plt.title("Interesting Graph\nCheck it out")
plt.legend()
plt.show()

plt.show()

"""
With plt.xlabel and plt.ylabel, we can assign labels to those respective axis. Next, we can assign the
plt's title with plt.title, and then we can invoke the default legend with plt.legend().
"""