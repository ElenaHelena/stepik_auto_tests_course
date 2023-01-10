# 3lesson2_step13
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class test_example_unittest(unittest.TestCase):
    # def test_browser(self):
    #     self.browser = webdriver.Chrome()

    def test_browser_get_link1(self):
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Petr")

        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("test@mail.ru")

    # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #     time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)



    def test_browser_get_link2(self):
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Petr")

        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("test@mail.ru")

    # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #     time.sleep(1)

    # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
    # закрываем браузер после всех манипуляций

if __name__ == "__main__": unittest.main()