from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Scoreboard

snake = snake.Snake()

screen = Screen()
screen.clear()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
# scoreboard.display_score()
screen.tracer(0)
screen.listen()

snake.creat_snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.gen_food()

        scoreboard.increase_score()

screen.exitonclick()
