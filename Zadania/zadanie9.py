from sympy import symbols, sin, exp, diff

# Całkowanie numeryczne — metoda parabol.
# S -3/1 | sin(x) * e^(-3 * x) + x^3 dx       n = 100       h = (b - a) / n = (1 - (-3)) / 100 = 4 / 100 = 0,04

# Definicja symboli i funkcji
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
f_x = sin(x) * exp(-3 * x) + x**3  # Funkcja podcałkowa
a = -3  # Dolna granica całkowania
b = 1  # Górna granica całkowania
n = 100  # Liczba podziałów (musi być parzysta)
h = (b - a) / n  # Szerokość każdego podziału

# Obliczenie punktów xi jako podział przedziałów
xi_wartosci = [a + i * h for i in range(1, n)]

# Podział punktów xi na punkty parzyste i nieparzyste
xi_wartosci_parzyste = [xi_wartosci[i] for i in range(1, len(xi_wartosci), 2)]
xi_wartosci_nieparzyste = [xi_wartosci[i] for i in range(0, len(xi_wartosci), 2)]

# Obliczenie przybliżonej wartości całki metodą parabol (złożony wzór Simpsona)
calka = h / 3 * (f_x.subs(x, a) + f_x.subs(x, b)
                 + 2 * sum(f_x.subs(x, xi) for xi in xi_wartosci_parzyste)
                 + 4 * sum(f_x.subs(x, xi) for xi in xi_wartosci_nieparzyste))

# Obliczenie czwartej pochodnej funkcji
f_x_pochodna4 = diff(f_x, x, 4)

# Obliczanie wartości dla 'a' i 'b' w czwartej pochodnej
wartosc_a_f_x_pochodna4 = f_x_pochodna4.subs(x, a).evalf()
wartosc_b_f_x_pochodna4 = f_x_pochodna4.subs(x, b).evalf()

# Wyznaczenie wartości maksymalnej
max_wartosc = max(wartosc_a_f_x_pochodna4, wartosc_b_f_x_pochodna4)

# Obliczenie błędu oszacowania
r = (((b - a)**5) / (n**4 * 90)) * max_wartosc

# Wypisanie wyniku
print("Wynik całki:", calka.evalf())
print("Wartość błędu:", r.evalf())
