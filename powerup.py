import random

from food import Food



class Powerup(Food):
    def __init__(self):
        super().__init__()  # not useful for getting food's properties, but need to get Turtle's properties
        self.shape('triangle')
        self.settiltangle(random.randrange(0, 180, 15))  # different every spawn
        self.color("orange")  # make 2 colored inscription
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.penup()
        self.speed("fastest")

        #self.refresh()
        self.goto(500,500)

    def refresh(self):
        super().refresh()

    def eaten(self):
        self.goto(500,500) # moves off screen
