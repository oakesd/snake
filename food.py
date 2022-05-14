from turtle import Turtle
import game_engine as ge


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("lime")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        coords = ge.get_random_coordinates()
        self.goto(coords[0], coords[1])

    def hide(self):
        self.hideturtle()