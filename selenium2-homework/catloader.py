import os
from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/loadmore.html")

    time.sleep(3)
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")  # megkeressük a lapozó gombot

    for i in range(3):
        load_more.click()
        time.sleep(3)

    cat_image_divs = driver.find_elements_by_xpath(
        "//div[@class='image']")  # a betöltött képek burkoló osztályait elmentjük egy listába
    os.makedirs("R:\\Cats", exist_ok=True)  # mappa látrehozása, ha nem kézzel hozzuk létre

    for i in range(len(cat_image_divs)):
        serial_number = i + 1

        cat_id_full = cat_image_divs[i].find_element_by_tag_name("p").text
        cat_id = cat_id_full[8::]

        file_name = (str(serial_number) + "_" + cat_id + ".jpg")
        print(file_name)

        cat_image_url = cat_image_divs[i].find_element_by_tag_name("img").get_attribute("src")

        img_data = requests.get(cat_image_url).content
        with open(f"R:\\Cats\\{file_name}",
                  'wb') as handler:  # a mappát létrehozni, ahová menteni akarunk, kézzel vagy pythonnal is lehet
            handler.write(img_data)



finally:
    driver.close()
