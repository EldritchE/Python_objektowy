

"""
POwJP ćwiczenia
Robert, Jaworski, 81591
grupa Grupa: L_I_NW_INFI_W1(2)

L1



"""
# z1


class Zwierze:
    '''Klasa Zwierze'''

    def __init__(self, imie: str, wiek: int, rodzaj: str) -> None:
        """
          # Konstruktor klasy Zwierze
          #
          # Parametry:
          # imie (str): imie zwierzecia
          # wiek (int): wiek zwierzecia
          # rodzaj (str): rodzaj zwierzecia
        """
        self.imie = imie
        self.wiek = wiek
        self.rodzaj = rodzaj


# stworzenie pierwszego zwierzęcia
z1 = Zwierze('Azor', 5, 'pies')
# stworzenie drugiego zwierzęcia
z2 = Zwierze('Misiek', 4, 'Chomik')

# sprawdzenie atrybutów pierwszego zwierzęcia
assert z1.imie == "Azor"
assert z1.wiek == 5
assert z1.rodzaj == "pies"

# wypisanie imienia pierwszego zwierzęcia
print(z1.imie)

# wypisanie atrybutów drugiego zwierzęcia
print(z2.imie, z2.wiek, 'lata', z2.rodzaj + ' takie to zwierze')


"""


"""
# z2


class Colors:
    '''Klasa Colors'''

    __colors_dict = {
        'red': '#e6194b',
        'green': '#3cb44b',
        'yellow': '#ffe119',
        'blue': '#4363d8',
        'orange': '#f58231',
        'purple': '#911eb4',
        'cyan': '#42d4f4',
        'magenta': '#f032e6',
        'lime': '#bfef45',
        'pink': '#fabebe',
        'teal': '#469990',
        'magenta': '#f032e6',
        'lavender': '#e6beff',
        'brown': '#9a6324',
        'beige': '#fffac8',
        'maroon': '#800000',
        'mint': '#aaffc3',
        'olive': '#808000',
        'apricot': '#ffd8b1',
        'navy': '#000075',
        'grey': '#a9a9a9',
        'black': '#000000',
        'white': '#ffffff',
    }
    '''prywatny atrybut klasy __colors_dict zawierający mapowania kolorów'''

    def __init__(self) -> None:
        '''Konstruktor klasy Colors'''
        pass

    def to_hex(self, color: str) -> str:
        """
          # metoda to_hex
          #
          # parametry:
          # color (str): kolor słownie
          #
          # zwraca: wartość hex koloru
          #
          # dzięki uzyciu lower() na parametrze color mozemy znaleźć wartość hex niezaleznie od wielkości liter
        """
        return self.__colors_dict[color.lower()]


c = Colors()
print(c.to_hex('Black'))
assert c.to_hex('Black') == '#000000'
assert c.to_hex('TeaL') == '#469990'
assert c.to_hex('YELLOW') == '#ffe119'

"""

"""
# Z3


# Stworzona klasa Prostokat do której przekazujemy dwie wartości długość i szerokość prostokąta z dwoma metodami
# obliczajacymi pole i obwód prostokąta  : Tworzymy obiekt figura1 o zadanych parametrach wywołanie metod na obiekcie
#  pole i obwód wypisuje obliczone wrtości podająć zadane parametry

class Prostokat:
    '''klasa Prostokąt'''

    def __init__(self, dlugosc: float, szerokosc: float) -> None:
        """
          # Konstruktor klasy prostokąt
          #
          # parametry:
          # dlugosc (float): dlugość prostokąta
          # szerokosc (float): szerokość prostokąta
          #
          # błędy:
          #   długosc musi być liczbą: kiedy długość nie jest liczba zwraca błąd
          #   szerokosc musi być liczbą: kiedy szerokosc nie jest liczba zwraca błąd
        """

        # sprawdzenie czy dlugosc jest liczba
        try:
            dlugosc_liczba = float(dlugosc)
        except:
            raise Exception('dlugosc musi byc liczbą')

        # sprawdzenie czy szerokosc jest liczba
        try:
            szerokosc_liczba = float(szerokosc)
        except:
            raise Exception('szerokosc musi byc liczbą')

        self.a = dlugosc_liczba
        self.b = szerokosc_liczba

    def pole(self) -> float:
        '''funkcja pole zwraca pole prostokąta'''
        print('dlugosc a=', self.a)
        print('szerokosc b=', self.b)
        pole = self.a * self.b
        print('Pole prostokąta', pole)

        return pole

    def obwod(self) -> float:
        '''funkcja obwod zwracajaca obwod prostokąta'''
        print('dlugosc a= ', self.a)
        print('szerokosc b=', self.b)
        obwod = (2 * self.a) + (2 * self.b)
        print('Obwód prostokąta', obwod)

        return obwod


