from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:9999/trickyelements.html")

buttons = driver.find_elements_by_xpath('//button')

try:
    buttons[0].click()
except:
    print("Nincs button elem")

result = driver.find_element_by_id("result")

# if (buttons[0].text + " was clicked") == result.text:
#     print("Helyes szöveg jelenik meg az elemek listája alatt.")
# else:
#     print("Nem helyes a megjelenített szöveg.")


assert buttons[0].text + " was clicked" == result.text

driver.close()
