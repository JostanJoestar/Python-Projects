class Konto:
    def __init__(self, inhaber, kontostand, pin):
        self.inhaber = inhaber
        self.kontostand = float(kontostand)
        self.pin = pin
        self.versuche = 3
    
    def kontostand_anzeigen(self, pin):
        if self.pin == pin:
            print(self.kontostand)
        else:
            print("Falscher Pin. Noch: " + str(self.versuche - 1) + "  Versuche")
            self.versuche -= 1
    
    def konto_aufladen(self, pin, geld):
        if self.pin == pin:
            self.kontostand += float(geld)
        else:
            print("Falscher Pin. Noch: " + str(self.versuche - 1) + "  Versuche")
            self.versuche -= 1

    def geld_abheben(self, pin, geld):
        if self.pin == pin:
            if self.kontostand - float(geld) > 0:
                self.kontostand -= float(geld)
            else:
                print("Nicht genug Geld auf der Bank")
        else:
            print("Falscher Pin. Noch: " + str(self.versuche - 1) + "  Versuche")
            self.versuche -= 1
        
if __name__ == "__main__":
    konto = None
    while True:
        if konto and konto.versuche <= 0:
            print("Konto gesperrt – zu viele falsche Versuche!")
            break
        print("\n1.Konto anlegen")
        print("2. Kontostand anzeigen")
        print("3. Geld einzahlen")
        print("4. Geld abheben")
        print("5. Abbrechen")

        wahl = input("Wählen Sie eine Option aus:")

        if wahl == "1":
            print("Ich brauche folgende Daten von Ihnen:")
            
            name = input("Ihren Vornamen")
            startkapial = input("Ihr Startkapital")
            pin = input("Ihren Pin")

            konto = Konto(name, startkapial, pin)
            print("Konto erfolgreich geöffnet")
        elif wahl == "2":
            if konto == None:
                print("Bitte legen Sie zuerst ein Konto an")
            else:
                pin = input("Nennen Sie Ihren Pin")
                konto.kontostand_anzeigen(pin)
        elif wahl == "3":
            if konto == None:
                print("Bitte legen Sie zuerst ein Konto an")
            else:
                pin = input("Nennen Sie Ihren Pin")
                geld = input("Wie viel möchten Sie einzahlen")
                konto.konto_aufladen(pin, geld)

        elif wahl == "4":
            if konto == None:
                print("Bitte legen Sie zuerst ein Konto an")
            else:
                pin = input("Nennen Sie Ihren Pin")
                geld = input("Wie viel möchten Sie abheben")
                konto.geld_abheben(pin, geld)
        elif wahl == "5":
            print("Danke und bis zum nächsten Mal!")
            break
        else:
            print("Ungültige Eingabe")