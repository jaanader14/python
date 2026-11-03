def  celsius_fahrenheit(c):
    return c * (9 / 5) + 32

väärtused = [0, 20, 37, 100]

for c_kraad in väärtused:
    f_kraad = celsius_fahrenheit(c_kraad)
    print(f"{c_kraad} celsiust on {f_kraad:.1f} fahrenheiti")