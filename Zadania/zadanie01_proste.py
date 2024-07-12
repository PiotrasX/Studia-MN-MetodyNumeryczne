from sympy import symbols, expand

# W(x) = a|n * x^n + a|n-1 * x^(n-1) + a|n-2 * x^(n-2) + ... + a|3 * x^3 + a|2 * x^2 + a|1 * x + a|0
# W(x) = ((...((a|n * x + a|n-1) * x + a|n-2) * x + ... + a|2) * x + a|1) * x + a|0


# Funkcja schematu Hornera do obliczania wartości wielomianu w punkcie
def horner(wspolczynniki, stopien_wielomianu, war_x):
    wynik = wspolczynniki[0]
    for indeks in range(1, stopien_wielomianu + 1):
        wynik = wynik * war_x + wspolczynniki[indeks]
    return wynik


# Przykładowa sesja dla programu
wspolczynniki_horner = [1, -2, 3, -4]  # Wielomian: x^3 - 2x^2 + 3x - 4
ile_wspolczynnikow = len(wspolczynniki_horner) - 1  # Stopień wielomianu: 3
wartosc_x = 3  # Przykładowa wartość x: 2

# Definicja symbolu 'x'
x = symbols('x')

# Tworzenie i wypisanie wielomianu
wielomian = sum(wspolczynniki_horner[i] * x**(ile_wspolczynnikow - i) for i in range(ile_wspolczynnikow + 1))
print("Twoje równanie:", expand(wielomian))

# Obliczenie wartości wielomianu metodą Hornera
wynik_horner = horner(wspolczynniki_horner, ile_wspolczynnikow, wartosc_x)

# Wypisanie wyniku
print(f"Wartość wielomianu dla x = {wartosc_x} wynosi: {wynik_horner}")
