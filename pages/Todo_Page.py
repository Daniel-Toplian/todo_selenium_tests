import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.Base_Page import Base_Page


@pytest.mark.usefixtures("init_driver")
class Todo_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.todo_list = driver.find_element(by=By.CLASS_NAME, value='todo-list')
        self.todo_input = driver.find_element(by=By.CLASS_NAME, value='todo-input')
        self.add_button = driver.find_element(by=By.CLASS_NAME, value='todo-btn')

    def add_todo(self, todo_description):
        self.todo_input.send_keys(todo_description)
        self.add_button.click()

    def delete_todo(self, todo_index):
        if self.todo_count() > todo_index:
            delete_button = self.get_todos()[todo_index].find_element(by=By.CLASS_NAME, value='todo-options') \
                .find_element(by=By.CLASS_NAME, value='delete-btn')
            delete_button.click()

    def update_todo(self, todo_index, updated_title):
        edit_button = self.get_todos()[todo_index].find_element(by=By.CLASS_NAME, value='todo-options') \
            .find_element(by=By.CLASS_NAME, value='edit-btn')
        edit_button.click()

        todo_to_updated = self.todo_list.find_elements(by=By.CLASS_NAME, value='TodoForm')[0]
        todo_text_input = todo_to_updated.find_element(by=By.CLASS_NAME, value='todo-input')
        todo_text_input.clear()
        todo_text_input.send_keys(updated_title)
        todo_to_updated.find_element(by=By.CLASS_NAME, value='todo-btn').click()

    def toggle_todo_status(self, todo_index):
        self.get_todo(todo_index).find_element(by=By.TAG_NAME, value='p').click()

    def todo_count(self):
        return len(self.todo_list.find_elements(by=By.CLASS_NAME, value='Todo'))

    def get_todos(self):
        return self.todo_list.find_elements(by=By.CLASS_NAME, value='Todo')

    def get_todo(self, index):
        return self.get_todos()[index] if index < self.todo_count() else None
