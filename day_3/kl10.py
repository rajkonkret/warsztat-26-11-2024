from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increments(self, by=1):
        self.values += by

    @abstractmethod
    def drukuj(self):
        pass

    @staticmethod
    def from_string():
        print('Metoda stayczna')

    @classmethod  # podobna rola jak konstruktor
    def from_counter(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values):
        if values > self.MAX:
            raise ValueError(f"Wartość nie może być większa niż {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje", self.values)


# TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'
class NewCounter(Counter):
    """
    Klasa NewCounter
    """


# musimy nadpisac metode drukuj()
class SecondCouter(Counter):
    """
    Klasa SecoundCounter
    """

    def drukuj(self):
        print('Drukuje SecondCounter', self.values)


# Po dodaniu kalsy abstrakcyjnej nie można utworzyc obiektu tej klasy
# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# c1 = Counter()
# c1.increments()
# c1.drukuj()
# print(c1.values)  # 1

bc = BoundedCounter(10)
bc.increments()
bc.drukuj()  # Drukuje 11

# nie potrzeba tworzyc obiektu klasy
Counter.from_string()  # Metoda stayczna

bd3 = BoundedCounter(bc.values)
bd3.drukuj()  # Drukuje 11

bd4 = BoundedCounter.from_counter(bc)
bc.drukuj()

# nie mozna tworzyc obiektu klasy,
# bo dziedziczy po klasie abstrakcyjnej,
# a nie ma nadpisanej metody abstrakcyjnej
# nc = NewCounter()

sc = SecondCouter(10)
sc.drukuj()  # Drukuje SecondCounter 10

# polimorfizm
# obiekty różnych klas
# dzięki dziedziczeniu ze wspólnej klasy mogą byc w zakresie metody drukuj()
# traktowane jako obiekt tej samej klasy
lista = [bd4, bc, bd3, sc]
for i in lista:
    i.drukuj()

# Drukuje 11
# Drukuje 11
# Drukuje 11
# Drukuje SecondCounter 10
