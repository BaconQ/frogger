from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280,250)
        self.hideturtle()
        self.level_update()

    def level_update(self):
        self.clear()
        self.write(f"Level: {self.level}", font = FONT)

    def level_up(self):
        self.level += 1
        self.level_update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", font = FONT, align= "center" )