# generator  - generuje wartośc w momencie kiedy jej potrzebuje

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zapamięta jaki użył, weźmie następny


kwa = kwadrat2(5)
print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print("Zrób cokolwiek")
print(next(kwa))
# 0
# 1
# 4
# 9
# Zrób cokolwiek
# 16
# print(next(kwa)) # StopIteration - gdy wyczerpie się generator

kwa2 = kwadrat2(10)
kwa3 = kwadrat2(20)

print(next(kwa2))
print(next(kwa3))
print(next(kwa2))
print(next(kwa3))
# 0
# 0
# 1
# 1

print(list(kwa3))
# [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
# print(next(kwa3)) # StopIteration
