from sympy import symbols, sqrt

# Całkowanie numeryczne — metoda trapezów.
# S 0/1 | sqrt(1 + x) dx       h = 1 / 3       n = (b - a) / h = (1 - 0) / (1 / 3) = 1 / (1 / 3) = 1 * 3 = 3

# Definicja symboli i funkcji
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
f_x = sqrt(1 + x)  # Funkcja podcałkowa
a = 0  # Dolna granica całkowania
b = 1  # Górna granica całkowania
h = 1 / 3  # Szerokość każdego trapezu
n = int((b - a) / h)  # Liczba podziałów (trapezów)

# Obliczenie punktów xi jako podział przedziałów
xi_wartosci = [a + i * h for i in range(1, n)]

# Obliczenie przybliżonej wartości całki metodą trapezów
calka = h / 2 * (f_x.subs(x, a) + f_x.subs(x, b) + 2 * sum(f_x.subs(x, xi) for xi in xi_wartosci))

# Wypisanie wyniku
print("Wynik całki:", calka.evalf())
