import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 1
player = Player()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()
screen.onkey(player.move_forward, "w")
screen.update()
for i in range(1, 30):
    car_manager = CarManager()
game_is_on = True
while game_is_on:

    scoreboard.write_level(level)
    time.sleep(0.1)
    if player.cross_road():
        level += 1
        scoreboard.write_level(level)

    screen.update()
