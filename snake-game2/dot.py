from turtle import Turtle
from random import randint


class Dot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("teal")
        self.penup()
        self.move()

    def get_random_location(self):
        return [randint(-300, 300), randint(-300, 300)]

    def move(self):
        # initialize dot to random location
        self.location = self.get_random_location()
        self.goto(self.location[0], self.location[1])

    def on_snake(self, snake):
        if snake.head.distance(self) < 20:
            return True

        return False
