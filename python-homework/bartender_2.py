choice1 = "kóla"
choice2 = "sör"


age = int(input("Hány éves? "))
drink = input("Mit iszik? ")

if (drink != choice2) and (drink != choice1):
    print("Csak kóla és sör van.")
elif age < 18 and drink == choice2:
    print("Nem adhatok sört.")
elif age > 60 and drink == choice1:
    print("A kóla megemelheti a vérnyomását.")
else:
    print("Parancsoljon a " + drink + "!")