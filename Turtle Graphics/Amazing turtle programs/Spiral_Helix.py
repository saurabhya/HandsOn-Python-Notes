# Python program to draw Spiral Helix pattern

import turtle

wn = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.lt(i)

turtle.done()