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
name = 90 # pycharm nas ostrzega, program nadal działa
print(name)
# Tomek
# 90
