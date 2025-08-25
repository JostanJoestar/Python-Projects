class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders = []

    #Bestellung hinzufügen
    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Kunde: {self.name} ({self.email})"