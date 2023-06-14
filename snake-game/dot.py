from turtle import Turtle, Screen, listen, onkey
from random import randint


class Dot():
    def __init__(self, snake):
        self.dot = Turtle()
        self.dot.shape("circle")
        self.dot.color("teal")
        self.dot.penup()

        # initialize dot to random location
        self.location = self.get_random_location()

        self.dot.goto(self.location[0], self.location[1])

    def get_random_location(self):
        return [randint(-300, 300), randint(-300, 300)]

    def move(self, snake):
        # check if random dot is already on top of the snake
        while True:
            self.location = self.get_random_location()

            if self.on_snake(snake):
                continue
            else:
                self.dot.goto(self.location[0], self.location[1])
                break

    def on_snake(self, snake):
        dot_location_x = self.location[0]
        dot_location_y = self.location[1]

        on_snake = False

        for section in snake:
            pos = section.pos()
            snake_x = pos[0]
            snake_y = pos[1]

            snake_x_on_dot_x = snake_x - 20 <= dot_location_x <= snake_x + 20
            snake_y_on_dot_y = snake_y - 20 <= dot_location_y <= snake_y + 20

            if snake_x_on_dot_x and snake_y_on_dot_y:
                on_snake = True

        return on_snake
