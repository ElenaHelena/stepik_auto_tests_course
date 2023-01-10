# browser.quit()
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.fullscreen_window()
browser.execute_script("window.scrollBy(0, 150);")

try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    browser.save_screenshot("booking.png")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value').text
    y = calc(int(x))
    fill_form = browser.find_element(By.CSS_SELECTOR,'input.form-control').send_keys(y)
    button_submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()


finally:
    time.sleep(3)