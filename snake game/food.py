from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.reappear()
    def reappear(self):
        random_x_coor = random.randint(-280, 280)
        random_y_coor = random.randint(-280, 280)
        self.goto(random_x_coor, random_y_coor)