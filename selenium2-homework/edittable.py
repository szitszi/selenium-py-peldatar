from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://localhost:9999/editable-table.html')

list = ["ham", "1", "10", "Food"]

need_to_fill_row = 3

start_number_of_rows = len(driver.find_elements_by_xpath("//tr[@class='eachRow']"))

add_button = driver.find_element_by_xpath('//button[text()="Add"]')


def automatic_fill():
    time.sleep(0.5)
    add_button.click()
    actual_number_of_rows = len(driver.find_elements_by_xpath("//tr[@class='eachRow']"))
    next_row_cells = driver.find_elements_by_xpath(
        f"//table[@class='table table-bordered']/tbody/tr[{actual_number_of_rows}]/td/input")
    for i in range(len(list)):
        next_row_cells[i].send_keys(list[i])


def repeater(need_to_fill_row):
    for i in range(need_to_fill_row):
        automatic_fill()


repeater(need_to_fill_row)

assert len(driver.find_elements_by_xpath("//tr[@class='eachRow']")) == start_number_of_rows + need_to_fill_row

# ---------------------------------------------------------------------------------------------


test_data = "basketball"

# test_data = list[0]
# print(list[0])

search = driver.find_element_by_xpath("//input[@type='text' and @placeholder='Search...']")
search.send_keys(test_data)
number_of_test_data = len(driver.find_elements_by_xpath(f"//input[@value='{test_data}']"))
print(number_of_test_data)

assert number_of_test_data == len(driver.find_elements_by_xpath("//tr[@class='eachRow']"))

# -------------------------------------------------------------------------------------

#
driver.close()