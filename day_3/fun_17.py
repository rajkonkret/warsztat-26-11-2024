from functools import reduce

transactions = [
    {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def filter_transactions(transactions, transaction_type):
    return list(filter(lambda x: x['type'] == transaction_type, transactions))


def map_transactions(transactions, currency):
    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


def reduce_transactions(transactions):
    return reduce(lambda x, y: x + y, transactions, 0)


def process_transactions(transactions, transaction_type, currency):
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)
    return total


def test_transaction_procesing():
    # assert 400 == 450
    assert map_transactions(filter_transactions(transactions, "income"), "USD") == [1000, 500, 700, 0]
    # assert [1000, 500, 700, 0] == [1000, 500, 700]
    assert reduce_transactions([1000, 500, 700, 0]) == 2200
    assert process_transactions(transactions, "expense", 'EUR') == 400
    # assert process_transactions(transactions, "expense", 'EUR') == 450
    print("All test passed")


# rootdir: C:\Users\CSComarch\PycharmProjects\warsztat-26-11-2024
# collected 1 item
#
# day_3\fun_17.py F                                                                                                                                                                                                      [100%]
#
# ========================================================================================================= FAILURES ==========================================================================================================
# ________________________________________________________________________________________________ test_transaction_procesing _________________________________________________________________________________________________
#
#     def test_transaction_procesing():
#         # assert 400 == 450
#         assert map_transactions(filter_transactions(transactions, "income"), "USD") == [1000, 500, 700, 0]
#         # assert [1000, 500, 700, 0] == [1000, 500, 700]
#         assert reduce_transactions([1000, 500, 700, 0]) == 2200
#         assert process_transactions(transactions, "expense", 'EUR') == 400
# >       assert process_transactions(transactions, "expense", 'EUR') == 450
# E       AssertionError: assert 400 == 450
# E        +  where 400 = process_transactions([{'amount': 1000, 'currency': 'USD', 'id': 1, 'type': 'income'}, {'amount': 200, 'currency': 'USD', 'id': 2, 'type': '...00, 'currency': 'USD', 'id': 5, 'type': 'income'}, {'amount': 400, 'currency': 'EUR', 'id': 6, 'type': 'expense'}, ...], 'expense', 'EUR')
#
# day_3\fun_17.py:39: AssertionError
# ================================================================================================== short test summary info ==================================================================================================
# FAILED day_3/fun_17.py::test_transaction_procesing - AssertionError: assert 400 == 450
# ===================================================================================================== 1 failed in 0.08s =====================================================================================================

# (.venv) PS C:\Users\CSComarch\PycharmProjects\warsztat-26-11-2024> pytest .\day_3\fun_17.py
# ==================================================================================================== test session starts ====================================================================================================
# platform win32 -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
# rootdir: C:\Users\CSComarch\PycharmProjects\warsztat-26-11-2024
# collected 1 item
#
# day_3\fun_17.py .                                                                                                                                                                                                      [100%]
#
# ===================================================================================================== 1 passed in 0.02s =====================================================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\warsztat-26-11-2024>

if __name__ == '__main__':
    filter_transactions(transactions, 'incoming')
    print(filter_transactions(transactions, "income"))
