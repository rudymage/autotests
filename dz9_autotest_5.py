from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

def init_browser():
    # Инициируем экземляр браузера Google Chrome, указав путь до его драйвера.
    browser = webdriver.Chrome(service=Service(str(Path(__file__).parent / 'chromedriver.exe')))
    return browser

def dz9_autotest_5(my_browser):
    # Необходимый web-адрес в браузере.
    my_browser.get('https://demoqa.com/webtables')

    # Характеристики пользователя
    department_list = ['Insurance', 'Compliance', 'Legal', 'Marketing']
    first_name = 'Ilya'
    last_name = 'Rudakov'
    email = 'rudymage@yandex.ru'
    age = 32
    salary = 20000
    department = 'Compliance'
    # Условия в формах ввода данных
    assert re.search(r'^[a-zA-Z]', first_name)
    assert re.search(r'^[a-zA-Z]', last_name)
    assert age >= 18
    assert 2000 <= salary <= 20000
    assert department in department_list
    # Кнопка редактирования
    button_edit = my_browser.find_element(By.XPATH, '//*[@id="edit-record-2"]')
    button_edit.click()
    # Редактирование форм [.clear()- очистить тескт поля]
    form_fn = my_browser.find_element(By.ID, 'firstName')
    form_fn.clear()
    form_fn.send_keys(first_name)
    form_ln = my_browser.find_element(By.ID, 'lastName')
    form_ln.clear()
    form_ln.send_keys(last_name)
    form_ue = my_browser.find_element(By.ID, 'userEmail')
    form_ue.clear()
    form_ue.send_keys(email)
    form_a = my_browser.find_element(By.ID, 'age')
    form_a.clear()
    form_a.send_keys(age)
    form_s = my_browser.find_element(By.ID, 'salary')
    form_s.clear()
    form_s.send_keys(salary)
    form_dep = my_browser.find_element(By.ID, 'department')
    form_dep.clear()
    form_dep.send_keys(department)
    button_submit = my_browser.find_element(By.ID, 'submit')
    button_submit.click()
    # Сравнение отредактированных данных с полученной записью
    assert first_name == str(my_browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[1]').text)
    assert last_name == str(my_browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[2]').text)
    assert email == str(my_browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[4]').text)
    assert age == int(my_browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[3]').text)
    assert salary == int(my_browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[5]').text)
    assert department == str(my_browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div[6]').text)
# Запуск
my_browser = init_browser()
dz9_autotest_5(my_browser)
my_browser.close()