class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y: int) -> float:
    if not isinstance(x, int):
        raise MyTypeError("x must be integer")
    if not isinstance(y, int):
        raise MyTypeError("y must be integer")
    if y == 0:
        raise MyValueError("y cannot be zero")

    return x / y


while True:
    try:
        a = input("Podaj pierwszą liczbę")
        b = input("Podaj drugą liczbę")
        if a == "q" or b == "q":
            break
        result = my_function(int(a), int(b))
    except MyTypeError:
        print("MyTypeError")
    except MyValueError:
        print("MyValueError, dzielenie przez zero")
    except TypeError:
        print("Bład typu")
    except ValueError:
        print("Bład wartości")
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Wynik wynosi {result}")
    finally:
        print("Koniec")
# Podaj pierwszą liczbę4
# Podaj drugą liczbę5
# Wynik wynosi 0.8
# Koniec
# Podaj pierwszą liczbę5
# Podaj drugą liczbę0
# MyValueError, dzielenie przez zero
# Koniec
# Podaj pierwszą liczbęa
# Podaj drugą liczbęf
# Bład wartości
# Koniec
# Podaj pierwszą liczbę
