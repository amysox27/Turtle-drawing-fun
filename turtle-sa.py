# Turtle drawing fun!
# by Amy Stocking
# 05.26.2025

import turtle
turtle.shape("turtle")
t = turtle.Turtle()
t.pensize(7)


def triangle(len):
    for i in range(3):
        t.forward(len)
        t.left(120)

def square(len):
    for i in range(4):
        t.forward(len)
        t.right(90)

def rectangle():
    len = 140
    width = 20

    for j in range(2):
        t.forward(len)
        t.left(90)
        t.forward(width)
        t.left(90)


def house(len):
    square(len)
    triangle(len)

def main():
    t.speed(0)
    t.color("purple")
    house(100)
    t.penup()
    t.color("red")
    t.forward(150)
    t.pendown()
    house(50)
#    rectangle()


main()


turtle.Screen().exitonclick()
