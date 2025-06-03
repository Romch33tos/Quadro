from tkinter import *
from tkinter import messagebox as mb
import math

def how_to_use():
	answer = mb.showinfo(title = "Как пользоваться программой?", message = "1. Введите коэффициенты уравнения, следуя правилам ввода данных.\n2. Нажмите на кнопку «Готово» и выберите интересующий вас способ.\n3. Чтобы завершить работу программы, нажмите кнопку «Выйти» в \nверхней панели меню.")

def entry_rules():
 	answer = mb.showinfo(title = "Правила ввода", message = "1. Поле ввода не должно содержать лишних символов кроме числового\nзначения коэффициента.\n2. Если у уравнения отсутствует коэффициент b или c, то в поле ввода\nнужно ввести число 0.\n3. Коэффициент a не может равняться нулю!\n4. Если перед x² или x отсутствует числовое значение, то коэффициент\nперед ними равен 1.")
 	
def ready():
	text.delete("1.0", END)
	a = float(a1.get())
	b = float(b1.get())
	c  = float(c1.get())
	d = (b**2 - 4*a*c)
	
	Button(window, state = DISABLED, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Теорема Виета", command = lambda: Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "a + b + c = 0", command = lambda: svoistva()).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)

	Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)
		
	if (a !=0) and (b !=0) and (c !=0) and d >= 0:
		Button(window, state = NORMAL, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)
		
	if (a !=0) and (b != 0) and (b % 2 == 0) and (c !=0) and d >= 0:
		
		Button(window, state = NORMAL, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)
		
	if (a == 1) and (b != 0) and (c != 0) and d >= 0:
		Button(window, state = NORMAL, width = 10, text = "Теорема Виета", command = lambda: Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)
	
	if (a != 0) and (b != 0) and (c != 0) and d >= 0:
		Button(window, state = NORMAL, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)
		
	if (a != 0) and (b != 0) and (c != 0)  and ((a + b + c == 0) or ( a - b + c == 0)) and d >= 0:
		Button(window, state = NORMAL, width = 10, text = "a + b + c = 0", command = lambda: svoistva()).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)
		
	if (a != 0) and (b != 0) and (c != 0) and d >= 0:
		Button(window, state = NORMAL, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)
		
	if (a != 0) and ((b == 0) or (c == 0)) and ((-c // a) > 0):
		Button(window, state = NORMAL, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)
		
	if (a == 0):
		answer = mb.showerror(title = "Ошибка" , message ="Коэффициент a не может быть равен нулю!")
	if d < 0 and (a != 0) and (b != 0) and (c != 0):
		text.insert("1.0", "D = " + str("%.2f"%(d)) + ". Нет корней.")
	if (b == 0) and (a !=0) and (c != 0) and ((-c // a) < 0):
			text.insert("1.0", "Нет корней.")
			
def discr():
	text.delete("1.0", END)
	Button(window, state = DISABLED, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = (b**2 - 4*a*c)
	if d >= 0:
	    x1 = ((-b + d**0.5) / (2*a))
	    x2 = ((-b - d**0.5) / (2*a))
	    text.insert("1.0", "D = b²-4ac = " +str(round(b)) + "²-4×" + str(round(a)) +"×" + str(round(c)) + " = " + str("%.2f"%(d)) + ". По формуле корней: ")
	    text.insert(END, "\nx1,2 = (-b±√D)÷2")
	    
	    
		
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
     		txt.set("D/4 = " + str("%.2f"%(d)) + ". Корни уравнения: х1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
     	 	
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
					txt.set("х1 + x2 = -" + str(b) + " x1 * x2 = " + str(c) + ". По теореме Виета: х1 =" + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)) + ".")
				
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
txt = StringVar()

window.title("Программа")
menubar = Menu(window)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=helpmenu)

helpmenu.add_command(label="Как пользоваться программой?", command=how_to_use)

helpmenu.add_command(label="Правила ввода", command=entry_rules)

menubar.add_command(label="Выйти", command=window.quit)

window.config(menu=menubar)

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

text = Text(width = 70, height = 2)
text.grid(row = 6, column = 0, padx = 50,pady = 10, sticky = NW)

Button(window, width = 15, text = "Готово", command = lambda: ready()).grid(row = 4, column = 0, sticky = NW, padx = 125, pady = 10, ipadx = 1)

Button(window, state = DISABLED, width = 10, text = "D", command = lambda: discr()).grid(row = 1, column = 0, sticky = SW, padx = 700, pady = 10)

Button(window, state = DISABLED, width = 10, text = "D/4", command = lambda: halfcoef()).grid(row = 1, column = 0, sticky = SW, padx = 980, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Теорема Виета", command = lambda:Viet()).grid(row = 2, column = 0, sticky = SW, padx = 700, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Переброска", command = lambda: perebros()).grid(row = 2, column = 0, sticky = SW, padx = 980, pady = 10)

Button(window, state = DISABLED, width = 10, text = "a + b + c = 0", command = lambda: svoistva()).grid(row = 3, column = 0, sticky = SW, padx = 700, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Схема Горнера", command = lambda: Gorner()).grid(row = 3, column = 0, sticky = SW, padx = 980, pady = 10)

Button(window, state = DISABLED, width = 10, text = "Неполное", command = lambda: nepolnoe()).grid(row = 4, column = 0, sticky = SW, padx = 840, pady = 10)

window.mainloop()
