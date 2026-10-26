import tkinter as tk

aken = tk.Tk()
aken.title("Värvilised ruudud")

tahvel = tk.Canvas(aken, width=520, height=100, bg="white")
tahvel.pack()

külg = 40
vahe = 10
algus_x = 15  
algus_y = 30 

for i in range(10):
    x1 = algus_x + i * (külg + vahe)
    y1 = algus_y
 
    x2 = x1 + külg
    y2 = y1 + külg
  
    if i % 2 == 0:
        varv = "red"
    else:
        varv = "blue"
  
    tahvel.create_rectangle(x1, y1, x2, y2, fill=varv)

aken.mainloop()