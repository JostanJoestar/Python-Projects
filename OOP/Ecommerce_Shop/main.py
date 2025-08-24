from Models.product import Product
from Models.customer import Customer
from Models.cart import Cart
from Models.order import Order

def show_menu():
    print("\n=== E-Commerce Shop ===")
    print("1. Produkte anzeigen")
    print("2. Kunde anlegen")
    print("3. Warenkorb anzeigen")
    print("4. Produkt zum Warenkorb hinzufügen")
    print("5. Bestellung abschließen")
    print("6. Bestellungen anzeigen")
    print("0. Beenden")

def main():
    # --- Beispiel-Daten ---
    products = [
        Product(1, "Laptop", 1200.0, 5),
        Product(2, "Maus", 25.0, 10),
        Product(3, "Tastatur", 45.0, 7)
    ]
    customers = []
    orders = []

    # --- Startkunde ---
    customer = Customer(1, "Max Mustermann", "max@example.com")
    customers.append(customer)

    # --- Warenkorb ---
    cart = Cart()

    # --- Menü-Schleife ---
    while True:
        show_menu()
        choice = input("Bitte Option wählen: ")

        if choice == "1":
            print("\n--- Produktliste ---")
            for p in products:
                print(f"[{p.product_id}] {p}")

        elif choice == "2":
            name = input("Name des Kunden: ")
            email = input("E-Mail: ")
            new_id = len(customers) + 1
            new_customer = Customer(new_id, name, email)
            customers.append(new_customer)
            customer = new_customer
            print(f"Kunde {name} wurde angelegt und ist nun aktiv.")

        elif choice == "3":
            print(cart)

        elif choice == "4":
            try:
                product_id = int(input("Produkt-ID eingeben: "))
                qty = int(input("Menge: "))
                product = next((p for p in products if p.product_id == product_id), None)
                if product:
                    if product.reduce_stock(qty):
                        cart.add_item(product, qty)
                        print(f"{qty}x {product.name} hinzugefügt.")
                    else:
                        print("Nicht genug Bestand!")
                else:
                    print("Produkt nicht gefunden.")
            except ValueError:
                print("Ungültige Eingabe!")

        elif choice == "5":
            if not cart.items:
                print("Warenkorb ist leer!")
            else:
                new_order_id = len(orders) + 1
                order = Order(new_order_id, customer, cart.items)
                orders.append(order)
                customer.add_order(order)
                print("\n--- Bestellung erfolgreich ---")
                print(order)
                cart = Cart()  # Warenkorb leeren

        elif choice == "6":
            print("\n--- Alle Bestellungen ---")
            for o in orders:
                print(o)

        elif choice == "0":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Option!")

if __name__ == "__main__":
    main()
