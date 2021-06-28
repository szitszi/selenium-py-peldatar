with open("adat.txt", "r" ) as f2:
    my_list = []
    for i in range(1):
        my_list.append(f2.readlines())
    print(my_list)