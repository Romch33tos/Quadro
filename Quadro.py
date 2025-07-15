import tkinter as tk
import math
from customtkinter import CTk, CTkTextbox, CTkLabel, CTkEntry, CTkButton, CTkToplevel
from customtkinter import set_appearance_mode, set_default_color_theme

class QuadraticEquationSolver:
  def __init__(self):
    self.root = CTk()
    self.root.title("Quadro")
    self.root.geometry("370x505")
    self.root.resizable(width=False, height=False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    self.active_color = ("#2b7de9", "#1a5cb3")  
    self.hover_color = ("#1f6cd1", "#145099")   
    self.border_color = self.active_color       
    self.text_color_active = "white"            
    self.text_color_disabled = ("gray70", "gray40") 

    self.coeff_a = 0
    self.coeff_b = 0
    self.coeff_c = 0
    self.discriminant = 0
    self.root1 = 0
    self.root2 = 0

    self.help_window = None

    self.create_widgets()
    self.root.mainloop()

  def animate_button_state(self, button, target_state):
    if button == self.btn_help:
      if target_state == tk.NORMAL:
        button.configure(text_color=self.text_color_active)
      else:
        button.configure(text_color=self.text_color_disabled)
      button.configure(state=target_state)
      return

    current_color = button.cget("fg_color")
    if target_state == tk.NORMAL:
      target_color = self.active_color
      steps = 10
      for index in range(steps + 1):
        alpha = index / steps
        if isinstance(current_color, tuple) and isinstance(target_color, tuple):
          color = self.interpolate_color(current_color, target_color, alpha)
        else:
          color = target_color
        button.configure(fg_color=color)
        self.root.update()
        self.root.after(20)
    else:
      button.configure(fg_color="transparent", border_color=self.border_color, border_width=1)
    button.configure(state=target_state)

  def interpolate_color(self, color1, color2, alpha):
    red_1, green_1, blue_1 = int(color1[0][1:3], 16), int(color1[0][3:5], 16), int(color1[0][5:7], 16)
    red_2, green_2, blue_2 = int(color2[0][1:3], 16), int(color2[0][3:5], 16), int(color2[0][5:7], 16)
    red = int(red_1 + (red_2 - red_1) * alpha)
    green = int(green_1 + (green_2 - green_1) * alpha)
    blue = int(blue_1 + (blue_2 - blue_1) * alpha)
    return f"#{red:02x}{green:02x}{blue:02x}"

  def show_help(self):
    if self.help_window is not None:
      self.help_window.lift()
      return

    self.animate_button_state(self.btn_help, tk.DISABLED)

    self.help_window = CTkToplevel(self.root)
    self.help_window.title("Руководство")
    self.help_window.geometry("500x340")
    self.help_window.resizable(width=False, height=False)

    self.help_window.protocol("WM_DELETE_WINDOW", self.on_help_window_close)

    help_text = """Руководство по использованию приложения:

1. Введите коэффициенты уравнения в поля ввода.
2. Нажмите кнопку "Готово" или Enter.
3. Выберите доступный метод решения.
4. Используйте кнопку "Очистить все" для очистки полей.

Правила ввода:

1. Если один из коэффициентов отсутствует, вместо него необходимо ввести 0.
2. Коэффициент "а" не может быть равен 0.
3. Нельзя вводить посторонние символы, помимо цифр и знака "-".
"""

    help_label = CTkTextbox(self.help_window, width=480, height=320, wrap=tk.WORD, font=("Calibri", 18))
    help_label.pack(padx=10, pady=10)
    help_label.insert("1.0", help_text)
    help_label.configure(state=tk.DISABLED)

  def on_help_window_close(self):
    if self.help_window:
      self.help_window.destroy()
      self.help_window = None
    self.animate_button_state(self.btn_help, tk.NORMAL)

  def create_widgets(self):
    self.btn_help = CTkButton(
      self.root, width=80, text="Справка", command=self.show_help,
      font=("Calibri", 18), fg_color="transparent", hover=False,
      text_color=self.text_color_active
    )
    self.btn_help.grid(row=0, column=0, sticky=tk.NW, padx=10, pady=7)

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
      border_color=self.border_color, border_width=1
    )
    self.btn_process.grid(row=5, column=0, sticky=tk.NW, padx=190, pady=4, ipady=4, ipadx=8)

    self.btn_clear = CTkButton(
      self.root, width=150, text="Очистить все", command=self.clear_all,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25,
      fg_color=self.active_color, hover_color=self.hover_color,
      border_color=self.border_color, border_width=1
    )
    self.btn_clear.grid(row=5, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.label_methods = CTkLabel(self.root, text="Методы решения:", font=("Calibri", 18))
    self.label_methods.grid(row=6, column=0, sticky=tk.NW, padx=10, pady=4)

    self.btn_discriminant = CTkButton(
      self.root, width=150, text="D", command=self.solve_with_discriminant,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=1
    )
    self.btn_discriminant.grid(row=7, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.btn_half_discriminant = CTkButton(
      self.root, width=150, text="D/4", command=self.solve_with_half_discriminant,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=1
    )
    self.btn_half_discriminant.grid(row=7, column=0, sticky=tk.NW, padx=190, pady=4, ipady=4, ipadx=8)

    self.btn_vieta = CTkButton(
      self.root, width=150, text="Теорема Виета", command=self.solve_with_vieta,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=1
    )
    self.btn_vieta.grid(row=8, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.btn_coefficient_transfer = CTkButton(
      self.root, width=150, text="Переброска", command=self.solve_with_coefficient_transfer,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=1
    )
    self.btn_coefficient_transfer.grid(row=8, column=0, sticky=tk.NW, padx=190, pady=4, ipady=4, ipadx=8)

    self.btn_coefficient_properties = CTkButton(
      self.root, width=150, text="a + b + c = 0", command=self.solve_with_coefficient_properties,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=1
    )
    self.btn_coefficient_properties.grid(row=9, column=0, sticky=tk.NW, padx=10, pady=4, ipady=4, ipadx=8)

    self.btn_incomplete = CTkButton(
      self.root, width=150, text="Неполное", command=self.solve_incomplete,
      font=("Calibri", 18, "bold"), corner_radius=7, height=25, state=tk.DISABLED,
      fg_color="transparent", border_color=self.border_color, border_width=1
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
      self.btn_incomplete
    ]
    for button in buttons:
      self.animate_button_state(button, tk.DISABLED)

  def format_number(self, num):
    if num == int(num):
      return int(num)
    return round(num, 2)

  def process_equation(self):
    self.disable_all_methods()
    self.clear_text()

    try:
      self.get_coefficients()
      if self.coeff_a == 0:
        self.text_display.insert("1.0", "Коэффициент «а» не может равняться 0!")
        self.lock_inputs()
        return
      elif (self.coeff_b == 0) or (self.coeff_c == 0):
        self.text_display.insert("1.0", "Вы ввели неполное уравнение.")
        self.text_display.insert(tk.END, "\nВыберите метод решения.")
        self.animate_button_state(self.btn_incomplete, tk.NORMAL)
        self.lock_inputs()
        return

      self.discriminant = self.coeff_b**2 - 4 * self.coeff_a * self.coeff_c
      formatted_d = self.format_number(self.discriminant)

      if (self.coeff_a > 0 and self.coeff_c > 0) or (self.coeff_a < 0 and self.coeff_c < 0):
        self.text_display.insert("1.0",
          f"D = {self.coeff_b}² - 4 × {self.coeff_a} × {self.coeff_c} = "
          f"{self.coeff_b**2} - {4 * self.coeff_a * self.coeff_c} = {formatted_d}"
        )
      elif (self.coeff_a < 0) ^ (self.coeff_c < 0):
        self.text_display.insert("1.0",
          f"D = {self.coeff_b}² + 4 × {abs(self.coeff_a)} × {abs(self.coeff_c)} = "
          f"{self.coeff_b**2} + {abs(4 * self.coeff_a * self.coeff_c)} = {formatted_d}"
        )

      if self.discriminant > 0:
        self.text_display.insert(tk.END, "\nУравнение имеет два различных корня.")
        self.text_display.insert(tk.END, "\nВыберите метод решения.")
      elif self.discriminant == 0:
        self.text_display.insert(tk.END, "\nУравнение имеет два одинаковых корня.")
        self.text_display.insert(tk.END, "\nВыберите метод решения.")
      else:
        self.text_display.insert(tk.END, "\nУравнение не имеет корней.")
        self.lock_inputs()
        return

      sqrt_d = math.sqrt(self.discriminant)
      self.root1 = (-self.coeff_b + sqrt_d) / (2 * self.coeff_a)
      self.root2 = (-self.coeff_b - sqrt_d) / (2 * self.coeff_a)
      self.animate_button_state(self.btn_discriminant, tk.NORMAL)
      sqrt_d_int = int(sqrt_d)
      root1_int = int(self.root1)
      root2_int = int(self.root2)

      if (self.coeff_b != 0) and (self.coeff_b % 2 == 0):
        self.animate_button_state(self.btn_half_discriminant, tk.NORMAL)
      if (self.coeff_a == 1) and root1_int == self.root1 and root2_int == self.root2:
        self.animate_button_state(self.btn_vieta, tk.NORMAL)
      if (root1_int == self.root1 or root2_int == self.root2 or sqrt_d_int == sqrt_d):
        self.animate_button_state(self.btn_coefficient_transfer, tk.NORMAL)
      if ((self.coeff_a + self.coeff_b + self.coeff_c == 0) or
          (self.coeff_a - self.coeff_b + self.coeff_c == 0)):
        self.animate_button_state(self.btn_coefficient_properties, tk.NORMAL)
     
    except ValueError:
      self.text_display.insert("1.0", "Убедитесь, что вы ввели все данные корректно!")
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
    sqrt_d = math.sqrt(self.discriminant)
    formatted_d = self.format_number(self.discriminant)
    formatted_root1 = self.format_number(self.root1)
    formatted_root2 = self.format_number(self.root2)

    if (self.coeff_a > 0 and self.coeff_c > 0) or (self.coeff_a < 0 and self.coeff_c < 0):
      self.text_display.insert("1.0",
        f"D = {self.coeff_b}² - 4 × {self.coeff_a} × {self.coeff_c} = "
        f"{self.coeff_b**2} - {4 * self.coeff_a * self.coeff_c} = {formatted_d}"
      )
    elif (self.coeff_a < 0) ^ (self.coeff_c < 0):
      self.text_display.insert("1.0",
        f"D = {self.coeff_b}² + 4 × {abs(self.coeff_a)} × {abs(self.coeff_c)} = "
        f"{self.coeff_b**2} + {abs(4 * self.coeff_a * self.coeff_c)} = {formatted_d}"
      )

    self.text_display.insert(tk.END, "\nПо формуле корней:")
    self.text_display.insert(tk.END,
      f"\nx₁ = ({-self.coeff_b} + {self.format_number(sqrt_d)}) / (2 × {self.coeff_a}) = "
      f"{self.format_number(-self.coeff_b + sqrt_d)} / {2 * self.coeff_a} = {formatted_root1}"
    )
    self.text_display.insert(tk.END,
      f"\nx₂ = ({-self.coeff_b} - {self.format_number(sqrt_d)}) / (2 × {self.coeff_a}) = "
      f"{self.format_number(-self.coeff_b - sqrt_d)} / {2 * self.coeff_a} = {formatted_root2}"
    )
    self.text_display.configure(state=tk.DISABLED)

  def solve_with_half_discriminant(self):
    self.clear_text()
    self.get_coefficients()
    half_b = self.coeff_b / 2
    d4 = half_b**2 - self.coeff_a * self.coeff_c
    sqrt_d4 = math.sqrt(d4)
    root1 = (-half_b + sqrt_d4) / self.coeff_a
    root2 = (-half_b - sqrt_d4) / self.coeff_a

    formatted_d4 = self.format_number(d4)
    formatted_root1 = self.format_number(root1)
    formatted_root2 = self.format_number(root2)

    if (self.coeff_a > 0 and self.coeff_c > 0) or (self.coeff_a < 0 and self.coeff_c < 0):
      self.text_display.insert("1.0",
        f"k = {self.format_number(half_b)}, D/4 = {self.format_number(half_b)}² - {self.coeff_a} × {self.coeff_c} = "
        f"{self.format_number(half_b**2)} - {self.coeff_a * self.coeff_c} = {formatted_d4}"
      )
    elif (self.coeff_a < 0) ^ (self.coeff_c < 0):
      self.text_display.insert("1.0",
        f"k = {self.format_number(half_b)}, D/4 = {self.format_number(half_b)}² + {abs(self.coeff_a)} × {abs(self.coeff_c)} = "
        f"{self.format_number(half_b**2)} + {abs(self.coeff_a * self.coeff_c)} = {formatted_d4}"
      )

    self.text_display.insert(tk.END, "\nЧерез половину коэффициента:")
    self.text_display.insert(tk.END,
      f"\nx₁ = ({self.format_number(-half_b)} + {self.format_number(sqrt_d4)}) / {self.coeff_a} = "
      f"{self.format_number(-half_b + sqrt_d4)} / {self.coeff_a} = {formatted_root1}"
    )
    self.text_display.insert(tk.END,
      f"\nx₂ = ({self.format_number(-half_b)} - {self.format_number(sqrt_d4)}) / {self.coeff_a} = "
      f"{self.format_number(-half_b - sqrt_d4)} / {self.coeff_a} = {formatted_root2}"
    )
    self.text_display.configure(state=tk.DISABLED)

  def solve_with_vieta(self):
    self.clear_text()
    self.get_coefficients()
    formatted_root1 = self.format_number(self.root1)
    formatted_root2 = self.format_number(self.root2)

    self.text_display.insert("1.0", "По теореме Виета:")
    self.text_display.insert(tk.END, f"\nx₁ + x₂ = {-self.coeff_b}")
    self.text_display.insert(tk.END, f"\nx₁ × x₂ = {self.coeff_c}")
    self.text_display.insert(tk.END, f"\nx₁ = {formatted_root1}, x₂ = {formatted_root2}")
    self.text_display.configure(state=tk.DISABLED)

  def solve_with_coefficient_transfer(self):
    self.clear_text()
    self.get_coefficients()
    formatted_root1 = self.format_number(self.root1)
    formatted_root2 = self.format_number(self.root2)

    self.text_display.insert("1.0", "Методом переброски коэффициента:")
    self.text_display.insert(tk.END, f"\nx₁ + x₂ = {-self.coeff_b}")
    self.text_display.insert(tk.END, f"\nx₁ × x₂ = {self.coeff_c * self.coeff_a}")
    self.text_display.insert(tk.END,
      f"\nx₁ = {self.format_number(self.root1 * self.coeff_a)} / {self.coeff_a} = {formatted_root1}, "
      f"x₂ = {self.format_number(self.root2 * self.coeff_a)} / {self.coeff_a} = {formatted_root2}"
    )
    self.text_display.configure(state=tk.DISABLED)

  def solve_with_coefficient_properties(self):
    self.clear_text()
    self.get_coefficients()

    self.text_display.insert("1.0", "По свойству коэффициентов:")
    if self.coeff_a + self.coeff_b + self.coeff_c == 0:
      root2 = self.coeff_c / self.coeff_a
      formatted_root2 = self.format_number(root2)

      self.text_display.insert(tk.END, "\nТак как a + b + c = 0,")
      self.text_display.insert(tk.END, "\nx₁ = 1")
      self.text_display.insert(tk.END, f"\nx₂ = c / a = {self.coeff_c} / {self.coeff_a} = {formatted_root2}")

    if self.coeff_a - self.coeff_b + self.coeff_c == 0:
      root2 = -self.coeff_c / self.coeff_a
      formatted_root2 = self.format_number(root2)

      self.text_display.insert(tk.END, "\nТак как a - b + c = 0,")
      self.text_display.insert(tk.END, "\nx₁ = -1")
      self.text_display.insert(tk.END, f"\nx₂ = -c / a = {-self.coeff_c} / {self.coeff_a} = {formatted_root2}")

    self.text_display.configure(state=tk.DISABLED)

  def solve_incomplete(self):
    self.get_coefficients()
    self.clear_text()

    a_sign = "-" if self.coeff_a == -1 else "" if self.coeff_a == 1 else self.coeff_a
    b_sign = "" if abs(self.coeff_b) == 1 else abs(self.coeff_b)
    sign = "+" if (self.coeff_c > 0 or self.coeff_b > 0) else "-"

    if self.coeff_c != 0 and self.coeff_b == 0:
      ratio = -self.coeff_c / self.coeff_a
      formatted_ratio = self.format_number(ratio)

      self.text_display.insert("1.0", f"{a_sign}x² {sign} {abs(self.coeff_c)} = 0")
      self.text_display.insert(tk.END, f"\nx² = {formatted_ratio}")
      if ratio < 0:
        self.text_display.insert(tk.END, "\nНет корней!")
      else:
        root1 = math.sqrt(ratio)
        root2 = -math.sqrt(ratio)
        formatted_root1 = self.format_number(root1)
        formatted_root2 = self.format_number(root2)

        self.text_display.insert(tk.END, f"\nx₁ = {formatted_root1}")
        self.text_display.insert(tk.END, f"\nx₂ = {formatted_root2}")

    elif self.coeff_c == 0 and self.coeff_b != 0:
      sign = "+" if (self.coeff_a < 0 and self.coeff_b < 0) else "-" if (self.coeff_a < 0) else sign
      a_sign = "" if self.coeff_a == -1 else abs(self.coeff_a) if self.coeff_a < 0 else a_sign

      self.text_display.insert("1.0", f"{a_sign}x² {sign} {b_sign}x = 0")

      ratio = self.coeff_b / self.coeff_a
      formatted_ratio = self.format_number(abs(ratio))

      self.text_display.insert(tk.END, f"\n{a_sign}x × (x {sign} {formatted_ratio}) = 0")
      self.text_display.insert(tk.END, f"\n{a_sign}x = 0, (x {sign} {formatted_ratio}) = 0")

      root1 = 0
      root2 = -ratio
      formatted_root2 = self.format_number(root2)

      self.text_display.insert(tk.END, f"\nx₁ = {root1}, x₂ = {formatted_root2}")

    elif self.coeff_a != 0 and self.coeff_b == 0 and self.coeff_c == 0:
      self.text_display.insert("1.0", f"{a_sign}x² = 0")
      self.text_display.insert(tk.END, "\nx = 0")

    self.text_display.configure(state=tk.DISABLED)

if __name__ == "__main__":
  QuadraticEquationSolver()
