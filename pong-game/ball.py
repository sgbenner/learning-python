from random import randint
from turtle import Turtle


class Ball(Turtle):
    def __init__(self, game_boarder):
        super().__init__()
        self.x_move = None
        self.y_move = None
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.speed = 1

        # reset ball on init
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def r_paddle_bounce(self):
        if self.x_move > 0:
            self.x_move *= -1

        if randint(0, 1) == 1:
            self.y_move = randint(1,8)
            self.y_move *= -1

        self.increase_speed()

    def l_paddle_bounce(self):
        if self.x_move < 0:
            self.x_move *= -1

        if randint(0, 1) == 1:
            self.y_move = randint(1,8)
            self.y_move *= -1

        self.increase_speed()

    def reset(self):
        self.x_move = 6
        self.y_move = 8
        self.goto(0, 0)

    def increase_speed(self):
        self.speed += 0.5
