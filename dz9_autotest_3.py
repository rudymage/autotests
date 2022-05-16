from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_3(my_browser):
    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/dynamic-properties')

    after_ena = WebDriverWait(my_browser, 5).until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
    after_ena.click()
    after_vis = WebDriverWait(my_browser, 5).until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
    after_vis.click()
# Запуск
my_browser = init_browser()
dz9_autotest_3(my_browser)
my_browser.close()
