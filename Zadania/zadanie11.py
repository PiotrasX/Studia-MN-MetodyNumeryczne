from sympy import symbols, linsolve, Matrix, Eq

# Eliminacja Gaussa.
# Macierz A = [3   0   6]       Wektor b = [-12]
#             [1   2   8]                  [-12]
#             [4   5  -2]                  [ 39]

# Definicja symboli i macierzy rozszerzonej [A|b]
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
y = symbols('y')  # Definiowanie zmiennej symbolicznej 'y'
z = symbols('z')  # Definiowanie zmiennej symbolicznej 'z'
macierz = Matrix([
    [3, 0, 6, -12],
    [1, 2, 8, -12],
    [4, 5, -2, 39]
])  # Macierz z równaniami do rozwiązania
n = 3  # Liczba równań

# Wykonanie metody eliminacji Gaussa
zredukowana_macierz, kolumny = macierz.rref()
# rref() -> Z angielskiego 'reduced row echelon form'. Służy do obliczania schodkowej postaci macierzy.

# Wypisanie zredukowanej macierzy schodkowej
print("Zredukowana macierz schodkowa:")
for wiersz in zredukowana_macierz.tolist():
    print(wiersz)

rownania = []  # Lista do przechowywania równań

# Iteracja przez każdy wiersz zredukowanej macierzy schodkowej
for i in range(n):  # Są 3 równania
    # Pobranie i-tego wiersza z macierzy, z pierwszymi 3 kolumnami (współczynniki przy x, y, z)
    wspolczynniki = Matrix(zredukowana_macierz.row(i)[:3])

    # Pobranie wartości wynikowej (prawą stronę równania) z i-tej czwartej kolumny
    wynik = zredukowana_macierz[i, 3]

    # Tworzenie równania korzystając z iloczynu skalarnego współczynników i zmiennych
    rownanie = Eq(wspolczynniki.dot(Matrix([x, y, z])), wynik)
    # Eq -> Funkcja tworząca równania symboliczne

    # Dodanie równania do listy równań
    rownania.append(rownanie)

# Rozwiązanie układu równań
rozwiazanie = linsolve(rownania, x, y, z)
# linsolve -> Funkcja rozwiązuje układ równań liniowych.

# Wypisanie wyniku
print()
print("Rozwiązanie układu równań:", rozwiazanie)
