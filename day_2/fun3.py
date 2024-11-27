# lambda - skrócony zapis funkcji
# lambda ma return
# funkcja anonimowa - możliwośc uzycia funkcji w miejscu deklaracji

def liczymy(x, y):
    return x * y


print(liczymy(5, 9))  # 45

liczmy2 = lambda x, y: x * y
print(liczmy2(5, 9))  # 45

# mapowanie danych
lista = [1, 2, 5, 56, 78, 90, 100, 200]
lista_wyn = []
for i in lista:
    lista_wyn.append(i ** 2)

print(lista_wyn)

# list comprehensions
print([i ** 2 for i in lista])  # [1, 4, 25, 3136, 6084, 8100, 10000, 40000]


def zmien(x):
    return x ** 2


lista_wyn_2 = []
for i in lista:
    lista_wyn_2.append(zmien(i))

print(lista_wyn_2)  # [1, 4, 25, 3136, 6084, 8100, 10000, 40000]

# funkcje wyższego rzędu
# map(), filter(), reduce(), lru_cache()

print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000]

# zastosowanie lambdy jako funkcja anonimowa
print(f"Zastosowanie map() {list(map(lambda x: x ** 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x / 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x + 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 1.50, lista))}")
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000]
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000]
# Zastosowanie map() [0.5, 1.0, 2.5, 28.0, 39.0, 45.0, 50.0, 100.0]
# Zastosowanie map() [4, 8, 20, 224, 312, 360, 400, 800]
# Zastosowanie map() [3, 4, 7, 58, 80, 92, 102, 202]
# Zastosowanie map() [1.5, 3.0, 7.5, 84.0, 117.0, 135.0, 150.0, 300.0]

# filter() - filtruje dane, zwraca spełniające warunek

for i in lista:
    if i < 10:
        print(i)

print(f'Uzycie filter() {list(filter(lambda x: x < 5, lista))}')
print(f'Uzycie filter() {list(filter(lambda x: x < 10, lista))}')
print(f'Uzycie filter() {list(filter(lambda x: x < 25, lista))}')
print(f'Uzycie filter() {list(filter(lambda x: x > 50, lista))}')
print(f'Uzycie filter() {list(filter(lambda x: x > 5 and x < 300, lista))}')
print(f'Uzycie filter() {list(filter(lambda x: 5 < x < 300, lista))}')
# Uzycie filter() [1, 2]
# Uzycie filter() [1, 2, 5]
# Uzycie filter() [1, 2, 5]
# Uzycie filter() [56, 78, 90, 100, 200]
# Uzycie filter() [56, 78, 90, 100, 200]
# Uzycie filter() [56, 78, 90, 100, 200]