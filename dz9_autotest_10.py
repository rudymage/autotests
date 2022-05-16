
from selenium.webdriver import ActionChains
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_10(my_browser):
    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/sortable')
    # Спасибо гугл
    justdoit = ActionChains(my_browser)
    #print('Позиция элемента')
    #old = input()
    #print('Новая позиция элемента')
    #new = input()

    # Номера позиций. Вырываемся на первое место.
    old = 3
    new = 1
    # Позиции элемента по XPATH
    position_old = my_browser.find_element(By.XPATH, f'//*[@id="demo-tabpane-list"]/div/div[{old}]')
    position_new = my_browser.find_element(By.XPATH, f'//*[@id="demo-tabpane-list"]/div/div[{new}]')
    # Смена позиции
    justdoit.drag_and_drop(position_old, position_new).perform()
# Запуск
my_browser = init_browser()
dz9_autotest_10(my_browser)
my_browser.close()