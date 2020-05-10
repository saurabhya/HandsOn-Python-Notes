"""
    Here, we'll see use of loops and conditonal statements in turtle with help of
    few examples. This will give a practical approach when it comes to understanding these concepts.
"""
import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

# Using for loop:
# creating square
for i in range(4):
    t.fd(100)
    t.rt(90)

# Using while loop
# to create circles
t.reset()#resetting turtle

n = 10
while n<= 40:
    t.circle(n)
    n += 10

turtle.done()
