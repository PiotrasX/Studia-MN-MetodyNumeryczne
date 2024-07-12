from sympy import symbols, diff, cos

# Rozwiązywanie równań nieliniowych — metoda falsi.
# f(x)   = 3 * x - cos(x) - 1       <0.25, 0.75>       E = 0.00001
# f'(x)  = sin(x) + 3
# f''(x) = cos(x)

# Definicja symboli i funkcji
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
f_x = 3 * x - cos(x) - 1  # Definicja funkcji f(x)
f_x_pochodna1 = diff(f_x, x)  # Pierwsza pochodna f(x) względem x
f_x_pochodna2 = diff(f_x_pochodna1, x)  # Druga pochodna f(x) względem x

# Parametry początkowe
blad = 0.00001  # Określenie dokładności szukanej wartości
wartosc_a = 0.25  # Początek przedziału
wartosc_b = 0.75  # Koniec przedziału

# Sprawdzenie warunku istnienia pierwiastka równania w przedziale
if f_x.subs(x, wartosc_a) * f_x.subs(x, wartosc_b) >= 0:
    print("\nRównanie f(x) nie zawiera pierwiastka równania w podanym przedziale")
else:
    print("\nRównanie f(x) zawiera pierwiastek równania w podanym przedziale")

    # Wyznaczenie początkowych wartości 'a' i 'b' w zależności od znaku f'(x) i f''(x)
    if f_x_pochodna1.subs(x, wartosc_a) * f_x_pochodna2.subs(x, wartosc_a) > 0:
        a, b = wartosc_a, wartosc_b
    else:
        a, b = wartosc_b, wartosc_a

    # Wyznaczenie początkowych wartości 'a' i 'b' w zależności od znaku f(x) i f''(x)
    if f_x.subs(x, wartosc_a) * f_x_pochodna2.subs(x, wartosc_a) > 0:
        a, b = wartosc_a, wartosc_b
    else:
        a, b = wartosc_b, wartosc_a

    ilosc_iteracji = 1  # Licznik iteracji
    while True:
        f_a = f_x.subs(x, a)  # Obliczenie wartości funkcji w punkcie 'a'
        f_b = f_x.subs(x, b)  # Obliczenie wartości funkcji w punkcie 'b'
        x_n = a - ((b - a) * f_a) / (f_b - f_a)  # Obliczenie kolejnego przybliżenia korzystając z reguły falsi

        # Sprawdzenie warunku zakończenia iteracji, kiedy wartość funkcji jest bliska zeru z uwzględnieniem błędu
        if abs(f_x.subs(x, x_n).evalf()) < blad:
            break

        ilosc_iteracji += 1  # Zwiększenie licznika iteracji

        # Aktualizacja wartości 'a' lub 'b' w zależności od znaku funkcji w punkcie x_n
        if f_x.subs(x, a) * f_x.subs(x, x_n) < 0:
            b = x_n  # Aktualizacja 'b', jeśli pierwiastek jest między 'a' a 'x_n', teraz przedział wynosi <a, x_n>
        else:
            a = x_n  # Aktualizacja 'a', jeśli pierwiastek jest między 'x_n' a 'b', teraz przedział wynosi <x_n, b>

    # Wypisanie wyniku
    print("Ilość iteracji pętli:", str(ilosc_iteracji))
    print("Przybliżone rozwiązanie równania wynosi:", x_n.evalf())
