"""
seaborn is definitely the best library to quickly build a histogram thanks to it distplot()
Note the importance of the bins parameter: try several values to seewhich represents your data the best.
"""

# import the library
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

# plot the histogram thanks to the distplot function
sns.set(style= "darkgrid")
sns.histplot(data=df, x= "sepal_length", kde= True, bins= 20)
plt.show()