#-*-coding: utf-8-*-
from tkinter import *
from tkinter import messagebox as mb
import math
import matplotlib.pyplot as plt
import numpy as np 

#Функция очистки окон с информацией

def clear_all(): 
	answer = mb.askyesno( title="Очистить данные", message="Вы действительно хотите\n   очистить все данные?")
	if answer == True:
		text.configure(state = NORMAL)
		text.delete("1.0", END)
		a1.configure(state = NORMAL)
		b1.configure(state = NORMAL)
		c1.configure(state = NORMAL)
		a1.delete(0, END)
		b1.delete(0, END)
		c1.delete(0, END)
		a1.focus()
		text.configure(state = DISABLED)
		READY.configure(state = NORMAL)
		DB.configure(state = DISABLED)
		D4.configure(state = DISABLED)
		V.configure(state = DISABLED)
		P.configure(state = DISABLED)
		S.configure(state = DISABLED)
		G.configure(state = DISABLED)
		PR.configure(state = DISABLED)
		N.configure(state = DISABLED)		
	else:
		pass

		
#Инструкция
	
def how_to_use(): 
	answer = mb.showinfo(title = "Справка", message = "Инструкция:", detail = "1. Введите коэффициенты уравнения, следуя правилам ввода данных. Для того, чтобы переключаться между полями ввода, нажмите на кнопку «Tab» на клавиатуре или используйте мышку.\n2. Нажмите на кнопку «Готово» и выберите доступный вам способ решения.\n3. Чтобы очистить все данные, нажмите на кнопку «CLR».\n4. Если вы хотите завершить работу приложения, нажмите на кнопку «Выйти» в верхней строке меню или воспользуйтесь кнопкой, расположенной в правом верхнем углу окна.")
	
#Правила ввода

def entry_rules():
 	answer = mb.showinfo(title = "Справка", message = "Правила ввода:", detail = "1. Поле ввода не должно содержать лишних символов, кроме числового значения коэффициента.\n2. Нельзя оставлять поле ввода пустым. Если один из коэффициентов отсутствует, вместо него нужно ввести 0. При этом, коэффициент перед х² ≠ 0!\n3. Если перед х² или х отсутствует числовое значение, то это значит, что коэффициент равен 1.")
 
#Примеры для ввода

def examples():
 	answer = mb.showinfo(title = "Справка", message = "Примеры для ввода данных", detail = "В скобках указаны данные, которые необходимо ввести в соответствующее поле.\n\nх² + 2x - 3 = 0 (a = 1, b = 2, c = -3)\nx² - x - 6 = 0 (a = 1, b = -1, c = -6)\n2х² - 50 = 0 (а = 2, b = 0, c = -50)\n3x² + 12x = 0 (a = 3, b = 12, c = 0)\n5x² = 0 (а = 5, b = 0, c = 0)")

#Функция выхода

def exit():
        answer = mb.askyesno( title="Выход", message="Вы действительно хотите выйти?")
        if answer == True:
        	root.quit()
        else:
        	pass
        	
#Проверка данных для опеределения дискриминанта и способов решения 
	
def ready():
	try:
		READY.configure(state = DISABLED)
		DB.configure(state = DISABLED)
		D4.configure(state = DISABLED)
		V.configure(state = DISABLED)
		P.configure(state = DISABLED)
		S.configure(state = DISABLED)
		G.configure(state = DISABLED)
		PR.configure(state = DISABLED)
		a1.configure(state = DISABLED)
		b1.configure(state = DISABLED)
		c1.configure(state = DISABLED)
		text.configure(state = NORMAL)
		text.delete("1.0", END)
		a = int(a1.get())
		b = int(b1.get())
		c  = int(c1.get())
		d = (b**2 - 4*a*c)		
		if a == 0:
			text.configure(state = NORMAL)
			text.delete("1.0", END)
			text.configure(state = DISABLED)
			answer = mb.showerror(title = "Ошибка" , message ="Коэффициент a не может быть равен нулю!")
		if d >= 0:
		    x1 = ((-b + d**0.5) / (2*a))
		    x2 = ((-b - d**0.5) / (2*a))
	except ValueError: 
		answer = mb.showerror(title = "Ошибкa" , message ="Убедитесь в том, что вы ввели все данные верно!")
		text.configure(state = DISABLED)
	
