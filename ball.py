from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#F9D949")
        self.goto(position)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.05
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)

    def shoot_ball(self):
        self.move_x = 1

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def go_ball(self, new_x, new_y):
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1

    def collide_l(self):
        self.move_x *= -1
        if self.move_x > 0:
            self.move_x = -2
        elif self.move_x < 0:
            self.move_x = 2
        self.move_y = 10

    def collide_m(self):
        self.move_x *= -1
        if self.move_x > 0:
            self.move_x = -5
        elif self.move_x < 0:
            self.move_x = 5
        self.move_y = 10

    def collide_h(self):
        self.move_x *= -1
        if self.move_x > 0:
            self.move_x = -10
        elif self.move_x < 0:
            self.move_x = 10
        self.move_y = 10

    def reset_game(self):
        self.goto(0, -180)
        self.bounce_y()
