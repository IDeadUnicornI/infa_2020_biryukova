from graph import *

w, h = windowSize()
penColor("black")
penSize(1)
brushColor("yellow")
circle(w / 2, h / 2, 100)

brushColor("red")
circle(w / 2 - 40, h / 2 - 30, 20)

brushColor("black")
circle(w / 2 - 40, h / 2 - 30, 8)

brushColor("red")
circle(w / 2 + 40, h / 2 - 30, 16)

brushColor("black")
circle(w / 2 + 40, h / 2 - 30, 8)

brushColor("black")
rectangle(w / 2 - 50, h / 2 + 65, w / 2 + 50, h / 2 + 45)

penSize(10)
brushColor("black")
line(w / 2 - 105, h / 2 - 80, w / 2 - 15, h / 2 - 45)

penSize(10)
brushColor("black")
line(w / 2 + 90, h / 2 - 75, w / 2 + 15, h / 2 - 40)


run()