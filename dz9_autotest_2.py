from pathlib import Path
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_2(my_browser):
    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/upload-download')

    # Загрузка файла на сервер с расширением.
    thisistheway = 'C:\Selenium\dz9_downloads.txt'
    choosefile = my_browser.find_element(By.XPATH, '//*[@id="uploadFile"]')
    choosefile.send_keys(thisistheway)
    output = my_browser.find_element(By.ID, 'uploadedFilePath').text
    path, file_in = os.path.split(thisistheway)
    path, file_out = os.path.split(output)

    # Сравнение имен файлов.
    assert file_out == file_in
# Запуск
my_browser = init_browser()
dz9_autotest_2(my_browser)
my_browser.close()
