from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/selects2.html")
option = driver.find_element(By.CSS_SELECTOR, '#num1')
option2 = driver.find_element(By.CSS_SELECTOR, '#num2')
x=int(option.text)+int(option2.text)

select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(str(x))

option1 = driver.find_element(By.CSS_SELECTOR, ".btn")
option1.click()
time.sleep(10)

driver.quit()

