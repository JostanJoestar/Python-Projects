class Kontakt():
    def __init__(self, name, telefon, email):
        self.name = name
        self.telefon = telefon
        self.email = email
    
    def __str__(self):
        return f"{self.name} | {self.telefon} | {self.email}"
