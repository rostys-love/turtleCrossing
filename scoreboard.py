from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.make_scoreboard()

    def make_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f'Level: {self.score}', align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.make_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)





