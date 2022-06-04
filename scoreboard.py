from turtle import Turtle
from game_engine import SCREEN_SIZE

ALIGNMENT = "center"
FONT_NAME = "Courier"
FONT_SIZE = 16
FONT_WEIGHT = "bold"
NORMAL = (FONT_NAME, FONT_SIZE, FONT_WEIGHT)
LARGE = (FONT_NAME, FONT_SIZE * 2, FONT_WEIGHT)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.x = 0
        self.y = int(SCREEN_SIZE/2 - 40)
        self.pu()
        self.goto(self.x, self.y)
        self.hideturtle()
        self.update()

    def update(self):
        text = f"HIGH SCORE: {self.high_score}  SCORE: {self.score}"
        self.clear()
        self.write(arg=text, align=ALIGNMENT, font=NORMAL)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update()

    def game_over(self):
        self.goto(0, 0)
        text = "GAME OVER"
        self.write(arg=text, align=ALIGNMENT, font=LARGE)
