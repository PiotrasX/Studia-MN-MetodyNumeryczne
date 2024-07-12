from sympy import symbols, expand, linsolve, Matrix

# Aproksymacja wielomianowa.
# Zestaw węzłów P1(0,4), P2(3,5), P3(6,4), P4(9,1), P5(12,2).

# Wzór aproksymacji wielomianowej (metoda najmniejszych kwadratów):
# Przedział <a,b>       Węzły x_1, x_2, ..., x_n       Wzór S_n(x) = E i=1/n | [y_i - y(x_i)]^2
# Gdzie y_i = f(x_i)

# Definicja symboli, zmiennych i węzłów
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
punkty_x = [0, 3, 6, 9, 12]  # Wartości 'x' dla danych węzłów
punkty_y = [4, 5, 4, 1, 2]  # Wartości 'y' dla danych węzłów
stopien = 3  # Stopień wielomianu aproksymującego

# Inicjalizacja list
macierz = []  # Lista (później macierz) równań
wektor = []  # Lista (później wektor) wyników

# Tworzenie macierzy i wektora
for x_i, y_i in zip(punkty_x, punkty_y):  # zip(punkty_x, punkty_y) = [(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)]
    # Tworzenie wiersza macierzy dla każdego punktu x_i
    wiersz = [x_i**k for k in range(stopien + 1)]  # Kolejne potęgi x_i
    macierz.append(wiersz)  # Dodanie wiersza do macierzy
    wektor.append(y_i)  # Dodanie wartości y_i do wektora

# Konwersja list
macierz = Matrix(macierz)  # Obiekt macierzy równań
wektor = Matrix(wektor)  # Obiekt wektora wyników

# Rozwiązanie układu równań metodą najmniejszych kwadratów
wspolczynniki = linsolve((macierz.T * macierz, macierz.T * wektor))
# macierz.T * macierz -> Mnożenie transpozycji macierzy (macierz zawierająca potęgi x_i) przez samą siebie.
# macierz.T * wektor  -> Mnożenie transpozycji macierzy przez wektor (zawiera wartości y_i).
# linsolve            -> Funkcja rozwiązuje układ równań liniowych.

# Wyodrębnienie współczynników
wspolczynniki = list(wspolczynniki.args[0])

# Tworzenie wielomianu aproksymującego
wielomian = sum(c * x**i for i, c in enumerate(wspolczynniki))
# enumerate(wspolczynniki) -> Iteracja przez listę współczynników, zwraca pary (indeks, współczynnik).
# sum(c * x**i for ...)    -> Sumowanie iloczynów każdego współczynnika z odpowiednią potęgą 'x'.

# Wypisanie wyniku
print("Wielomian aproksymujący (m = 3):", expand(wielomian).evalf())
