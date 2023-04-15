from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = 0
        self.shape()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        with open('score.txt', 'r') as file:
            self.high_score = int(file.read())
        self.clear()
        self.goto(300, -250)
        self.write(f"Score:{self.current_score}", False, "center", ("Courier", 20, "bold"))
        self.goto(-270, -250)
        self.write(f"High Score:{self.high_score}", False, "center", ("Courier", 20, "bold"))

    def increase_score(self):
        self.current_score += 1
        if self.current_score > self.high_score:
            self.increase_high_score()
        self.update_score()

    def increase_high_score(self):
        self.high_score += 1
        with open('score.txt', 'w') as file:
            file.write(str(self.high_score))

    def game_over(self):
        self.goto(10, 10)
        self.write("Game Over", False, "center", ("Courier", 24, "bold"))
        self.current_score = 0
