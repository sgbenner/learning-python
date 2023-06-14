from turtle import Screen, Turtle


class Game():
    def __init__(self, screen_size_x, screen_size_y):
        # score
        self.score = 0 # default to 0

        # initialize the screen
        self.screen = Screen()
        self.screen_size_x = screen_size_y
        self.screen_size_y = screen_size_y
        self.screen.screensize(screen_size_x + 50, screen_size_y + 50)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("Classic Snake Game")

        # draw the boarder edge
        self.draw_edge_border()
        self.write_score = []

        self.write_score.append(self.draw_score())

    def update_score(self):
        for item in self.write_score:
            item.clear()
            item.hideturtle()

        self.score += 1
        self.draw_score()

    def at_edge(self, snake):
        location = snake[0].pos()
        snake_x = location[0]
        snake_y = location[1]

        if abs(snake_x) >= self.screen_size_x * 2 or abs(snake_y) >= self.screen_size_y * 2:
            return True
        else:
            return False

    def draw_edge_border(self):
        screen_size_2x = self.screen_size_x * 2
        screen_size_2y = self.screen_size_y * 2

        border = Turtle()
        border.pencolor("white")
        border.width(15)
        border.penup()
        border.goto(screen_size_2x * -1, screen_size_2y * -1)
        border.pendown()
        border.goto(screen_size_2x * -1, screen_size_2y)
        border.goto(screen_size_2x, screen_size_2y)
        border.goto(screen_size_2x, screen_size_2y * -1)
        border.goto(screen_size_2x * -1, screen_size_2y * -1)
        border.hideturtle()

    def draw_score(self):
        write_score = Turtle()
        write_score.color("white")
        write_score.hideturtle()
        write_score.penup()
        write_score.goto(-25, self.screen_size_y * 2 + 25)
        write_score.write(f"Your Score: {self.score}", font=("Verdana",
                                                        15, "normal"))
        return write_score
