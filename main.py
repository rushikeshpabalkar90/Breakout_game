from turtle import *
import random
import time

from paddle import Paddle
from ball import Ball
from brick import Brick
from scoareboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('#2D2727')
shoot = False
all_ball_down = False
a = 0

all_ball = []
scoreboard = Scoreboard()
paddle1 = Paddle((0, -200))

for _ in range(2):
    ball = Ball((0, -180))
    all_ball.append(ball)


fifty_bricks = []
colors = ['#B2A4FF', '#FFB4B4', '#FFDEB4', '#FDF7C3', '#C0EEE4', '#F8F988', '#FFCAC8', '#FF9E9E']
# colors = ["red", "yellow", "green", "blue", "purple", "orange"]

y_position = [375, 325, 275, 225, 175, 125, 75, 25, -25, -75, -125, -175, -225, -275, -325, -375]
x_position = [90, 120, 150, 180, 210, 240, 270]

# y_position = [380, 340, 300, 260, 220, 180, 140, 100, 60, 20, -20, -60, -100, -140, -180, -220, -260, -300, -340,
# -380]
# x_position = [90, 110, 130, 150, 170, 190, 210, 230, 250, 270]

for a in range(70):
    brick1 = Brick((random.choice(y_position), random.choice(x_position)), random.choice(colors))
    fifty_bricks.append(brick1)


def shoot_ball():
    global shoot
    for ball1 in all_ball:
        ball1.shoot_ball()
    shoot = True


def move_paddle_and_ball_right():
    if paddle1.xcor() < 335:
        paddle1.go_right()
        if not shoot:
            for ball1 in all_ball:
                ball1.go_ball(new_x=paddle1.xcor(), new_y=paddle1.ycor() + 20)


def move_paddle_and_ball_left():
    if paddle1.xcor() > -335:
        paddle1.go_left()
        if not shoot:
            for ball1 in all_ball:
                ball1.go_ball(new_x=paddle1.xcor(), new_y=paddle1.ycor() + 20)


screen.listen()
screen.onkey(key="Right", fun=move_paddle_and_ball_right)
screen.onkey(key="Left", fun=move_paddle_and_ball_left)
screen.onkey(key="Up", fun=shoot_ball)

is_game_on = True

while is_game_on:
    screen.update()
    for ball1 in all_ball:
        time.sleep(ball1.move_speed)

    # check if ball shot or not
    if shoot:
        for ball1 in all_ball:
            ball1.move_ball()

            # detect collision with right and left wall
            if ball1.xcor() > 379 or ball1.xcor() < -380:
                ball1.bounce_x()

            # detect collision with upper wall
            if ball1.ycor() > 280:
                ball1.bounce_y()

            # detect collision with paddle in center side
            if ball1.distance(paddle1) < 25 and ball1.ycor() < -170:
                ball1.collide_l()

            # detect collision with paddle in median side
            elif ball1.distance(paddle1) < 35 and ball1.ycor() < -172:
                ball1.collide_m()

            # detect collision with paddle in outer side
            elif ball1.distance(paddle1) < 48 and ball1.ycor() < -172:
                ball1.collide_h()

            # detect collision with bricks
            for brick in fifty_bricks:
                if ball1.distance(brick) < 20 and brick.isvisible():
                    brick.collide()
                    ball1.bounce_y()
                    scoreboard.increase_score()

            # detect miss the ball and reset game
            if ball1.ycor() < -295:
                a += 1
                # ball1.reset_game()
                # paddle1.reset_game()
                if len(all_ball) == a:
                    scoreboard.game_over()
                    shoot = False
                    is_game_on = False
                    all_ball_down = True


screen.mainloop()
