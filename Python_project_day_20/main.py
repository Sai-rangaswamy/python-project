
#STEP 2 move a snake body.
#STEP 3 control the snake.
#STEP 4 detect the collision with the food.
#STEP 5 create a scoreboard.
#STEP 6 detect the collision with wall.
#STEP 7 detect the collision with the wall.

import turtle as t
import time
import snake_game as s
import food as f
import scoreboard as sc

WIDTH = 600
HEIGHT = 600
screen = t.Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = s.Snake()
point = f.Food()
score = sc.ScoreBoard()


t.listen()
t.onkey(snake.up, "Up")
t.onkey(snake.down , "Down")
t.onkey(snake.left, "Left")
t.onkey(snake.right, "Right")


#STEP 2 move a snake body.
isGameOn = True
while isGameOn:
    screen.update()
    time.sleep(0.1)
    snake.movement()

    #decting collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        isGameOn = False
        score.game_over()


    #deceting collision with food.
    if snake.segments[0].distance(point) < 15:
        point.refresh()
        score.increase_score()
        snake.extendSnake()


    #deceting collision with itself.
    for segment in snake.segments:

        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            isGameOn = False
            score.game_over()

    #decting collision with snake itself
    if snake.segments[0].distance(point) == snake.segments[-1].distance(point):
        score.game_over()
        isGameOn = False



screen.exitonclick()