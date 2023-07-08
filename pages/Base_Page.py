import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys_to_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys()

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click().text

    def is_visible(self, by_locator):
        return bool(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click())



