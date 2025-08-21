from datetime import datetime
class Aufgabe:
    def __init__(self, titel, datum, beschreibung=""):
        self.titel = titel
        self.datum = datetime.strptime(datum, "%Y-%m-%d").date()
        self.beschreibung = beschreibung
        self.erledigt = False

    def __str__(self):
        status = "✔️" if self.erledigt else "❌"
        return f"{self.titel} | {self.datum} | {self.beschreibung} | {status}"

    def erledigen(self):
        self.erledigt = True