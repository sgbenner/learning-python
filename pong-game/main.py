from screen import GameScreen
from scoreboard import Scoreboard
from ball import Ball

SCREEN_SIZE = [300, 300]
GAME_BOARDER = [(SCREEN_SIZE[0] * 2) - 10, (SCREEN_SIZE[1] * 2) - 10]


screen = GameScreen(screen_size=SCREEN_SIZE, game_boarder=GAME_BOARDER)
scoreboard = Scoreboard(GAME_BOARDER)
ball = Ball()

# scoreboard.update_score("p1")
# scoreboard.update_score("p1")
# scoreboard.update_score("p1")
# scoreboard.update_score("p1")

screen.screen.exitonclick()

