# funkcje stworzy raport
# generator to wygenerowania danych
# przetworzenie danych np.: filtrowanie danych
# pomierzyc czas dla metody generującej raport
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time:.4f} sekundy")

        return result

    return wrapper


def generator_danych(dane):
    for element in dane:
        yield element


def przetworz_dane(dane):
    return [element for element in dane if element % 3 == 0]


@measure_time
def stworz_raport(dane):
    for element in generator_danych(dane):
        print(f"Raport dla systemu {element}")


dane = range(1_000_000)
pr_dane = przetworz_dane(dane)
stworz_raport(pr_dane)
# Czas wykonania funkcji stworz_raport: 0.1291 sekundy
# Raport dla systemu 999993
# Raport dla systemu 999996
# Raport dla systemu 999999

# test Tabnine
print("Koniec programu")
print("Raport został wygenerowany")
for _ in range(1000000):  # _ niema zmienna
    suma = sum(range(1000000))
    if suma == 500000500000:
        break
        print("Zakończono pętlę")
        print("Suma wynosi 500000500000")


def generator_danych_ze_slownika(slownik):
    for key, value in slownik.items():
        yield key, value


slownik = {"Radek": 34, "Tomek": 56, "Zenek": 78, "Agnieszka": None}
