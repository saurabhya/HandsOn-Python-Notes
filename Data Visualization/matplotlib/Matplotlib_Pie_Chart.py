"""
    Pie charts are used to parts of the whole for a certain point in time, and often a % share.
    Luckily for us, Matplotlib handles the sizes of the slices and everything, we just feed it
    the numbers.
"""

import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
#cols = ['c','m','r','b']
plt.pie(slices,
        labels = activities,
        startangle=90,
        shadow=True,
        explode=(0,0.2,0,0),
        autopct='%1.1f%%')

plt.title("Interesting Graph")
plt.show()

"""
    Within the plt.pie(), we specify the "slices" which are the relevant sizes for each part. Then, we specify the color list for the
    corresponding slices. Next, we can optionally specify the "start angle" for the graph. This lets you start the line where you want.
    In our case, we chose 90 degree angle for the pie chart, which means the first division will be a vertical line.
    Next, we can optionally add a shadow to the plot for a bit of character, and then we can even use "explode" to pull out a slice a bit.
"""