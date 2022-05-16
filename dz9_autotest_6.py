from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_6(my_browser):
    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/webtables')
    # Данные ввода
    #data = input()
    data = 'Alden'
    form_search = my_browser.find_element(By.ID, 'searchBox')
    form_search.send_keys(data)
    # Верификация
    # Получаем все строчки в таблице, они черт побери одинаковые О_о
    rows_in_table = my_browser.find_elements(By.XPATH, '//div[@class="rt-tr-group"]')
    # Сканирование всех строк с данными ввода
    for data in rows_in_table:
        # Условие отсекает пустые строки
        if not data.text.isspace():
            # Пушка-способ Артемия замены в строке \n (перенос на новую строку) на обычный пробел
            print(' '.join(data.text.splitlines()))
# Запуск
my_browser = init_browser()
dz9_autotest_6(my_browser)
my_browser.close()