figura1 = Prostokat(5.0, '3')

assert figura1.pole() == 15

assert figura1.obwod() == 16


"""

"""
# Z4


# CiaGeometryczny obsługuje metody print() (drukuje obecną postać ciągu) , rozmiar() (podaje obecną długość ciagu,
# oraz metodę add() dodaje kolejny wyraz ciągu odczytując z listy wyrazy ostatni  i mnoży go przez liczbę q i dodaje
# do listy wyrazy na ostatnie pozycji


class CiagGeometryczny:
    '''klasa CiagGeometryczny'''
    wyrazy = []
    '''przechowywane wyrazy ciągu'''

    def __init__(self, a1: float, q: float, n: int) -> int:
        """
            # konstruktor klasy CiagGeometryczny
            #
            # parametry:
            # a1 (float): pierwszy wyraz ciagu
            # q (float): iloraz
            # n (int): początkowa liczba wyrazów
            #
            # błędy:
            # a1 nie jest liczba: kiedy a1 nie jest liczbą zwraca błąd
            # q nie jest liczba: kiedy q nie jest liczbą zwraca błąd
            # n nie jest liczba całkowitą: kiedy n nie jest liczbą całkowitą zwraca błąd

        """

        # sprawdzenie czy a1 jest liczba
        try:
            a1_liczba = float(a1)
        except:
            raise Exception('a1 nie jest liczba')

        # sprawdzenie czy q jest loczba
        try:
            q_liczba = float(q)
        except:
            raise Exception('q nie jest liczba')

        # sprawdzenie czy n jest liczba całkowitą
        try:
            n_liczba = int(n)
        except:
            raise Exception('n nie jest liczbą całkowitą')

        self.q = q_liczba
        self.n = n_liczba
        self.a1 = a1_liczba
        print('Parametry ciagu : Pierwszy wyraz : ', a1,
              'iloraz ', q, 'poczatkowa ilość wyrazów : ', n)
        self.wyrazy.append(a1_liczba)
        # ilosc wyrazów do policzenia
        ilosc = n_liczba - 1
        # poprzedni wyraz ciagu
        wyraz = a1_liczba
        # obliczanie początkowych n wyrazów
        while ilosc > 0:
            # obliczanie kolejnego wyrazu
            kolejny_wyraz = q * wyraz
            # wkładanie wyrazu do tablicy wyrazów
            self.wyrazy.append(kolejny_wyraz)
            # zmniejszenie ilości wymaganych do utworzenia wyrazów
            ilosc = ilosc - 1
            # zmiana poprzedniego wyrazu
            wyraz = kolejny_wyraz

    def print(self) -> None:
        '''funkcja print wypisuje przechowywane wyrazy ciagu'''
        print('kolejne wyrazy ciągu to : ', self.wyrazy)

    def rozmiar(self) -> int:
        '''funkcja rozmiar zwraca przechowywana dlugosc ciagu'''
        print('Obecna długość ciąu to : ', len(self.wyrazy))

        return len(self.wyrazy)

    def add(self) -> None:
        '''funkcja add dodaje kolejny wyraz ciagu do przechowywania'''
        index_kolejnego_wyrazu = len(self.wyrazy) + 1
        # znalezienie ostatniego wyrazu ciagu
        ostatni_wyraz = self.wyrazy[-1]
        print('ostatni wyraz ma wartosc', ostatni_wyraz)
        # stworzenie kolejnego wyrazu ciągu
        dodany_wyraz = self.q * ostatni_wyraz
        # dodanie kolejnego wyrazu do przechowywanych wyrazów
        self.wyrazy.append(dodany_wyraz)

        print('Dodano kolejny : ', index_kolejnego_wyrazu,
              'wyraz ciągu, czyli :', dodany_wyraz)


ciag = CiagGeometryczny(1, 2, 3)
assert ciag.wyrazy == [1, 2, 4]
ciag.print()
ciag.rozmiar()
ciag.add()
assert ciag.rozmiar() == 4
ciag.print()
ciag.add()
ciag.print()
ciag.add()
ciag.add()
ciag.add()
assert ciag.wyrazy == [1, 2, 4, 8, 16, 32, 64, 128]
assert ciag.rozmiar() == 8
assert ciag.wyrazy[-1] == 128
assert ciag.wyrazy[1] == 2
assert ciag.wyrazy[2] == 4
assert ciag.wyrazy[3] == 8
assert ciag.wyrazy[4] == 16

"""

"""
#z5


from datetime import datetime


class Czas:
    '''klasa Czas'''

    def __init__(self, godzin=None, minut=None) -> None:
        """
            # konstruktor klasy czas
            #
            # parametry:
            # godzin (int): liczba godzin
            # minut (int): liczba minut
        """

        if minut is None and godzin is None:
            # czas systemu
            teraz = datetime.now()
            self.godziny = teraz.hour
            self.minuty = teraz.minute
            return

        # minuty nie podane więc mozliwe ze mamy "12 h 58 min"
        if minut is None:
            a = godzin.split()
            godziny = a[0]
            minuty = a[2]

            try:
                godziny_liczba = int(godziny)
            except:
                raise Exception('godziny muszą być liczbą całkowitą lub w formacie "12 h"')

            try:
                minuty_liczba = int(minuty)
            except:
                raise Exception('minuty muszą być liczbą całkowitą lub w formacie "58 min" ')

            self.minuty = minuty_liczba
            self.godziny = godziny_liczba
            return

        # mamy liczby lub "12 h", "58 min"
        try:
            godziny_liczba = int(godzin)
            self.godziny = godziny_liczba
        except:
            # mamy "12 h"
            g = godzin.split()[0]
            try:
                godziny_liczba = int(g)
                self.godziny = godziny_liczba
            except:
                # niepoprawny argument
                raise Exception('godziny muszą być liczbą całkowitą lub w formacie "12 h"')

        try:
            minuty_liczba = int(minut)
            self.minuty = minuty_liczba
        except:
            # mamy "58 min"
            m = minut.split()[0]
            try:
                minuty_liczba = int(m)
                self.minuty = minuty_liczba
            except:
                # niepoprawny argument
                raise Exception('minuty muszą być liczbą całkowitą lub w formacie "58 min" ')

    def __str__(self):
        return str(self.godziny) + ' h ' + str(self.minuty) + ' min'

    def dodaj(self, inny):
        '''funkcja dodaj dodaje do siebie czasy i zwraca nowy obiekt czas'''
        godziny = self.godziny + inny.godziny
        # wszystkie minuty
        minuty = self.minuty + inny.minuty + godziny * 60

        nowe_godziny = int(minuty / 60)
        # pozostałe minuty
        nowe_minuty = minuty % 60

        return Czas(nowe_godziny, nowe_minuty)

    def __add__(self, inny):
        return self.dodaj(inny)

    def odejmij(self, inny):
        '''funkcja odejmij odejmuje od siebie czasy i zwraca nowy obiekt czas'''
        # wszystkie minuty
        minuty = (self.minuty + self.godziny * 60) - (inny.minuty + inny.godziny * 60)

        nowe_godziny = int(minuty / 60)
        # pozostałe minuty
        nowe_minuty = minuty % 60

        return Czas(nowe_godziny, nowe_minuty)

    def __sub__(self, inny):
        return self.odejmij(inny)

    def pomnoz(self, ile: int):
        '''funkcja pomnoz mnozy czas przez daną wartość'''
        minuty = self.minuty + self.godziny * 60

        pomnozone = minuty * ile

        nowe_godziny = int(pomnozone / 60)
        nowe_minuty = int(pomnozone % 60)

        return Czas(nowe_godziny, nowe_minuty)

    def __mul__(self, ile: int):
        return self.pomnoz(ile)


c1 = Czas('12 h 58 min')
c2 = Czas('12 h', '58 min')
c3 = Czas(12, 58)
c4 = c1.dodaj(c2)
c5 = c1+c2
c6 = Czas()
c7=c1.pomnoz(2)
c8=c2.pomnoz(4)
c9=c2*4

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)