"""
Objective:
    The player whose turtle reaches its home first wins the game.

How to play:
    * Each player rolls a dice to get a number.
    * The player then moves thier turtle by that many steps.
    * The players alternate turns until one of them wins.

The Structures:
    * Each player had a turtle indicated by a differet color, You can have more than two player, but here you'll
      be creating a two - player game.
    * Each turtle has a home position that it must reach.
    * Each player uses a die to choose a value at random for their turn. Here, the die is represented by list of
      numbers from 1 to 6.
"""

import turtle
import random



# creating turtles and positioning them.

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

player_two = player_one.clone()
player_two.color("blue")
player_one.penup()
player_two.goto(-200, -100)

# Positioning at starting position
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# creating the die
die = [1, 2, 3, 4, 5, 6]


# Implementing logic

for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Player One Wins!!!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player two Wins!!!")
        break
    else:
        player_one_turn = input("press enter to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The nuber of steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)

        player_two_turn = input("press enter to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The nuber of steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)


turtle.done()