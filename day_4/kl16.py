from functools import total_ordering


class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(5)
num2 = MyNumber(15)


# print(num1 + num2) # TypeError: unsupported operand type(s) for +: 'MyNumber' and 'MyNumber'

@total_ordering
class MyDecimal:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


n1 = MyDecimal(5)
n2 = MyDecimal(15)
print(n1 < n2)  # True
print(n1 > n2)
print(n1 != n2)
# True
# False
# True
