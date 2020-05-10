"""
    Sometimes you want to move you turtle to another point on the screen without drawing anything on the screen
    itself. To do this, you can use .penup(). Then, when you want to start draing again, you can use .pendown().
"""
import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(2)

# drawing
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()


"""
Undoing changes

    No matter how careful you are, there's always a possibility of making mistakes. Don't worry, though! The Python
    tutle library gives you the option to undo what you've done. To undo the very last thing you did:
"""
t.undo()
t.undo()
"""
    This undoes the last command that you ran. If you want to undo your last three commamds, then type
    t.undo() three times.
"""

"""
Resetting the Environment
    you also have the option on starting on a clean slate with reset command. The screen will get cleared up, and
    the turtle's settings will all be restored to their default parmeters.
"""
t.reset()
""" This clears the screen and teakes the turtle back to its home postion. """

"""
Leaving a stamp
    You have the option of leaving a stamp of your turtle on the screen, which is nothing but an imprint
    of the turtle.
"""

t.stamp() # returns an stamp ID
t.fd(100)
t.stamp()
t.fd(100)

# if you want to remove a particular stamp, then just remove the particular stamp.

"""
Cloning the turtle

    Sometimes, you may need to have more than one turtle on your screen. You can get another turtle by cloning
    your current turtle into your environment.
"""
t.reset() # reset turtle
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)


turtle.done()