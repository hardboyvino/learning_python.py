"""
Automated program to play https://gabrielecirulli.github.io/2048/
"""

# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

# open the game in browser
# bypass the endless loading once the html shows on screen
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=capa)

wait = WebDriverWait(driver, 10)
driver.get("https://gabrielecirulli.github.io/2048/")
wait.until(EC.presence_of_element_located((By.XPATH, "//html")))

# wait for the endless loading to resolve itself then game commences
sleep(3)

# repeatedly press up, right, down, left in that order
buttons = driver.find_element(By.XPATH, "//html")

while True:
    try:
        # check for the try again button
        # print the current high score
        driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/a[2]").click()
        high_score = driver.find_element(By.CSS_SELECTOR, ".best-container")
        print(high_score.text)
    except Exception as ex:
        buttons.send_keys(Keys.UP)
        buttons.send_keys(Keys.RIGHT)
        buttons.send_keys(Keys.DOWN)
        buttons.send_keys(Keys.LEFT)
