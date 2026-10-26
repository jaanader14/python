import tkinter as tk

aken = tk.Tk()
aken.title("Geomeetrilised kujundid")

tahvel = tk.Canvas(aken, width=500, height=400, bg="white")
tahvel.pack()

tahvel.create_rectangle(50, 50, 180, 150, fill="red")

tahvel.create_oval(250, 50, 350, 150, fill="blue")

tahvel.create_line(50, 220, 200, 320, fill="green", width=4)

tahvel.create_oval(250, 220, 450, 300, fill="yellow")

tahvel.create_text(250, 360, text="Minu kujundid", font=("Arial", 16, "bold"), fill="black")

aken.mainloop()