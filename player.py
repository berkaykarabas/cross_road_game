STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid=2,stretch_len=1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def move_turtle(self):
        self.forward(MOVE_DISTANCE)
    def finish_line_pass(self):
        new_y =self.ycor()
        if new_y >= FINISH_LINE_Y:
            return True
        else:
            return False
    def go_to_start(self):
        self.goto(STARTING_POSITION)

