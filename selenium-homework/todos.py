import time

from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get("http://localhost:9999/todo.html")

    todos = driver.find_elements_by_xpath('//span[@class="done-false"]')

    for todo in todos:
        print(todo.text)


finally:
    time.sleep(1.0)
    driver.close()