from pprint import pprint


class ContactList(list["Contact"]):
    def search(self, name):
        matching_contact = []
        for c in self:
            if name in c.name:
                matching_contact.append(c)
        return matching_contact


class Contact:
    # all_contact = []  # pustaa lista
    all_contact = ContactList()  # pustaa lista

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

    def __repr__(self):  # __repr__ tez nadpisuje __str__
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    Klasa dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f'{order} zamówiono od {self.name}')


# zrobic klasę Friend z klasy Suplier
# ma miec dodatkowo numer telefonu
class Friend(Suplier):
    """
    Kalsa Friend
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # super() klasa nadrzędna, musimy wywołać
        self.phone = phone

    def __repr__(self):  # __repr__ tez nadpisuje __str__
        return f"{self.name!r} {self.email!r} +48{self.phone!r}"


c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c3.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

s1 = Suplier("Marek", "marek@onet.pl")
print(s1.all_contact)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl]
s1.order("kawa")  # kawa zamówiono od Marek

lista_contact = ContactList()
print(lista_contact.search("radek"))  # []
# Adam admin@wp.pl
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl]
print(c3.all_contact.search("Radek"))  # [Radek radek@wp.pl]

f1 = Friend("Kasia", 'kasia@wp.pl', "789987789")
print(f1)
print(f1.order("herbata"))
print(f1.all_contact)
# Kasia kasia@wp.pl +48789987789
# herbata zamówiono od Kasia
# None
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl, Kasia kasia@wp.pl +48789987789]
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
pprint(s1.all_contact)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@onet.pl,
#  Kasia kasia@wp.pl +48789987789]
# po dodaniu !r w __repr__ dla Friend
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@onet.pl,
#  'Kasia' 'kasia@wp.pl' +48'789987789']
