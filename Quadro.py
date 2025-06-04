import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from customtkinter import *

root = CTk()
root.title("Приложение")
root.geometry("600x680")
root.resizable(width = False, height= False)
set_appearance_mode("dark")
set_default_color_theme("blue")

def clear_text():
     text.configure(state = NORMAL)
     text.delete("1.0", END)
     text.configure(state = DISABLED)
     
def clear_entry():
    a1.configure(state = NORMAL)
    b1.configure(state = NORMAL)
    c1.configure(state = NORMAL)
    a1.delete(0, END)
    b1.delete(0, END)
    c1.delete(0, END)
    a1.configure(state = DISABLED)
    b1.configure(state = DISABLED)
    c1.configure(state = DISABLED)
    
def clear_all():
    clear_text()
    clear_entry()
    block()
    READY.configure(state = NORMAL)
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
    block()
    try:
        a = int(a1.get())
        b = int(b1.get())
        c  = int(c1.get())
        if (a == 0):
            answer = mb.showerror(title = "Ошибка" , message ="Коэффициент «a» не может\nбыть равен нулю!")
        elif (a != 0):
            d = (b**2 - 4*a*c)		  
    except ValueError:
        answer = mb.showerror(title = "Ошибка ввода" , message ="Убедитесь в том, что вы\nввели все данные верно!")
		
text = CTkTextbox(root, width = 567, height = 160, wrap = WORD, font = ("Arial", 30))
text.grid(row = 0, column = 0, padx = 10,pady = 5, sticky = NW, ipadx = 5)
text.configure(state = DISABLED)

l = CTkLabel(root, text="Введите коэффициенты уравнения: ", font = ("Arial", 30))
l.grid(row = 1, column = 0, sticky = NW, padx = 10, pady = 5)

l3 = CTkLabel(root, text="Коэффициент а =", font = ("Arial", 30))
l3.grid(row = 2, column = 0, sticky = NW, padx = 10, pady = 6)

l4 = CTkLabel(root, text="Коэффициент b =", font = ("Arial", 30))
l4.grid(row = 3, column = 0, sticky = NW, padx = 10, pady = 6)

l5 = CTkLabel(root, text="Коэффициент c =", font = ("Arial", 30))
l5.grid(row = 4, column = 0, sticky = NW, padx = 10, pady = 5)

a1 = CTkEntry(root, width = 100, justify = CENTER, font = ("Arial", 30))
a1.grid(row = 2, column = 0, sticky = NW, padx = 260, pady = 5)
a1.focus()

b1 = CTkEntry(root, width = 100, justify = CENTER, font = ("Arial", 30))
b1.grid(row = 3, column = 0, sticky = NW, padx = 260, pady = 5)

c1 = CTkEntry(root, width = 100, justify = CENTER, font = ("Arial", 30))
c1.grid(row = 4, column = 0, sticky = NW, padx = 260, pady = 5)

READY = CTkButton(root, width = 255, text = "Готово", command = lambda: ready(), font = ("Arial", 30), corner_radius = 20)
READY.grid(row = 5, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

CLR = CTkButton(root, width = 255, text = "Очистить все", command = lambda: clear_all(), font = ("Arial", 30), corner_radius = 20)
CLR.grid(row = 5, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

l6 = CTkLabel(root, text = "Метод решения:",font = ("Arial", 30))
l6.grid(row = 6, column = 0, sticky = NW, padx = 10, pady = 5)

D = CTkButton(root, width = 255, text = "D", command = lambda: Discriminant(), font = ("Arial", 30), corner_radius = 20)
D.grid(row = 7, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

D4 = CTkButton(root, width = 255, text = "D/4", command = lambda: Discriminant(), font = ("Arial", 30), corner_radius = 20)
D4.grid(row = 7, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

D = CTkButton(root, width = 255, text = "D", command = lambda: Discriminant(), font = ("Arial", 30), corner_radius = 20)
D.grid(row = 7, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

V = CTkButton(root, width = 255, text = "Теорема Виета", command = lambda: Discriminant(), font = ("Arial", 30), corner_radius = 20)
V.grid(row = 8, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

P = CTkButton(root, width = 255, text = "Переброска", command = lambda: Discriminant(), font = ("Arial", 30), corner_radius = 20)
P.grid(row = 8, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

S = CTkButton(root, width = 255, text = "a ± b + c = 0", command = lambda: Discriminant(), font = ("Arial", 30), corner_radius = 20)
S.grid(row = 9, column = 0, sticky = NW, padx = 10, pady = 5,ipady = 5, ipadx = 10)

N = CTkButton(root, width = 255, text = "Неполное", command = lambda: Discriminant(), font = ("Arial", 30), corner_radius = 20)
N.grid(row = 9, column = 0, sticky = NW, padx = 310, pady = 5,ipady = 5, ipadx = 10)

root.mainloop()
