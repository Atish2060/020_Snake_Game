from turtle import Screen,Turtle
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Atish's Snake Game")
screen.tracer(0)
segments = []

# border along the screen of the snake
border_turtle = Turtle()
border_turtle.color("white")
border_turtle.penup()
border_turtle.goto(-295, 295)
border_turtle.pendown()
border_turtle.pensize(3)
border_turtle.speed(5)

for _ in range(4):
    border_turtle.forward(585)
    border_turtle.right(90)
border_turtle.hideturtle()


snake = Snake()
snake_food = Food()
score_board = Scoreboard()

# changing the direction of snake using the keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # checking the collision of snake with the food
    if snake.snake_head.distance(snake_food) < 15:
        snake_food.random_food()
        score_board.increase_score()
        snake.extend()

    # checking collision with the wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -295 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        score_board.reset()
        score_board.update_score()
        snake.snake_reset()

    # detect collision with tail.
    for segments in snake.segments[1:]:
        # if segments == snake.snake_head:
        #     pass
        if snake.snake_head.distance(segments) < 10:
            score_board.reset()
            snake.snake_reset()


screen.exitonclick()
