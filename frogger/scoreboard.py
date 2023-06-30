from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, game_boarder):
        super().__init__()

        self.r_score = 0
        self.l_score = 0

        self.hideturtle()
        self.color("Black")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(-125, game_boarder[1] + 40)

        self.write_score()

    def write_score(self):
        self.write(f"LEFT Score: {self.l_score} | RIGHT Score: {self.r_score}", move=False, align="left",
                   font=("Arial", 24, "normal"))

    def update_score(self, who_scored):
        if who_scored == "RIGHT":
            self.r_score += 1
        else:
            self.l_score += 1

        self.clear()
        self.write_score()
