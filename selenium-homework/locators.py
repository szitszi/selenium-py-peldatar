import time

from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get("http://localhost:9999/kitchensink.html")

    element_mousehover = driver.find_element_by_id("mousehover")
    element_showhide = driver.find_element_by_name("show-hide")
    element_confirm = driver.find_element_by_xpath('//input[@id="confirmbtn"]')

    collection = [element_mousehover, element_showhide, element_confirm]

    for i in collection:
        print("tag of the element : " + str(i.tag_name))

finally:
    time.sleep(1.0)
    driver.close()
