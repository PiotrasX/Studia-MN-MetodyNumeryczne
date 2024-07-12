# W(x) = a|n * x^n + a|n-1 * x^(n-1) + a|n-2 * x^(n-2) + ... + a|3 * x^3 + a|2 * x^2 + a|1 * x + a|0
# W(x) = ((...((a|n * x + a|n-1) * x + a|n-2) * x + ... + a|2) * x + a|1) * x + a|0

def horner(wspolczynniki, stopien_wielomianu, x):
    wynik = wspolczynniki[0]
    for indeks in range(1, stopien_wielomianu + 1):
        wynik = wynik * x + wspolczynniki[indeks]
    return wynik


def podaj_wartosc(tekst, czy_int, czy_niezerowe):
    while True:
        x = input(tekst).replace(",", ".")
        try:
            if czy_int:
                x_cyfra = int(x)
            else:
                x_cyfra = float(x)
            if czy_niezerowe:
                if x_cyfra >= 0:
                    return x_cyfra
                else:
                    print("Wartość musi być równa bądź większa od zera.")
            else:
                return x_cyfra
        except ValueError:
            if czy_int:
                print("Musisz podać wartość liczbową typu 'int'.")
            else:
                print("Musisz podać wartość liczbową typu 'float'.")


def wypisz_wielomian(ilosc_wspolczynnikow, wspolczynniki_rownanie):
    for stopien_rownania in range(ilosc_wspolczynnikow, 0 - 1, -1):
        wartosc = wspolczynniki_rownanie[ilosc_wspolczynnikow - stopien_rownania]
        if wartosc != 0:
            if wartosc >= 0:
                znak = "+"
            else:
                znak = "-"
            if stopien_rownania == 0:
                print(f" {znak} {abs(wartosc)}", end="")
            elif stopien_rownania == 1:
                print(f" {znak} {abs(wartosc)} * x", end="")
            else:
                print(f" {znak} {abs(wartosc)} * x^{stopien_rownania}", end="")


wspolczynniki_horner = []
ile_wspolczynnikow = podaj_wartosc("\nPodaj stopień wielomianu: ", True, True)
for stopien in range(ile_wspolczynnikow, 0 - 1, -1):
    wspolczynnik = podaj_wartosc("\nPodaj wartość współczynnika dla x^" + str(stopien) + ": ", False, False)
    wspolczynniki_horner.append(wspolczynnik)
wartosc_x = podaj_wartosc("\nPodaj wartość, dla jakiej chcesz obliczyć wartość wielomianu: ", False, False)

print("\nTwoje równanie:", end="")
wypisz_wielomian(ile_wspolczynnikow, wspolczynniki_horner)
wynik_horner = horner(wspolczynniki_horner, len(wspolczynniki_horner) - 1, wartosc_x)
print(f"\nWartość wielomianu dla x = {wartosc_x} wynosi {wynik_horner}")
