from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.garage = []
        self.speed = 5
    
        
    def create(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len= 2, stretch_wid= 1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randint(260,800), random.randint(-220,250))
            self.garage.append(new_car)
        

    def move(self):
        for car in self.garage:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

            if car.xcor() < -340:
                car.hideturtle()
                self.garage.remove(car)
    
        

            
                
                
                
            
   
  