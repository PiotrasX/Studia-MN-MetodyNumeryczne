# Rozwiązywanie równań nieliniowych — metoda bisekcji.
# Metoda jest inaczej zwana metodą połowienia przedziału.

def horner(wspolczynniki, stopien_wielomianu, x):
    wynik = wspolczynniki[0]
    for indeks in range(1, stopien_wielomianu + 1):
        wynik = wynik * x + wspolczynniki[indeks]
    return wynik


def podaj_wartosc(tekst, czy_int, czy_wieksze_1):
    while True:
        x = input(tekst).replace(",", ".")
        try:
            if czy_int:
                x_cyfra = int(x)
            else:
                x_cyfra = float(x)
            if czy_wieksze_1:
                if x_cyfra >= 0:
                    return x_cyfra
                else:
                    print("Wartość musi być równa bądź większa od jeden.")
            else:
                return x_cyfra
        except ValueError:
            if czy_int:
                print("Musisz podać wartość liczbową typu 'int'.")
            else:
                print("Musisz podać wartość liczbową typu 'float'.")


def wypisz_wielomian(ilosc_wspolczynnikow, wspolczynniki_rownania):
    for stopien_rownania in range(ilosc_wspolczynnikow, 0 - 1, -1):
        wartosc = wspolczynniki_rownania[ilosc_wspolczynnikow - stopien_rownania]
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


def oblicz_srodek(a, b):
    return (a + b) / 2


wspolczynniki_dla_rownania = []
ile_wspolczynnikow = podaj_wartosc("\nPodaj stopień wielomianu: ", True, True)
for stopien in range(ile_wspolczynnikow, 0 - 1, -1):
    wspolczynnik = podaj_wartosc("\nPodaj wartość współczynnika dla x^" + str(stopien) + ": ", False, False)
    wspolczynniki_dla_rownania.append(wspolczynnik)
blad_e = 0.01
wartosc_a = podaj_wartosc("\nPodaj dolny przedział dla szukania pierwiastka równania: ", False, False)
wartosc_b = podaj_wartosc("\nPodaj górny przedział dla szukania pierwiastka równania: ", False, False)
while wartosc_b <= wartosc_a:
    print("Wartość dla górnego przedziału musi być większa od wartości dla dolnego przedziału")
    wartosc_b = podaj_wartosc("\nPodaj górny przedział dla szukania pierwiastka równania: ", False, False)

print("Twoje równanie:", end="")
wypisz_wielomian(ile_wspolczynnikow, wspolczynniki_dla_rownania)
print(f"\nWartość a = {wartosc_a}; Wartość b = {wartosc_b}")
wynik_fa_fb = (horner(wspolczynniki_dla_rownania, len(wspolczynniki_dla_rownania) - 1, wartosc_a) *
               horner(wspolczynniki_dla_rownania, len(wspolczynniki_dla_rownania) - 1, wartosc_b))
if wynik_fa_fb < 0:
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
else:
    print("\nPierwiastek równania nie znajduje się w podanym przedziale")
