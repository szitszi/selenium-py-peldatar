import csv
import os

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://localhost:9999/another_form.html')

def find_and_clear(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

input_csv_content = []

with open('table_in.csv', encoding='utf-8') as csvfile:
    input_csv = csv.reader(csvfile, delimiter=',')              # megadjuk, hogy mit olvasson a csv olvasó, valamint azt, hogy milyen elválasztót használtunk( ez lehet , és ; stb)
    next(input_csv)                              # erre azért van szükség, mert az első sor csak a fejléc konkrét értékeket nem tartalmaz
    for row in input_csv:
        input_csv_content.append(row)
        find_and_clear("fullname").send_keys(row[0])

        find_and_clear("email").send_keys(row[1])

        find_and_clear("dob").send_keys(row[2])

        find_and_clear("phone").send_keys(row[3])

        submit = driver.find_element_by_id("submit")
        submit.click()



        # name = driver.find_element_by_id("fullname")
        # name.clear()
        # name.send_keys(row[0])
        # time.sleep(2)
        #
        # email = driver.find_element_by_id("email")
        # email.clear()
        # email.send_keys(row[1])
        # time.sleep(2)
        #
        # dob = driver.find_element_by_id("dob")
        # dob.clear()
        # dob.send_keys(row[2])
        # time.sleep(2)
        #
        # phone = driver.find_element_by_id("phone")
        # phone.clear()
        # phone.send_keys(row[3])
        # time.sleep(2)
        #
        # submit = driver.find_element_by_id("submit")
        # submit.click()

driver.find_element_by_xpath("/html/body/main/div/button").click()
# export_button.click()
time.sleep(1)




# table_list = driver.find_elements_by_xpath("//table[@id='detailsTable']/tbody/tr")

# for row in table_list:
#     cells = row.find_elements_by_tag_name("td")
#     # print(cells[0].text, cells[1].text, cells[2].text)
#     print(type(cells))
#     print(cells[0])

result_csv_content = []

with open("C:\\Users\\czink\\Downloads\\table.csv", encoding='utf-8') as result_file:
    result_csv = csv.reader(result_file, delimiter=',') # megadjuk, hogy mit olvasson a csv olvasó, valamint azt, hogy milyen elválasztót használtunk( ez lehet , és ; stb)
    print(result_csv)
    next(result_csv) # erre azért van szükség, mert az első sor csak a fejléc konkrét értékeket nem tartalmaz
    for row in result_csv:
        result_csv_content.append(row)


print(type(input_csv_content))
print(input_csv_content)
print(type(result_csv_content))
print(result_csv_content)



assert input_csv_content == result_csv_content


os.remove("C:\\Users\\czink\\Downloads\\table.csv") #töröljük a legenerált csv, hogy újra ismételhető legyen a teszt



time.sleep(2)

driver.close()