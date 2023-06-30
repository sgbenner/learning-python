from turtle import Turtle
from random import choice

COLORS = ["green", "blue", "red", "yellow", "black", "purple"]
lanes = {1: -120, 2: -80, 3: -40, 4: 0, 5: 40, 6: 80, 7: 120}


class Car(Turtle):
    def __init__(self, lane):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(choice(COLORS))
        self.penup()
        self.setheading(180)
        self.lane = lane
        self.goto(500, lanes[lane])

    def move(self):
        self.forward(20)
