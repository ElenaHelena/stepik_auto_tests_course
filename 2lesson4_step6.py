# 2lesson4_step6.py  Про Exceptions
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()


find_valuex = browser.find_element(By.ID, "input_value")
valuex = find_valuex.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = valuex
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button2 = browser.find_element(By.ID, "solve")
button2.click()


    # # успеваем скопировать код за 30 секунд
time.sleep(10)
    # # закрываем браузер после всех манипуляций
    # driver.quit()

# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text
