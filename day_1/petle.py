for i in range(10):  # 0 do 9
    print(i)

for i in range(1, 10, 2):  # od 1 do 9 co drugą start, stop, krok
    print(i)

for i in range(10):
    for j in range(10):
        print(f"{i} + {j} = {i + j}")
# 2 + 6 = 8
# 2 + 7 = 9
# 2 + 8 = 10

# list comprehensions
lista2 = [j for j in range(10)]
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for c in lista2:
    print(c)

# petla while - sterowana warunkiem
licznik = 0
while licznik < 10:
    licznik += 1
    print(licznik)
print(licznik)

lista2.append(55)
lista2.append(55)
lista2.append(55)
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 55, 55, 55]
while 55 in lista2:
    lista2.remove(55)  # usunięcie elementu z listy
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# warunki
logiczna = True
logiczna = "radek"
logiczna = ""
if logiczna:  # bool(logiczna) -> True
    print("prawda")
    print("prawda")
    print("prawda")
else:
    print("falsz")

odp = "Radek"
if odp == "radek":
    print("Radek")
elif odp == "Tomek":
    print("Tomek")
else:
    print("Nie znam Cię")
# falsz
# Nie znam Cię

# od pythona 3.10 match case
odp = input("Podaj imię")  # odczytuje odpowiedź, -> str

match odp.lower().capitalize().strip():
    case "Radek":
        print("Ok")
    case "Tomek":
        print("Też Ok")
    case _:  # odpowiednik else
        print("Nie znam")
# Podaj imięRadek
# Ok
