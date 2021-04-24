import enchant
from tkinter import *
from math import *

master = Tk()
canvas_width = 1400
canvas_height = 900
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()
w.configure(background="dark orange")


class Coord:
    pass


closest_obj = Coord()
coords = []
chance = 1

sn = 1
for i in range(0,20):
    for j in range(0,14):
        w.create_rectangle(200 + (50 * i), 34 + (50 * j), 250 + (50 * i), 84 + (50 * j), fill="yellow", outline="blue")
        coord_obj = Coord()
        coord_obj.x = 225 + (50 * i)
        coord_obj.y = 59 + (50 * j)
        coord_obj.c = ''
        coord_obj.s = sn
        coord_obj.p = 0
        coords.append(coord_obj)
        sn +=1


d = enchant.Dict("en_US")

def check_word_h(length):

    i = 1
    while i < 280 - (14*(length-1)):
        wrd = ""
        for l in range (0,length):
            if coords[i - 1 + (14 * l)].c != '':
                wrd = wrd + coords[i-1 + (14*l)].c

        if len(wrd) == length:
            if d.check(wrd):
                print ("Word : ", wrd)
        i = i + 1


def key(event):

    global closest_obj, chance

    if closest_obj.p == 0:
        chance = chance + 1
        txt = event.char.upper()
        if chance % 2 == 1:
            w.create_text(closest_obj.x, closest_obj.y, fill="blue", font="times 25 bold", text=txt)
        else:
            w.create_text(closest_obj.x, closest_obj.y, fill="red", font="times 25 bold", text=txt)
        closest_obj.c = txt
        closest_obj.p = (chance % 2) + 1
        print("Turn of Player : ", (chance % 2) + 1)
        for ln in range(1,21):
            print ("Horizontal", ln ,"letter words in this chance")
            check_word_h(ln)


def click(event):

    global closest_obj
    smallest = 10000

    for obj in coords:
        distance = sqrt(((event.y - obj.y) ** 2) + ((event.x - obj.x) ** 2))
        if distance < smallest:
            smallest = distance
            closest_obj = obj


w.bind("<Key>", key)
w.bind("<Button-1>", click)
w.focus_set()
mainloop()