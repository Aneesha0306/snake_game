from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0) # when you don't want to see the animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True


while game_is_on:
    screen.update()#if you put this inside the for loop then the snake will move block my block
    time.sleep(0.1)
    scoreboard.display()
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        snake.extend()

    #detect collision with wall
    posx=snake.head.xcor()
    posy=snake.head.ycor()
    if posx>290 or posx<-290 or posy>290 or posy<-290:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with snake itself

    for segment in snake.segments[1:]: #we need to write segments[1:] because we don't want to include the head itself
        if snake.head.distance(segment) < 10:
            game_is_on = False

screen.exitonclick()



