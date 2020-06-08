import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2], label= "Example One")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label= "Example two")
plt.legend()
plt.xlabel('Bar number')
plt.ylabel('Bar height')

plt.title('Graph Example')
plt.show()

"""
    The plt.baar creates the bar chart for us. If you do not explicitly choose a color, then,
    despite doing mutliple plots, all bars will look the same. This gives us a change to cover a new
    Matplotlib customization option, however, you can use color to color just about any kind of plot.
"""