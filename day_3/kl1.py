# klasy - szablon, przepis, matryca
# obiekt - instancja klasy - element zbudowany wg przepisu
# ma cechy i funkcje zadane klasą
# hermetyzacja, polimorfizm, dziedziczenie, abstrakcja

import math


class MyFirstClass:
    """
    Klasa w Pythonie opisująca punkty w przestrzeni x, y
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """

        # self - obiekt ktory wykona to
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        Metoda przemieszcza obiekt w punkt x, y
        :param x:
        :param y:
        :return:
        """
        self.x = x  # np.: ob.x
        self.y = y

    # metoda reset()
    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        Obliczenie odległości  między dwoma punktami w przestrzeni euklidesowej
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):  # opis obiektu
        return f"{self.x, self.y}"

    def __repr__(self):  # reprezentacja obiektu
        return f"Point({self.x, self.y})"


print(MyFirstClass.__doc__)
#     Klasa w Pythonie opisująca punkty w przestrzeni x, y
ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x000001F398017530>
# pydoc -b - serwer z dokumentacją
# pydoc -w .\day_3\kl1.py plik html z dokumentacją
# python -m pydoc -b
# po dodaniu __str__ obiekt wyswietla sie tak: (0, 0)
print(ob.x)
print(ob.y)
print(ob)
# 0
# 0
# (0, 0)
ob.move(45, 89)
print(ob)  # (45, 89)
ob2 = MyFirstClass(120, 678)
print(ob2)
# (45, 89)
# (120, 678)
ob.reset()
print(ob)
# (0, 0)

print(ob.calculate(ob2))
# 688.5375806737059
# print(ob.calculate(200)) # Pycharm sugeruje błedny typ

lista = [ob, ob2]
print(ob)  # (0, 0)
print(lista)
# [<__main__.MyFirstClass object at 0x0000022A11B7A360>, <__main__.MyFirstClass object at 0x0000022A11B7AE70>]
print(ob)
print(str(ob))
# (0, 0)
# (0, 0)
# po nadpisaniu __repr__
# [Point((0, 0)), Point((120, 678))]
for p in lista:
    print(p)  # __str__
    # (0, 0)
    # (120, 678)
