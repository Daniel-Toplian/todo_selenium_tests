import configparser

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = None


def setup_module(module):
    print("-----------------setup-----------------")
    global driver
    # config = configparser.ConfigParser()
    # config.read('../env.properties')
    # URL = config.get('DEFAULT', 'URL')
    URL = "http://localhost:3000/"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get(URL)


def teardown_module(module):
    print("-----------------teardown-----------------")
    driver.quit()


class todo_page_tester:

    def test_add_task(self):
        todo_list = driver.find_element(by=By.CLASS_NAME, value='TodoWrapper')
        todo_input = driver.find_element(by=By.CLASS_NAME, value='todo-input')
        add_button = driver.find_element(by=By.CLASS_NAME, value='todo-btn')

        old_todos_count = len(todo_list.find_elements(by=By.CLASS_NAME, value='Todo'))

        todo_input.send_keys('test 1')
        add_button.click()

        updated_todos_count = len(todo_list.find_elements(by=By.CLASS_NAME, value='Todo'))

        assert updated_todos_count == old_todos_count + 1

    def test_edit_task(self):
        assert True

    def test_check_task(self):
        assert True

    def test_uncheck_task(self):
        assert True

    def test_delete_task(self):
        assert True
