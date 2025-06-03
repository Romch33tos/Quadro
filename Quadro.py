from tkinter import *
from tkinter import messagebox as mb
import math

def help():
	answer = mb.showinfo(title = "Справка", message = "Информация")
	
def ready():
	ans.delete(0, END)
	a = float(a1.get())
	b = float(b1.get())
	c  = float(c1.get())
	
	Button(window, state = DISABLED, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Теорема Виета", command = lambda: Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "a + b + c = 0", command = lambda: svoistva()).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)

	if (a != 0) and ((b == 0) or (c == 0)):
		Button(window, state = NORMAL, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)
		
	if (a !=0) and (b !=0) and (c !=0):
		Button(window, state = NORMAL, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)
		
	if (a !=0) and (b != 0) and (b % 2 == 0) and (c !=0):
		
		Button(window, state = NORMAL, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)
		
	if (a == 1) and (b != 0) and (c != 0):
		Button(window, state = NORMAL, width = 10, text = "Теорема Виета", command = lambda: Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)
	
	if (a != 0) and (b != 0) and (c != 0):
		Button(window, state = NORMAL, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)
		
	if (a != 0) and (b != 0) and (c != 0) and ((a + b + c == 0) or ( a - b + c == 0)):
		Button(window, state = NORMAL, width = 10, text = "a + b + c = 0", command = lambda: svoistva()).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)
		
	if (a != 0) and (b != 0) and (c != 0):
		Button(window, state = NORMAL, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)
		
	if (a == 0):
		answer = mb.showerror(title = "Ошибка" , message ="Коэффициент a не может быть равен нулю!")
		
