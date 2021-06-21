# sör és kóla


age = int(input("Hány éves vagy? "))
drink = input("Mit iszol? ")

if age < 18:
    if drink == "sör":
        print("Nem adhatok sört.")
    elif drink == "kóla":
        print("Parancsoljon, a kólája!")
    else:
        print("Csak kóla és sör van.")
elif age > 60:
    if drink == "kóla":
        print("A kóla megemelhetti a vérnyomását.")
    elif drink == "sör":
        print("Parancsoljon, a söre.")
    else:
        print("Csak kóla és sör van.")
else:
    if drink == "kóla":
        print("Parancsoljon, a kólája.")
    elif drink == "sör":
        print("Parancsoljon, a söre.")
    else:
        print("Csak kóla és sör van.")