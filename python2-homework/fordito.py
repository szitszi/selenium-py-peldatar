# létrehozunk egy üres listát, amiben a felhasználótól bekért számokat tároljuk
user_list = []

# while ciklussal érjük el azt, hogy amíg a feltételünk teljesül, addig folyton új elemet kérünk be és tároljuk a számokat, ha pedig már nem teljesül
while True:
    number = int(input("Írj be egy számot: "))
    if number == 0:
        print(user_list[-1::-1])
        break

    user_list.append(number)