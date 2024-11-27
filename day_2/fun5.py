# pobrać wszystkie wartości ze słownika i zliczyc je
def sum_nested(data):
    total = 0
    if isinstance(data, dict):
        for key, value in data.items():
            total += sum_nested(value)
    elif isinstance(data, list):
        for item in data:
            total += sum_nested(item)
    elif isinstance(data, (int, float)):
        total += data  # total = total + data

    return total


nested_data = {
    "a": 1,
    "b": {
        "c": 2,
        "d": [3, 4, {"e": 5}]
    },
    "f": [6, 7]
}

result = sum_nested(nested_data)
print("Sum is:", result)  # Sum is: 28
