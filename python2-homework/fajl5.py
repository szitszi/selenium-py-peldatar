# def iras(v):
#     file.write(v)
#     file.write("\n")

with open("adat.txt", "r" ) as f5:
    for i in range(9):
        result5 = f5.readline()
        # with open("mas.txt", "a") as file:
        #     iras(result5)
        with open("mas.txt", "a") as file:
            file.write(result5)
        print(result5)