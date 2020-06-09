"""
    The idea of stack plots is to show "parts of the whole" over time.
    A stack plot is basically like a pie chart, only over time.

    Let's consider a situation where we have 24 hours in a day, and we'd like to see
    how we're spending our time. We'll divide our activities into: Slepeing, eating,
    working and playing.
    We're going to assume that we're tracking this over the ourse of 5 days,
    so our starting data will loke like:
"""
import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

"""
    The problem is, we don't really know which color is which without looking back at the code.
    The next problem is with polygons, we cannot actyally have "labels" for the data.
    So anywhere where there is more than just a line, with things like fills or stckplots like this,
    we cannot label the specific part inherently. We can work around it.
"""
plt.plot([],[],color='m',label='Sleeping', linewidth= 5)
plt.plot([],[],color='c',label='Eating', linewidth= 5)
plt.plot([],[],color='r',label='Working', linewidth= 5)
plt.plot([],[],color='k',label='Playing', linewidth= 5)


"""
    So, our "x" axis will consist of the days variable, which is 1,2,3,4 and 5.
    Then, our constituent for the days are held in their respective activities. To plot them:
"""
plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])

plt.xlabel("X")
plt.ylabel("Y")
plt.title('Interesting Graph')
plt.legend()
plt.show()