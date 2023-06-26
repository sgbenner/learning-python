from gamescreen import GameScreen
from turtle import listen, onkey, Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

SCREEN_SIZE = [200, 125]
GAME_BOARDER = [(SCREEN_SIZE[0] * 2) - 10, (SCREEN_SIZE[1] * 2) - 10]

RIGHT = "RIGHT"
LEFT = "LEFT"

# screen
screen = Screen()
screen.screensize(SCREEN_SIZE[0], SCREEN_SIZE[1])
screen.bgcolor("black")
screen.title("Retro Pong")
screen.tracer(0)

# draw game stuff
gamescreen = GameScreen(SCREEN_SIZE, GAME_BOARDER)

# create the scorebaord
scoreboard = Scoreboard(GAME_BOARDER)

# initialize paddles
r_paddle = Paddle(GAME_BOARDER, RIGHT)
l_paddle = Paddle(GAME_BOARDER, LEFT)

# initialize key functions for game
listen()
onkey(r_paddle.up, "Up")  # This will call the up function if the "Left" arrow key is pressed
onkey(r_paddle.down, "Down")
onkey(l_paddle.up, "w")
onkey(l_paddle.down, "s")

# initialize ball
ball = Ball(GAME_BOARDER)

# play ball
game_on = True

while game_on:
    screen.update()

    # move ball
    ball.move()

    # hits top/bottom:
    if abs(ball.ycor()) >= abs(GAME_BOARDER[1]) - 15:
        ball.bounce()

    # hit right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= GAME_BOARDER[0] - 40:
        ball.r_paddle_bounce()

    # hit left paddle
    if ball.distance(l_paddle) < 50 and abs(ball.xcor()) >= GAME_BOARDER[0] - 40:
        ball.l_paddle_bounce()

    # out of bounds
    elif abs(ball.xcor()) >= abs(GAME_BOARDER[0]):
        # update score
        if ball.xcor() > 0:
            scoreboard.update_score(LEFT)
        else:
            scoreboard.update_score(RIGHT)

        # wait 3 seconds
        time.sleep(3)

        # reset ball and start over
        ball.reset()
        ball.r_paddle_bounce()

    sleep = 0.08 / ball.speed

    time.sleep(sleep)

# end game
screen.exitonclick()
