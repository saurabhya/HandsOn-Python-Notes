# Python program to user input pattern

import turtle
import time
import random

print("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shapes you want to draw: ")
if num_str.isdigit():
    squares = int(num_str)


angle = 180 - 180*(squares-2)/squares

turtle.up()

x = 0
y = 0
turtle.setpos(x, y)


numshapes = 8
for x in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    turtle.fd(x)
    turtle.lt(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.fd(40)
        turtle.lt(angle)
        turtle.fd(40)
        print(turtle.pos())
        turtle.up()
        turtle.end_fill()

time.sleep(10)
turtle.bye()