# Drawing and Loops
# Author: Ubial
# 14 October 2025

import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

# TMNT - turtles
# create a turtle called mike
mike = turtle.Turtle()
mike.turtlesize(5)  # set size
mike.shape("turtle")  # shape
mike.color("orange")  # colour

# move mike around
mike.speed(1)
mike.penup()
mike.forward(1000)
mike.left(90)


window.exitonclick()
