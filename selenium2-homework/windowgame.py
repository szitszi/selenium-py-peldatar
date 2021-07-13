from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/windowgame.html")
    random_color = driver.find_element_by_id("target_color").text
    print(f"The color you are looking for is: {random_color}")
    while True:

        buttons = driver.find_elements_by_xpath("//table[@style='width:100%']/tbody/tr/td/button")
        # print(len(buttons))
        time.sleep(0.1)
        main_window = driver.window_handles[0]

        for each_button in buttons:
            each_button.click()
            new_window = driver.window_handles[1]
            driver.switch_to.window(new_window)
            window_color = driver.find_element_by_tag_name("h1").text
            # print(window_color)
            time.sleep(0.1)
            driver.close()
            driver.switch_to.window(main_window)
            time.sleep(0.1)

            if random_color != window_color:
                pass
                # print("not OK")
            else:
                print("You found the target color!")
                print("Number of guesses made: " + driver.find_element_by_id("numberOfGuesses").text)
                break

    time.sleep(1)

finally:
    # pass
    driver.close()
