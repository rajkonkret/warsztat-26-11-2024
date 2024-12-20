# lambda - skrócony zapis funkcji
# lambda ma return
# funkcja anonimowa - możliwośc uzycia funkcji w miejscu deklaracji
from functools import reduce, lru_cache


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

r0 = {'miasto': "Kielce"}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}
print(r0['miasto'])
print(r1['miasto'])
# Kielce
# Kielce
print(r1['ZIP'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

print(r0.get('ZIP', "00-000"))  # 00-000
# 25-900
# 00-000
d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(min(lata))  # (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

# reduce()

liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda a, b: a + b, liczby)  # ((((1+2)+3)+4)+5)
"""
   reduce(function, iterable[, initial]) -> value

   Apply a function of two arguments cumulatively to the items of a sequence
   or iterable, from left to right, so as to reduce the iterable to a single
   value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
   ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
   of the iterable in the calculation, and serves as a default when the
   iterable is empty.
"""
print(wynik)  # 15
wynik_mnozenie = reduce(lambda a, b: a * b, liczby)
print("Wnik mnożenia reduce()", wynik_mnozenie)  # Wnik mnożenia reduce() 120


# ((((1*2)*3)*4)*5)

@lru_cache(maxsize=1000)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(10))
print(fib_cached.cache_info())
# CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
print(fib_cached(5))
print(fib_cached.cache_info())
# CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
# hits - ile razy uzyskał wynik nie musząć wykonąć obliczeń
# misses - ile razy wykonywał obliczenia
fib_cached.cache_clear()
print(fib_cached.cache_info())
# CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)
