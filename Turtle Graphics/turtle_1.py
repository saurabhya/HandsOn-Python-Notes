"""
    Turtle is a pre-installed Python library that enables users to create pictures and shapes by providing them
    in a virtual canvas. The onscreen pen that you use for drawing is called the turtle and this is what gives
    the library its name.
"""
# Importing turtle
import turtle

"""
    Since turtle is a grphic library, which means you'll need to create a separate window to ccaeey out each drawing
    command . You can create this screen by initializing a variable for it.
"""
s = turtle.getscreen()

# to refer to the turtle we will use an object throughout the program

t = turtle.Turtle()

"""
    Turtle can move in 4 different direction: forward, backward, left and right.
"""
t.right(90) # t.rt() is short hand
t.forward(100) # t.fd()
t.left(90) # t.lt()
t.backward(100) # t.bk()

"""
    turtle is moving too fast so we can control its speed using:
"""
t.speed(1)
"""
    You can also draw a line from  your current position to any other arbitrary position on the screen.
    This is done with the help of coordinates.
"""
t.goto(100, 100)

# to bring turtle back to its original position we can use home()
t.home()

turtle.done()