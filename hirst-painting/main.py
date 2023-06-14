from get_colors import Colors
import turtle as t
from random import choice

c = Colors('image.jpg', 10)

screen = t.Screen()
t = t.Turtle()
t.speed(0)
screen.colormode(255)

def set_random_color():
    t.color(choice(c.colors))

def draw_circle():
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def do_work():
    # do work
    set_random_color()
    t.pendown()
    draw_circle()
    t.penup()
    t.forward(50)

for _ in range(10):
    for _ in range(10):
        do_work()
    t.goto(0, t.ycor() + 50)

screen.exitonclick()
