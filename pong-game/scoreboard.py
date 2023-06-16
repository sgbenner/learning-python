from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, game_boarder):
        super().__init__()

        self.p1_score = 0
        self.p2_score = 0

        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(-125, game_boarder[1] + 40)

        self.write_score()

    def write_score(self):
        self.write(f"P1 Score: {self.p1_score} | P2 Score: {self.p2_score}", move=False, align="left",
                   font=("Arial", 24, "normal"))

    def update_score(self, who_scored):
        if who_scored == "p1":
            self.p1_score += 1
        else:
            self.p2_score += 1

        self.clear()
        self.write_score()