#Случай, если d > 0

	if d > 0 and (a !=0) and (b !=0) and (c !=0):
			text.configure(state = NORMAL)
			text.insert("1.0", "D = b² - 4ac = " +str(round(b*b)) + " - 4 × " + str(round(a)) +" × " + str(round(c)) + " = " + str("%.2f"%(d)))
			text.insert(END, "\nУравнение имеет два различных корня.")
			text.insert(END, "\nВыберите способ решения. ")
			text.configure(state = DISABLED)
			
#Случай, если d == 0

	if d == 0 and (a !=0) and (b !=0) and (c !=0):
		text.configure(state = NORMAL)
		text.insert("1.0", "D = b² - 4ac = " +str(round(b*b)) + " - 4 × " + str(round(a)) +" × " + str(round(c)) + " = " + str("%.2f"%(d)))
		text.insert(END, "\nУравнение имеет два одинаковых корня.")
		text.insert(END, "\nВыберите способ решения.")
		text.configure(state = DISABLED)

#Алгортим активации кнопок

#Условия для дискриминанта, схемы Горнера и переброски

	if (a !=0) and (b !=0) and (c !=0) and d >= 0:
	    DB.configure(state = NORMAL)
	    PR.configure(state = NORMAL)
	    x3 = int(x1)
	    x4 = int(x2)
	    Dcheck = int(math.sqrt(d))
	    if x3 == x1 and x4 == x2:
	        G.configure(state = NORMAL)
	    if Dcheck == math.sqrt(d) or x3 == x1 or x4 == x2:
	        P.configure(state = NORMAL)

#Условия для половины коэффициента
		
	if (a !=0) and (b != 0) and (b % 2 == 0) and (c !=0) and d >= 0:
		D4.configure(state = NORMAL)
		
#Условия для теоремы Виета
		
	if (a == 1) and (b != 0) and (c != 0) and d >= 0:
	    x3 = int(x1)
	    x4 = int(x2)
	    if x3 == x1 and x4 == x2:
	        V.configure(state = NORMAL)
	
#Условия для свойств коэффициентов
		
	if (a != 0) and (b != 0) and (c != 0)  and ((a + b + c == 0) or ( a - b + c == 0)) and d >= 0:
	    S.configure(state = NORMAL)
	    
#Условия для параболы (неполное)
		
	if ((b == 0) and (a !=0) and (c != 0) and ((-c / a) >= 0)) or ((c == 0) and (b != 0) and (a != 0)) or ((b == 0) and (c == 0) and (a != 0)):		
		PR.configure(state = NORMAL)

#ax² + c = 0
				
	if (a != 0) and (b == 0) and (c != 0):
		text.configure(state = NORMAL)
		text.insert("1.0", "Вы ввели неполное квадратное уравнение.")
		text.insert(END, "\nВыберите метод решения.")
		text.configure(state = DISABLED)
		N.configure(state = NORMAL)

#ax² + bx = 0
		
	if (a != 0) and (b != 0) and (c == 0):
		text.configure(state = NORMAL)
		text.insert("1.0", "Вы ввели неполное квадратное уравнение.")
		text.insert(END, "\nВыберите метод решения.")
		text.configure(state = DISABLED)
		N.configure(state = NORMAL)

#ax² = 0

	if (a != 0) and (b == 0) and (c == 0):
		text.configure(state = NORMAL)
		text.insert("1.0", "Вы ввели неполное квадратное уравнение.")
		text.insert(END, "\nВыберите метод решения.")
		text.configure(state = DISABLED)
		N.configure(state = NORMAL)
		
#Отрицательный дискриминант

	if d < 0 and (a != 0) and (b != 0) and (c != 0):
		text.configure(state = NORMAL)
		text.delete("1.0", END)
		text.insert("1.0", "D = b² - 4ac = " +str(round(b*b)) + " - 4 × " + str(round(a)) +" × " + str(round(c)) + " = " + str("%.2f"%(d)) + ", D < 0, нет корней")
		text.configure(state = DISABLED)

#Общий случай
		
	if (a < 0) and (c < 0) and (a != -1):
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x²" + " - " + str(round(-c)) + " = 0")
		text.insert(END, "\nx² = " + str(round(-c)) + " / " + str(round(a)))
		text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
		text.insert(END, "\nНет корней")
		text.configure(state = DISABLED)
		
