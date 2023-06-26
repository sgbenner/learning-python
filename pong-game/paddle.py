from turtle import Turtle

UP = "UP"
DOWN = "DOWN"


class Paddle(Turtle):
    def __init__(self, game_boarder, side):
        super().__init__()

        self.game_boarder = game_boarder
        self.side = side

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        if self.side == "RIGHT":
            self.goto((game_boarder[0] - 20), 0)
        else:
            self.goto((game_boarder[0] - 20) * -1, 0)

        self.direction = None

    def up(self):
        if self.ycor() < self.game_boarder[1] - 50:
            self.goto(self.xcor(), self.ycor() + 40)

    def down(self):
        if self.ycor() > (self.game_boarder[1] - 50) * -1:
            self.goto(self.xcor(), self.ycor() - 40)
