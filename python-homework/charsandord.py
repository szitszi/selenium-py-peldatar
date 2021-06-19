# print(ord("a")) ennek az eredménye a 97
# print(chr(97)) ennek az eredménye az a betű

x = 97
for i in range(10):
    i = (str(chr(x)) + str(" ") + str(x) + " " + str(chr(x+5)) + " " + str(x+5) + " " +str(chr(x+10)) + " " + str(x+10))
    x += 1
    print(i)
    pass
