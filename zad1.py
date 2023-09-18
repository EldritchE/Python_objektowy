class Zwierze:
    def __init__(self, imie=None, wiek=None, rodzaj=None):
        self.imie=str(imie)
        self.wiek=int(wiek)
        self.rodzaj=str(rodzaj)
z1 = Zwierze('Azor', 5, 'pies')
assert z1.imie=="Azor"
assert z1.wiek==5
assert z1.rodzaj=="pies"
print (z1.imie)

