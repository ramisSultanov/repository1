import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()
print(driver.find_element(By.XPATH, "//header//a[contains(text(), 'California Real Estate')]").get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='custom-logo']").get_attribute("src"))
assert(driver.title == "California Real Estate – QA at Silicon Valley Real Estate")
print(driver.title)
driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
driver.find_element(By.ID, "g2-name").send_keys("Ramis")
driver.find_element(By.NAME, "g2-email").send_keys("mrrs1007@gmail.com")
driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("Hit")
time.sleep(4)
driver.find_element(By.CLASS_NAME, "pushbutton-wide").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
assert(driver.find_element(By.CLASS_NAME, "pushbutton-wide"))

driver.quit()
