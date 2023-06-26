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

        if self.y_move > 0:
            self.y_move *= -1

    def l_paddle_bounce(self):
        if self.x_move < 0:
            self.x_move *= -1

        if self.y_move < 0:
            self.y_move *= -1

    def reset(self):
        self.x_move = 5
        self.y_move = 5
        self.goto(0,0)
