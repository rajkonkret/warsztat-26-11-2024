# wyjątki
# błędy podczas wykonywania programu
# należy przechwycic i obsłużyc
try:
    print("12" + 34)
except Exception as e:
    print("Błąd", e)
else:
    print("Wykona się gdy nie ma błędu")
finally:
    print("Wykona się zawsze")

print("program nadal działa")
# Błąd can only concatenate str (not "int") to str
# Błąd can only concatenate str (not "int") to str
# Wykona się zawsze
# program nadal działa
