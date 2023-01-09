# 2lesson2_step6 execute_script

import select
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://SunInJuly.github.io/execute_script.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    find_valuex = driver.find_element(By.ID, "input_value")
    valuex = find_valuex.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = driver.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input = driver.find_element(By.ID, "answer")
    input.send_keys(y)

    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    option1 = driver.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = driver.find_element(By.ID, "robotsRule")
    option2.click()

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
        time.sleep(3)
    # закрываем браузер после всех манипуляций
        driver.quit()