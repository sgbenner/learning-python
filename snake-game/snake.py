from turtle import Turtle, Screen, listen, onkey


class Snake():
    def __init__(self):
        self.snake = []

        for _ in range(0, 3):
            new_section = Turtle()
            new_section.shape("square")
            new_section.color("white")
            new_section.penup()

            # add section to end of snake
            if _ > 0:
                tail_location = self.snake[-1].pos()
                x, y = tail_location[0], tail_location[1]
                new_section.goto(x - 20, y)

            self.snake.append(new_section)

    def move(self):
        # first segment moves, all other segments move to the position of the segment in front of it
        snake_length = len(self.snake)

        for _ in range(snake_length, 0, -1):
            index = _ - 1
            self.snake[index].forward(20)

        # now make segments 1 and 2 match heading of the segment before it
        for _ in range(snake_length, 0, -1):
            index = _ - 1
            if index > 0:
                self.snake[index].setheading(self.snake[index - 1].heading())

    def grow(self):
        new_section = Turtle()
        new_section.shape("square")
        new_section.color("white")
        new_section.penup()

        # add section to end of snake
        if len(self.snake) > 0:
            tail_location = self.snake[-1].pos()
            x, y = tail_location[0], tail_location[1]
            new_section.goto(x - 20, y)

        self.snake.append(new_section)

    def up(self):
        self.snake[0].setheading(90)

    def down(self):
        self.snake[0].setheading(270)

    def right(self):
        self.snake[0].setheading(0)

    def left(self):
        self.snake[0].setheading(180)
