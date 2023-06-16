from turtle import Screen, Turtle

class GameScreen:
    def __init__(self, screen_size, game_boarder):
        self.p1_score = 0
        self.p2_score = 0
        self.screen_size_x = screen_size[0]
        self.screen_size_y = screen_size[1]
        self.game_boarder_x = game_boarder[0]
        self.game_boarder_y = game_boarder[1]

        self.screen = Screen()
        self.screen.screensize(self.screen_size_x, self.screen_size_y)
        self.screen.bgcolor("black")
        self.screen.title("Retro Pong")

        self.draw_boarder()
        self.draw_middle_line()

    def draw_boarder(self):
        self.border = Turtle()
        self.border.speed("fastest")
        self.border.hideturtle()
        self.border.pencolor("white")
        self.border.penup()
        self.border.width(10)
        self.border.goto(self.game_boarder_x, self.game_boarder_y)
        self.border.pendown()
        self.border.goto(self.game_boarder_x, self.game_boarder_y * -1)
        self.border.goto(self.game_boarder_x * -1, self.game_boarder_y * -1)
        self.border.goto(self.game_boarder_x * -1, self.game_boarder_y)
        self.border.goto(self.game_boarder_x, self.game_boarder_y)

    def draw_middle_line(self):
        dash_count = 11
        dash_size = (self.game_boarder_y * 2) / (dash_count * 2)

        self.middle_line = Turtle()
        self.middle_line.speed("fastest")
        self.middle_line.penup()
        self.middle_line.color("white")
        self.middle_line.goto(0, self.game_boarder_y) # start at top
        self.middle_line.pensize(7)

        for _ in range(0, dash_count * 2):
            position = self.middle_line.pos()
            y_to_go_to = position[1] - dash_size
            print(position)
            print(y_to_go_to)

            # alternate pen up/pen down
            if _ % 2 == 0:
                self.middle_line.pendown()
            else:
                self.middle_line.penup()

            self.middle_line.goto(0, y_to_go_to)
