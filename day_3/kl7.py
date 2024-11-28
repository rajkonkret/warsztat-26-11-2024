# klasy mixin

class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def scan_document(self):
        print("Skanowannie dokumentu...")
        return "Zawartość dokumentu"


class MultifunctionDevice(Printer, Scanner):
    def photocopy(self):
        content = self.scan_document()
        self.print_message(content)


printer = Printer()
printer.print_message("Komunikat")

scanner = Scanner()
wynik = scanner.scan_document()
print("Wynik scanowania", wynik)
# Drukowanie wiadomości Komunikat
# Skanowannie dokumentu...
# Wynik scanowania Zawartość dokumentu

device = MultifunctionDevice()
device.photocopy()
# Skanowannie dokumentu...
# Drukowanie wiadomości Zawartość dokumentu
