def addieren(num1, num2):
    return num1 + num2

def subtrahieren(num1, num2):
    return num1 - num2

def multiplizieren(num1, num2):
    return num1 * num2

def dividieren(num1, num2):
    if num1 / num2 == 0:
        return "Fehler bei der division"
    return num1 / num2

while True:
    print("Taschenrechner")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")
    print("5. Beenden")

    option = input("Wähle eine Option")

    if option == "5":
        print("Programm beendet")
        break

    num1 = float(input("Wähle Zahl 1"))
    num2 = float(input("Wähle Zahl 2"))

    if option == "1":
        print("Ergebnis: ", addieren(num1, num2))
    elif option == "2":
        print("Ergebnis: ", subtrahieren(num1, num2))
    elif option == "3":
        print("Ergebnis: ", multiplizieren(num1, num2))
    elif option == "4":
        print("Ergebnis: ", dividieren(num1, num2))
    else:
        print("Ungültiges Ergebnis")