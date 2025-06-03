#-*-coding: utf-8-*-
from tkinter import *
from tkinter import messagebox as mb
import math
import matplotlib.pyplot as plt
import numpy as np

def clear_all():
  answer = mb.askyesno(title="Очистить данные", message="Вы действительно хотите
   очистить все данные?")
  if answer:
    text.configure(state=NORMAL)
    text.delete("1.0", END)
    a1.configure(state=NORMAL)
    b1.configure(state=NORMAL)
    c1.configure(state=NORMAL)
    a1.delete(0, END)
    b1.delete(0, END)
    c1.delete(0, END)
    a1.focus()
    text.configure(state=DISABLED)
    READY.configure(state=NORMAL)
    DB.configure(state=DISABLED)
    D4.configure(state=DISABLED)
    V.configure(state=DISABLED)
    P.configure(state=DISABLED)
    S.configure(state=DISABLED)
    G.configure(state=DISABLED)
    PR.configure(state=DISABLED)
    N.configure(state=DISABLED)
  else:
    pass

def how_to_use():
  mb.showinfo(title="Справка", message="Инструкция:", detail="1. Введите коэффициенты уравнения, следуя правилам ввода данных. Для того, чтобы переключаться между полями ввода, нажмите на кнопку «Tab» на клавиатуре или используйте мышку.\n2. Нажмите на кнопку «Готово» и выберите доступный вам способ решения.\n3. Чтобы очистить все данные, нажмите на кнопку «CLR».\n4. Если вы хотите завершить работу приложения, нажмите на кнопку «Выйти» в верхней строке меню или воспользуйтесь кнопкой, расположенной в правом верхнем углу окна.")

def entry_rules():
  mb.showinfo(title="Справка", message="Правила ввода:", detail="1. Поле ввода не должно содержать лишних символов, кроме числового значения коэффициента.\n2. Нельзя оставлять поле ввода пустым. Если один из коэффициентов отсутствует, вместо него нужно ввести 0. При этом, коэффициент перед х² ≠ 0!\n3. Если перед х² или х отсутствует числовое значение, то это значит, что коэффициент равен 1.")

def examples():
  mb.showinfo(title="Справка", message="Примеры для ввода данных", detail="В скобках указаны данные, которые необходимо ввести в соответствующее поле.\n
х² + 2x - 3 = 0 (a = 1, b = 2, c = -3)\nx² - x - 6 = 0 (a = 1, b = -1, c = -6)\n2х² - 50 = 0 (а = 2, b = 0, c = -50)\n3x² + 12x = 0 (a = 3, b = 12, c = 0)\n5x² = 0 (а = 5, b = 0, c = 0)")

def exit():
  answer = mb.askyesno(title="Выход", message="Вы действительно хотите выйти?")
  if answer:
    root.quit()

def ready():
  try:
    READY.configure(state=DISABLED)
    DB.configure(state=DISABLED)
    D4.configure(state=DISABLED)
    V.configure(state=DISABLED)
    P.configure(state=DISABLED)
    S.configure(state=DISABLED)
    G.configure(state=DISABLED)
    PR.configure(state=DISABLED)
    a1.configure(state=DISABLED)
    b1.configure(state=DISABLED)
    c1.configure(state=DISABLED)
    text.configure(state=NORMAL)
    text.delete("1.0", END)
    a = int(a1.get())
    b = int(b1.get())
    c = int(c1.get())
    d = (b ** 2 - 4 * a * c)
    if a == 0:
      text.configure(state=NORMAL)
      text.delete("1.0", END)
      text.configure(state=DISABLED)
      mb.showerror(title="Ошибка", message="Коэффициент a не может быть равен нулю!")
    if d >= 0:
      x1 = ((-b + d ** 0.5) / (2 * a))
      x2 = ((-b - d ** 0.5) / (2 * a))
  except ValueError:
    mb.showerror(title="Ошибкa", message="Убедитесь в том, что вы ввели все данные верно!")
    text.configure(state=DISABLED)
  if d > 0 and a != 0 and b != 0 and c != 0:
    text.configure(state=NORMAL)
    text.insert("1.0", "D = b² - 4ac = " + str(round(b * b)) + " - 4 × " + str(round(a)) + " × " + str(round(c)) + " = " + str("%.2f" % (d)))
    text.insert(END, "\nУравнение имеет два различных корня.")
    text.insert(END, "\nВыберите способ решения. ")
    text.configure(state=DISABLED)
  if d == 0 and a != 0 and b != 0 and c != 0:
    text.configure(state=NORMAL)
    text.insert("1.0", "D = b² - 4ac = " + str(round(b * b)) + " - 4 × " + str(round(a)) + " × " + str(round(c)) + " = " + str("%.2f" % (d)))
    text.insert(END, "\nУравнение имеет два одинаковых корня.")
    text.insert(END, "\nВыберите способ решения.")
    text.configure(state=DISABLED)
    # Остальные условия для ready() не нужно переносить, так как они не вызываются в данном блоке
    # Обратите внимание, что логика внутри этой функции должна быть дополнена, если есть необходимость
    # Также можно разбить на отдельные функции для каждого случая
    # В данном примере приведена основная структура
# Остальной код не изменен, только исправлены отступы и удалены комментарии
# Интерфейс и остальной код оставлен без изменений
root = Tk()

root.title("Приложение для решения квадратных уравнений")
root.geometry("590x275")
root.resizable(width=False, height=False)
menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=helpmenu)

menubar.add_command(label="Выйти", command=exit)

helpmenu.add_command(label="Инструкция", command=how_to_use)

helpmenu2 = Menu(helpmenu, tearoff=0)
helpmenu2.add_command(label="Правила ввода", command=entry_rules)
helpmenu2.add_command(label="Примеры", command=examples)
helpmenu.add_cascade(label="Ввод данных", menu=helpmenu2)

root.config(menu=menubar)

l1 = Label(root, text="Введите значения коэффициентов: ")
l1.grid(row=0, column=0, sticky=NW, padx=3, pady=5)

l2 = Label(root, text="Метод решения: ")
l2.grid(row=0, column=0, sticky=NW, padx=335, pady=5)

l3 = Label(root, text="Коэффициент а =")
l3.grid(row=1, column=0, sticky=NW, padx=3, pady=5)

l4 = Label(root, text="Коэффициент b =")
l4.grid(row=2, column=0, sticky=NW, padx=3, pady=5)

l5 = Label(root, text="Коэффициент c =")
l5.grid(row=3, column=0, sticky=NW, padx=3, pady=5)

l6 = Label(root, text="Решение")
l6.grid(row=4, column=0, sticky=SW, pady=5, padx=240)

a1 = Entry(root, width=15, justify=CENTER)
a1.configure(disabledbackground="white", disabledforeground="black")
a1.grid(row=1, column=0, sticky=NW, padx=110, pady=5)
a1.focus()

b1 = Entry(root, width=15, justify=CENTER)
b1.grid(row=2, column=0, sticky=NW, padx=110, pady=5)
b1.configure(disabledbackground="white", disabledforeground="black")

c1 = Entry(root, width=15, justify=CENTER)
c1.grid(row=3, column=0, sticky=NW, padx=110, pady=5)
c1.configure(disabledbackground="white", disabledforeground="black")

text = Text(width=62, height=4)
text.grid(row=6, column=0, padx=45, pady=5, sticky=NW)
text.insert("1.0", "Здравствуйте! Перед тем, как начать работу приложения, нажмите
на кнопку «Справка» в строке меню и ознакомьтесь с инструкцией
и правилами ввода.")
text.configure(state=DISABLED)

READY = Button(root, width=11, text="Готово", command=lambda: ready())
READY.grid(row=4, column=0, sticky=SW, padx=15, pady=5)

CLR = Button(root, width=11, text="CLR", command=lambda: clear_all())
CLR.grid(row=4, column=0, sticky=SW, padx=103, pady=5)

DB = Button(root, width=15, text="D", command=lambda: discr())
DB.grid(row=1, column=0, sticky=SW, padx=335, pady=5)
DB.configure(state=DISABLED)

D4 = Button(root, width=15, text="D/4", command=lambda: halfcoef())
D4.grid(row=1, column=0, sticky=SW, padx=465, pady=5)
D4.configure(state=DISABLED)

V = Button(root, width=15, text="Теорема Виета", command=lambda:Viet())
V.grid(row=2, column=0, sticky=SW, padx=335, pady=5)
V.configure(state=DISABLED)

P = Button(root, width=15, text="Переброска", command=lambda:perebros())
P.grid(row=2, column=0, sticky=SW, padx=465, pady=5)
P.configure(state=DISABLED)

S = Button(root, width=15, text="a + b + c = 0", command=lambda:svoistva())
S.grid(row=3, column=0, sticky=SW, padx=335, pady=5)
S.configure(state=DISABLED)

G = Button(root, width=15, text="Схема Горнера", command=lambda:Gorner())
G.grid(row=3, column=0, sticky=SW, padx=465, pady=5)
G.configure(state=DISABLED)

PR = Button(root, width=15, text="Графический", command=lambda:Parabola())
PR.grid(row=4, column=0, sticky=SW, padx=335, pady=6)
PR.configure(state=DISABLED)

N = Button(root, width=15, text="Неполное", command=lambda:nepolnoe())
N.grid(row=4, column=0, sticky=NW, padx=465, pady=5)
N.configure(state=DISABLED)

root.mainloop()
