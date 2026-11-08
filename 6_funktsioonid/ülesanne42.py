import tkinter as tk

def joonista_sein(canvas, x, y, laius, korgus, varv="lightgray"):
    canvas.create_rectangle(x, y, x + laius, y + korgus, fill=varv, width=2)

def joonista_katus(canvas, x, y, laius, katuse_korgus, varv="red"):
    punkt1_x, punkt1_y = x, y
    punkt2_x, punkt2_y = x + laius / 2, y - katuse_korgus
    punkt3_x, punkt3_y = x + laius, y
    
    canvas.create_polygon(punkt1_x, punkt1_y, punkt2_x, punkt2_y, punkt3_x, punkt3_y, fill=varv, width=2)

def joonista_aken(canvas, x, y, suurus, varv="lightblue"):
    canvas.create_rectangle(x, y, x + suurus, y + suurus, fill=varv, width=2)
    canvas.create_line(x + suurus / 2, y, x + suurus / 2, y + suurus, fill="black")
    canvas.create_line(x, y + suurus / 2, x + suurus, y + suurus / 2, fill="black")

def joonista_maja(canvas, x, y, laius, seina_korgus, katuse_korgus, seina_varv="lightgray", katuse_varv="red"):
    joonista_sein(canvas, x, y, laius, seina_korgus, seina_varv)

    joonista_katus(canvas, x, y, laius, katuse_korgus, katuse_varv)

    akna_suurus = laius * 0.3
    akna_x = x + (laius - akna_suurus) / 2
    akna_y = y + (seina_korgus - akna_suurus) / 2
    
    joonista_aken(canvas, akna_x, akna_y, akna_suurus)

aken = tk.Tk()
aken.title("Maja joonistamine")

louend = tk.Canvas(aken, width=800, height=500, bg="skyblue")
louend.pack()

louend.create_rectangle(0, 350, 800, 500, fill="green", outline="green")

joonista_maja(louend, x=50, y=250, laius=120, seina_korgus=100, katuse_korgus=60, seina_varv="yellow", katuse_varv="brown")

joonista_maja(louend, x=250, y=180, laius=220, seina_korgus=170, katuse_korgus=90, seina_varv="beige", katuse_varv="darkred")

joonista_maja(louend, x=550, y=150, laius=150, seina_korgus=200, katuse_korgus=120, seina_varv="lightblue", katuse_varv="darkgreen")

aken.mainloop()