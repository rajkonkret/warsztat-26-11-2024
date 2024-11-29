class Boat:
    def __init__(self, model, year):
        # __ - pole prywatne
        self.__speed = 0
        self.model = model
        self.year = year

    def sail(self):
        self.__speed += 10
        self.__wynik()

    def speedometer(self):
        print(f"Speed in knots {self.__speed}")

    def __wynik(self):
        print("Wynik testu łodzi OK")


boat = Boat("Maxus", 2024)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# po oznaczeniu jako pole prywatne
# AttributeError: 'Boat' object has no attribute '__speed'
# print(boat.__speed)  # 50
boat.speedometer()  # Speed in knots 50
boat.__speed = 0  # dodaje pole publiczne
boat.speedometer()  # Speed in knots 50
print(boat.__speed)  # 0

# hermetyzacja - zabezpieczanie pol przed dostępem z zewnątrz(poza klasą)
# Enkapsulacja - hermetyzowanie pól i wystawianie dedykowanych metod do odczytu i zmmiany
# Wynik testu łodzi OK
# Wynik testu łodzi OK
# Wynik testu łodzi OK
# Wynik testu łodzi OK
# Wynik testu łodzi OK
# Speed in knots 50
# Speed in knots 50
# 0
