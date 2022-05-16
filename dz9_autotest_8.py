from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_8(my_browser):
    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/browser-windows')

    #Переменная title
    page_1 = my_browser.current_window_handle
    page_1_title = page_1.title

    # Кнопка New Tab
    new_tab = my_browser.find_element(By.ID, 'tabButton')
    new_tab.click()

    # Переход на новую вкладку и ее закрытие
    my_browser.switch_to.window(my_browser.window_handles[1])
    my_browser.close()

    # Переход на старую вкладку и запись нового заголовка
    my_browser.switch_to.window(page_1)
    page_1_new_title = page_1.title

    # Сравнение заголовков
    assert page_1_title == page_1_new_title
    
    # Перебор кнопок в общем элементе
    for button in my_browser.find_elements(By.ID, 'browserWindows'):
        if button.is_enabled() is True:
            print(button.text)
        else:
            print('Нет активных кнопочек')
# Запуск
my_browser = init_browser()
dz9_autotest_8(my_browser)
my_browser.close()
