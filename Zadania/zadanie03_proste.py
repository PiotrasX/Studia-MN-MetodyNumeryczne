from sympy import symbols, expand

# Rozwiązywanie równań nieliniowych — metoda bisekcji.
# f(x) = x^3 + x - 1       <0, 1>       E = 0.01


# Funkcja schematu Hornera do obliczania wartości wielomianu w punkcie
def horner(wspolczynniki, stopien_wielomianu, x_var):
    wynik = wspolczynniki[0]
    for indeks in range(1, stopien_wielomianu + 1):
        wynik = wynik * x_var + wspolczynniki[indeks]
    return wynik


# Funkcja do wyznaczania środka przedziału
def oblicz_srodek(a, b):
    return (a + b) / 2


# Zadeklarowanie początkowych wartości
wspolczynniki_dla_rownania = [1, 0, 1, -1]  # Wielomian: x^3 + x - 1
ile_wspolczynnikow = len(wspolczynniki_dla_rownania) - 1  # Stopień wielomianu: 3
blad_e = 0.01  # Błąd
wartosc_a = 0  # Wartość dolnego przedziału
wartosc_b = 1  # Wartość górnego przedziału

# Definicja symbolu 'x'
x = symbols('x')

# Tworzenie wielomianu
wielomian = sum(wspolczynniki_dla_rownania[i] * x**(ile_wspolczynnikow - i) for i in range(ile_wspolczynnikow + 1))

print("Twoje równanie:", expand(wielomian))
print(f"Wartość a = {wartosc_a}; Wartość b = {wartosc_b}")

wynik_fa = horner(wspolczynniki_dla_rownania, ile_wspolczynnikow, wartosc_a)
wynik_fb = horner(wspolczynniki_dla_rownania, ile_wspolczynnikow, wartosc_b)
wynik_fa_fb = wynik_fa * wynik_fb

if wynik_fa_fb > 0:
    print("\nPierwiastek równania nie znajduje się w podanym przedziale")
else:
    print("\nPierwiastek równania znajduje się w podanym przedziale")
    ilosc_iteracji = 1
    while True:
        wartosc_s = oblicz_srodek(wartosc_a, wartosc_b)
        wynik_s = horner(wspolczynniki_dla_rownania, len(wspolczynniki_dla_rownania) - 1, wartosc_s)
        if abs(wynik_s) <= blad_e:
            break
        wynik_fa = horner(wspolczynniki_dla_rownania, len(wspolczynniki_dla_rownania) - 1, wartosc_a)
        wynik_fs = horner(wspolczynniki_dla_rownania, len(wspolczynniki_dla_rownania) - 1, wartosc_s)
        if wynik_fa * wynik_fs < 0:
            wartosc_b = wartosc_s
        else:
            wartosc_a = wartosc_s
        ilosc_iteracji += 1
    print("Ilość iteracji:", ilosc_iteracji)
    print(f"Pierwiastek równania wynosi {wartosc_s}")
