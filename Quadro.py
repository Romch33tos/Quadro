from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("Программа")
txt = StringVar()
txt2 = StringVar()
txt3 = StringVar()
txt4 = StringVar()
def clicked():
	a = float(a1.get())
	b = float(b1.get())
	c  = float(c1.get())
	if (a == 0) or (b ==0) or (c == 0):
		answer = mb.showerror(title = "Ошибка" , message ="Убедитесь в правильности введенных данных!")
	if (a !=0) and (b != 0) and (c !=0) and (b % 2 == 0):
		answer = mb.showinfo( title="Способы решения", message="Уравнение можно решить через половину коэффициента или дискриминант")
		Button(root, state = NORMAL,text="Решить через половину коэффициента", command=lambda: clicked3()).grid(row=5,column=0)
		Button(root, state = NORMAL, text="Решить через дискриминант", command=lambda: clicked2()).grid(row=5, column=1)
	elif (a !=0) and (b !=0) and (c !=0):
		answer = mb.showinfo(
		title="Способы решения",message="Уравнение можно решить через дискриминант" )
		Button(root, state = DISABLED,text="Решить через половину коэффициента", command=lambda: clicked3()).grid(row=5,column=0)
		Button(root, state = NORMAL, text="Решить через дискриминант", command=lambda: clicked2()).grid(row=5,column=1)
		
def clicked2():
    Button(root, state = DISABLED, text="Решить через дискриминант", command=lambda: clicked2()).grid(row=5, column=1)
    a = float(a1.get())
    b = float(b1.get())
    c = float(c1.get())
    d = (b**2 - 4*a*c)
    if d >= 0:
     x1 = ((-b + d**0.5) / (2*a))
     x2 = ((-b - d**0.5) / (2*a))
     txt.set("%.2f"%(d))
     if d > 0:
     	txt2.set("Уравнение имеет два различных корня")
     if d == 0:
     	txt2.set("Уравнение имеет два одинаковых корня")
     txt3.set("%.2f"%(x1))
     txt4.set("%.2f"%(x2))
    else:
     Button(root, state = DISABLED, text="Решить через дискриминант", command=lambda: clicked2()).grid(row=5, column=1)
     txt.set("%.2f"%(d))
     txt2.set("Нет корней")
def clicked3():
    Button(root, state = DISABLED, text="Решить через половину коэффициента", command=lambda: clicked3()).grid(row=5, column=0)
    a = float(a1.get())
    b = float(b1.get())
    c = float(c1.get())
    k = (b / 2)
    d = (k**2 - a*c)
    if d >= 0:
     x1 = ((-k + d**0.5)/ a)
     x2 = ((-k - d**0.5)/ a)
     txt.set("%.2f"%(d))
     if d > 0:
      	txt2.set("Уравнение имеет два различных корня")
     if d == 0:
     	txt2.set("Уравнение имеет два одинаковых корня")
     txt3.set("%.2f"%(x1))
     txt4.set("%.2f"%(x2))
    else:
     Button(root, state = DISABLED, text="Решить через половину коэффициента", command=lambda: clicked3()).grid(row=5, column=0)
     txt.set("%.2f"%(d))
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

l5 = Label(root, text="Дискриминант уравнения = ")
l5.grid(row=6, column=0)

dis = Entry(root, textvariable=txt)
dis.grid(row=6, column=1)

l6 = Label(root, text="Корни уравнения: ")
l6.grid(row=7, column=0)

sol = Label(root, textvariable = txt2)
sol.grid(row=7, column=1)

l7 = Label(root, text="x1 =")
l7.grid(row=8, column=0)

l8 = Label(root, text="x2 =")
l8.grid(row=9, column=0)

x1 = Entry(root, textvariable=txt3)
x1.grid(row=8, column=1)

x2 = Entry(root, textvariable=txt4)
x2.grid(row=9, column=1)

Button(root, text="Готово", command=lambda: clicked()).grid(row=4, column=1)

Button(root, state = DISABLED, text="Решить через дискриминант", command=lambda: clicked2()).grid(row=5, column=1)

Button(root, state = DISABLED, text="Решить через половину коэффициента", command=lambda: clicked3()).grid(row=5, column=0)

root.mainloop()
