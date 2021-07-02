from selenium import webdriver
import time

links = []
driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999")

    # egy listába kigyűjtjük a link elemeket, azaz az anchorokat
    anchors = driver.find_elements_by_xpath("//a")

    # a kigyűjtött anchorokhoz tartozó link szöveget for ciklussak kigyűjtjük egy links nevű listába
    for a in anchors:
        links.append(a.get_attribute("href"))
    # print(links)
    # print(type(links))
    # print(type(links[0]))

    # a links lista elemeit kiírjuk egy fájlba, itt figyelni kell arra, hogy ha a lista elemek nem string-ek akkor át kell alakítani őket
    # mivel soronként kell kiírni ezért for ciklussal kell dolgozni, illetve minden elemhez sortörést kell betenni
    with open("links.txt", "w") as file:
        for link in links:
            # file.write(str(link) + "\n")
            file.write((link) + "\n")
            # file.write(f"{link}, \n")
            # file.write(f"Number {links.index(link)} link: {link} \n")

    # print(len(anchors))
    print(f"Number of links: {len(links)}")

    time.sleep(1)

finally:
    # pass
    driver.close()
