from tkinter import *

root = Tk()
root.title("Программа")
txt = StringVar()
txt2 = StringVar()
d = 0

def clicked():
    x1 = 0
    a = float(a1.get())
    b = float(b1.get())
    c = float(c1.get())
    d = b**2 - 4*a*c
    if d >= 0:
     x1 = ((-b + d**0.5) / 2*a)
     x2 = ((-b - d**0.5) / 2*a)
     txt.set(str(d))
     txt2.set("x1 = " + str(x1) + ", x2 = " + str(x2))
    else:
     txt.set(str(d))
     txt2.set("Нет корней")
    

l1 = Label(root, text="Введите значения коэффициентов уравнения")
l1.grid(row=0, column=0, columnspan=2)

lA = Label(root, text="a = ")
lA.grid(row=1, column=0)

lB = Label(root, text="b = ")
lB.grid(row=2, column=0)

lC = Label(root, text="c = ")
lC.grid(row=3, column=0)

a1 = Entry(root)
a1.grid(row=1, column=1)

b1 = Entry(root)
b1.grid(row=2, column=1)

c1 = Entry(root)
c1.grid(row=3, column=1)

l4 = Label(root, text="Дискриминант уравнения = ")
l4.grid(row=5, column=0)

dis = Entry(root, textvariable=txt)
dis.grid(row=5, column=1)

l5 = Label(root, text="Корни уравнения: ")
l5.grid(row=6, column=0)

ans = Entry(root, textvariable=txt2)
ans.grid(row=6, column=1)

Button(root, text="Готово", command=lambda: clicked()).grid(row=4, column=1)
root.mainloop()