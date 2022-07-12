
# I decided to not use this segement of code because it is over convoluted compared to my streamlined version.  However this was a good first rough draft during the process
# powerup timer and spawning lock
    if powerup_timer > 0:      # positive mode counts super snake time remaining
        powerup_timer -= 1
        if powerup_timer == 0:
                power = False
                powerup_timer = MIN_NO_PWRUP * -1
                no_pwr_spawn = True
                scoreboard.powerdown()
    elif powerup_timer < 0:    # negative mode counts time until powerup can spawn again
        powerup_timer += 1
        if powerup_timer == 0:
            no_pwr_spawn = False

    if no_pwr_spawn == False:      # the chance for a powerup to spawn is only activated when unlocked
        if random.randint(1, 25) == 1:
            powerup.refresh()










# this is my first attempt for the hard part: The engine that makes the snake move



from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")

# history is a dictionary, where each key is a segment of the snake
# and each key's value is it's history of posititions as a list
# history = {}
    ## "Braincube" : []

# history is a list, history[segmentnumber][tickhistory][(x,y,heading)]
#                             the block     time-date       position
history = [[[0, 0, 90], []], []]
# starts with brain at starting position, and dummy lists for proper calling of nested lists

### def createplayer():
braincube = Turtle()
braincube.goto(0,0)
braincube.shape("square")
braincube.color("white")
braincube.penup()
braincube.setheading(90)

snakeUnitLength = 1
currentTick = 1



def placebehind():#unfinished, will be used to clean the code
    return new_position

def extendsnake():
    name = "segment" + str(snakeUnitLength + 1)
    name = Turtle()
    name.shape("square")
    name.color("white")
    name.penup()

    temptuple = history[snakeUnitLength -1][currentTick-1]
    name.goto(temptuple[0], temptuple[1])
    name.setheading(temptuple[2])
    name.backward(20)

    templist = []
    for tick in range(0, currentTick): # subtract snakeLength ?
        # create empty tick measurements, so that tuple can be read with an accurate tick date
        #do not need to record history for a greater number of ticks than there are lengths
        templist.append("")
    x = name.xcor()
    y = name.ycor()
    head = name.heading()
    templist.append((x,y,head))
    history.insert(snakeUnitLength + 1, templist)
    #insert adds a list to the desired index
    #avoids problem of deleting dummy index


#
# Running Code:
#

extendsnake()
extendsnake()

#operate the game in ticks, which are like FPS but allows us to control speed of game for difficulty
#braincube is controlled by player input, and moves one pixel per tick - where a 'pixel' is one snake_segment size
#each segment reads the position of the cube in front of it via the history list

#My code is good because it was the most direct application of my view of the problem,
#however the deliberate control over each segment is a double edged sword,
#it overcomplicates the code too much

#

screen.exitonclick()
