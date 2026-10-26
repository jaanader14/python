import tkinter as tk

aken = tk.Tk()
aken.title("Malelaud")

ruudu_arv = 8
külg = 50
laua_mõõt = ruudu_arv * külg

tahvel = tk.Canvas(aken, width=laua_mõõt, height=laua_mõõt, bg="white", highlightthickness=0)
tahvel.pack()

for rida in range(ruudu_arv):
    for veerg in range(ruudu_arv):
      
        x1 = veerg * külg
        y1 = rida * külg
        
        x2 = x1 + külg
        y2 = y1 + külg
        
        if (rida + veerg) % 2 == 0:
            varv = "white"
        else:
            varv = "black"
        
        tahvel.create_rectangle(x1, y1, x2, y2, fill=varv, outline="")

aken.mainloop()