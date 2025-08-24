from ToDoListe import ToDoListe
from Aufgabe import Aufgabe

def menu():
    liste = ToDoListe()

    while True:
        print("\n--- ToDo-Liste Menü ---")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe löschen")
        print("4. Aufgabe erledigen")
        print("5. Beenden")

        wahl = input("Wähle eine Option: ")

        if wahl == "1":
            titel = input("Titel: ")
            datum = input("Fälligkeitsdatum (YYYY-MM-DD): ")
            if datum.strip() == "":
                datum = None
            beschreibung = input("Beschreibung (optional): ")
            liste.hinzufuegen(Aufgabe(titel, datum, beschreibung))
        elif wahl == "2":
            liste.anzeigen()
        elif wahl == "3":
            titel = input("Titel des zu löschenden Elements eingeben: ")
            liste.loeschen(titel)
        elif wahl == "4":
            liste.anzeigen()
            index = int(input("Index der zu erledigenden Aufgabe: "))
            if 0 <= index < len(liste.aufgaben):
                liste.aufgaben[index].erledigen()
                liste.speichern()
            else:
                print("Ungültiger Index")
        elif wahl == "5":
            break
        else:
            print("Ungültige Eingabe")

if __name__ == "__main__":
    menu()