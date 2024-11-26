import sys

print("Nazywam się Radek")
print('Nazywam się Radek')
print(type("Radek"))  # <class 'str'>, string, tekstowe

print(39)
print(type(39))  # <class 'int'>, liczby całkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
# ctrl / - komentarz
print("93")
print(type("93"))  # <class 'str'>

print("93" + "93")  # konkatenacja, 9393, łączenie znaków
print(93 + 93)  # 186
print(5 * "93")  # 9393939393
print(5 * 93)  # 465
# alt shift e - uruchomienie fragmentu kodu

# silne typowanie - nie zamienia typów sam
# print("93" + 45) # TypeError: can only concatenate str (not "int") to str

# rzutownie
print(int("93") + 45)  # int() - rzutowanie, zamiana na int, 138
print("93" + str(39))  # str() - rzutowanie na str, 9339

# zmienna - pudełko na dane, przechowuje jedną wartość
# PEP8 - mała litera
# snake_case
# nazwa powinna podpowiadać co przechowuje

# typowanie dynamiczne
# można w każdej chwili wrzucić inny typ danych do zmiennej
name = "Radek"
print(name)
print(type(name))  # <class 'str'>
name = 90
print(name)
print(type(name))

# tylko podpowiedz typu dla programisty  i pycharm
name: str = "Tomek"
print(name)
name = 90  # pycharm nas ostrzega, program nadal działa
print(name)  #
# Tomek
# 90

wiek = 47  # int
rok = 2024  # int
temp = 36.6
print(type(temp))  # <class 'float'>
print(temp)  # 36.6

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=35,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)


print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# float - bład zaokrąglenia
# decimal - pozwala ominąc problem błedu zaokrąglenia

print(wiek + rok)  # 2069
print(wiek - rok)  # -1979
print(wiek * rok)  # 91080
print(wiek / rok)  # 0.022233201581027668

print(rok // wiek)  # częśc całkowita z dzielenia, 43 całe
print(rok % wiek)  # reszta z dzielenia, modulo, reszty 3
print(10 % 3)  # 3 całe reszty 1

print(wiek ** rok)  # potęgowanie
print(len(str(wiek ** rok)))  # długość 3385
# print(len(str(wiek ** rok ** 2)))  #
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 / 2 + 4 / 2)  # -51.5
print(54 - 5 * 43 / (2 + 4) / 2)  # -36.08333333333333

wersja = 3.90001
# f - string - string sformatowany
print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.90001
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4 zaokrąglił
print("Wersja", wersja)  # Wersja 3.90001

wersja_zaokraglona = round(wersja)
print("Zaokrąglone", wersja_zaokraglona)  # Zaokrąglone 4
#     sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
print("Zaokrąglone", wersja_zaokraglona, sep="")  # Zaokrąglone4
print(f"{wersja:^25}")  # "         3.90001         "
print(f"{wersja:<10}")  # "3.90001   "
print(f"{wersja:>20}")  # "             3.90001"

# tutaj sprawdza typy
print("Używamy %f" % wersja)  # Używamy 3.900010
print("Używamy %s" % wersja)  # %s - string,  Używamy 3.90001
print("Używamy %s" % wersja)  # %s - string,  Używamy 3.90001
# print("Używamy %d" % "Radek")  # %d - liczba,  TypeError: %d format: a real number is required, not str

print("Używamy wersji {}".format(wersja))  # Używamy wersji 3.90001

print("""Tekst
    wielolinjikowy
        {wersja}""")
# "Tekst
#     wielolinjikowy
#         {wersja}"
print(f"""Tekst
    wielolinjikowy
        {wersja}""")
# "Tekst
#     wielolinjikowy
#         3.90001"

# teksty są niemutowalne
imie = "Radek Radek"
imie.upper()
""" Return a copy of the string converted to uppercase. """
print(imie)  # Radek Radek
print(imie.upper())
tekst_upper = imie.upper()
print(tekst_upper)
# Radek Radek
# RADEK RADEK
# RADEK RADEK

liczba = 890789765432
print(liczba)
print(f"Nasza duża liczba {liczba:,}")
print(f"Nasza duża liczba {liczba:_}")
# Nasza duża liczba 890,789,765,432
# Nasza duża liczba 890_789_765_432

print(f"NAsza duża liczba {liczba:_}".replace("_", "."))  # NAsza duża liczba 890.789.765.432

liczba2 = 15000000000
liczba2 = 15_000_000_000
print(liczba2)
print(type(liczba2))
# 15000000000
# <class 'int'>

# typ logiczny
# prawda, fałsz
# True, False

print(int(True))  # 1
print(int(False))  # 0

# bool() rzutowanie na typ logiczny, boolean
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True

print(bool(""))  # False
print(bool(None))  # False None - nic, stan nieokreslony, nie wiem -> odpowiednik nulla w innych językach

tekst = "   Tekst   "
# usunie białe znaki i spacje
print(tekst.strip())  # "Tekst" z przodu i z tyłu
print(tekst.rstrip())  # "   Tekst" z prawej strony
print(tekst.lstrip())  # "Tekst   " z lewej strony

a = 10
print(f"Zmienna a = {a}")  # Zmienna a = 10
print(f"Zmienna {a = }")  # Zmienna a = 10

text_x = "Witaj Świecie"
print(text_x.lower())  # witaj świecie
print(text_x.upper())  # WITAJ ŚWIECIE
print(text_x.capitalize())  # Witaj świecie
print(text_x.casefold())  # witaj świecie
""" Return a version of the string suitable for caseless comparisons. """
# ẞ - ss
name1 = "groẞ"
name2 = "GROSS"

print(name1.lower() == name2.lower())  # == porównanie, False
print(name1.casefold() == name2.casefold())  # == porównanie, True

encode_s = text_x.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'> typ bajtowy
# \x zapis liczby w sytemie szesnastkowym

print(encode_s.decode('utf-8'))  # Witaj Świecie
