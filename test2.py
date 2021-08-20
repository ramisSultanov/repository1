import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

driver.get('https://form.123formbuilder.com/5012215')
driver.maximize_window()
driver.find_element(By.XPATH, '//input[@placeholder="First"]').send_keys('Vasya')
time.sleep(0.3)
driver.find_element(By.XPATH, '//input[@placeholder="Last"]').send_keys('Pupkin')
driver.find_element(By.XPATH, '//input[@type="email"]').send_keys('a@a.ru')
driver.find_element(By.XPATH, "//input[@placeholder='### ### #### ']").send_keys('1234567890')
driver.find_element(By.XPATH, "//span[contains(text(),'Product 1')]").click()

driver.find_element(By.XPATH, "//input[@type='number']").send_keys('1')

driver.find_element_by_xpath("//div[@data-role='expander']").click()
time.sleep(0.6)
driver.find_element_by_xpath("//div[@data-day='18']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys('123 E Side')
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys('Old York')
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Postal')]").send_keys('12345')
driver.find_element(By.XPATH, "//*[@placeholder='Country']").send_keys('United States' + Keys.ARROW_DOWN + Keys.ENTER)
driver.find_element(By.XPATH, "//option[@value='Choice2']").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Choice 2')]").click()
time.sleep(1)

frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0])

driver.find_element_by_class_name("recaptcha-checkbox-border").click()
time.sleep(3)

driver.find_element(By.XPATH, "//span[contains(text(),'Submit order')]").click()