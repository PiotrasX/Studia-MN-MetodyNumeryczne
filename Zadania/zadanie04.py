from sympy import symbols, diff, sin, pi

# Rozwiązywanie równań nieliniowych — metoda stycznych.
# f(x)   = sin(x) - 1/2 * x       <PI/2, PI>       E = 0.01
# f'(x)  = cos(x) - 1/2
# f''(x) = -sin(x)

# Definicja symboli i funkcji
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
f_x = sin(x) - (1/2) * x  # Definicja funkcji f(x)
f_x_pochodna1 = diff(f_x, x)  # Pierwsza pochodna f(x) względem x
f_x_pochodna2 = diff(f_x_pochodna1, x)  # Druga pochodna f(x) względem x

# Parametry początkowe
blad = 0.01  # Określenie dokładności szukanej wartości
wartosc_a = pi / 2  # Początek przedziału
wartosc_b = pi  # Koniec przedziału

# Sprawdzenie warunku istnienia pierwiastka równania w przedziale
if f_x.subs(x, wartosc_a) * f_x.subs(x, wartosc_b) >= 0:
    print("\nRównanie f(x) nie zawiera pierwiastka równania w podanym przedziale")
else:
    print("\nRównanie f(x) zawiera pierwiastek równania w podanym przedziale")

    # Wyznaczenie początkowej wartości x0 w zależności od znaku f'(x) i f''(x)
    x0 = wartosc_a if f_x_pochodna1.subs(x, wartosc_a) * f_x_pochodna2.subs(x, wartosc_a) > 0 else wartosc_b

    # Wyznaczenie początkowej wartości x0 w zależności od znaku f(x) i f''(x)
    x0 = wartosc_a if f_x.subs(x, wartosc_a) * f_x_pochodna2.subs(x, wartosc_a) > 0 else wartosc_b

    ilosc_iteracji = 1  # Licznik iteracji
    while True:
        f_x_x0 = f_x.subs(x, x0)  # Obliczenie wartości funkcji w punkcie x0
        f_x_pochodna1_x0 = f_x_pochodna1.subs(x, x0)  # Obliczenie wartości pierwszej pochodnej w punkcie x0
        x0_next = x0 - f_x_x0 / f_x_pochodna1_x0  # Aktualizacja x0 przy użyciu metody stycznych (metoda Newtona)

        # Sprawdzenie warunku zakończenia iteracji, kiedy wartość funkcji jest bliska zeru z uwzględnieniem błędu
        if abs(f_x.subs(x, x0_next).evalf()) < blad:
            break

        x0 = x0_next  # Aktualizacja punktu startowego dla kolejnej iteracji
        ilosc_iteracji += 1  # Zwiększenie licznika iteracji

    # Wypisanie wyniku
    print("Ilość iteracji pętli:", str(ilosc_iteracji))
    print("Przybliżone rozwiązanie równania wynosi:", x0_next.evalf())
