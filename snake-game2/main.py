from turtle import listen, onkey
from snake import Snake
from dot import Dot
from game import Game
import time

GAME_SPEED = 0.05
GAME_SIZE_X = 200
GAME_SIZE_Y = 200

# Start the game
game = Game(screen_size_x=GAME_SIZE_X, screen_size_y=GAME_SIZE_Y)

snake = Snake()  # initialize snake
dot = Dot()  # initialize dot/food

listen()
onkey(snake.up, "Up")  # This will call the up function if the "Left" arrow key is pressed
onkey(snake.down, "Down")
onkey(snake.left, "Left")
onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    snake.move()
    game.screen.update()

    if game.at_edge(snake.snake):  # game over
        game_is_on = False
    else:
        if dot.on_snake(snake):
            game.update_score()
            snake.grow()
            dot.move()

    time.sleep(GAME_SPEED)

# exit on click
game.screen.exitonclick()
