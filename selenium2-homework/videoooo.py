from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

try:
    driver.get("http://localhost:9999/videos.html")

    html5video = driver.find_element_by_id("html5video")
    # html5video.click() itt nem működik a kattintás, mert a szimuláció nem úgy viselkedik jelen esetben, mint amikor direktben az egérrel manipulálom/indítom klikkeléssel a lejátszást
    html5video.send_keys(Keys.SPACE)
    time.sleep(4)
    html5video.screenshot('video1_screenshot.png')
    time.sleep(1)
    html5video.send_keys(Keys.SPACE)
    time.sleep(2)

    video_bunny = driver.find_element_by_id("video1")
    play_pause_button = driver.find_element_by_xpath("//button[text()='Play/Pause']")
    play_pause_button.click()
    time.sleep(4)
    video_bunny.screenshot('video2_screenshot.png')
    time.sleep(1)
    play_pause_button.click()
    time.sleep(2)

    iframe_video = driver.find_element_by_id("youtubeframe")
    # iframe_video = driver.find_element_by_xpath("//iframe[@src='https://www.youtube.com/embed/tgbNymZ7vqY']")
    #
    driver.switch_to.frame(iframe_video)
    # iframe_video.send_keys(Keys.SPACE)

    # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@src='https://www.youtube.com/embed/tgbNymZ7vqY']"))    #ez működött


    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play']"))).click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Play"]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="player"]'))).click()



    # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    # link = iframe_video.get_attribute("scr")
    # link.click()
    time.sleep(6)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="player"]'))).screenshot('video3_screenshot.png')
    # iframe_video.click()
    # iframe_video.screenshot('video3_screenshot.png')
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="player"]'))).click()
    # iframe_video.click()
    time.sleep(2)



finally:
    driver.close()