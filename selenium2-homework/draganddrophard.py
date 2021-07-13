from selenium import webdriver
import time
from os import getcwd

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://localhost:9999/dragndrop2.html#/lists")

time.sleep(2)

cwd = getcwd()
JS_DRAG_DROP = open(cwd + '\\dnd.js', 'r').read()
# print(JS_DRAG_DROP)


todos = driver.find_elements_by_xpath("//ul[@id='Todo']/li")
# print(len(todos))

target_place = driver.find_element_by_xpath("//ul[@id='Doing']")

for e_task in todos:
    driver.execute_script(JS_DRAG_DROP, e_task, target_place)
    time.sleep(2)

driver.implicitly_wait(5)

driver.close()
