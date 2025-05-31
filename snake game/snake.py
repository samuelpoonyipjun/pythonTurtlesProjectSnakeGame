from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)
    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    def increase_size(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x_coor = self.segments[segment_number - 1].xcor()
            new_y_coor = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x_coor, new_y_coor)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)