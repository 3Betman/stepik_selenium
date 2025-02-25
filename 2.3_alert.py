import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")
option1 = driver.find_element(By.CSS_SELECTOR, ".btn")
option1.click()
confirm = driver.switch_to.alert
confirm.accept()
time.sleep(1)

x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
y=calc(x)

input_field = driver.find_element(By.CSS_SELECTOR, "#answer")
input_field.send_keys(y)

option1 = driver.find_element(By.CSS_SELECTOR, ".btn")
option1.click()
time.sleep(10)

driver.quit()

