from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "C:/Users/111/testqa/3.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Багдасарьян")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="firstName"]')
    input3.send_keys("Михаил")
    input4 = browser.find_element(By.CSS_SELECTOR, '[name="middleName"]')
    input4.send_keys("Владиславович")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла