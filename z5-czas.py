from datetime import datetime

class Czas:
    '''klasa Czas'''

    def __init__(self, godzin = None, minut = None) -> None:
        """
            konstruktor klasy czas

            parametry:
            godzin (int): liczba godzin
            minut (int): liczba minut
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
c4 = Czas(12, '58 min')
c5 = Czas()
print(c5)
print(c1 - c2)
print(c1 + c2)
print(c1 * 2)