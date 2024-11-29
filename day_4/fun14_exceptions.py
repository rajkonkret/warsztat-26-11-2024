class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą"))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")
except MyException as e:
    print("Wartoość musi być większa od zera", e)
except Exception as e:
    print("Błąd", e)
else:
    print("Podana wartość prawidłowa", x)
finally:
    print("Koniec")
