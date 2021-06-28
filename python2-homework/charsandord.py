with open("text.txt", "r") as file:
    result = file.read()
    # print(result)

text2 = result.lower().replace("\n", "").split(" ")
# print(text2)

dict = {}
for word in text2:
    dict[word] = dict.get(word, 0) + 1
print(dict)

for k, v in dict.items():  # ez a kulcsok és az értékek együttes listája
    print(k, v)
