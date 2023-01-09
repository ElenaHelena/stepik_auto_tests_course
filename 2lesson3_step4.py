# 2lesson3_step4.py
import time
import os
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/alert_accept.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)


    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    find_valuex = driver.find_element(By.ID, "input_value")
    valuex = find_valuex.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = valuex
    y = calc(x)

    input = driver.find_element(By.ID, "answer")
    input.send_keys(y)

    button2 = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла