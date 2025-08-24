class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity: int):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    
    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
        
    def total_price(self):
        return sum(p.price * q for p, q in self.items.items())
    
    def __str__(self):
        cart_str = "Warenkorb:\n"
        for product, qty in self.items.items():
            cart_str += f" - {product.name} x{qty} = {product.price * qty}€\n"
        cart_str += f"Gesamt: {self.total_price()}€"
        return cart_str
