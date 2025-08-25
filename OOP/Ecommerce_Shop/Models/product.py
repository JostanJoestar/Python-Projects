class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    #Bestand reduzieren
    def reduce_stock(self, quantity: int):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} (Preis: {self.price}€, Lager: {self.stock})"
