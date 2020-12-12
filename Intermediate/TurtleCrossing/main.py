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
car_list = []
for i in range(1, 20):
    car_manager = CarManager()
    car_list.append(car_manager)

game_is_on = True
while game_is_on:
    scoreboard.write_level(level)
    for car in range(0, len(car_list)):
        car_list[car].car_move_forward()
        if car_list[car].xcor() < -280:
            car_list[car].reset_position()
        if player.cross_road():
            level += 1
            scoreboard.write_level(level)
            car_list[car].increase_speed()
        if player.distance(car_list[car]) < 30:
            scoreboard.game_over()
            game_is_on = False
    time.sleep(0.1)
    screen.update()

screen.exitonclick()