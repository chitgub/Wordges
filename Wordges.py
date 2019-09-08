import enchant
from tkinter import *
from math import *

master = Tk()
canvas_width = 1400
canvas_height = 900
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()
w.configure(background="dark orange")

coords = []
closest_x = 0
closest_y = 0

class Coord:
    pass


for i in range(0,20):
    for j in range(0,14):
        w.create_rectangle(200 + (50 * i), 34 + (50 * j), 250 + (50 * i), 84 + (50 * j), fill="yellow", outline="blue")
        coord_obj = Coord()
        coord_obj.x = 225 + (50 * i)
        coord_obj.y = 59 + (50 * j)
        coords.append(coord_obj)


d = enchant.Dict("en_US")
print d.check("Hello")
print d.check("Helo")


def check_word():


def key(event):

    global closest_x, closest_y
    w.create_text(closest_x, closest_y, fill="blue", font="times 25 bold", text=event.char.upper())
    check_word()


def click(event):

    global closest_x, closest_y
    smallest = 10000

    for obj in coords:
        distance = sqrt(((event.y - obj.y) ** 2) + ((event.x - obj.x) ** 2))
        if distance < smallest:
            smallest = distance
            closest_x = obj.x
            closest_y = obj.y


w.bind("<Key>", key)
w.bind("<Button-1>", click)
w.focus_set()
mainloop()