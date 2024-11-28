class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


print(Matematyka.dodaj(5, 6))  # 11


class KalkulatorTemperatur:

    @staticmethod
    def celcius_farenheit(celcius):
        return celcius * 9 / 5 + 32

    @staticmethod
    def farenheit_celcius(farenheit):
        return (farenheit - 32) * 5 / 9


print(KalkulatorTemperatur.farenheit_celcius(100))
print(KalkulatorTemperatur.celcius_farenheit(36.6))
# 37.77777777777778
# 97.88000000000001
