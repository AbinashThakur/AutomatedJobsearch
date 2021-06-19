from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

path = '/home/surya/Documents/chromedriver'

driver = webdriver.ChromeOptions() 
driver.add_argument("--profile-directory=Default")
# driver.add_argument("--headless") #For headless
#driver.add_argument('--user-data-dir=C:/Temp/ChromeProfile')
driver.add_argument('--user-data-dir=/home/surya/Desktop/test/automation/C:/Temp/ChromeProfile')
driver = webdriver.Chrome(executable_path=path, chrome_options=driver)

print("success1")
driver.get("https://www.naukri.com/mnjuser/homepage")
print("success2")
time.sleep(5)

driver.find_element_by_xpath('//a[@href="/mnjuser/profile?id=&orgn=homepage"]').click()
print("success3")
time.sleep(5)

pen = driver.find_element_by_css_selector('em.edit').click()
print("success4")
time.sleep(5)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE']"))).click()

time.sleep(5)
print("success5")
driver.close()

