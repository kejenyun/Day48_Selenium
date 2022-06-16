from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # select Keys and hit F4 to see the constants available

chrome_drive_path ="C:\Development\chromedriver.exe"
srv = Service(chrome_drive_path)
driver = webdriver.Chrome(service=srv)
#
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# article_count =driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# #article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
#
# ##Click on a item use ".click()"  Also specify which link to click
# #article_count.click()
#
# community_portal = driver.find_element(By.LINK_TEXT, "Community portal")
# community_portal.click()
#
# # Type something using ".send_keys()"
# search_box = driver.find_element(By.NAME,"search") #Finding search bar
# search_box.send_keys("Python") # type in search word
# search_box.send_keys(Keys.ENTER) #hit enter #other than ENTER, we can use in any keys on the keyboard ex: shift, ctrl

####Challenge####

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Maggie")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Yun")
email = driver.find_element(By.NAME, "email")
email.send_keys("yahoyun228@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.send_keys(Keys.ENTER)





# driver.quit()
