from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()

    #Check if player reach finish line
    if player.ycor() > 280:
        player.finish_line()
        scoreboard.level_up()

        #max speed
        if car_manager.speed <= 20:
            car_manager.speed *= 1.2
    
    #game over if player colides with car
    for car in car_manager.garage:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