def discr():
	Button(window, state = DISABLED, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = (b**2 - 4*a*c)
	if d >= 0:
	    x1 = ((-b + d**0.5) / (2*a))
	    x2 = ((-b - d**0.5) / (2*a))
	    txt.set("D = " + str("%.2f"%(d)) + ". Корни уравнения: х1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
	else:
		Button(window, state = DISABLED, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)
		txt.set("D = " + str("%.2f"%(d)) + ". Корней нет. ")
		
def halfcoef():
     	Button(window, state = DISABLED, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)
     	a = float(a1.get())
     	b = float(b1.get())
     	c = float(c1.get())
     	k = (b / 2)
     	d = (k**2 - a*c)
     	if d >= 0:
     		x1 = ((-k + d**0.5)/ a)
     		x2 = ((-k - d**0.5)/ a)
     		txt.set("D = " + str("%.2f"%(d)) + ". Корни уравнения: х1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
     	else:
     	 	Button(window, state = DISABLED, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)
     	 	txt.set("D = " + str("%.2f"%(d)) + ". Корней нет. ")
     	 	
def Viet():
	Button(window, state = DISABLED, width = 10, text = "Теорема Виета", command = lambda:Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = b**2 - 4*a*c
	if d >= 0:
		for x1 in range(-100, 100):
			for x2 in range(-100, 100):
				p = (x1 + x2)
				q = (x1 * x2)
				if (p == -b) and (q == c):
					txt.set("По теореме Виета: х1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
	if d < 0:
	   					Button(window, state = DISABLED, width = 10, text = "Теорема Виета", command = lambda: Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)
	   					txt.set("D = " + str("%.2f"%(d)) + ". Корней нет. ")
	   					
def perebros():
	Button(window, state = DISABLED, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = b**2 - 4*a*c
	if d >= 0:
		for x1 in range(-100, 100):
			for x2 in range(-100, 100):
			   p = (x1 + x2)
			   q = (x1 * x2)
			   if (p == -b) and (q == c * a):
			   	txt.set("Методом «переброски» : х1 = " + str("%.2f"%(x1/a)) + ", x2 = " + str("%.2f"%(x2/a)) + ".")
	if d < 0:
		Button(window, state = DISABLED, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)
		txt.set("D = " + str("%.2f"%(d)) + ". Корней нет. ")
		
def svoistva():
    Button(window, state = DISABLED, width = 10, text = "a + b + c = 0", command = lambda: svoistva).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)
    a = float(a1.get())
    b = float(b1.get())
    c = float(c1.get())
    d = b**2 - 4*a*c
    if d >= 0:
    	if a + b + c == 0:
    		x1 = 1
    		x2 = (c / a)
    		txt.set("По свойству коэффициентов: х1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
    	if a - b + c == 0:
    		x1 = -1
    		x2 = (-c / a)
    		txt.set("По свойству коэффициентов: х1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
    	if d < 0:
    		Button(window, state = DISABLED, width = 10, text = "a + b + c = 0", command = lambda: svoistva).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)
    		txt.set("D = " + str("%.2f"%(d)) + ". Корней нет. ")

def Gorner():
	Button(window, state = DISABLED, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = b**2 - 4*a*c
	if d >= 0:
		for f in range(-100, 100):
			b2 = ((a * f) + b)
			c2 = ((b2 * f) + c)
			if c2 == 0:
				for e in range(-100, 100):
					b2 = ((a * e) + b)
					c2 = ((b2 * e) + c)
					if (e != f) and (c2 == 0):
						txt.set("По схеме Горнера: x1 = " + str("%.2f"%(f)) + ", x2 = " + str("%.2f"%(e)))
	else:
		Button(window, state = DISABLED, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)
		txt.set("D = " + str("%.2f"%(d)) + ". Корней нет. ")

def nepolnoe():
	Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	if (b == 0) and (a !=0) and (c != 0) and ((-c / a) >= 0):
		x1 = -(math.sqrt(-(c/a)))
		x2 = math.sqrt(-(c/a))
		txt.set("Корни уравнения: х1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
	if (-c / a < 0):
		Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)
		txt.set("Нет корней") #ax² + c = 0
	if (c == 0) and (b != 0) and (a != 0):
		Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)
		x1 = 0
		x2 =(-b/a)
		txt.set("Корни уравнения: х1 = " + str(x1) + ", x2 = " + str("%.2f"%(x2)) + ".")
	if (b == 0) and (c == 0) and (a != 0):
		Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)
		txt.set("Корень уравнения: x = 0")
	
window = Tk()
window.title("Программа")

txt = StringVar()

main_menu = Menu()

main_menu.add_cascade(label="Справка", command = lambda:help())

window.config(menu=main_menu)

l1 = Label(window, text="Введите значения коэффициентов: ")
l1.grid(row = 0, column = 0, sticky = NW, padx = 10, pady = 10)

l2 = Label(window, text="Выберите способ решения: ")
l2.grid(row = 0, column = 0, sticky = NW, padx = 700, pady = 10)

l3 = Label(window, text="Коэффициент а =")
l3.grid(row = 1, column = 0, sticky = NW, padx = 10, pady = 10)

l4 = Label(window, text="Коэффициент b =")
l4.grid(row = 2, column = 0, sticky = NW, padx = 10, pady = 10)

l5 = Label(window, text="Коэффициент c =")
l5.grid(row = 3, column = 0, sticky = NW, padx = 10, pady = 10)

l6 = Label(window, text = "Решение")
l6.grid(row = 5, column = 0, sticky = SW, pady = 10, padx = 590)

a1 = Entry(window, width = 14, justify = CENTER)
a1.grid(row = 1, column = 0, sticky = NW, padx = 300, pady = 10)

b1 = Entry(window, width = 14, justify = CENTER)
b1.grid(row = 2, column = 0, sticky = NW, padx = 300, pady = 10)

c1 = Entry(window, width = 14, justify = CENTER)
c1.grid(row = 3, column = 0, sticky = NW, padx = 300, pady = 10)

ans = Entry(window, width = 51, textvariable = txt)
ans.grid(row = 6, column = 0, padx = 125, ipady = 20, pady = 10, sticky = NW)

Button(window, width = 15, text = "Готово", command = lambda: ready()).grid(row = 4, column = 0, sticky = NW, padx = 125, pady = 10, ipadx = 1)

Button(window, state = DISABLED, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)

Button(window, state = DISABLED, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Теорема Виета", command = lambda:Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)

Button(window, state = DISABLED, width = 10, text = "a + b + c = 0", command = lambda: svoistva()).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)

window.mainloop()
