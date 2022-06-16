from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # select Keys and hit F4 to see the constants available
import time


chrome_drive_path ="C:\Development\chromedriver.exe"
srv = Service(chrome_drive_path)
driver = webdriver.Chrome(service=srv)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

#get cookie to click
cookie = driver.find_element(By.ID, "cookie")

timeout =time.time() +5*60 #5 min from now
five_sec = time.time()+5 #5 sec

def buy_upgrade():
    upgrades = driver.find_elements(By.CSS_SELECTOR, f"#store :not(.grayed) b")
    upgrades_price =[]
    for upgrade in upgrades:
        if "," not in upgrade.text:
            upgrades_price.append(int(upgrade.text.split('-')[1]))
        else:
            upgrades_price.append(int(upgrade.text.split(" - ")[1].replace(",", "")))

        index = upgrades_price.index(max(upgrades_price))
        upgrades[index].click()


while time.time() < timeout:
    cookie.click()

    #EVERY 5 Sec.
    if time.time() > five_sec:
        buy_upgrade()
        five_sec +=5

click_per_sec = driver.find_element(By.ID, "cps").text
print(click_per_sec)

driver.quit()