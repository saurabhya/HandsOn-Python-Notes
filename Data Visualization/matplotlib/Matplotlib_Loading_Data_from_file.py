"""
    Many times, people want to graoh data from a file. There are many types of file, and
    many ways you may extract data from a file to graph it. Here, we'll try a couple of ways
    to load data froma file. First, we'll use the built-in csv module to load CSV files,
    then we'll try to utilize NumPy module to load files.
"""

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open("./Data Visualization/matplotlib/example.txt",'r') as csvfile:
    plots = csv.reader(csvfile, delimiter= ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label= 'Loaded from file!')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

"""
    We use the csv module to read data, the csv module automatically splits the file by line,
    and then the data in the file by the delimiter we choose. In our case it is ','
"""

# -------------------------------------------------------------------------------------------------------------- #

"""
    While using the CSV module is completely fine, using the NumPy module to load our files
    and data is likely to make more sense for us down the line.
"""

import numpy as np

x,y = np.loadtxt("./Data Visualization/matplotlib/example.txt", delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('X')
plt.ylabel('Y')
plt.title("Interesting Graph")
plt.legend()
plt.show()
