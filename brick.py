from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, colors):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.color(colors)
        self.penup()
        self.goto(position)

    def collide(self):
        self.hideturtle()
        print('ball hits')


