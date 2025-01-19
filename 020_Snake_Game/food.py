import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def random_food(self):
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        self.goto(x=x_cor, y=y_cor)
