from datetime import datetime

class Order:
    def __init__(self, order_id: int, customer, items: dict):
        self.order_id = order_id
        self.customer = customer
        self.items = items  # {product: quantity}
        self.created_at = datetime.now()

    def __str__(self):
        order_str = f"Bestellung #{self.order_id} für {self.customer.name} am {self.created_at}\n"
        for product, qty in self.items.items():
            order_str += f" - {product.name} x{qty} = {product.price * qty}€\n"
        return order_str