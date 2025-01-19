from turtle import Turtle

MAX_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.draw_snake()
        self.snake_head = self.segments[0]
        self.snake_head.color("red")

    # draw the snake in the initial moment of the game
    def draw_snake(self):
        for i in STARTING_POSITIONS:
            self.add_snake(i)

    # add the snake body
    def add_snake(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color("green")
        self.segments.append(new_turtle)

    # extend the snake from its tail
    def extend(self):
        self.add_snake(self.segments[-1].position())

    # moving the snake on the basis of the position of the body in front of it
    def snake_move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.snake_head.forward(MAX_DISTANCE)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.draw_snake()
        self.snake_head = self.segments[0]
        self.snake_head.color("red")

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
