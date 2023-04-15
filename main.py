import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:

        if car.distance(player) < 25:
            game_is_on = False
            print('Game over!')
            scoreboard.game_over()

    if player.ycor() > 290:
        player.level_up()
        scoreboard.level_up()
        car_manager.level_up()

screen.exitonclick()