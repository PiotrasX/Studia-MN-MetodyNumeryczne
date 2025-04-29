from sympy import symbols, expand

# Interpolacja wielomianem Lagrange'a.
# Zestaw węzłów P1(1,5), P2(2,7), P3(3,6).

# Wzór interpolacyjny Lagrange'a:
# Przedział <a,b>       Węzły x_0, x_1, ..., x_n       Wzór L_n(x) = E k=0/n | lambda_k(x) * y_k
# Gdzie y_k = f(x_k)
#       lambda_k(x) = TT i=0,i!=k/n | (x - x_i)/(x_k - x_i), k = 0, 1, ..., n

# Definicja symboli i węzłów
x = symbols('x')  # Definiowanie zmiennej symbolicznej 'x'
wezly = [(1, 5), (2, 7), (3, 6)]  # Definiowanie węzłów
n = len(wezly)  # Liczba węzłów


# Funkcja do obliczania bazowych wielomianów Lagrange'a dla danego indeksu
def bazowy_wielomian_lagrangea(k):
    x_k = wezly[k][0]  # k-ty węzeł
    # Lista czynników wielomianu bazowego, pomijając k-ty węzeł
    czynniki = [(x - wezly[i][0]) / (x_k - wezly[i][0]) for i in range(n) if i != k]
    wielomian_bazowy = 1  # Wielomian bazowy
    for czynnik in czynniki:
        wielomian_bazowy *= czynnik  # Ręczne mnożenie czynników wielomianu bazowego
    return wielomian_bazowy  # Iloczyn czynników wielomianu bazowego


# Sumowanie iloczynów wartości y_k oraz odpowiednich wielomianów bazowych
wielomian_lagrangea = sum(wezly[k][1] * bazowy_wielomian_lagrangea(k) for k in range(n))

# Wypisanie wyniku
print("Wielomian interpolacyjny Lagrange'a:", expand(wielomian_lagrangea).evalf())
