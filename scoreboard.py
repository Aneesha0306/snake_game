from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color('white')

    def display(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME 0VER",align='center', font=('Courier', 24, 'bold'))