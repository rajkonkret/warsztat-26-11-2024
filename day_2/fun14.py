from itertools import zip_longest

generator_1 = [x for x in range(5)]
print(generator_1)
print(type(generator_1))
# [0, 1, 2, 3, 4]
# <class 'list'>

generator_2 = (x for x in range(5))
print(generator_2)
print(type(generator_2))  # To jest generator
# <generator object <genexpr> at 0x00000224DEF9CE80>
# <class 'generator'>

print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


# 0
# 1
# 2

def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


# 1
# 2
# 3

def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


# 1
# 4
# 9
# 16
# 25

def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        i += 1
        if command == "stop":
            break


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
g5.send('Ok')  # Ok
print(next(g5))
try:
    g5.send('stop')  # StopIteration
except Exception as e:
    print("koniec", e)


# None
# 36
# stop
# koniec

def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib1 = fibo()
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))


# 1
# 1
# 2
# 3
# 5
# 8
# 13

def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib2 = fibo_with_index(10)
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2) -> i, n

for i, n in fibo_with_index(10):
    print(f"Pozycja {i}, element {n}")
# Pozycja 0, element 0
# Pozycja 1, element 1
# Pozycja 2, element 1
# Pozycja 3, element 2
# Pozycja 4, element 3
# Pozycja 5, element 5
# Pozycja 6, element 8
# Pozycja 7, element 13
# Pozycja 8, element 21
# Pozycja 9, element 34

# print(list(fib1)) - program zapętli się

person = ["Radek", "Tomek", "Zenek", "Agnieszka"]
wiek = [34, 56, 78]

# zip() łączenie kolekcji
for p, w in zip(person, wiek):
    print(p, w)
# Radek 34
# Tomek 56
# Zenek 78

zipped = zip_longest(person, wiek, fillvalue='Brak danych')
print(zipped)  # <itertools.zip_longest object at 0x000002561CC846D0>
lista = list(zipped)  # wyczerpie dane generatora
for p, w in zipped:
    print(p, w)
# Radek 34
# Tomek 56
# Zenek 78
# Agnieszka Brak danych
print("-----")
for p, w in zipped:
    print(p, w)
# -----
# dane wyczerpane, generator nie zadziała

# dane w liscie są wielokrotnego użytku
for p, w in lista:
    print(p, w)
# -----
# Radek 34
# Tomek 56
# Zenek 78
# Agnieszka Brak danych
