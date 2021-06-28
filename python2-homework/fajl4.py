with open("adat.txt", "r" ) as f4:
    my_list = []
    for i in range(9):
        my_list.append(f4.readline())
print(my_list)
print(len(my_list))
# new_list = my_list.split(",")
# print(my_list[1])


with open("uj_adat.txt", "w") as file:
    for i in range(9):
        file.write(str(my_list[i]))