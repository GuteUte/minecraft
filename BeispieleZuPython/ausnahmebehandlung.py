while True:
    try:
        eingabewert = input("Bitte geben Sie ein Zahl ein: ")
        eingabewert = int(eingabewert)
        break
    except ValueError:
           print("Die war leider keine Zahl!")

print("Danke fuer die Eingabe der Zahl " + str(eingabewert))