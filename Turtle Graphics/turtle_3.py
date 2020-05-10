"""
    Turtle Customization
"""
import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(2)


# *Changing the screen title

# Sometomes, you may want to change the title of your screen . You can make it more personal, like "My turtle program"
# or more suitable to what you're working on, like "Drawing with turtle".

turtle.title("My turtle program")




# *Changing the turtle shape

# The initial shape of the really a turtle, but a triangular figure. However, you can change the way the turtle
# looks, and you do have the options when it comes to doing so.

t.shape("arrow")
time.sleep(1)
t.shape("circle")
time.sleep(1)



# *Changing the turtle sizes
# You can increase or decrease the size of the onscreen turtle to make it look bigger ot smaller. This changes
# only the size of the shape without affecting the output of the oen as it draws on the screen.

t.shapesize(1, 5, 10)
time.sleep(1)
t.shapesize(10, 5, 1)
time.sleep(1)
t.shapesize(1, 10, 5)
time.sleep(1)
t.shapesize(10, 1, 5)

# The numbers given are the parameters for the size of the turtle:
# Stretch length
# Stretch width
# Outline width
# You can change these according to your preference.


# *Changing the pen size

# The previous command chnaged the size of the turtle's shape only. However, sometimes, you may need to increse
# or decrease the thickness  of your pen.
t.shapesize(1, 1, 1) # Get to the original size

t.pensize(5) # pen is 5 times the original size.
t.forward(100)


# *Changing the turtle and pen color

# When you first open a new screen, the turtle starts out as a black figure and draws with black ink.
# Based on your requirements, you can do two things:
# Change the color of the turtle: This chnages the fill color.
# Change the color of the penL: This changes the outline or the ink color.

# change the color of the turtle
t.fillcolor("red")
# to change the color of the pen
t.pencolor("green")

# to chnage the color of both, you type the following:
t.color("green", "red")


# *Filling in an image

# Coloring in an image usually makes it look better, doesn't it? The Python turtle library gives you the option
# to add color to your drawings.
t.clear()
t.home()

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

# When you use .begin_fill(), you're telling your program that you're going to be drawing a closed shape which
# will lead to be filled in. Then, you can use .end_fill() to indicate that you're done creating your shape
# and it can now be filled in.



# *Changing the screen color

# By default, turtle always opens up a screen with a white background. However, you can change the coloe of
# the screen at any time using the following command



turtle.bgcolor("blue")
time.sleep(2)
turtle.bgcolor("red")
time.sleep(2)
turtle.bgcolor("green")

# You can set a variety of colors for your screen jus by tyoing in thier hex code number.


# *Customizing in one line
t.clear()
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()


turtle.done()