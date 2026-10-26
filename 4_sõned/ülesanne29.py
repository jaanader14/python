import tkinter as tk

aken = tk.Tk()
aken.title("Eesti lipp")

lipu_laius = 600
lipu_korgus = 300

triibu_korgus = lipu_korgus // 3

tahvel = tk.Canvas(aken, width=lipu_laius, height=lipu_korgus, bg="white", highlightthickness=0)
tahvel.pack()
sinine = "blue"
must = "black"
valge = "white"

tahvel.create_rectangle(0, 0, lipu_laius, triibu_korgus, fill=sinine, outline="")

tahvel.create_rectangle(0, triibu_korgus, lipu_laius, triibu_korgus * 2, fill=must, outline="")

tahvel.create_rectangle(0, triibu_korgus * 2, lipu_laius, lipu_korgus, fill=valge, outline="")

aken.mainloop()