from turtle import Turtle
import time

FONT_TUPLE = ('Helvetica', 12, 'bold')
NOTIF_FONT_TUPLE = ('Helvetica', 25, 'bold')
BOARD = (0,270)
NOTIFICATION = (0,0)
MESSAGE = (0,-75)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(10)
        self.penup()
        self.speed("fastest")

        self.score = 0
        self.supersnake = False  # only needed to patch a corner case

        self.goto(BOARD)
        self.write(f"SCORE: {self.score}", move=False, align='center', font=FONT_TUPLE)



    def addpoint(self, adjustment):    # also functions as a refresh
        self.score += adjustment
        self.clear() # must erase to write new score overtop
        self.goto(BOARD)
        self.color("white")
        self.write(f"SCORE: {self.score}", False, 'center', font=FONT_TUPLE)

        if self.supersnake:
            self.powerup()  # erasing also eliminated supersnake notification, so needs refreshing


    def powerdisplay(self, mode):
        if mode:
            self.goto(NOTIFICATION)
            self.color("red")
            self.write("SUPERSNAKE", False, 'center', font=NOTIF_FONT_TUPLE)
            self.supersnake = True
        else:
            self.clear()

    def buylife(self):
        self.addpoint(-20)
        self.goto(MESSAGE)
        self.color("lightgreen")
        self.write("Purchased a life in exchange for 20 points", False, 'center', font=FONT_TUPLE)


    def player_suggestion(self):
        self.goto(MESSAGE)  # refreshes notifications
        self.color('white')
        self.write("An extra life can be purchased with SPACE for 20 points", False, 'center', font=FONT_TUPLE)

    def gameover(self):
        self.addpoint(0)
        self.goto(NOTIFICATION)
        self.color('white')
        for x in range(0,6):   # repeating and writing white over white causes coloration distortion, similar to old arcade cabinets: at least for my oled display
            self.write("G A M E   O V E R",False, 'center', font=NOTIF_FONT_TUPLE)

        #Score Rainbow Underline Animation


    def selfcollision(self):
        self.goto(MESSAGE)  # refreshes notifications
        self.color('white')
        self.write("Self Collision", False, 'center', font=FONT_TUPLE)

    def outofbounds(self):
        self.goto(MESSAGE)  # refreshes notifications
        self.color('white')
        self.write("Out of Bounds", False, 'center', font=FONT_TUPLE)
