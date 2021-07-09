from selenium import webdriver
import time
import pprint

driver = webdriver.Chrome()

driver.get("http://localhost:9999/pagination.html")

# firstname_with_a = driver.find_elements_by_xpath("//table[@id='contacts-table']/tbody/tr/td[2][starts-with(text(),'A')]")
# print(len(firstname_with_a))


extracted_data = []

try:
    while True:
        time.sleep(2)
        firstname_with_a_rows = driver.find_elements_by_xpath(
            "//table[@id='contacts-table']/tbody/tr/td[2][starts-with(text(),'A')]/parent::tr")
        for row in firstname_with_a_rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            extracted_data.append(data_row)

            # for k, v in data_row.items():  # ez a kulcsok és az értékek együttes listája
            #     print(k, v)
            #     list = (k, v)
            #     print(list)

        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break  # ha már nem elérhető a next button, akkor kitörünk a ciklusból
        else:
            next_button.click()

    # pprint.pprint(extracted_data)  # Pretty-print a Python object to a stream [default is sys.stdout] # szép
    pprint.pprint(extracted_data)

    # print(extracted_data)
    print(len(extracted_data))
    # print(str(extracted_data))
    # csv_list = str(extracted_data).split(",")
    # print(csv_list)

    # csv_list = extracted_data

    with open("firstname_a.csv", "w") as file:
        file.write(str(extracted_data))

    time.sleep(2)
finally:
    driver.close()
