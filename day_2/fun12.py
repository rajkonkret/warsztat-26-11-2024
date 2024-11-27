# napisać funkcję, która przyjmuje argumenty age, first, last
# age powinien miec ustawioną wartość domyślną
# zbudować słownik z podanych argumentó
# argumenty nalezy pobierac w petli while
# zastosowac "sposób ucieczki"
def build_dict(first, last, age=None):
    person = {"first": first, "last": last}
    if age:
        person['age'] = age

    return person


while True:
    print("Podaj imię i nazwisko")
    print("Wpisz q by wyjść")

    f_name = input("Podaj imię")
    if f_name == 'q':
        break

    l_name = input("Podaj nazwisko")
    if l_name == 'q':
        break

    age = input("Podaj wiek")
    if age == 'q':
        break

    print(build_dict(f_name, l_name, age))

# Podaj imięRadek
# Podaj nazwiskokowalski
# Podaj wiek
# {'first': 'Radek', 'last': 'kowalski'}
# Podaj imię i nazwisko
# Wpisz q by wyjść
# Podaj imięTomek
# Podaj nazwiskoWisnia
# Podaj wiek67
# {'first': 'Tomek', 'last': 'Wisnia', 'age': '67'}
# Podaj imię i nazwisko
# Wpisz q by wyjść
# Podaj imię i nazwisko
# Wpisz q by wyjść
# Podaj imięq