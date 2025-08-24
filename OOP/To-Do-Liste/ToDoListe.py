import csv
from Aufgabe import Aufgabe
from datetime import date, datetime

class ToDoListe:
    def __init__(self, datei="todo.csv"):
        self.datei = datei
        self.aufgaben = []
        self.laden()
    
    def laden(self):
        try:
            with open(self.datei, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    if line:
                        self.aufgaben.append(Aufgabe(line[0],line[1],line[2]))
        except FileNotFoundError:
            pass

    def speichern(self):
        with open(self.datei, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for i in self.aufgaben:
                writer.writerow([i.titel, i.datum, i.beschreibung])

    def hinzufuegen(self, aufgabe):
        self.aufgaben.append(aufgabe)
        self.speichern()
    
    def loeschen(self, titel):
        self.aufgaben = [i for i in self.aufgaben if i.titel != titel]
        self.speichern()

    def anzeigen(self):
        if not self.aufgaben:
            print("Keine Aufgaben vorhanden")
            return

        sortierte_aufgaben = sorted(
            self.aufgaben, 
            key=lambda a: a.datum if a.datum else date.max
        )

        for idx, a in enumerate(sortierte_aufgaben):
            print(f"{idx}: {a}")
        

