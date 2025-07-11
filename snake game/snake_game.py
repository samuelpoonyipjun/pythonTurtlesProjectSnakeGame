from turtle import Screen
from snake import Snake # type: ignore
from food import Food # type:ignore
from scoreboard import Scoreboard # type:ignore
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Welcome to the ultimate snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.reappear()
        snake.increase_size()
        scoreboard.increase_score()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()