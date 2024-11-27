# dekorator - funkcja, które jako argument przyjmuje funkcje
# dodaje, modyfikuje jej działanie
# wykorzystuje mechanizm funkcji wewnętrznej
def dekor(func):
    def wew():
        print("Dekorator. Dodatkowy napis")
        return func()

    return wew  # adres funkcji wew

@dekor
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorować")


nasza_funkcja()
# działa bez dekoratora
# Funkcja, którą chcemy udekorować

# po dodaniu dekorator @dekor
# Dekorator. Dodatkowy napis
# Funkcja, którą chcemy udekorować
