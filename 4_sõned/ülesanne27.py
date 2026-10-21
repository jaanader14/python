imporimport tkinter as tk
aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=600,
    height=400,
    bg="white")

tahvel.pack()

aken.mainloop()