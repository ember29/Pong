from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        """turtle size is always 20*20"""
        self.pu()
        self.goto(position)
    def up(self):
            new_y = self.ycor() + 20
            self.goto(x=350, y=new_y)

    def down(self):
            new_y = self.ycor() - 20
            self.goto(x=350, y=new_y)

    def l_down(self):
        n_y=self.ycor()-20
        self.goto(x=-350,y=n_y)

    def l_up(self):
        n_y = self.ycor() +20
        self.goto(x=-350, y=n_y)

