from turtle import Turtle
import game_engine as ge


STARTING_LENGTH = 3
MOVEMENT_SPEED = 20
COLOR = "white"
SHAPE = "square"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.heading = ge.get_random_heading()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.add_segments(STARTING_LENGTH)

    def add_segment(self):
        if len(self.segments) == 0:
            new_coords = ge.get_random_coordinates()
        else:
            last_coords = self.segments[-1].position()
            new_coords = ge.modify_coordinates(last_coords, self.heading)

        new_segment = self.Segment()
        new_segment.goto(new_coords[0], new_coords[1])
        new_segment.setheading(self.heading)
        self.segments.append(new_segment)

    def add_segments(self, num_segments):
        for _ in range(num_segments):
            self.add_segment()

    def set_speed(self, new_speed):
        for segment in self.segments:
            segment.speed(new_speed)

    def set_heading(self, new_heading):
        self.heading = new_heading
        self.head.setheading(new_heading)

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.segments[0].forward(MOVEMENT_SPEED)

    def up(self):
        if self.heading != DOWN:
            self.set_heading(UP)

    def down(self):
        if self.heading != UP:
            self.set_heading(DOWN)

    def left(self):
        if self.heading != RIGHT:
            self.set_heading(LEFT)

    def right(self):
        if self.heading != LEFT:
            self.set_heading(RIGHT)

    def hide(self):
        for segment in self.segments:
            segment.hideturtle()

    class Segment(Turtle):

        def __init__(self):
            super().__init__()
            self.shape(SHAPE)
            self.color(COLOR)
            self.speed(0)
            self.pu()
