from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://imdb.com")

    x = driver.find_element_by_id("nemletezik")
    x.click()


except:
    print("The element is not exist.")
    driver.close

# finally:
#     driver.close
