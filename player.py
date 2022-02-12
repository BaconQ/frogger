from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.shape("turtle")
        self.penup()
        self.finish_line()
        self.setheading(90)
        self.move()
        
        

    def up(self):
        self.forward(MOVE_DISTANCE)


    def move(self):
        self.screen.onkey(self.up, "w")

    def finish_line(self):
            self.goto(STARTING_POSITION)