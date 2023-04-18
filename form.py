from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

try: 
    link = "C:/Users/111/test_rep/form.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "FIO")
    input1.send_keys("Мой ответ 1")
    input2 = browser.find_element(By.NAME, "email")
    input2.send_keys("Мой ответ 2")
    input3 = browser.find_element(By.NAME, "Phone")
    input3.send_keys("Мой ответ 3")
    select1 = Select(browser.find_element(By.NAME, "transfer"))
    select1.select_by_value("Да") # ищем элемент с текстом "Python"
    select2 = Select(browser.find_element(By.NAME, "HowManyPeople"))
    select2.select_by_value("1") # ищем элемент с текстом "Python"
    select3 = Select(browser.find_element(By.NAME, "HowManyChild"))
    select3.select_by_value("1") # ищем элемент с текстом "Python"
    input4 = browser.find_element(By.NAME, "ChildAge")
    input4.send_keys("Мой ответ 4")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()