#Алгоритм для дискриминанта
			
def discr():
	text.configure(state = NORMAL)
	text.delete("1.0", END)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = (b**2 - 4*a*c)
	if d >= 0:
	    x1 = ((-b + d**0.5) / (2*a))
	    x2 = ((-b - d**0.5) / (2*a))
	    text.insert("1.0", "D = b² - 4ac = " +str(round(b*b)) + " - 4 × " + str(round(a)) +" × " + str(round(c)) + " = " + str("%.2f"%(d)))
	    text.insert(END, "\nПо формуле корней квадратного уравнения: ")
	    text.insert(END, "\nx1 = (-b + √D) / 2a = (" + str(round(-b)) + " + " + str(round(math.sqrt(d))) + ") / " + str(round(2*a)) + " = " + str("%.2f"%(x1)))
	    text.insert(END, "\nx2 = (-b - √D) / 2a = (" + str(round(-b)) + " - " + str(round(math.sqrt(d))) + ") / " + str(round(2*a)) + " = " + str("%.2f"%(x2)))
	    text.configure(state = DISABLED)

#Алгоритм для половины коэффициента
		
def halfcoef():
     	text.configure(state = NORMAL)
     	text.delete("1.0", END)
     	a = float(a1.get())
     	b = float(b1.get())
     	c = float(c1.get())
     	k = (b / 2)
     	d = (k**2 - a*c)
     	if d >= 0:
     		x1 = ((-k + d**0.5)/ a)
     		x2 = ((-k - d**0.5)/ a)
     		text.insert("1.0", "k = " + str(round(b/2)) + ", D/4 = k² - ac = " + str(round(k*k)) + " - (" + str(round(a)) + " × " + str(round(c)) + ") = " + str("%.2f"%(d)))
     		text.insert(END, "\nПо формуле корней для чётного коэффициента b: ")
     		text.insert(END, "\nx1 = (-k + √D) / a = (" + str(round(-k)) + " + " + str(round(math.sqrt(d))) + ") / " + str(round(a)) + " = " + str("%.2f"%(x1)))
     		text.insert(END, "\nx2 = (-k - √D) / a = (" + str(round(-k)) + " - " + str(round(math.sqrt(d))) + ") / " + str(round(a)) + " = " + str("%.2f"%(x2)))
     		text.configure(state = DISABLED)
   
#Алгортим для теоремы Виета
  		
def Viet():
	text.configure(state = NORMAL)
	text.delete("1.0", END)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = b**2 - 4*a*c
	if d >= 0:
		text.insert("1.0", "По теореме Виета: ")
		text.insert(END, "\nx1 + x2 = " + str(round(-b)))
		text.insert(END, "\nx1 × x2 = " + str(round(c)))			
		for x1 in range(-100, 100):
			for x2 in range(-100, 100):
				p = (x1 + x2)
				q = (x1 * x2)
				if (p == -b) and (q == c) and (x1 != x2):
					text.insert(END, "\nx1 = " + str(x1) + ", x2 = " + str(x2))
					text.configure(state = DISABLED)
				if (p == -b) and (q == c) and (x1 == x2):
					text.configure(state = NORMAL)
					text.insert(END, "\nx1 = x2 = " + str(x1))
					text.configure(state = DISABLED)

#Алгортим для метода переброски									
def perebros():
	text.configure(state = NORMAL)
	text.delete("1.0", END)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = b**2 - 4*a*c
	if d >= 0:
		text.insert("1.0", "Методом переброски коэффициента:")
		text.insert(END, "\nx1 + x2 = " + str(round(-b)))
		text.insert(END, "\nx1 × x2 = " + str(round(c*a)))
		for x1 in range(-100, 100):
	  	 for x2 in range(-100, 100):
			   p = (x1 + x2)
			   q = (x1 * x2)
			   if (p == -b) and (q == c * a) and (x1 != x2):
			   	text.insert(END, "\nx1 = " + str(round(x1)) + " / " + str(round(a)) + " = " + str("%.2f"%(x1/a)) + ", x2 = " + str(round(x2)) + " / " + str(round(a)) + " = " + str("%.2f"%(x2/a)))
			   	text.configure(state = DISABLED)
			   if (p == -b) and (q == c * a) and (x1 == x2):
			   			   text.configure(state = NORMAL)
			   			   text.insert(END, "\nx1 = x2 = " + str(round(x1)) + " / " + str(round(a)) + " = " + str("%.2f"%(x1/a)))
			   			   text.configure(state = DISABLED)

