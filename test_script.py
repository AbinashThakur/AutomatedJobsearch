from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

path = '/home/surya/Documents/chromedriver'

# driver = webdriver.ChromeOptions() 
# driver.add_argument("--profile-directory=Default")
# driver.add_argument("--headless") #For headless
# driver.add_argument('--user-data-dir=C:/Temp/ChromeProfile')
# driver = webdriver.Chrome(executable_path=path, chrome_options=driver)


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(path, chrome_options=options)
print("success1")
driver.get("https://www.naukri.com/mnjuser/homepage")
print("success2")
# time.sleep(10)

# submit_p1 = driver.find_element_by_xpath('//a[starts-with(@href,"/mnjuser/profile?id=&orgn=homepage")]')
# ActionChains(driver).click(submit_p1).perform()

# driver.execute_script("document.querySelector('div.dp-wrapper').click()")
element=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@href, '/mnjuser/profile?id=&orgn=homepage')]")))
driver.execute_script("arguments[0].click();", element)
# WebDriverWait(driver, 0).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/mnjuser/profile?id=&orgn=homepage')]"))).click()


# driver.find_element_by_xpath('//a[@href="/mnjuser/profile?id=&orgn=homepage"]').click()
# submit_p2 = driver.find_element_by_xpath('//a[@href="/mnjuser/profile?id=&orgn=homepage"]')
# ActionChains(driver).click(submit_p2).perform()
print("success3")
time.sleep(5)

# submit_p2 = driver.find_elements_by_xpath("//*[@class='icon' and @class='edit']")
# ActionChains(driver).click(submit_p2).perform()
driver.execute_script("document.querySelector('em.edit').click()")
# print(submit_p2)
# pen = driver.find_element_by_css_selector('em.edit').click()
print("success4")
time.sleep(10)

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE']"))).click()

# submit_p3 = driver.find_element_by_xpath("//button[text()='SAVE']")
# ActionChains(driver).click(submit_p3).perform()

# submit_p3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE']")))
# wait = WebDriverWait(driver, 10)
# submit_p3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SAVE']")))
# ActionChains(driver).click(submit_p3).perform()


# time.sleep(5)
print("success5")
driver.close()