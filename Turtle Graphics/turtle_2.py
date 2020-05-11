"""
    Now that we know the movements of the turtle, you can move on to making actul shapes. We can start by drawing
    polygons since they all consist of straight lines connected at certain angles.
"""
import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(2)

# Square
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)


time.sleep(1)
t.reset()

# Circle
"""
    I you attempt to draw a circle as you drew square then you'd have to spend a lot of time just for that one
    shape. Thankfully, turtle library provides a solution for this. You can use a single command to draw the circle.
"""
t.setposition(0,0)
t.circle(60)


time.sleep(1)
t.reset()

"""
    In the same way, you can also draw a dot, which is nothing but a filled-in circle.
"""
t.setposition(0,0)
t.dot(60)

time.sleep(1)
t.reset() # resetting turtle to its original place


# Star



# using loop
for i in range(5):
    t.fd(50)
    t.rt(144)

time.sleep(1)
t.reset() # resetting turtle to its original place


# Hexagon

num_sides = 6
side_length = 70
angle = 360.0/num_sides

# using loop
for i in range(num_sides):
    t.fd(side_length)
    t.rt(angle)


turtle.done()
