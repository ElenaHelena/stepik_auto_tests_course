# 2lesson1_step7


import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/get_attribute.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)


    find_valuex = driver.find_element(By.ID, "treasure")
    valuex = find_valuex.get_attribute("valuex")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = valuex
    y = calc(x)


    input = driver.find_element(By.ID, "answer")
    input.send_keys(y)

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

# не забываем оставить пустую строку в конце файла
