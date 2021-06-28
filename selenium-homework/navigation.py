from selenium import webdriver

driver = webdriver.Chrome()

good_links = []


def selection():
    for a in anchors:
        if a.get_attribute("target") != "_blank":
            good_links.append(a)


driver.get("http://localhost:9999/general.html")

anchors = driver.find_elements_by_xpath('//a')

selection()

for g in good_links:
    g_href = g.get_attribute("href")
    url = driver.current_url
    g.click()
    # assert(driver.current_url == g.get_attribute("href"))
    if g_href == url:
        print("tag és href egyezik")
        driver.back()

    # while url == g_href:
    #     # time.sleep(1.0)
    #     driver.back()

driver.close()
