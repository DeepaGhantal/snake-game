from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()


      # for segments in snake.segments:
      #       if segments == snake.head:
      #             pass
      #       elif snake.head.distance(segment) < 10:
      #             game_is_on = False
      #             scoreboard.gameover()

# tim_1 = Turtle("square")
# tim_1.color("white")
#
# tim_2= Turtle("square")
# tim_2.color("white")
# tim_2.goto(-20,0)
#
# tim_3 = Turtle("square")
# tim_3.color("white")
# tim_3.goto(-40,0)

# screen.exitonclick()


# from turtle import Screen
# from snake import Snake
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake game")
# screen.tracer(0)
#
# snake = Snake()
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()
#
# screen.exitonclick()