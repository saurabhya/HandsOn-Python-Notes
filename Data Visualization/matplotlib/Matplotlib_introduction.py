import matplotlib.pyplot as plt

"""
    This line imports the integral pyplot, which we're going to use throughout this entire series.
    we import pyplot as plt, and this is a tradition standard for python programs using pyplot.
"""
plt.plot([1,2,3], [5,7,4])

"""
    Next, we invoke the .plot method of pyplot to plot some coordinates. This .plot takes many parameters,
    but the first wo here are 'x' and 'y' coordinates, which we've placed lists into.
    This means, we have 3 coordinates according to these lists: 1,5,2,7 and 3,4.

    The plt.plot will "draw" this plot in the background, but we need to bring it to the screen when we're
    ready, after graphing everything we intend to.
"""
plt.show()

"""
With that, the graph pop up. If not, sometimes it can pop under, or you may have gotten an error.
"""