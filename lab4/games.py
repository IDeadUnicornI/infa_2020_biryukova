from tkinter import Tk, Canvas, Label, RIGHT, Entry, Button

from random import randint, choice
from math import sqrt


class Ball:
    def __init__(self, canvas, x1, y1, x2, y2, velx, vely, fill):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.velx = velx
        self.vely = vely
        self.fill = fill
        self.canvas = canvas
        self.ball = canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, fill=self.fill, activefill='yellow')

    def move_ball(self):
        deltax = self.velx
        deltay = self.vely

        self.canvas.move(self.ball, deltax, deltay)

        if self.canvas.coords(self.ball)[0] < 0 or self.canvas.coords(self.ball)[2] > self.canvas.winfo_width():
            self.velx *= -1
        if self.canvas.coords(self.ball)[1] < 5 or self.canvas.coords(self.ball)[3] > self.canvas.winfo_height():
            self.vely *= -1

        self.canvas.after(20, self.move_ball)


# creating canvas
root = Tk()
root.title("Blue Balls")
canvas = Canvas(root, width=512, height=512, bg='pink', cursor='cross')
canvas.pack()

# number of the balls
n = 80

# color set for balls
colors = ['red', 'blue', 'green', 'red', 'red']

# creating list of balls
balls = []
for i in range(n):
    x1 = randint(20, canvas.winfo_reqwidth() - 50)
    x2 = x1 + randint(20, 50)
    y1 = randint(20, canvas.winfo_reqheight() - 50)
    y2 = y1 + (x2 - x1)
    velx = choice([-5, -3, 3, 5])
    vely = choice([-5, -3, 3, 5])
    balls.append(Ball(canvas, x1, y1, x2, y2, velx, vely, colors[i % 4]))
# balls start to move
for i in range(n):
    balls[i].move_ball()

# creating score panel
scr = 0
score = Label(root, text='Score: ' + str(scr))
score.pack(side=RIGHT)


def click(event):
    global scr
    for i in range(n):
        r = (balls[i].x2 - balls[i].x1) / 2
        x_b = canvas.coords(balls[i].ball)[0] + r
        y_b = canvas.coords(balls[i].ball)[1] + r
        dist = sqrt((event.x - x_b) ** 2 + (event.y - y_b) ** 2)
        if dist < r:

            if balls[i].fill == 'blue':
                inc = int(10 * sqrt(balls[i].velx ** 2 + balls[i].vely ** 2) / r)
                scr += inc
                print('Catched +' + str(inc))
            elif balls[i].fill == 'red':
                inc = int(r / sqrt(balls[i].velx ** 2 + balls[i].vely ** 2))
                scr -= inc
                print('Catched -' + str(inc))
            else:
                rnd = choice([-4, 0, 0, 4])
                scr += rnd
                print('Catched ' + str(rnd))
            score.config(text='Score ' + str(scr))
            break


# creates entry for username
player = Entry(root, text='User_name: ', justify=RIGHT)
player.insert(0, 'User_name')
player.pack(side=RIGHT)


def savescore(event):
    global scr
    print('Saved')
    f = open('scoreboard.txt', 'a')
    f.write('Player: ' + player.get() + ' ==> points: ' + str(scr) + '\n')
    f.close()
    scr = 0
    score.config(text='Score ' + str(scr))


# creates the button to launch savescore()
save = Button(root, text=' Save ')
save.bind('<Button-1>', savescore)
save.pack(side=RIGHT)
canvas.bind('<Button-1>', click)

root.mainloop()
