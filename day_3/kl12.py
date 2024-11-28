class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "kowalski")
print(osoba1.imie, osoba1.nazwisko)  # Jan kowalski

# Anna Nowak
print('Anna Nowak'.split())  # ['Anna', 'Nowak']

a, b = "Anna Nowak".split()
print(a, b)
osoba2 = Osoba(a, b)
print(osoba2.imie, osoba2.nazwisko)  # Anna Nowak

osoba3 = Osoba.z_nazwy_pelnej("Magda Tkacz")
print(osoba3.imie, osoba3.nazwisko)
# Magda Tkacz
