import tkinter as tk
import math
import os
from customtkinter import CTk, CTkTextbox, CTkLabel, CTkEntry, CTkButton, CTkToplevel, CTkComboBox, CTkSwitch
from customtkinter import set_appearance_mode, set_default_color_theme

class QuadraticEquationSolver:
  def __init__(self):
    self.root = CTk()
    self.root.title("Quadro")
    self.root.geometry("370x520")
    self.root.resizable(width=False, height=False)
    
    self.dark_mode = False
    set_appearance_mode("light")
    set_default_color_theme("blue")

    self.active_color = ("#2b7de9", "#1a5cb3")  
    self.hover_color = ("#1f6cd1", "#145099")   
    self.border_color = self.active_color       
    self.text_color_active = "white"            
    self.text_color_disabled = ("gray70", "gray40") 
    self.label_color = "black"  
    self.button_text_color = "black" 

    self.coeff_a = 0
    self.coeff_b = 0
    self.coeff_c = 0
    self.discriminant = 0
    self.root1 = 0
    self.root2 = 0

    self.help_window = None
    self.theory_window = None
    self.history_window = None

    self.history_file = os.path.join(os.path.expanduser("~"), "quadro_history.txt")
    self.create_history_file()

    self.create_widgets()
    self.root.mainloop()

  def create_history_file(self):
    if not os.path.exists(self.history_file):
      with open(self.history_file, "w", encoding="utf-8") as file:
        file.write("")

  def toggle_theme(self):
    self.dark_mode = not self.dark_mode
    if self.dark_mode:
      set_appearance_mode("dark")
      self.label_color = "white"
      self.button_text_color = "white"
    else:
      set_appearance_mode("light")
      self.label_color = "black"
      self.button_text_color = "black"
    
    for widget in self.root.winfo_children():
      if isinstance(widget, CTkLabel):
        widget.configure(text_color=self.label_color)
      elif widget in [self.btn_help, self.btn_theory, self.btn_history]:
        widget.configure(text_color=self.button_text_color)

  def animate_button_state(self, button, target_state):
    if button in [self.btn_help, self.btn_theory, self.btn_history]:
      if target_state == tk.NORMAL:
        button.configure(text_color=self.button_text_color)
      else:
        button.configure(text_color=self.text_color_disabled)
      button.configure(state=target_state)
      return

    current_color = button.cget("fg_color")
    if target_state == tk.NORMAL:
      target_color = self.active_color
      button.configure(fg_color=target_color)
    else:
      button.configure(fg_color="transparent", border_color=self.border_color, border_width=2)
    button.configure(state=target_state)

  def load_text_from_file(self, filename):
    try:
      base_dir = os.path.dirname(os.path.abspath(__file__))
      resources_dir = os.path.join(base_dir, "resources")
      filepath = os.path.join(resources_dir, filename)
      
      with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    except Exception as error:
      print(f"Error loading file {filename}: {error}")
      return f"Не удалось загрузить содержимое файла {filename}"

  def show_help(self):
    if self.help_window is not None:
      self.help_window.lift()
      return

    self.animate_button_state(self.btn_help, tk.DISABLED)

    self.help_window = CTkToplevel(self.root)
    self.help_window.title("Справка")
    self.help_window.geometry("500x340")
    self.help_window.resizable(width=False, height=False)
    self.help_window.protocol("WM_DELETE_WINDOW", self.on_help_window_close)

    help_text = self.load_text_from_file("help.txt")
    
    help_label = CTkTextbox(self.help_window, width=480, height=320, wrap=tk.WORD, font=("Calibri", 18))
    help_label.pack(padx=10, pady=10)
    help_label.insert("1.0", help_text)
    help_label.configure(state=tk.DISABLED)

  def on_help_window_close(self):
    self.animate_button_state(self.btn_help, tk.NORMAL)
    self.help_window.destroy()
    self.help_window = None

  def show_theory(self):
    if self.theory_window is not None:
      self.theory_window.lift()
      return

    self.animate_button_state(self.btn_theory, tk.DISABLED)

    self.theory_window = CTkToplevel(self.root)
    self.theory_window.title("Теория")
    self.theory_window.geometry("500x370")
    self.theory_window.resizable(width=False, height=False)
    self.theory_window.protocol("WM_DELETE_WINDOW", self.on_theory_window_close)

    label_title = CTkLabel(
      self.theory_window, 
      text="Выберите раздел:", 
      font=("Calibri", 18)
    )
    label_title.pack(padx=10, pady=(10, 0), anchor=tk.W)

    self.theory_sections = [
      "1. Понятие квадратного уравнения",
      "2. Понятие дискриминанта",
      "3. Метод решения через половину коэффициента b",
      "4. Теорема Виета",
      "5. Метод переброски",
      "6. Свойства коэффициентов",
      "7. Решение неполных квадратных уравнений"
    ]
    
    self.theory_combobox = CTkComboBox(
      self.theory_window,
      values=self.theory_sections,
      font=("Calibri", 18),
      command=self.load_theory_section,
      state="readonly"
    )
    self.theory_combobox.set(self.theory_sections[0])
    self.theory_combobox.pack(padx=10, pady=(0, 10), fill=tk.X)

    self.theory_textbox = CTkTextbox(
      self.theory_window, 
      width=480, 
      height=300, 
      wrap=tk.WORD, 
      font=("Calibri", 18)
    )
    self.theory_textbox.pack(padx=10, pady=(0, 10))
    
    self.full_theory_text = self.load_text_from_file("theory.txt")
    self.theory_textbox.configure(state=tk.NORMAL)
    self.theory_textbox.insert("1.0", self.full_theory_text)
    self.load_theory_section(self.theory_sections[0])
    self.theory_textbox.configure(state=tk.DISABLED)

  def load_theory_section(self, section_name):
    if not hasattr(self, 'full_theory_text'):
      return

    self.theory_textbox.configure(state=tk.NORMAL)
    start_index = self.full_theory_text.find(section_name)
    
    if start_index != -1:
      line_start = self.full_theory_text.count('\n', 0, start_index) + 1
      self.theory_textbox.see(f"{line_start}.0")
    else:
      self.theory_textbox.see("1.0")
    
    self.theory_textbox.configure(state=tk.DISABLED)

  def on_theory_window_close(self):
    if self.theory_window:
      self.theory_window.destroy()
      self.theory_window = None
    self.animate_button_state(self.btn_theory, tk.NORMAL)

  def show_history(self):
    if self.history_window is not None:
      self.history_window.lift()
      return

    self.animate_button_state(self.btn_history, tk.DISABLED)

    self.history_window = CTkToplevel(self.root)
    self.history_window.title("История решений")
    self.history_window.geometry("500x400")
    self.history_window.resizable(width=False, height=False)
    self.history_window.protocol("WM_DELETE_WINDOW", self.on_history_window_close)

    self.history_textbox = CTkTextbox(
      self.history_window, 
      width=480, 
      height=340, 
      wrap=tk.WORD, 
      font=("Calibri", 18))
    self.history_textbox.pack(padx=10, pady=10)

    self.btn_clear_history = CTkButton(
      self.history_window,
      text="Очистить историю",
      command=self.clear_history,
      font=("Calibri", 18, "bold"),
      width=150,
      height=25,
      corner_radius=7,
      fg_color=self.active_color, hover_color=self.hover_color,
      border_color=self.border_color, border_width=2
    )
    self.btn_clear_history.pack(pady=(0, 10))

    self.load_history()

  def load_history(self):
    try:
      with open(self.history_file, "r", encoding="utf-8") as file:
        history_content = file.read()
        self.history_textbox.configure(state=tk.NORMAL)
        self.history_textbox.delete("1.0", tk.END)
        self.history_textbox.insert("1.0", history_content)
        self.history_textbox.configure(state=tk.DISABLED)
    except Exception as error:
      print(f"Ошибка при загрузке истории решений: {error}")

  def clear_history(self):
    try:
      with open(self.history_file, "w", encoding="utf-8") as file:
        file.write("")
      self.history_textbox.configure(state=tk.NORMAL)
      self.history_textbox.delete("1.0", tk.END)
      self.history_textbox.configure(state=tk.DISABLED)
    except Exception as error:
      print(f"Ошибка при очистке истории решений: {error}")

  def on_history_window_close(self):
    self.animate_button_state(self.btn_history, tk.NORMAL)
    self.history_window.destroy()
    self.history_window = None

  def format_equation(self, a, b, c):
    a_part = ""
    if a == 1:
      a_part = "x²"
    elif a == -1:
      a_part = "-x²"
    else:
      a_part = f"{a}x²"
    
    b_part = ""
    if b == 1:
      b_part = " + x"
    elif b == -1:
      b_part = " - x"
    elif b > 0:
      b_part = f" + {b}x"
    elif b < 0:
      b_part = f" - {abs(b)}x"
    
    c_part = ""
    if c > 0:
      c_part = f" + {c}"
    elif c < 0:
      c_part = f" - {abs(c)}"
    
    return f"{a_part}{b_part}{c_part} = 0"

  def save_to_history(self, equation, solution, solution_steps):
    try:
      with open(self.history_file, "a", encoding="utf-8") as file:
        file.write(f"{equation}\n")
        file.write(solution_steps + "\n")
        file.write(f"Ответ: {solution}\n")
        file.write("-" * 50 + "\n")
    except Exception as error:
      print(f"Ошибка при сохранении истории: {error}")

  def create_widgets(self):
    self.btn_help = CTkButton(
      self.root, width=80, text="Справка", command=self.show_help,
      font=("Calibri", 18), fg_color="transparent", hover=False,
      text_color=self.button_text_color
    )
    self.btn_help.grid(row=0, column=0, sticky=tk.NW, padx=10, pady=7)

    self.btn_theory = CTkButton(
      self.root, width=80, text="Теория", command=self.show_theory,
      font=("Calibri", 18), fg_color="transparent", hover=False,
      text_color=self.button_text_color
    )
    self.btn_theory.grid(row=0, column=0, sticky=tk.NW, padx=85, pady=7)

    self.btn_history = CTkButton(
      self.root, width=80, text="История", command=self.show_history,
      font=("Calibri", 18), fg_color="transparent", hover=False,
      text_color=self.button_text_color
    )
    self.btn_history.grid(row=0, column=0, sticky=tk.NW, padx=165, pady=7)

    self.theme_switch = CTkSwitch(
      self.root, 
      text="", 
      command=self.toggle_theme,
      width=40
    )
    self.theme_switch.grid(row=0, column=0, sticky=tk.NW, padx=295, pady=10)
    self.theme_switch.select() if self.dark_mode else self.theme_switch.deselect()

    self.theme_label = CTkLabel(
      self.root, 
      text="🌙", 
      font=("Calibri", 18),
      text_color=self.label_color
    )
    self.theme_label.grid(row=0, column=0, sticky=tk.NW, padx=340, pady=5)

    self.text_display = CTkTextbox(self.root, width=340, height=120, wrap=tk.WORD, font=("Calibri", 18))
    self.text_display.grid(row=1, column=0, padx=10, pady=7, sticky=tk.NW, ipadx=5)
    self.text_display.insert("1.0", "Введите коэффициенты уравнения")
    self.text_display.configure(state=tk.DISABLED)

    self.label_a = CTkLabel(self.root, text="Коэффициент а =", font=("Calibri", 18))
    self.label_a.grid(row=2, column=0, sticky=tk.NW, padx=10, pady=4)

    self.label_b = CTkLabel(self.root, text="Коэффициент b =", font=("Calibri", 18))
    self.label_b.grid(row=3, column=0, sticky=tk.NW, padx=10, pady=4)

    self.label_c = CTkLabel(self.root, text="Коэффициент c =", font=("Calibri", 18))
    self.label_c.grid(row=4, column=0, sticky=tk.NW, padx=10, pady=4)

    self.entry_a = CTkEntry(self.root, width=60, justify=tk.CENTER, font=("Calibri", 18))
    self.entry_a.grid(row=2, column=0, sticky=tk.NW, padx=150, pady=4)
    self.entry_a.focus()
    self.entry_a.bind('<Return>', lambda event: self.process_equation())

    self.entry_b = CTkEntry(self.root, width=60, justify=tk.CENTER, font=("Calibri", 18))
    self.entry_b.grid(row=3, column=0, sticky=tk.NW, padx=150, pady=4)
    self.entry_b.bind('<Return>', lambda event: self.process_equation())

    self.entry_c = CTkEntry(self.root, width=60, justify=tk.CENTER, font=("Calibri", 18))
    self.entry_c.grid(row=4, column=0, sticky=tk.NW, padx=150, pady=4)
    self.entry_c.bind('<Return>', lambda event: self.process_equation())

    self.btn_process = CTkButton(
      self.root, width=150, text="Готово", command=self.process_equation,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25,
      fg_color=self.active_color, hover_color=self.hover_color,
      border_color=self.border_color, border_width=2
    )
    self.btn_process.grid(row=5, column=0, sticky=tk.NW, padx=190, pady=4, ipady=4, ipadx=8)

    self.btn_clear = CTkButton(
      self.root, width=150, text="Очистить все", command=self.clear_all,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color=self.active_color, hover_color=self.hover_color,
      border_color=self.border_color, border_width=2
    )
    self.btn_clear.grid(row=5, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.label_methods = CTkLabel(self.root, text="Методы решения:", font=("Calibri", 18))
    self.label_methods.grid(row=6, column=0, sticky=tk.NW, padx=10, pady=4)

    self.btn_discriminant = CTkButton(
      self.root, width=150, text="D", command=self.solve_with_discriminant,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=2
    )
    self.btn_discriminant.grid(row=7, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.btn_half_discriminant = CTkButton(
      self.root, width=150, text="D/4", command=self.solve_with_half_discriminant,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=2
    )
    self.btn_half_discriminant.grid(row=7, column=0, sticky=tk.NW, padx=190, pady=4, ipady=4, ipadx=8)

    self.btn_vieta = CTkButton(
      self.root, width=150, text="Теорема Виета", command=self.solve_with_vieta,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=2
    )
    self.btn_vieta.grid(row=8, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.btn_coefficient_transfer = CTkButton(
      self.root, width=150, text="Переброска", command=self.solve_with_coefficient_transfer,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=2
    )
    self.btn_coefficient_transfer.grid(row=8, column=0, sticky=tk.NW, padx=190, pady=4, ipady=4, ipadx=8)

    self.btn_coefficient_properties = CTkButton(
      self.root, width=150, text="a ± b + c = 0", command=self.solve_with_coefficient_properties,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=2
    )
    self.btn_coefficient_properties.grid(row=9, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.btn_incomplete = CTkButton(
      self.root, width=150, text="Неполное", command=self.solve_incomplete,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=2
    )
    self.btn_incomplete.grid(row=9, column=0, sticky=tk.NW, padx=190, pady=4, ipady=4, ipadx=8)

  def clear_text(self):
    self.text_display.configure(state=tk.NORMAL)
    self.text_display.delete("1.0", tk.END)

  def get_coefficients(self):
    self.coeff_a = int(self.entry_a.get())
    self.coeff_b = int(self.entry_b.get())
    self.coeff_c = int(self.entry_c.get())

  def clear_entries(self):
    self.entry_a.configure(state=tk.NORMAL)
    self.entry_b.configure(state=tk.NORMAL)
    self.entry_c.configure(state=tk.NORMAL)

    self.entry_a.delete(0, tk.END)
    self.entry_b.delete(0, tk.END)
    self.entry_c.delete(0, tk.END)

  def clear_all(self):
    self.clear_text()
    self.clear_entries()
    self.disable_all_methods()

    self.animate_button_state(self.btn_process, tk.NORMAL)
    self.text_display.insert("1.0", "Введите коэффициенты уравнения")
    self.text_display.configure(state=tk.DISABLED)
    self.entry_a.focus()
  
    self.entry_a.configure(state=tk.NORMAL)
    self.entry_b.configure(state=tk.NORMAL)
    self.entry_c.configure(state=tk.NORMAL)

  def disable_all_methods(self):
    buttons = [
      self.btn_process,
      self.btn_discriminant,
      self.btn_half_discriminant,
      self.btn_vieta,
      self.btn_coefficient_transfer,
      self.btn_coefficient_properties,
      self.btn_incomplete,
      self.btn_clear
    ]
    for button in buttons:
      self.animate_button_state(button, tk.DISABLED)

  def format_number(self, number):
    if number == int(number):
      return int(number)
    return round(number, 2)

  def format_coeff(self, coeff, for_display=False):
    if coeff == 1:
      return "" if not for_display else "1"
    elif coeff == -1:
      return "-" if not for_display else "-1"
    elif coeff < 0:
      return f"-{abs(coeff)}" if not for_display else f"-{abs(coeff)}"
    else:
      return f"{coeff}"

  def format_coeff_with_sign(self, coeff):
    """Форматирует коэффициент со знаком для отображения в уравнениях"""
    if coeff == 1:
      return " + "
    elif coeff == -1:
      return " - "
    elif coeff < 0:
      return f" - {abs(coeff)}"
    else:
      return f" + {coeff}"

  def process_equation(self):
    self.disable_all_methods()
    self.clear_text()

    try:
      self.get_coefficients()
      equation = self.format_equation(self.coeff_a, self.coeff_b, self.coeff_c)
      
      if self.coeff_a == 0:
        self.text_display.insert("1.0", "Коэффициент «а» не может равняться 0!")
        self.lock_inputs()
        self.animate_button_state(self.btn_clear, tk.NORMAL)
        return
      elif (self.coeff_b == 0) or (self.coeff_c == 0):
        self.text_display.insert("1.0", "Вы ввели неполное уравнение.")
        self.text_display.insert(tk.END, "\nВыберите метод решения.")
        self.animate_button_state(self.btn_incomplete, tk.NORMAL)
        self.animate_button_state(self.btn_clear, tk.NORMAL)
        self.lock_inputs()
        return

      self.discriminant = self.coeff_b**2 - 4 * self.coeff_a * self.coeff_c
      formatted_discriminant = self.format_number(self.discriminant)

      # Форматированные коэффициенты для отображения
      a_display = self.format_coeff(self.coeff_a, True)
      b_display = self.format_coeff(abs(self.coeff_b), True)
      c_display = self.format_coeff(abs(self.coeff_c), True)

      solution_steps = ""
      if (self.coeff_a > 0 and self.coeff_c > 0) or (self.coeff_a < 0 and self.coeff_c < 0):
        solution_steps = (
          f"D = {self.coeff_b}² - 4 · {a_display} · {c_display} = "
          f"{self.coeff_b**2} - {4 * self.coeff_a * self.coeff_c} = {formatted_discriminant}"
        )
      elif (self.coeff_a < 0) ^ (self.coeff_c < 0):
        solution_steps = (
          f"D = {self.coeff_b}² + 4 · {a_display} · {c_display} = "
          f"{self.coeff_b**2} + {abs(4 * self.coeff_a * self.coeff_c)} = {formatted_discriminant}"
        )

      self.text_display.insert("1.0", solution_steps)

      if self.discriminant > 0:
        self.text_display.insert(tk.END, "\nУравнение имеет два различных корня.")
        self.text_display.insert(tk.END, "\nВыберите метод решения.")
      elif self.discriminant == 0:
        self.text_display.insert(tk.END, "\nУравнение имеет два одинаковых корня.")
        self.text_display.insert(tk.END, "\nВыберите метод решения.")
      else:
        self.text_display.insert(tk.END, "\nУравнение не имеет корней.")
        self.animate_button_state(self.btn_clear, tk.NORMAL)
        self.save_to_history(
          equation,
          "Нет корней",
          solution_steps
        )
        self.lock_inputs()
        return

      sqrt_discriminant = math.sqrt(self.discriminant)
      self.root1 = (-self.coeff_b + sqrt_discriminant) / (2 * self.coeff_a)
      self.root2 = (-self.coeff_b - sqrt_discriminant) / (2 * self.coeff_a)
      
      # Активация соответствующих методов решения
      self.animate_button_state(self.btn_discriminant, tk.NORMAL)
      sqrt_discriminant_int = int(sqrt_discriminant)
      root1_int = int(self.root1)
      root2_int = int(self.root2)

      if (self.coeff_b != 0) and (self.coeff_b % 2 == 0):
        self.animate_button_state(self.btn_half_discriminant, tk.NORMAL)
      if (self.coeff_a == 1) and root1_int == self.root1 and root2_int == self.root2:
        self.animate_button_state(self.btn_vieta, tk.NORMAL)
      if (root1_int == self.root1 or root2_int == self.root2 or sqrt_discriminant_int == sqrt_discriminant):
        self.animate_button_state(self.btn_coefficient_transfer, tk.NORMAL)
      if ((self.coeff_a + self.coeff_b + self.coeff_c == 0) or
          (self.coeff_a - self.coeff_b + self.coeff_c == 0)):
        self.animate_button_state(self.btn_coefficient_properties, tk.NORMAL)
      
      self.animate_button_state(self.btn_clear, tk.NORMAL)
    
    except ValueError:
      self.text_display.insert("1.0", "Убедитесь, что вы ввели все данные корректно!")
      self.animate_button_state(self.btn_clear, tk.NORMAL)
      self.lock_inputs()

    self.text_display.configure(state=tk.DISABLED)
    self.lock_inputs()


  def lock_inputs(self):
    self.entry_a.configure(state=tk.DISABLED)
    self.entry_b.configure(state=tk.DISABLED)
    self.entry_c.configure(state=tk.DISABLED)
    self.animate_button_state(self.btn_process, tk.DISABLED)

  def solve_with_discriminant(self):
    self.clear_text()
    self.get_coefficients()
    equation = self.format_equation(self.coeff_a, self.coeff_b, self.coeff_c)

    solution_steps = ""
    if (self.coeff_a > 0 and self.coeff_c > 0) or (self.coeff_a < 0 and self.coeff_c < 0):
      solution_steps = (
        f"D = {self.coeff_b}² - 4 · {self.format_coeff(self.coeff_a, True)} · {self.format_coeff(abs(self.coeff_c), True)} = "
        f"{self.coeff_b**2} - {4 * self.coeff_a * self.coeff_c} = {self.format_number(self.discriminant)}\n"
      )
    elif (self.coeff_a < 0) ^ (self.coeff_c < 0):
      solution_steps = (
        f"D = {self.coeff_b}² + 4 · {self.format_coeff(abs(self.coeff_a), True)} · {self.format_coeff(abs(self.coeff_c), True)} = "
        f"{self.coeff_b**2} + {abs(4 * self.coeff_a * self.coeff_c)} = {self.format_number(self.discriminant)}\n"
      )

    if self.discriminant > 0:
      sqrt_discriminant = math.sqrt(self.discriminant)
      root1 = (-self.coeff_b + sqrt_discriminant) / (2 * self.coeff_a)
      root2 = (-self.coeff_b - sqrt_discriminant) / (2 * self.coeff_a)
      formatted_root1 = self.format_number(root1)
      formatted_root2 = self.format_number(root2)
      
      solution_steps += "По формуле корней:\n"
      solution_steps += (
        f"x₁ = ({-self.coeff_b} + √{self.format_number(self.discriminant)}) / (2 · {self.format_coeff(self.coeff_a, True)}) = "
        f"({-self.coeff_b} + {self.format_number(sqrt_discriminant)}) / {2 * self.coeff_a} = {formatted_root1}\n"
      )
      solution_steps += (
        f"x₂ = ({-self.coeff_b} - √{self.format_number(self.discriminant)}) / (2 · {self.format_coeff(self.coeff_a, True)}) = "
        f"({-self.coeff_b} - {self.format_number(sqrt_discriminant)}) / {2 * self.coeff_a} = {formatted_root2}"
      )
      
      solution = f"x₁ = {formatted_root1}, x₂ = {formatted_root2}"
    elif self.discriminant == 0:
      root = -self.coeff_b / (2 * self.coeff_a)
      formatted_root = self.format_number(root)
      
      solution_steps += (
        f"x = {-self.coeff_b} / (2 · {self.format_coeff(self.coeff_a, True)}) = "
        f"{formatted_root}"
      )
      solution = f"x = {formatted_root}"
  
    self.text_display.insert("1.0", solution_steps)
    self.text_display.configure(state=tk.DISABLED)

    self.save_to_history(
      equation,
      solution,
      solution_steps
    )
 
  def solve_with_half_discriminant(self):
    self.clear_text()
    self.get_coefficients()
    half_b = self.coeff_b / 2
    discriminant_4 = half_b**2 - self.coeff_a * self.coeff_c
    sqrt_discriminant_4 = math.sqrt(discriminant_4)
    root1 = (-half_b + sqrt_discriminant_4) / self.coeff_a
    root2 = (-half_b - sqrt_discriminant_4) / self.coeff_a

    formatted_discriminant_4 = self.format_number(discriminant_4)
    formatted_root1 = self.format_number(root1)
    formatted_root2 = self.format_number(root2)
    equation = self.format_equation(self.coeff_a, self.coeff_b, self.coeff_c)

    solution_steps = ""
    if (self.coeff_a > 0 and self.coeff_c > 0) or (self.coeff_a < 0 and self.coeff_c < 0):
      solution_steps += (
        f"k = {self.format_number(half_b)}, D/4 = {self.format_number(half_b)}² - {self.coeff_a} · {self.coeff_c} = "
        f"{self.format_number(half_b**2)} - {self.coeff_a * self.coeff_c} = {formatted_discriminant_4}\n"
      )
    elif (self.coeff_a < 0) ^ (self.coeff_c < 0):
      solution_steps += (
        f"k = {self.format_number(half_b)}, D/4 = {self.format_number(half_b)}² + {abs(self.coeff_a)} · {abs(self.coeff_c)} = "
        f"{self.format_number(half_b**2)} + {abs(self.coeff_a * self.coeff_c)} = {formatted_discriminant_4}\n"
      )

    solution_steps += "Через половину коэффициента:\n"
    solution_steps += (
      f"x₁ = ({self.format_number(-half_b)} + {self.format_number(sqrt_discriminant_4)}) / {self.coeff_a} = "
      f"{self.format_number(-half_b + sqrt_discriminant_4)} / {self.coeff_a} = {formatted_root1}\n"
    )
    solution_steps += (
      f"x₂ = ({self.format_number(-half_b)} - {self.format_number(sqrt_discriminant_4)}) / {self.coeff_a} = "
      f"{self.format_number(-half_b - sqrt_discriminant_4)} / {self.coeff_a} = {formatted_root2}"
    )

    self.text_display.insert("1.0", solution_steps)
    self.text_display.configure(state=tk.DISABLED)

    self.save_to_history(
      equation,
      f"x₁ = {formatted_root1}, x₂ = {formatted_root2}",
      solution_steps
    )

  def solve_with_vieta(self):
    self.clear_text()
    self.get_coefficients()
    formatted_root1 = self.format_number(self.root1)
    formatted_root2 = self.format_number(self.root2)
    equation = self.format_equation(self.coeff_a, self.coeff_b, self.coeff_c)

    solution_steps = "По теореме Виета:\n"
    solution_steps += f"x₁ + x₂ = {-self.coeff_b}\n"
    solution_steps += f"x₁ · x₂ = {self.coeff_c}\n"
    solution_steps += f"x₁ = {formatted_root1}, x₂ = {formatted_root2}"

    self.text_display.insert("1.0", solution_steps)
    self.text_display.configure(state=tk.DISABLED)

    self.save_to_history(
      equation,
      f"x₁ = {formatted_root1}, x₂ = {formatted_root2}",
      solution_steps
    )

  def solve_with_coefficient_transfer(self):
    self.clear_text()
    self.get_coefficients()
    formatted_root1 = self.format_number(self.root1)
    formatted_root2 = self.format_number(self.root2)
    equation = self.format_equation(self.coeff_a, self.coeff_b, self.coeff_c)

    solution_steps = "Методом переброски коэффициента:\n"
    solution_steps += f"x₁ + x₂ = {-self.coeff_b}\n"
    solution_steps += f"x₁ · x₂ = {self.coeff_c * self.coeff_a}\n"
    solution_steps += (
      f"x₁ = {self.format_number(self.root1 * self.coeff_a)} / {self.coeff_a} = {formatted_root1}, "
      f"x₂ = {self.format_number(self.root2 * self.coeff_a)} / {self.coeff_a} = {formatted_root2}"
    )

    self.text_display.insert("1.0", solution_steps)
    self.text_display.configure(state=tk.DISABLED)

    self.save_to_history(
      equation,
      f"x₁ = {formatted_root1}, x₂ = {formatted_root2}",
      solution_steps
    )

  def solve_with_coefficient_properties(self):
    self.clear_text()
    self.get_coefficients()
    equation = self.format_equation(self.coeff_a, self.coeff_b, self.coeff_c)
    solution_steps = "По свойству коэффициентов:\n"
    
    if self.coeff_a + self.coeff_b + self.coeff_c == 0:
      root2 = self.coeff_c / self.coeff_a
      formatted_root2 = self.format_number(root2)

      solution_steps += "Так как a + b + c = 0:\n"
      solution_steps += "x₁ = 1\n"
      solution_steps += f"x₂ = c / a = {self.coeff_c} / {self.coeff_a} = {formatted_root2}"
      
      solution = f"x₁ = 1, x₂ = {formatted_root2}"
    

    if self.coeff_a - self.coeff_b + self.coeff_c == 0:
      root2 = -self.coeff_c / self.coeff_a
      formatted_root2 = self.format_number(root2)

      solution_steps += "Так как a - b + c = 0:\n"
      solution_steps += "x₁ = -1\n"
      solution_steps += f"x₂ = -c / a = {-self.coeff_c} / {self.coeff_a} = {formatted_root2}"
      
      solution = f"x₁ = -1, x₂ = {formatted_root2}"
  
    self.text_display.insert("1.0", solution_steps)
    self.text_display.configure(state=tk.DISABLED)

    self.save_to_history(
      equation,
      solution,
      solution_steps
    )

  def solve_incomplete(self):
    self.get_coefficients()
    self.clear_text()
    equation = self.format_equation(self.coeff_a, self.coeff_b, self.coeff_c)
    solution_steps = ""

    if self.coeff_c != 0 and self.coeff_b == 0:
      ratio = -self.coeff_c / self.coeff_a
      formatted_ratio = self.format_number(ratio)

      solution_steps += f"{equation}\n"
      solution_steps += f"x² = {formatted_ratio}\n"
      
      if ratio < 0:
        solution_steps += "Нет корней!"
        solution = "Нет корней"
      else:
        root1 = math.sqrt(ratio)
        root2 = -math.sqrt(ratio)
        formatted_root1 = self.format_number(root1)
        formatted_root2 = self.format_number(root2)

        solution_steps += f"x₁ = {formatted_root1}\n"
        solution_steps += f"x₂ = {formatted_root2}"
        solution = f"x₁ = {formatted_root1}, x₂ = {formatted_root2}"

    elif self.coeff_c == 0 and self.coeff_b != 0:
      ratio = self.coeff_b / self.coeff_a
      formatted_ratio = self.format_number(abs(ratio))
      sign = "-" if ratio > 0 else "+"

      solution_steps += f"{equation}\n"
      solution_steps += f"x · (x {sign} {formatted_ratio}) = 0\n"
      solution_steps += f"x = 0 или x {sign} {formatted_ratio} = 0\n"

      root1 = 0
      root2 = -ratio
      formatted_root2 = self.format_number(root2)

      solution_steps += f"x₁ = {root1}, x₂ = {formatted_root2}"
      solution = f"x₁ = {root1}, x₂ = {formatted_root2}"

    elif self.coeff_a != 0 and self.coeff_b == 0 and self.coeff_c == 0:
      solution_steps += f"{equation}\n"
      solution_steps += "x = 0"
      solution = "x = 0"
    
    self.text_display.insert("1.0", solution_steps)
    self.text_display.configure(state=tk.DISABLED)

    self.save_to_history(
      equation,
      solution,
      solution_steps
    )

if __name__ == "__main__":
  QuadraticEquationSolver()
