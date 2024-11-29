from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal(5.50)

suma = kwota2 + kwota1
print("Suma", suma) # Suma 15.75

precyzja = Decimal('0.00')

podatek =Decimal('0.23')
kwota_z_podatkiem = kwota1 *(1 + podatek)
print(kwota_z_podatkiem)
print(kwota_z_podatkiem.quantize(precyzja))
# Suma 15.75
# 12.6075
# 12.61