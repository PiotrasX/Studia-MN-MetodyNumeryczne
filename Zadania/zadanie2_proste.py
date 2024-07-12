from sympy import symbols, expand

# W(x) = a|n * x^n + a|n-1 * x^(n-1) + a|n-2 * x^(n-2) + ... + a|3 * x^3 + a|2 * x^2 + a|1 * x + a|0
# W(x) = P(x)(x - x|0) + R


# Funkcja schematu Hornera do dzielenia wielomianu przez dwumian
def horner(wspolczynniki, stopien_wielomianu, war_x):
    wynik = [wspolczynniki[0]]
    for indeks in range(1, stopien_wielomianu + 1):
        wynik.append(wynik[indeks - 1] * war_x + wspolczynniki[indeks])
    return wynik


# Przykładowa sesja dla programu
wspolczynniki_horner = [2, -5, 4, -1]  # Wielomian: 2x^3 - 5x^2 + 4x - 1
ile_wspolczynnikow = len(wspolczynniki_horner) - 1  # Stopień wielomianu: 3
wartosc_x = 1  # Przykładowa wartość x0 -> (x - x0): (x - 1)

# Definicja symbolu 'x'
x = symbols('x')

# Tworzenie i wypisanie wielomianu
wielomian = sum(wspolczynniki_horner[i] * x**(ile_wspolczynnikow - i) for i in range(ile_wspolczynnikow + 1))
print("Początkowy wielomian:", expand(wielomian))

# Obliczenie punktów nowego równania poprzez dzielenia wielomianu metodą Hornera
wynik_horner = horner(wspolczynniki_horner, ile_wspolczynnikow, wartosc_x)

# Tworzenie reszty oraz nowego wielomianu
reszta = wynik_horner.pop()
ile_wspolczynnikow = len(wynik_horner) - 1
nowy_wielomian = sum(wynik_horner[i] * x**(ile_wspolczynnikow - i) for i in range(ile_wspolczynnikow + 1))

# Wypisanie wyniku
print(f"{expand(wielomian)} / (x - {wartosc_x}) = {expand(nowy_wielomian)} + reszta {reszta}")
