from food import Food



class LifeSupport(Food):
    def __init__(self):
        super().__init__()  # not useful for getting food's properties, but need to get Turtle's properties
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.penup()
        self.speed("fastest")
        self.goto(500,500) # off screen
        # self.refresh()

        self.numlives = 0


    def refresh(self):
        super().refresh()


    def addlife(self):
        x = -290 + self.numlives * 20
        self.goto(x, 290)
        self.color("green")
        self.stamp()
        self.numlives += 1

    def subtractlife(self):
        self.clearstamps(-1)
        self.numlives -= 1