#Алгортим для свойства коэффициентов
			   			   
def svoistva():
    text.configure(state = NORMAL)
    text.delete("1.0", END)
    a = float(a1.get())
    b = float(b1.get())
    c = float(c1.get())
    d = b**2 - 4*a*c
    if d >= 0:
    	if a + b + c == 0:
    		x1 = 1
    		x2 = (c / a)
    		text.insert("1.0", "Так как a + b + c = 0, то: ")
    		text.insert(END, "\nx1 = " + str("%.2f"%(x1)))
    		text.insert(END, "\nx2 = c / a = " + str("%.2f"%(c/a)))
    	if a - b + c == 0:
    		x1 = -1
    		x2 = (-c / a)
    		text.insert("1.0", "Так как a - b + c = 0, то:")
    		text.insert(END, "\nx1 = " + str("%.2f"%(x1)))
    		text.insert(END, "\nx2 = -c / a = " + str("%.2f"%(-c/a)))
    		text.configure(state = DISABLED)

#Алгортим для схемы Горнера
    		
def Gorner():
	text.configure(state = NORMAL)
	text.delete("1.0", END)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	d = b**2 - 4*a*c
	if d >= 0:
		text.insert("1.0", "По схеме Горнера: ")
		for f in range(-100, 100):
			b2 = ((a * f) + b)
			c2 = ((b2 * f) + c)
			if c2 == 0:
				text.insert(END, "\n| " + str(round(a)) + " | " + str(round(b2)) + " | " + str(round(c2)) + " |" + " при х = " + str("%.2f"%(f)))

def Parabola():
    text.configure(state = NORMAL)
    text.delete("1.0", END)
    text.insert("1.0", "Решение представлено на графике.")
    text.insert(END, "\nКорни уравнения отмечены синими точками.")
    a = int(a1.get())
    b = int(b1.get())
    c = int(c1.get())
    if b != 0 and c != 0:
            d = (b**2 - 4*a*c)
            x1 = ((-b + d**0.5) / (2*a))
            x2 = ((-b - d**0.5) / (2*a))
    if (b == 0) and (a !=0) and (c != 0) and ((-c / a) >= 0):
           x1 = -(math.sqrt(-(c/a)))
           x2 = math.sqrt(-(c/a))
    if (c == 0) and (b != 0) and (a != 0):
        x1 = 0
        x2 =(-b/a)
    if (b == 0) and (c == 0) and (a != 0):
        x1 = 0
        x2 = 0	
    x = np.linspace(-20, 20, 1000)
    y = a*x**2 + b*x + c
    fig, ax = plt.subplots()
    plt.grid(True)
    
    fig.set_size_inches(5, 4)
    ax.set_title("График функции")
    ax.plot(x, y, color = "black")
    ax.hlines(y = 0, xmin = min(x), xmax = max(x), color = "black", linestyles = '-', lw = 1)
    plt.plot(x1, 0, 'o', color = "blue")
    plt.plot(x2, 0, 'o',color = "blue")
    plt.show()
    text.configure(state = DISABLED)
    
#Алгоритм для решения неполных квадратных уравнений
						
def nepolnoe():
	N.configure(state = DISABLED)
	text.configure(state = NORMAL)
	text.delete("1.0", END)
	a = float(a1.get())
	b = float(b1.get())
	c = float(c1.get())
	
#Блокировка кнопки, если уравнение ax² + c = 0 не имеет корней
		
	if (b == 0) and (a !=0) and (c != 0) and ((-c / a) < 0) and (a > 0) and (c > 0):
		N.configure(state = DISABLED)
		
#Вывод данных, когда уравнение ax² + c = 0 не имеет корней (случай с а = 1)

	if (a == 1) and (c != 0) and (c > 0) and (b == 0):
		text.configure(state = NORMAL)
		text.insert("1.0", "x²" + " + " + str(round(c)) + " = 0")
		text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
		text.insert(END, "\nНет корней")
		text.configure(state = DISABLED)
		
