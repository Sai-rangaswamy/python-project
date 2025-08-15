import turtle as t
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.head = None
        self.segments = []
        self.creation()
        self.head = self.segments[0]

    def creation(self):

        for position in COORDINATES:
            ahamed = t.Turtle()
            ahamed.shape("square")
            ahamed.color("white")
            ahamed.penup()
            ahamed.goto(position)
            self.segments.append(ahamed)
        self.head = self.segments[0]

    def createSnake(self):
        for position in COORDINATES:
            self.addSegment(position)


    def addSegment(self,position):
        ahamed = t.Turtle()
        ahamed.shape("square")
        ahamed.color("white")
        ahamed.penup()
        ahamed.goto(position)
        self.segments.append(ahamed)

    def extendSnake(self):
        self.addSegment(self.segments[-1].position())


    def movement(self):
        for _ in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[_ - 1].xcor()
            new_y = self.segments[_ - 1].ycor()
            self.segments[_].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
