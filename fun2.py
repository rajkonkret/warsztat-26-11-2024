# funkcja wewnętrzna, zagnieżdżona
# dekorator - funkcja, która jako argument przyjmuje inną funkcję
# wykorzystuje zasady funkcji wewnętrznej
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    print(fun2)  # <function fun1 at 0x0000025989325C60>
    return fun2  # zwracam adres funkcji


fun1()
print(fun1)  # <function fun1 at 0x000001D51E0C5C60>
fun_wew = fun1()
print(fun_wew)
print(type(fun_wew))
# <function fun1.<locals>.fun2 at 0x000001B3C7DA4AE0>
# <class 'function'>

fun_wew()  # To jest fun2


# zrobic funkcje plik
# funkcja przyjmie parametr zapis, odczyt
# w zaleznosci od parametru zwroci funkcje zapis, odczyt
def plik(arg):
    print("Sprawdzam czy plik istnieje")

    def zapis():
        print("Zapisałem do pliku")

    def odczyt():
        print("Odczytałem z pliku")

    if arg == 'zapis':
        return zapis  # zwrócić adres
    else:
        return odczyt


fh = open('test.txt', 'w')
fh.write("Zapisano\n")
fh.close()

zapis_plik = plik("zapis")  # Sprawdzam czy plik istnieje
zapis_plik()  # Zapisałem do pliku
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()
odczyt_plik = plik("odczyt")

odczyt_plik()
zapis_plik()
odczyt_plik()
# Odczytałem z pliku
# Zapisałem do pliku
# Odczytałem z pliku
