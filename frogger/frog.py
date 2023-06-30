from turtle import Turtle


class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1)
        self.color("green")
        self.penup()
        self.setheading(90)

        self.restart()

    def restart(self):
        self.goto(0, -180)

    def up(self):
        self.forward(40)

    def back(self):
        self.forward(-40)
