from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

your_name = "Szilvi"

driver.get("http://localhost:9999/alert_playground.html")

buttons = driver.find_elements_by_xpath("//input[@type='button']")
print(len(buttons))



def button_normal_click(button_element):
    button_element.click()
    time.sleep(2.0)
    driver.switch_to.alert.accept()
    time.sleep(2.0)

def button_click_with_text_insert(button_element):
    button_element.click()
    time.sleep(1.0)
    driver.switch_to.alert.send_keys(your_name)
    driver.switch_to.alert.accept()
    time.sleep(1.0)

try:
    for button in buttons[0:2:1]:
        button_normal_click(button)

    button_click_with_text_insert(buttons[2])
    label = driver.find_element_by_id("demo")
    assert label.text == (f"You entered: {your_name}")
    print(label.text)
    time.sleep(1.0)



    act = ActionChains(driver)
    double_click_button = driver.find_element_by_id("double-click")
    act.double_click(double_click_button).perform()
    double_click_window = driver.switch_to.alert
    print(double_click_window.text)
    time.sleep(1.0)
    double_click_window.accept()
    time.sleep(1.0)


finally:
    # pass
    driver.close()