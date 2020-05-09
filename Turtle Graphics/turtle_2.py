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


time.sleep(3)
turtle.clearscreen()

# Circle
"""
    I you attempt to draw a circle as you drew square then you'd have to spend a lot of time just for that one
    shape. Thankfully, turtle library provides a solution for this. You can use a single command to draw the circle.
"""
t.setposition(0,0)
t.circle(60)


time.sleep(3)
turtle.clearscreen()

"""
    In the same way, you can also draw a dot, which is nothing but a filled-in circle.
"""
t.setposition(0,0)
t.dot(60)


turtle.done()
