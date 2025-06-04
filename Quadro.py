import tkinter as tk
from tkinter import *
from customtkinter import *
import math

a, b, c, d, x1, x2 = 0, 0, 0, 0, 0, 0

root = CTk()
root.title("Приложение")
root.geometry("600x670")
root.resizable(width = False, height = False)
set_appearance_mode("dark")
set_default_color_theme("blue")

def clear_text():
     text.configure(state = NORMAL)
     text.delete("1.0", END)
          
def get_entry():
     global a, b, c
     a = int(a1.get())
     b = int(b1.get())
     c = int(c1.get())
       
def clear_entry():
    a1.configure(state = NORMAL)
    b1.configure(state = NORMAL)
    c1.configure(state = NORMAL)
    a1.delete(0, END)
    b1.delete(0, END)
    c1.delete(0, END)
    
def clear_all():
    clear_text()
    clear_entry()
    block()
    READY.configure(state = NORMAL)    
    text.insert("1.0", "Введите коэффициенты уравнения")
    text.configure(state = DISABLED)
    a1.focus()
    a1.configure(state = NORMAL)
    b1.configure(state = NORMAL)
    c1.configure(state = NORMAL)
    
def block():
    READY.configure(state = DISABLED)
    D.configure(state = DISABLED)
    D4.configure(state = DISABLED)
    V.configure(state = DISABLED)
    P.configure(state = DISABLED)
    S.configure(state = DISABLED)
    N.configure(state = DISABLED)
    a1.configure(state = DISABLED)
    b1.configure(state = DISABLED)
    c1.configure(state = DISABLED)		
        
def ready():
    global d, x1, x2
    block()
    clear_text()  
    try:
        get_entry()
        if (a == 0):
            text.insert("1.0", "Коэффициент «а» не может равняться 0!")  
        if ((b == 0) or (c == 0)) and (a != 0):
            text.insert("1.0", "Вы ввели неполное уравнение.")
            text.insert(END, "\nВыберите метод решения.") 
            N.configure(state = NORMAL)    
        elif (a != 0 and b != 0 and c!= 0):
            d = b**2 - 4*a*c
            if (a > 0 and c > 0) or (a < 0 and c < 0):
                text.insert("1.0", f"D = {b}² - 4 × {a} x {c}  = {b**2} - {4 * a * c} = {d}")
            if ((a < 0) ^ (c < 0)):
                    text.insert("1.0", f"D = {b}² + 4 × {abs(a)} x {abs(c)}  = {b**2} + {abs(4 * a * c)} = {d}")
            if d > 0:
                text.insert(END, "\nУравнение имеет два различных корня.")
                text.insert(END, "\nВыберите метод решения.")   
            if d == 0:
                text.insert(END, "\nУравнение имеет два одинаковых корня.")
                text.insert(END, "\nВыберите метод решения.")   
            if d < 0:
                 text.insert(END,"\nУравнение не имеет корней.")		  
    except ValueError:
        text.insert("1.0", "Убедитесь, что вы ввели все данные корректно!")
    text.configure(state = DISABLED)
    
    if (a != 0) and (b != 0) and (c != 0) and d >= 0:
     x1 = ((-b + d**0.5) / (2*a))
     x2 = ((-b - d**0.5) / (2*a))
     D.configure(state = NORMAL)
     Dcheck = int(math.sqrt(d))
     x3 = int(x1)
     x4 = int(x2)
     
     if x3 == x1 or x4 == x2 or Dcheck == (math.sqrt(d)):
         P.configure(state = NORMAL)
         
     if (a == 1) and (b != 0) and (c != 0) and d >= 0:
         x3 = int(x1)
         x4 = int(x2)
         if x3 == x1 and x4 == x2:
             V.configure(state = NORMAL)
             
     if (a != 0) and (b != 0) and (c != 0)  and ((a + b + c == 0) or (a - b + c == 0)) and d >= 0:
         S.configure(state = NORMAL)
         
     if (a !=0) and (b != 0) and (b % 2 == 0) and (c !=0) and d >= 0:
         D4.configure(state = NORMAL)
		
