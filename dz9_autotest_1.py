from lib2to3.pgen2 import driver
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_1(my_browser):
    un = str('Arnold Schwarzenegger')
    ue = str('arnold@schwarzenegger.com')
    ca = str('Santa Monica')
    pa = str('USA')

    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/text-box')
    # Элементы полей ввода запроса.
    search_form_un = my_browser.find_element(By.ID, 'userName')
    search_form_ue = my_browser.find_element(By.ID, 'userEmail')
    search_form_ca = my_browser.find_element(By.ID, 'currentAddress')
    search_form_pa = my_browser.find_element(By.ID, 'permanentAddress')
    # Введение значений переменных в поля ввода запросов.
    search_form_un.send_keys(un)
    search_form_ue.send_keys(ue)
    search_form_ca.send_keys(ca)
    search_form_pa.send_keys(pa)
    # Элемент "кнопка".
    button = my_browser.find_element(By.ID, 'submit')
    # Скролл до элемента.
    button.location_once_scrolled_into_view
    # Эмулятор клика на кнопку.
    button.click()
    # Поле с выводом всех значений.
    output = my_browser.find_element(By.ID,'output')
    # Поля значений в поле вывода с отсечением ненужной части.
    result_un = output.find_element(By.ID,'name').text.split(':', 1)[1]
    result_ue = output.find_element(By.ID, 'email').text.split(':', 1)[1]
    result_ca = output.find_element(By.ID, 'currentAddress').text.split(':', 1)[1]
    result_pa = output.find_element(By.ID, 'permanentAddress').text.split(':', 1)[1]
    # Сравнение ввода с выводом.
    assert result_un == un
    assert result_ue == ue
    assert result_ca == ca
    assert result_pa == pa
# Запуск
my_browser = init_browser()
dz9_autotest_1(my_browser)
my_browser.close()
