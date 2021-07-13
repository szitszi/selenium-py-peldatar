import os
from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/scrolltoload.html")
    driver.set_window_rect(200, 300, 200, 300)

    time.sleep(3)
    cat_image_divs = []
    requested_number_of_picture = 20

    while len(cat_image_divs) < requested_number_of_picture:
        cat_image_divs = driver.find_elements_by_xpath("//div[@class='image']")
        js = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(js)
        time.sleep(3)

    print(len(cat_image_divs))
    os.makedirs("R:\\Cats", exist_ok=True)

    for i in range(requested_number_of_picture):
        serial_number = i + 1

        cat_id_full = cat_image_divs[i].find_element_by_tag_name("p").text
        cat_id = cat_id_full[8::]

        file_name = (str(serial_number) + "_" + cat_id + ".jpg")
        print(file_name)

        cat_image_url = cat_image_divs[i].find_element_by_tag_name("img").get_attribute("src")

        img_data = requests.get(cat_image_url).content
        with open(f"R:\\Cats\\{file_name}", 'wb') as handler:  #
            handler.write(img_data)



finally:
    driver.close()
