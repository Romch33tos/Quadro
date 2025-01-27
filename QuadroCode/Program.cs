using System;
using System.Net.Http.Headers;

class Programm {
  static void Main() {
    
    Console.Write("Введите значение коэффициента а: ");
    duble a = Convert.ToDouble(Console.ReadLine());

    Console.Write("Введите значение коэффициента b: ");
    double b = Convert.ToDouble(Console.ReadLine());

    Console.Write("Введите значение коэффициента c: ");
    double c = Convert.ToDouble(Console.ReadLine());

    double D = b * b - 4 * a * c;
    if (D >= 0) {
      Console.WriteLine($"Дискриминант уравнения = {D}\nКорни уравнения: ");
      double x1 = (-b + Math.Sqrt(D)) / (2 * a);
      double x2 = (-b - Math.Sqrt(D)) / (2 * a);
      Console.WriteLine($"x1 = {x1}, x2 = {x2}");
    } else {
        Console.WriteLine($"Дискриминант уравнения = {D}\nУравнение не имеет корней.");
      }
  }
}