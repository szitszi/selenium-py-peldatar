import csv

with open('table_in.csv') as csvfile:  #('table_in_original.csv')
    with open('selection.txt', "w") as output_list:
        csvreader = csv.reader(csvfile, delimiter=',')
    # print(type(csvreader))
    # next(csvreader) # erre azért van szükség, mert az első sor csak a fejléc konkrét értékeket nem tartalmaz
        for row in csvreader:
            # output_list.encode('ascii', 'ignore')
            # print(row[-3::-1])
            output_list.write(str(row[-3::-1]) + "\n")
            # print(type(row))
            # print(row[0])
        # print(type(csvreader))

# ki kellene szedni a space karaktereket az emailcímből
# a karakternek olvashatónak kellene lenni: encoding="utf-8" a beolvasáskor-->OK
# .encode('ascii', 'ignore'))