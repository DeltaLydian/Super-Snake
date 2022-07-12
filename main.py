import random
from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from powerup import Powerup
from lifesupport import LifeSupport

POWERUP_DURATION = 50 # MEASURED IN TICKS!!
MIN_NO_PWRUP = 40
PWRUP_SPWN_CHANCE = 110 # higher is less likely

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0) # puts the screen into tick and update-on-command mode, rather than live animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()
powerup = Powerup()
lifesupport = LifeSupport()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")









power = False
powerup_timer = 0
tick_speed = 8
game_on = True
lives = 0


def death():
    global power
    if power == True:
        return False
    elif lifesupport.numlives > 0:
        lifesupport.numlives -= 1
        return False
    else:
        scoreboard.gameover()
        return True

def spendpoints():
    if scoreboard.score >=  20:
        # print("SPace!")
        lifesupport.addlife()
        scoreboard.buylife()
screen.onkey(spendpoints, "space")

def testingcheat():
    # print("F!")
    for x in range(0,9):
        scoreboard.addpoint(1)
screen.onkey(testingcheat,"f")



#
#
#
#
#
#
#
# Running the game
while game_on:

# run the game in increments of ticks
    screen.update()
    time.sleep(1/tick_speed)

# move the snake
    snake.move()

# powerup timer and spawning lock
    print(powerup_timer)
    if powerup_timer > 0:      # counts supersnake time remaining when power is on, and time until next spawn when power is off
        powerup_timer -= 1
    elif powerup_timer == 0:                 # using 'if' instead of 'elif' would still work the same, accept the timer would be one tick shorter than what it is supposed to be.
            if power == True:
                power = False
                scoreboard.powerdisplay(False)
            if power == False:
                powerup.refresh()

            powerup_timer = random.randint(MIN_NO_PWRUP, PWRUP_SPWN_CHANCE)

# powerup collision
    if snake.head.distance(powerup) < 15:
        scoreboard.powerdisplay(True)
        powerup.eaten()
        powerup_timer = POWERUP_DURATION
        power = True
        print("SUPERSNAKE")

# collision test with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.addpoint(1)
        snake.extend()
        powerup_timer += 5
        # scale difficulty with score
        if scoreboard.score % 10 == 0:
            if scoreboard.score > 60:
                tick_speed += 1
            else:
                tick_speed += 2
        # suggest to player to buy another life
        if scoreboard.score == 20:
            scoreboard.player_suggestion()

# collision test for wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        status = death()
        game_on = not status
        # print("Death!")
        if status:
            scoreboard.outofbounds()

# collision test for self/snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            status = death()
            game_on = not status
            # print("Death!")
            if status:
                scoreboard.selfcollision()

screen.exitonclick()