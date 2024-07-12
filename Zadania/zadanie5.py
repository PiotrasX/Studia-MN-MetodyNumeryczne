from sympy import symbols, diff

# Rozwiązywanie równań nieliniowych — metoda siecznych.
# f(x)   = x^3 + x^2 - 3 * x - 3       <1, 2>       E = 0.0001
# f'(x)  = 3 * x^2 + 2 * x - 3
# f''(x) = 6 * x + 2

# Definicja symboli i funkcji
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
f_x = x**3 + x**2 - 3 * x - 3  # Definicja funkcji f(x)
f_x_pochodna1 = diff(f_x, x)  # Pierwsza pochodna f(x) względem x
f_x_pochodna2 = diff(f_x_pochodna1, x)  # Druga pochodna f(x) względem x

# Parametry początkowe
blad = 0.0001  # Określenie dokładności szukanej wartości
wartosc_a = 1  # Początek przedziału
wartosc_b = 2  # Koniec przedziału

# Sprawdzenie warunku istnienia pierwiastka równania w przedziale
if f_x.subs(x, wartosc_a) * f_x.subs(x, wartosc_b) >= 0:
    print("\nRównanie f(x) nie zawiera pierwiastka równania w podanym przedziale")
else:
    print("\nRównanie f(x) zawiera pierwiastek równania w podanym przedziale")

    # Wyznaczenie początkowych wartości x_n i x_n1 w zależności od znaku f'(x) i f''(x)
    if f_x_pochodna1.subs(x, wartosc_a) * f_x_pochodna2.subs(x, wartosc_a) > 0:
        x_n, x_n1 = wartosc_a, wartosc_b
    else:
        x_n, x_n1 = wartosc_b, wartosc_a

    # Wyznaczenie początkowych wartości x_n i x_n1 w zależności od znaku f(x) i f''(x)
    if f_x.subs(x, wartosc_a) * f_x_pochodna2.subs(x, wartosc_a) > 0:
        x_n, x_n1 = wartosc_a, wartosc_b
    else:
        x_n, x_n1 = wartosc_b, wartosc_a

    ilosc_iteracji = 1  # Licznik iteracji
    while True:
        f_x_n = f_x.subs(x, x_n)  # Obliczenie wartości funkcji w punkcie x_n
        f_x_n1 = f_x.subs(x, x_n1)  # Obliczenie wartości funkcji w punkcie x_n1

        # Obliczanie następnego przybliżenia pierwiastka metodą siecznych
        x_next = x_n1 - (f_x_n1 * (x_n1 - x_n)) / (f_x_n1 - f_x_n)

        # Sprawdzenie warunku zakończenia iteracji, kiedy wartość funkcji jest bliska zeru z uwzględnieniem błędu
        if abs(x_next - x_n1) < blad:
            break

        x_n = x_n1  # Przygotowanie zmiennej do następnej iteracji
        x_n1 = x_next  # Przygotowanie zmiennej do następnej iteracji
        ilosc_iteracji += 1  # Zwiększenie licznika iteracji

    # Wypisanie wyniku
    print("Ilość iteracji pętli:", str(ilosc_iteracji))
    print("Przybliżone rozwiązanie równania wynosi:", x_n1.evalf())