#Если уравнение ax² + c = 0 не имеет корней (общий случай)		

	if (a != 1) and (a > 0) and (c != 0) and (c > 0) and (b == 0):
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x²" + " + " + str(round(c)) + " = 0")
		text.insert(END, "\nx² = " + str(round(-c)) + " / " + str(round(a)))
		text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
		text.insert(END, "\nНет корней")
		text.configure(state = DISABLED)

#Случай, когда a < 0 и c < 0	
	
	if (b == 0) and (a !=0) and (c != 0) and ((-c / a) < 0) and (a < 0) and (c < 0):
		N.configure(state = DISABLED)
		
#Вывод для a = -1

	if (a == - 1) and (c < 0):
		text.insert("1.0", "-x²" + " - " + str(round(-c)) + " = 0")
		text.insert(END, "\n-x² = " + str("%.2f"%(c//a)) + " | × (-1)")
		text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
		text.insert(END, "\nНет корней")
		text.configure(state = DISABLED)
	
#ах² + с = 0, когда а = 1
	
	if (b == 0) and (a !=0) and (c != 0) and ((-c / a) >= 0) and (a > 0):
		if (a == 1) and (c != 0):
			x1 = -(math.sqrt(-(c/a)))
			x2 = math.sqrt(-(c/a))
			text.configure(state = NORMAL)
			text.insert("1.0", "x²" + " - " +str(round(-c)) + " = 0")
			text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
			text.insert(END, "\nx1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)))
			text.configure(state = DISABLED)
	
#ах² + с = 0, общий случай, а > 0

		if (a > 0) and (a != 1) and (c != 0):
			x1 = -(math.sqrt(-(c/a)))
			x2 = math.sqrt(-(c/a))
			text.configure(state = NORMAL)
			text.insert("1.0", str(round(a)) + "x²" + " - " +str(round(-c)) + " = 0")
			text.insert(END, "\nx² = " + str(round(-c)) + " / " + str(round(a))) 
			text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
			text.insert(END, "\nx1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)))
			text.configure(state = DISABLED)

#ах² + с = 0, когда а = -1
		
	if (b == 0) and (a !=0) and (c != 0) and ((-c / a) >= 0) and (a < 0):
		if (a == -1) and (c != 0):
			x1 = -(math.sqrt(-(c/a)))
			x2 = math.sqrt(-(c/a))
			text.configure(state = NORMAL)
			text.insert("1.0", "-x²" + " + " +str(round(c)) + " = 0")
			text.insert(END, "\n-x² = " + str("%.2f"%(-c)) + " | × (-1)") 
			text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
			text.insert(END, "\nx1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)))
			text.configure(state = DISABLED)

#ах² + с = 0, случай для a < 0	
	
	if (a < 0) and (a != -1) and (c != 0):
		x1 = -(math.sqrt(-(c/a)))
		x2 = math.sqrt(-(c/a))
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x²" + " + " +str(round(c)) + " = 0")
		text.insert(END, "\nx² = " + str(round(-c)) + " / " + str(round(a))) 
		text.insert(END, "\nx² = " + str("%.2f"%(-c//a)))
		text.insert(END, "\nx1 = " + str("%.2f"%(x1)) + ", x2 = " + str("%.2f"%(x2)))
		text.configure(state = DISABLED)

#ax² + bx = 0, a > 0, b > 0

	if (c == 0) and (b != 0) and (a != 0) and (b > 0) and (a > 0) and (a != 1) and (b != 1):
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x² + " + str(round(b)) + "x = 0")
		text.insert(END, "\n" + str(round(a)) + "x × (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\n" + str(round(a)) + "x = 0, (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)
		
#ax² + bx = 0, a > 0, b > 0, a = 1, b != 1
		
	if (a == 1) and (b > 0) and (b != 1):
		text.configure(state = NORMAL)
		text.insert("1.0", "x² + " + str(round(b)) + "x = 0")
		text.insert(END, "\n" + "x × (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\n" + "x = 0, (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)

#ax² + bx = 0, a > 0, b > 0, a != 1, b = 1
		
	if (a != 1) and (a > 0) and (b == 1):
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x² + " + "x = 0")
		text.insert(END, "\n" + str(round(a)) + "x × (x + " + str("%.1f"%(b/a)) + ") = 0")
		text.insert(END, "\n" + str(round(a)) + "x = 0, (x + " + str("%.1f"%(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.1f"%(-b/a))))
		text.configure(state = DISABLED)
		
#ax² + bx = 0, a > 0, b < 0, a == 1, b = -1

	if (c == 0) and (b != 0) and (a != 0) and (a > 0) and (b < 0): 
		if (a == 1) and (b == -1):
			x1 = 0
			x2 =(-b/a)
			text.configure(state = NORMAL)
			text.insert("1.0", "x² - " + "x = 0")
			text.insert(END, "\n" +  "x × (x - " + str(round(-b/a)) + ") = 0")
			text.insert(END, "\n" + "x = 0, (x - " + str(round(-b/a)) + ") = 0")
			text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
			text.configure(state = DISABLED)
	
#ax² + bx = 0, a > 0, b < 0, a == 1, b != -1

	if (a == 1) and (b < 0) and (b != -1): 
			x1 = 0
			x2 =(-b/a)
			text.configure(state = NORMAL)
			text.insert("1.0", "x² - " + str(round(-b)) + "x = 0")
			text.insert(END, "\n"  + "x × (x - " + str(round(-b/a)) + ") = 0")
			text.insert(END, "\n" + "x = 0, (x - " + str(round(-b/a)) + ") = 0")
			text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
			text.configure(state = DISABLED)

#ax² + bx = 0, a > 0, b < 0, a != 1, b = -1
						
	if (a != 1) and (a > 0) and (b == -1):
			x1 = 0 
			x2 =(-b/a)
			text.configure(state = NORMAL)
			text.insert("1.0", str(round(a)) + "x² " + "- x = 0")
			text.insert(END, "\n" + str(round(a)) + "x × (x - " + str("%.1f"%(-b/a)) + ") = 0")
			text.insert(END, "\n" + str(round(a)) + "x = 0, (x - " + str("%.1f"%(-b/a)) + ") = 0")
			text.insert(END, "\nx1 = 0, x2 = " + str(str("%.1f"%(-b/a))))
			text.configure(state = DISABLED)

#ax² + bx = 0, a > 0, b < 0, a != 1, b != -1

	if (a != 1) and (a > 0) and (b < 0) and (b != -1):
			x1 = 0
			x2 =(-b/a)
			text.configure(state = NORMAL)
			text.insert("1.0", str(round(a)) + "x² - " + str(round(-b)) + "x = 0")
			text.insert(END, "\n" + str(round(a)) + "x × (x - " + str(round(-b/a)) + ") = 0")
			text.insert(END, "\n" + str(round(a)) + "x = 0, (x - " + str(round(-b/a)) + ") = 0")
			text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
			text.configure(state = DISABLED)

#ax² + bx = 0, a < 0, b < 0, a != -1, b != -1
			
	if (c == 0) and (b != 0) and (a != 0) and (a  < 0) and (b < 0) and (a != -1) and (b != -1): 
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x² - " + str(round(-b)) + "x = 0 | × (-1)")
		text.insert(END, "\n" + str(round(-a)) + "x × (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\n" + str(round(-a)) + "x = 0, (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)

#ax² + bx = 0, a < 0, b < 0, a == -1, b == -1
		
	if (c == 0) and (b != 0) and (a != 0) and (a  < 0) and (b < 0) and (a == -1) and (b == -1): 
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", "-x² - " + "x = 0 | × (-1)")
		text.insert(END, "\n" + "x × (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\n" + "x = 0, (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)
		
#ax² + bx = 0, a > 0, b > 0, a == 1 b == 1

	if (c == 0) and (a == 1) and (b == 1): 
		text.configure(state = NORMAL)
		text.insert("1.0", "x² + " + "x = 0")
		text.insert(END, "\n" + "x × (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\n" + "x = 0, (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)

#ax² + bx = 0, a < 0, b > 0, a != -1, b != 1

	if (c == 0) and (b != 0) and (a != 0) and (a < 0) and (b > 0) and (a != -1) and (b != 1): 
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x² + " + str(round(b)) + "x = 0 | × (-1)")
		text.insert(END, "\n" + str(round(-a)) + "x × (x - " + str(round(-b/a)) + ") = 0")
		text.insert(END, "\n" + str(round(-a)) + "x = 0, (x - " + str(round(-b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)

#ax² + bx = 0, a < 0, b > 0, a != -1, b == 1
		
	if (c == 0) and (b != 0) and (a != 0) and (a < 0) and (b > 0) and (a != -1) and (b == 1): 
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x² + " + "x = 0 | × (-1)")
		text.insert(END, "\n" + str(round(-a)) + "x × (x - " + str("%.1f"%(-b/a)) + ") = 0")
		text.insert(END, "\n" + str(round(-a)) + "x = 0, (x - " + str("%.1f"%(-b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.1f"%(-b/a))))
		text.configure(state = DISABLED)
		
#ax² + bx = 0, a < 0, b > 0, a == -1, b != 1,b > 0
		
	if (c == 0) and (b != 0) and (a != 0) and (a < 0) and (b > 0) and (a == -1) and (b != 1): 
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", "-x² + " + str(round(b)) + "x = 0 | × (-1)")
		text.insert(END, "\n" + "x × (x - " + str(round(-b/a)) + ") = 0")
		text.insert(END, "\n" + "x = 0, (x - " + str(round(-b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)
		
#ax² + bx = 0, a < 0, b > 0, a == -1, b != 1,b < 0

	if (a == -1) and (b != 1) and (b !=0) and (b != -1) and (b < 0): 
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", "-x² - " + str(round(-b)) + "x = 0 | × (-1)")
		text.insert(END, "\n" + "x × (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\n" + "x = 0, (x + " + str(round(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)
		
#ax² + bx = 0, a < 0, b > 0, a != -1, b == -1

	if (a != 1) and (a != -1) and (a < 0) and (b == -1): 
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x² - " + "x = 0 | × (-1)")
		text.insert(END, "\n" + str(round(-a)) + "x × (x + " + str("%.1f"%(b/a)) + ") = 0")
		text.insert(END, "\n" + str(round(-a))+ "x = 0, (x + " + str("%.1f"%(b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.1f"%(-b/a))))
		text.configure(state = DISABLED)

#ax² + bx = 0, a < 0, b > 0, a == -1, b == 1
		
	if (a == -1) and (b == 1) and (b != 0):
		x1 = 0
		x2 =(-b/a)
		text.configure(state = NORMAL)
		text.insert("1.0", "-x² + " + "x = 0 | × (-1)")
		text.insert(END, "\n" + "x × (x - " + str(round(-b/a)) + ") = 0")
		text.insert(END, "\n" + "x = 0, (x - " + str(round(-b/a)) + ") = 0")
		text.insert(END, "\nx1 = 0, x2 = " + str(str("%.2f"%(-b/a))))
		text.configure(state = DISABLED)

#ax² = 0, общий случай
		
	if (a != 0) and(b == 0) and (c == 0) and (a != 1) and (a != -1):
		text.configure(state = NORMAL)
		text.insert("1.0", str(round(a)) + "x² = 0")
		text.insert(END, "\nx = 0")
		text.configure(state = DISABLED)
		
#ах² = 0, а = 1
		
	if (a == 1) and (a != 0) and(b == 0) and (c == 0):
		text.configure(state = NORMAL)
		text.insert("1.0", "x² = 0")
		text.insert(END, "\nx = 0")
		text.configure(state = DISABLED)
		
#ах² = 0, а = -1

	if (a == -1) and (a != 0) and (b == 0) and (c == 0):
		text.configure(state = NORMAL)
		text.insert("1.0", "-x² = 0")
		text.insert(END, "\nx = 0")
		text.configure(state = DISABLED)
	
#Графический интерфейс
		
root = Tk()

root.title("Приложение для решения квадратных уравнений")
root.geometry("590x275")
root.resizable(width = False, height = False)
menubar = Menu(root)

#Меню

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=helpmenu)

menubar.add_command(label="Выйти", command=exit)

helpmenu.add_command(label="Инструкция", command=how_to_use)

helpmenu2 = Menu(helpmenu, tearoff=0)
helpmenu2.add_command(
    label="Правила ввода", command = entry_rules)
helpmenu2.add_command(
    label="Примеры", command = examples)
 
helpmenu.add_cascade(label="Ввод данных", menu = helpmenu2)

root.config(menu=menubar)

#Надписи

l1 = Label(root, text="Введите значения коэффициентов: ")
l1.grid(row = 0, column = 0, sticky = NW, padx = 3, pady = 5)

l2 = Label(root, text="Метод решения: ")
l2.grid(row = 0, column = 0, sticky = NW, padx = 335, pady = 5)

l3 = Label(root, text="Коэффициент а =")
l3.grid(row = 1, column = 0, sticky = NW, padx = 3, pady = 5)

l4 = Label(root, text="Коэффициент b =")
l4.grid(row = 2, column = 0, sticky = NW, padx = 3, pady = 5)

l5 = Label(root, text="Коэффициент c =")
l5.grid(row = 3, column = 0, sticky = NW, padx = 3, pady = 5)

l6 = Label(root, text = "Решение")
l6.grid(row = 4, column = 0, sticky = SW, pady = 5, padx = 240)

#Поля ввода коэффициентов

a1 = Entry(root, width = 15, justify = CENTER)
a1.configure(disabledbackground="white", disabledforeground="black")
a1.grid(row = 1, column = 0, sticky = NW, padx = 110, pady = 5)
a1.focus()

b1 = Entry(root, width = 15, justify = CENTER)
b1.grid(row = 2, column = 0, sticky = NW, padx = 110, pady = 5)
b1.configure(disabledbackground="white", disabledforeground="black")

c1 = Entry(root, width = 15, justify = CENTER)
c1.grid(row = 3, column = 0, sticky = NW, padx = 110, pady = 5)
c1.configure(disabledbackground="white", disabledforeground="black")

#Текстовый виджет для вывода данных

text = Text(width = 62, height = 4)
text.grid(row = 6, column = 0, padx = 45, pady = 5, sticky = NW)
text.insert("1.0", "Здравствуйте! Перед тем, как начать работу приложения, нажмите\nна кнопку «Справка» в строке меню и ознакомьтесь с инструкцией\nи правилами ввода.")
text.configure(state = DISABLED)

#Кнопки

READY = Button(root, width = 11, text = "Готово", command = lambda: ready())
READY.grid(row = 4, column = 0, sticky = SW, padx = 15, pady = 5)

CLR = Button(root, width = 11, text = "CLR", command = lambda: clear_all())
CLR.grid(row = 4, column = 0, sticky = SW, padx = 103, pady = 5)

DB = Button(root, width = 15, text = "D", command = lambda: discr())
DB.grid(row = 1, column = 0, sticky = SW, padx = 335, pady = 5)
DB.configure(state = DISABLED)

D4 = Button(root,  width = 15, text = "D/4", command = lambda: halfcoef())
D4.grid(row = 1, column = 0, sticky = SW, padx = 465, pady = 5)
D4.configure(state = DISABLED)

V = Button(root, width = 15, text = "Теорема Виета", command = lambda:Viet())
V.grid(row = 2, column = 0, sticky = SW, padx = 335, pady = 5)
V.configure(state = DISABLED)

P = Button(root, width = 15, text = "Переброска", command = lambda: perebros())
P.grid(row = 2, column = 0, sticky = SW, padx = 465, pady = 5)
P.configure(state = DISABLED)

S = Button(root, width = 15, text = "a + b + c = 0", command = lambda: svoistva())
S.grid(row = 3, column = 0, sticky = SW, padx = 335, pady = 5)
S.configure(state = DISABLED)

G = Button(root, width = 15, text = "Схема Горнера", command = lambda: Gorner())
G.grid(row = 3, column = 0, sticky = SW, padx = 465, pady = 5)
G.configure(state = DISABLED)

PR = Button(root, width = 15, text = "Графический", command = lambda: Parabola())
PR.grid(row = 4, column = 0, sticky = SW, padx = 335, pady = 6)
PR.configure(state = DISABLED)

N = Button(root, width = 15, text = "Неполное", command = lambda: nepolnoe())
N.grid(row = 4, column = 0, sticky = NW, padx = 465, pady = 5)
N.configure(state = DISABLED)

root.mainloop()
