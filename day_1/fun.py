# funkcja - fragment kodu, który możemy wywołąć w dowolnym momencie
# funkcja musi byc zadeklarowana zanim zostanie użyta
# wywołanie funkcji uruchamia funkcję

a = 10
b = 90


# zwracające wynik, niezwrcające wyniku
def dodaj():
    print(a + b)


def dodaj2(a, b):  # obowiązkowe argumenty a i b
    print(a + b)


# można zasymulować przeciązanie funkcji liczbą argumentów
def odejmij(a, b, c=0):  # c - argument o wartości domyślnej
    print(a - b - c)


# podpowiedz typów
def mnozenie(a: int, b: int) -> int:
    return a * b  # zwraca wynik


def mnozenie2(a, b):
    return a, b, a * b


# wywołanie funkcji
print(dodaj)  # <function dodaj at 0x0000028204604AE0>
print(type(dodaj))  # <class 'function'>
dodaj()  # uruchomienie funkcji, 100
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty pozycyjne
dodaj2(56, 89)  # 145
odejmij(1, 2)
odejmij(1, 2, 3)

print(mnozenie(5, 6))  # 30
print(dodaj())  # None

print(mnozenie2(5, 6))  # (5, 6, 30)
wynik = mnozenie2(6, 9)
x, y, z = wynik  # rozpakowanie krotki
print(f"Wynik działania {x} * {y} = {z}")  # Wynik działania 6 * 9 = 54

# argumenty po nazwie
odejmij(b=9, a=90, c=87)  # -6
odejmij(b=9, a=90)  # 81

# mieszane
odejmij(1, c=9, b=76)  # -84
# arguemnty pozycyjne przed nazwanymi
# odejmij(c=9, 1, b=9)  # SyntaxError: positional argument follows keyword argument

# print(dodaj() + dodaj2(6,9)) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(mnozenie(89, 89) + mnozenie(6, 9))  # 7975
