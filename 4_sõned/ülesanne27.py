import tkinter as tk

laius = 600
kõrgus = 400
tausta_värv = "white"

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(aken, width=laius, height=kõrgus, bg=tausta_värv)
tahvel.pack()

aken.mainloop()