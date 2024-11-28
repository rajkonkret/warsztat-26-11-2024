class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


# słownik w którym klucze sa małąlitera
# metoda missing ma byc niezależna od wielkości liter
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        # return self.get(key.lower())
        return self.get(key.casefold())


d_python = {}
# print(d_python['name']) # KeyError: 'name'

d1 = DefaultDict()
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1)  # {}
print(d1['name'])  # default

a1 = AutoKeyDict()
print(a1)
print(a1['name'])
print(a1)
# {}
# name
# {'name': 0}

csd = CaseInsensitiveDict()
csd['name'] = 'Radek'
print(csd['Name'])  # Radek
