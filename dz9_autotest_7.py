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
    my_browser.get('https://demoqa.com/webtables')
    # Путь до удаляемой строки
    path_row_old = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]'
    # Данные строки
    row_old = my_browser.find_element(By.XPATH, path_row_old).text.split()
    #print(row_old)
    # Кнопка удаления
    button_del = my_browser.find_element(By.ID, 'delete-record-2')
    button_del.click()
    # Верификация
    count = 0
    while count != 3:       # Надо знать общее количество строк (?)
        count = count + 1
        row_new = my_browser.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[{count}]').text.split()  #Спасибо согражданам за f-строки
        print(row_new)
        try:
            assert row_old != row_new
        except:
            print('Строка на месте')
    print('Какое количество строк ты проверил?')
    print('Ответ:' + str(count))
# Запуск
my_browser = init_browser()
dz9_autotest_7(my_browser)
my_browser.close()
