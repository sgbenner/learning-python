import random
import time
import turtle
from turtle import listen, onkey, Screen
from frog import Frog
from car import Car

SCREENSIZE = [250, 150]
GAMEBOARDER = [225, 125]

screen = Screen()
screen.screensize(SCREENSIZE[0], SCREENSIZE[1])
screen.title("Frogger!")
screen.tracer(0)

"""
TO DO:
- Create screen
- Create Frog class
    - Move
    - 
- Car class
- Build cars that move across screen
    - random # of cars per lane
    - Random speed of cars per lane
    - Cars get created at random distances
Score to keep track of # of times I've made it to end
Speed up cars with each time I get through
"""

frog = Frog()

cars = []

# initialize key inputs
listen()
onkey(frog.up, "Up")  # This will call the up function if the "Left" arrow key is pressed
onkey(frog.back, "Down")

game_on = True
difficulty = 0 # starts with 0, increment each time frog gets to goal

while game_on:
    screen.update()

    # if frog gets to end, increase difficulty until at 0
    if frog.ycor() > 180 and difficulty < 5:
        difficulty += 1
        time.sleep(3)
        frog.restart()

    # randomly add new cars to screen
    if random.randint(0, 10 - difficulty) <= 2:
        cars.append(Car(random.randint(1, 7))) # add car to random lane

    for car in cars:
        if frog.distance(car) < 25:
            game_on = False
            break
        car.move()
        if car.xcor() < -550:
            cars.remove(car)

    time.sleep(.1)

screen.exitonclick()
