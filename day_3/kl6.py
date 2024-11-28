# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z kalsy A")


class B:
    def method(self):
        print("Metoda z kalsy B")


class C(B, A):
    """
    klasa dziedziczy po A i B
    """


a = A()
a.method()  # Metoda z kalsy A

b = B()
b.method()  # Metoda z kalsy B

c = C()
c.method()  # Metoda z kalsy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Kalsa dziedziczy po A,B
    """


d = D()
d.method()  # Metoda z kalsy A


class E(A, B):
    def method(self):
        print("Metoda  z klasy E")


e = E()
e.method()  # Metoda  z klasy E


class F(A, B):
    def method(self):
        B.method(self)  # jawne wywołanie metody z klasy B


f = F()
f.method()  # Metoda z kalsy B


class G(A, B):
    def method(self):
        super().method()  # super() - klasa nadrzędna, tutaj A
        print("Dopisane")


g = G()
g.method()
# Metoda z kalsy A
# Dopisane
