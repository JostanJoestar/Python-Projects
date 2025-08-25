import csv
from kontakt import Kontakt

class Adressbuch():
    def __init__(self, datei="adressbuch.csv"):
        self.datei = datei
        self.kontakte = []
        self.laden()
    
    #File laden
    def laden(self):
        try:
            with open(self.datei, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row:
                        self.kontakte.append(Kontakt(row[0], row[1], row[2]))
        except FileNotFoundError:
            pass
    
    #File speichern
    def speichern(self):
        with open(self.datei, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for k in self.kontakte:
                writer.writerow([k.name, k.telefon, k.email])

    #Kontakt hinzufügen
    def hinzufügen(self, kontakt):
        self.kontakte.append(kontakt)
        self.speichern()
    
    #Kontakte anzeigen
    def anzeigen(self):
        if len(self.kontakte) == 0:
            print("Keine Kontakte vorhanden")
        for i in self.kontakte:
            print(i)
    
    #Kontakt löschen
    def löschen(self, name):
        newList = []
        for i in self.kontakte:
            if i.name != name:
                newList.append(i)
        self.kontakte = newList
        self.speichern()

#main Menu
def menu():
    buch = Adressbuch()

    while True:
        print("\n1. Kontakt hinzufügen")
        print("2. Kontakte anzeigen")
        print("3. Kontakt löschen")
        print("4. Beenden")

        wahl = input("Wähle eine Option: ")

        if wahl == "1":
            name = input("Name: ")
            telefon = input("Telefon: ")
            email = input("E-Mail: ")
            buch.hinzufügen(Kontakt(name, telefon, email))
        elif wahl == "2":
            buch.anzeigen()
        elif wahl == "3":
            name = input("Name des zu löschenden Kontakts: ")
            buch.löschen(name)
        elif wahl == "4":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Option!")

if __name__ == "__main__":
    menu()  