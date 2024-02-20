import tkinter as tk
import Plate_deflection
import math as m

# These numbers are used for calculation of derivatives and integrals
N = 100
M = 100


def transformation(Str):
    St = Str.replace("^", "**")
    St = St.replace("sin", "m.sin")
    St = St.replace("cos", "m.cos")
    St = St.replace("exp", "m.exp")
    return St


def Reading():
    Load = transformation(EnterLoad.get())
    LvL = int(EnterLvL.get())
    a = float(EnterOX.get())
    b = float(EnterOY.get())
    Thick = float(EnterThick.get())
    Young = float(EnterYoung.get())
    Nu = float(EnterNu.get())
    try:
        Scale = float(EnterScale.get())
    except:
        Scale = ""

    exec('Q = lambda x,y:' + Load, globals())

    Num = 5 * LvL
    dx = 2 * a / N
    dy = 2 * b / M
    D = Young * Thick ** 3 / (12 * (1 - Nu ** 2))
    Plate_deflection.DEFLECTION(a, b, Q, N, M, dx, dy, D, LvL, Num, Scale)


window = tk.Tk()

window.title("Plate deflection")
w = 750
h = 350

window.geometry(f"{w}x{h}+600+300")  # f-string
# window.minsize(int(w / 2), int(h / 2))
window.resizable(False, False)
window.config(bg='#8EE8F6')  # RGB - color codes

way = tk.Label(window, text="Enter load:", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
way.place(x=80, y=20)

wid = 40
EnterLoad = tk.Entry(fg="black", width=wid)
EnterLoad.place(x=10, y=60)

btn = tk.Button(window, text="Calculate", font=("Arial Bold", 15), command=Reading, width=int(wid / 4), height="   1",
                fg="Black",
                bg='#3399FF')
btn.place(x=70, y=100)

# Title start
lvl = tk.Label(window, text="Computational LvL:", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
lvl.place(x=280, y=20)
EnterLvL = tk.Entry(fg="black", width=wid)
EnterLvL.place(x=460, y=27)
# Title end

# OX and OY
OXl = tk.Label(window, text="side a =", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
OXl.place(x=350, y=60)
EnterOX = tk.Entry(fg="black", width=wid)
EnterOX.place(x=460, y=66)
OYl = tk.Label(window, text="side b =", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
OYl.place(x=350, y=60 + 40)
EnterOY = tk.Entry(fg="black", width=wid)
EnterOY.place(x=460, y=66 + 40)
# OX and OY  end

# thickness start
thick = tk.Label(window, text="thickness =", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
thick.place(x=350, y=60 + 80)
EnterThick = tk.Entry(fg="black", width=wid)
EnterThick.place(x=460, y=66 + 80)
# end thickness

# young start
young = tk.Label(window, text="E =", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
young.place(x=350, y=60 + 120)
EnterYoung = tk.Entry(fg="black", width=wid)
EnterYoung.place(x=460, y=66 + 120)
# end young

# Nu start
nu = tk.Label(window, text="ν =", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
nu.place(x=350, y=60 + 120 + 40)
EnterNu = tk.Entry(fg="black", width=wid)
EnterNu.place(x=460, y=66 + 120 + 40)
# end Nu

# ScaleZ start
scale = tk.Label(window, text="Scale OZ:", font=("Arial Bold", 15), fg="Black", bg='#8EE8F6')
scale.place(x=350, y=60 + 120 + 80)
EnterScale = tk.Entry(fg="black", width=wid)
EnterScale.place(x=460, y=66 + 120 + 40 + 40)
# end Result

window.mainloop()
