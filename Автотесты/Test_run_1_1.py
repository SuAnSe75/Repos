from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://zdravmir.github.io/"

try:
  
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[href="#description"]')
    input1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла