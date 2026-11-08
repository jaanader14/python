import tkinter as tk

def joonista_ruut(canvas, x, y, suurus, varv):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill=varv)

aken = tk.Tk()
aken.title("Ruutude joonistamine")

loovend = tk.Canvas(aken, width=600, height=400)
loovend.pack()

joonista_ruut(loovend, 50, 50, 80, "red")
joonista_ruut(loovend, 180, 40, 120, "blue")
joonista_ruut(loovend, 350, 80, 50, "green")
joonista_ruut(loovend, 100, 200, 150, "yellow")
joonista_ruut(loovend, 400, 220, 90, "purple")

aken.mainloop()