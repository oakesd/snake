from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_engine import SCREEN_SIZE
import time

game_on = True


def pause():
    global game_on
    if game_on:
        game_on = False
        screen.exitonclick()
    else:
        game_on = True
        play()


def stop():
    global game_on
    game_on = False
    screen.exitonclick()


def game_over():
    scoreboard.game_over()
    stop()


snake = Snake()
food = Food()
scoreboard = Scoreboard()

# configure screen
screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Ssssssnake")
screen.tracer(0)

# add event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop, "Escape")
screen.onkey(pause, "space")


def play():
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            food.respawn()
            snake.add_segment()

        # detect collision with wall
        if snake.head.xcor() < (SCREEN_SIZE/2 * -1) or snake.head.xcor() > (SCREEN_SIZE/2) \
                or snake.head.ycor() < (SCREEN_SIZE/2 * -1) or snake.head.ycor() > (SCREEN_SIZE/2):

            game_over()

        # detect collision with self
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_over()


play()




