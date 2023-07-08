import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class Todo_page(Base_Page):

    def __init__(self, driver):
        super.__init__(driver)

    def add_todo(self):
        pass

    def delete_todo(self):
        pass

    def update_todo(self):
        pass

    def complete_todo(self):
        pass

    def incomplete_todo(self):
        pass

