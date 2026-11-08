import tkinter as tk
import random

def joonista_ring(canvas, x, y, raadius, varv):
    x1 = x - raadius
    y1 = y - raadius
    x2 = x + raadius
    y2 = y + raadius
    canvas.create_oval(x1, y1, x2, y2, fill=varv)

aken = tk.Tk()
aken.title("Värvilised ringid")

lõuend = tk.Canvas(aken, width=600, height=400, bg="white")
lõuend.pack()

varvid = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta"]

for i in range(15):
    suvaline_raadius = random.randint(15, 50)
    suvaline_x = random.randint(suvaline_raadius, 600 - suvaline_raadius)
    suvaline_y = random.randint(suvaline_raadius, 400 - suvaline_raadius)
    suvaline_varv = random.choice(varvid)

    joonista_ring(lõuend, suvaline_x, suvaline_y, suvaline_raadius, suvaline_varv)

aken.mainloop()