from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_7(my_browser):
    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/alerts')
    # Кнопка
    button_alert = my_browser.find_element(By.ID, 'alertButton')
    button_alert.click()
    # Переход в alert и его подтверждение
    alert = my_browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    # Вывод
    print(alert_text)
# Запуск
my_browser = init_browser()
dz9_autotest_7(my_browser)
my_browser.close()
