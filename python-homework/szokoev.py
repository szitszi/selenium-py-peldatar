requested_year = int(input("Írj be egy évszámot! : "))


def leap_year(x_year):
    if x_year % 400 == 0:
        return True
    elif x_year % 100 == 0:
        return False
    elif x_year % 4 == 0:
        return True
    else:
        return False


result = leap_year(requested_year)   #Ez egy boolean típusu változó


def user_output(y_result):
    if y_result:
        print("Szökőév")
    else:
        print("Nem szökőév")


user_output(result)