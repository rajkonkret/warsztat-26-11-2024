# zrobić dekorator, który zamienia wynik dziłania funkcji na duże litery
# funkcja zwraca tekst
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # *args - wiele argumentów pozycyjnych, krotka
        # **kwargs - wszystkie argumenty przekazane po nazwie, słownik
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


# dekorator zmainijący wynik dziłania funkcji (str) na pogrubione litery
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "\033[31m" + result + "\033[0m"

    return wrapper

@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!!!"

@bold_decorator
def greting2(string):
    return f"Podałeś {string}"


print(greeting())  # HELLO WORLD!!!
print("\033[31mHello\033[0m")
print(greting2("Radek"))