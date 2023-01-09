# 2lesson2_step3
import select
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    find_num1 = driver.find_element(By.ID, "num1")
    num1 = find_num1.text

    find_num2 = driver.find_element(By.ID, "num2")
    num2 = find_num2.text

    sum = int(num1)+int(num2)
    x= str(sum)
    print(x)

    driver.find_element(By.TAG_NAME, "select").click()
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()





finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    driver.quit()