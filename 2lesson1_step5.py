# 2lesson1_step5

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = driver.find_element(By.ID, 'input_value')
    x = x_element.text
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
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