def discriminant():
	clear_text()
	get_entry()	
	if (a > 0 and c > 0) or (a < 0 and c < 0):
	   text.insert("1.0", f"D = {b}² - 4 × {a} x {c}  = {b**2} - {4 * a * c} = {d}")
	elif ((a < 0) ^ (c < 0)):
	  text.insert("1.0", f"D = {b}² + 4 × {abs(a)} x {abs(c)}  = {b**2} + {abs(4 * a * c)} = {d}")
	text.insert(END, "\nПо формуле корней:")	
	text.insert(END, f"\nх1 = ({-b} + {int(math.sqrt(d))}) / (2 × {a}) = {int(-b + math.sqrt(d))} / {2 * a} = {x1:.2f}")
	text.insert(END, f"\nх2 = ({-b} - {int(math.sqrt(d))}) / (2 × {a}) = {int(-b - math.sqrt(d))} / {2 * a} = {x2:.2f}")	
	text.configure(state = DISABLED)
	
def halfOfTheCoefficient():
	clear_text()
	get_entry()	
	k = int(b/2)
	d = k**2 - a*c
	x1 = (-k + math.sqrt(d)) / a
	x2 = (-k - math.sqrt(d)) / a
	if (a > 0 and c > 0) or (a < 0 and c < 0):
	   text.insert("1.0", f"k = {k}, D/4 = {k}² - {a} x {c}  = {k**2} - {a * c} = {d}")
	elif ((a < 0) ^ (c < 0)):
	  text.insert("1.0", f"k = {k}, D/4 = {k}² + {abs(a)} x {abs(c)}  = {k**2} + {abs(a * c)} = {d}")
	text.insert(END, "\nЧерез половину коэффициента: ")	
	text.insert(END, f"\nх1 = ({-k} + {int(math.sqrt(d))}) / {a} = {int(-k + math.sqrt(d))} / { a} = {x1:.2f}")
	text.insert(END, f"\nх2 = ({-k} - {int(math.sqrt(d))}) / {a} = {int(-k - math.sqrt(d))} / {a} = {x2:.2f}")	
	text.configure(state = DISABLED)
	
def Viet():
	clear_text()
	get_entry()	
	text.insert("1.0", "По теореме Виета: ")
	text.insert(END, f"\nx1 + x2 = {-b}")
	text.insert(END, f"\nx1 × x2 = {c}")
	text.insert(END, f"\nx1 = {int(x1)}, x2 = {int(x2)}")
	text.configure(state = DISABLED)
	
def perebroska():
	clear_text()
	get_entry()	
	text.insert("1.0", "Методом переброски коэффициента: ")
	text.insert(END, f"\nx1 + x2 = {-b}")
	text.insert(END, f"\nx1 × x2 = {c * a}")
	text.insert(END, f"\nx1 = {int(x1 * a)} / {a} = {x1:.2f}, x2 = {int(x2 * a)} / {a} = {x2:.2f}")
	text.configure(state = DISABLED)						   			   
def svoistva():
    clear_text()
    get_entry()   
    text.insert("1.0", "По свойству коэффициентов:")
    if a + b + c == 0:       
    		text.insert(END, "\nТак как a + b + c = 0,")
    		text.insert(END, "\nx1 = 1")
    		text.insert(END, f"\nx2 = c / a = {c} / {a} = {int(c / a)}")	
    if a - b + c == 0:    		
    		text.insert(END, "\nТак как a - b + c = 0,")
    		text.insert(END, "\nx1 = -1")
    		text.insert(END, f"\nx2 = -c / a = {-c} / {a} = {int(-c/a)}")
    text.configure(state = DISABLED)
    
a_sign = ""
b_sign = ""
sign = ""
    
def replacement():
	global a, b, c, a_sign, sign,b_sign
	get_entry()
	clear_text()	
	if a == 1:
	    a_sign = ""
	elif a == -1:
	    a_sign = "-"
	else:
	    a_sign = a
	if b == 1 or b == -1:
	    b_sign = ""
	else:
	    b_sign = abs(b)
	if c > 0 or b > 0:
	    sign = "+"
	elif c < 0 or b < 0:
	    sign = "-"		
	
def nepolnoe():
	global sign, a_sign, b_sign
	replacement()
	get_entry()
	clear_text()		
	if (c != 0) and (-c/a < 0) and (b == 0):
		text.insert("1.0", f"{a_sign}x² {sign} {abs(c)} = 0")
		text.insert(END, f"\nx² = {int(-c/a)}")
		text.insert(END, "\nНет корней!")
		
	if (c != 0) and (-c/a > 0) and (b == 0):
		text.insert("1.0", f"{a_sign}x² {sign} {abs(c)} = 0")
		text.insert(END, f"\nx² = {int(-c/a)}")
		text.insert(END, f"\nx1 = {int(math.sqrt(-c/a))}")
		text.insert(END, f"\nx2 = {-int(math.sqrt(-c/a))}")
			
	if (c == 0) and (b != 0) and (a != 0):		
		text.insert("1.0", f"{a_sign}x² {sign} {b_sign}x = 0")
		if (a < 0) and (b < 0):
		    sign = "+"
		    a_sign = abs(a)
		if (a < 0) and (b > 0):
		    sign = "-"		
		    a_sign = abs(a)
		if (a == -1):
		    a_sign = ""
		text.insert(END, f"\n{a_sign}x × (x  {sign} {abs(int(b/a))}) = 0")
		text.insert(END, f"\n{a_sign}x = 0, (x {sign} {abs(int(b/a))}) = 0")
		text.insert(END, f"\nx1 = 0, x2 = {int(-b/a)}")
				
	if (a != 0) and (b == 0) and (c == 0):
		text.insert("1.0", f"{a_sign}x² = 0")
		text.insert(END, "\nx = 0")
	text.configure(state = DISABLED)
		
text = CTkTextbox(root, width = 567, height = 160, wrap = WORD, font = ("Arial", 29))
text.grid(row = 0, column = 0, padx = 10,pady = 7, sticky = NW, ipadx = 5)
text.insert("1.0", "Введите коэффициенты уравнения")
text.configure(state = DISABLED)

l1 = CTkLabel(root, text="Коэффициент а =", font = ("Arial", 30))
l1.grid(row = 2, column = 0, sticky = NW, padx = 10, pady = 6)

l2 = CTkLabel(root, text="Коэффициент b =", font = ("Arial", 30))
l2.grid(row = 3, column = 0, sticky = NW, padx = 10, pady = 6)

l3 = CTkLabel(root, text="Коэффициент c =", font = ("Arial", 30))
l3.grid(row = 4, column = 0, sticky = NW, padx = 10, pady = 5)

a1 = CTkEntry(root, width = 100, justify = CENTER, font = ("Arial", 30))
a1.grid(row = 2, column = 0, sticky = NW, padx = 260, pady = 5)
a1.focus()

b1 = CTkEntry(root, width = 100, justify = CENTER, font = ("Arial", 30))
b1.grid(row = 3, column = 0, sticky = NW, padx = 260, pady = 5)

c1 = CTkEntry(root, width = 100, justify = CENTER, font = ("Arial", 30))
c1.grid(row = 4, column = 0, sticky = NW, padx = 260, pady = 5)

READY = CTkButton(root, width = 255, text = "Готово", command = lambda: ready(), font = ("Arial", 30), corner_radius = 10, height = 50)
READY.grid(row = 5, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

CLR = CTkButton(root, width = 255, text = "Очистить все", command = lambda: clear_all(), font = ("Arial", 30), corner_radius = 10, height = 50)
CLR.grid(row = 5, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

l6 = CTkLabel(root, text = "Методы решения:",font = ("Arial", 30))
l6.grid(row = 6, column = 0, sticky = NW, padx = 10, pady = 5)

D = CTkButton(root, width = 255, text = "D", command = lambda: discriminant(), font = ("Arial", 30), corner_radius = 10, height = 50, state = DISABLED)
D.grid(row = 7, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

D4 = CTkButton(root, width = 255, text = "D/4", command = lambda: halfOfTheCoefficient(), font = ("Arial", 30), corner_radius = 10, height = 50, state = DISABLED)
D4.grid(row = 7, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

V = CTkButton(root, width = 255, text = "Теорема Виета", command = lambda: Viet(), font = ("Arial", 30), corner_radius = 10, height = 50, state = DISABLED)
V.grid(row = 8, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

P = CTkButton(root, width = 255, text = "Переброска", command = lambda: perebroska(), font = ("Arial", 30), corner_radius = 10, height = 50, state = DISABLED)
P.grid(row = 8, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

S = CTkButton(root, width = 255, text = "a ± b + c = 0", command = lambda: svoistva(), font = ("Arial", 30), corner_radius = 10, height = 50, state = DISABLED)
S.grid(row = 9, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

N = CTkButton(root, width = 255, text = "Неполное", command = lambda: nepolnoe(), font = ("Arial", 30), corner_radius = 10, height = 50, state = DISABLED)
N.grid(row = 9, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

root.mainloop()
