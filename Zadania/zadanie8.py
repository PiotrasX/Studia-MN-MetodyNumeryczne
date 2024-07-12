from sympy import symbols

# Całkowanie numeryczne — metoda prostokątów.
# S 1/4 | 0.06 * x^2 + 2 dx       n = 3       h = (b - a) / n = (4 - 1) / 3 = 3 / 3 = 1

# Definicja symboli i funkcji
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
f_x = 0.06 * x**2 + 2  # Funkcja podcałkowa
a = 1  # Dolna granica całkowania
b = 4  # Górna granica całkowania
n = 3  # Liczba podziałów (prostokątów)
h = (b - a) / n  # Szerokość każdego prostokąta

# Obliczenie punktów środkowych każdego prostokąta
xi_wartosci = [a + (i + 0.5) * h for i in range(n)]

# Obliczenie przybliżonej wartości całki metodą prostokątów (użyto środkowego punktu każdego prostokąta)
calka = h * sum(f_x.subs(x, xi) for xi in xi_wartosci)

# Wypisanie wyniku
print("Wynik całki:", calka)
