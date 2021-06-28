with open("adat.txt", "r" ) as f3:
    my_list = []
    for i in range(1):
        my_list.append(f3.readlines())
    print(my_list)


with open("mas_adat.txt", "w") as file:
    file.write(str(my_list))