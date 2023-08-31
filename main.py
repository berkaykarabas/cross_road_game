import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
player.move_turtle()
car_manager = CarManager()
score_board = Scoreboard()
screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.crate_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False
    if player.finish_line_pass():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.mainloop()