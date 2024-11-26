# kolekcja
# lista, krotka (tuple), zbiór (set), słownik

# lista - dowolna ilośc danych, różnego typu na raz
# zachowuje kolejnośc przy dodawaniu elementów

lista = []
lista = list()
print(lista)  # []
print(type(lista))  # <class 'list'>
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Ania")
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Ania']
lista2 = lista  # kopia referencji, kopia adresu listy
print(lista2)
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Ania']
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Ania']
lista_copy = lista.copy()
lista.clear()
print(lista2)  # []
print(lista)  # []
print(lista_copy)  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Ania']
print(id(lista))
print(id(lista2))
print(id(lista_copy))
# 2047516868544
# 2047516868544
# 2047513467072

# krotka, tuple - niemutowalna kolekcja, tylko do odczytu
# krotka pozwala lepiej zarządzac pamięcią
krotka = tuple(lista_copy)  # tuple() - rzutowanie na krotke
print(krotka)  # ('Radek', 'Tomek', 'Zenek', 'Marek', 'Ania')
print(type(krotka))

krotka_liczby = 6, 7, 8, 9, 200
print(type(krotka_liczby))  # <class 'tuple'>
print(krotka_liczby)  # (6, 7, 8, 9, 200)

krotka_jeden = "Radek",
print(type(krotka_jeden))  # <class 'tuple'>
print(krotka_jeden)  # ('Radek',)
# PEP8 zaleca aby krotka jednoelementowała była tworzona z nawiasami
krotka_jeden = ("Radek",)
print(type(krotka_jeden))

print(krotka_liczby.count(9))  # wystepuje 1 raz
print(krotka_liczby.index(9))  # indeks numer 3

# nie można zmieniac
# krotka_liczby[0] = 7# TypeError: 'tuple' object does not support item assignment
del krotka_jeden  # usunięcie calej krotki
# print(krotka_jeden) #
# # NameError: name 'krotka_jeden' is not defined
# garabage collector - automatyczne usunięcie zbędnych danych z pamięci

# rozpakowanie krotki
a, b = 1, 2
a, *b = krotka_liczby  # * worek na pozostałe dane
print(f"{a=}, {b=}")  # a=6, b=[7, 8, 9, 200]

# zbiór (set) - przechowuje unikalne wartości
# nie posiada indeksu, nie zachowuje kolejności przy dodawaniu elementów
lista = [44, 55, 66, 77, 33, 31, 33, 55, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 11, 44, 77, 55, 31}
zbior.add(18)
zbior.add(18)
zbior.add(23)
zbior.add(55)
zbior.add(76)
print(zbior)  # {33, 66, 11, 44, 77, 76, 18, 23, 55, 31}

zbior2 = {66, 11, 44, 55, 66, 999, 999, 62}
print(zbior2)

# suma zbiorów
print(zbior | zbior2)  # {33, 66, 999, 11, 44, 77, 76, 18, 23, 55, 62, 31}
print(zbior.union(zbior2))  # {33, 66, 999, 11, 44, 77, 76, 18, 23, 55, 62, 31}

lista = list(zbior)
print(lista)  # [33, 66, 11, 44, 77, 76, 18, 23, 55, 31]

pusty_zbior = set()
print(pusty_zbior)  # set()

# frozenset() - niemutowalny set
immutable_set = frozenset([1, 2, 3, 4])
print(immutable_set)  # frozenset({1, 2, 3, 4})

nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_set)  # {frozenset({3, 4}), frozenset({1, 2})}

# słownik
# para klucz-wartosc
# {"name":"Radek",'age':89}
# odwzorowanie jsona w pythonie
# klucze nie mogą sie powtórzyć

slownik = dict()
print(slownik)  # {} - pusty słownik
slownik = {}
print(slownik)  # {}
print(type(slownik))  # <class 'dict'>

slownik['name'] = "Radek"
slownik['age'] = 90
print(slownik)  # {'name': 'Radek', 'age': 90}

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['name', 'age'])
# dict_values(['Radek', 90])
# dict_items([('name', 'Radek'), ('age', 90)])

print(slownik['name'])
# print(slownik['namE']) # KeyError: 'namE'


print(slownik.get("Name"))  # None, nie ma takiego klucza
print(slownik.get("NAme", 'default'))  # default

lista_duplikaty = [33, 66, 11, 44, 77, 45, 18, 54, 31, 55]
print(dict.fromkeys(lista_duplikaty))
# {33: None, 66: None, 11: None, 44: None, 77: None, 45: None, 18: None, 54: None, 31: None, 55: None}
print(list(dict.fromkeys(lista_duplikaty)))
# [33, 66, 11, 44, 77, 45, 18, 54, 31, 55] usuniete duplikaty, zachowana kolejność
