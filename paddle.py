from turtle import *


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape('square')
        self.color('#eb1d36')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(positions)

    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def reset_game(self):
        self.goto(0, -200)
