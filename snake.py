from turtle import Turtle

MOVE_SIZE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()  # function fired upon creation
        self.head = self.segments[0]

    def create_snake(self):
        for x in range(0,3):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(0 - x * 20, 0)
            self.segments.append(new_segment)

    def extend(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)



    # inverting the range to high-low is the clever trick needed to make it easy to send each segment to the one in front of it
    # as well as only updating screen after each has been moved
    def move(self):
        for seg_num in range(len(self.segments) - 1,  0, -1):  # (start, end, step)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # triggers errors within the snake library, but still works ¯\_(ツ)_/¯
        self.head.forward(MOVE_SIZE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

# ______Known_Bug______
# if player inputs two movements in one tick, player does a 180, and dies of self collision
# Best avoided by increasing tick speed and decreasing how much snake moves each tick
# and then only allow turns at grid increments