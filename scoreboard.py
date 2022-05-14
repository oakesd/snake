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
        self.x = 0
        self.y = int(SCREEN_SIZE/2 - 40)
        self.pu()
        self.goto(self.x, self.y)
        self.hideturtle()
        self.update()

    def update(self):
        text = f"SCORE: {self.score}"
        self.write(arg=text, align=ALIGNMENT, font=NORMAL)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        text = "GAME OVER"
        self.write(arg=text, align=ALIGNMENT, font=LARGE)
