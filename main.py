from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_drive_path = "C:\Development\chromedriver.exe"
ser = Service(chrome_drive_path)
driver =webdriver.Chrome(service=ser)

# driver.get("https://www.amazon.ca/dp/B091M91SB3/?coliid=IQGUHGMO0PQ9U&colid=14WWARX76XG5J&psc=1&ref_=lv_ov_lig_dp_it")
# price = driver.find_element(By.CLASS_NAME,"a-offscreen")
# print(price.get_attribute('innerHTML'))

driver.get("https://www.python.org")
search_bar = driver.find_element(By.NAME,"q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element(By.CLASS_NAME,"python-logo")
print(logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

### Challenge##
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time") # this is a list, so print with for loop
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        'time':event_times[n].text,
        'name':event_names[n].text
    }

print(events)
# driver.close() #close one tab
driver.quit() #close more than one tab all together (whole program)
