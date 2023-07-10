import configparser

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pages.Todo_Page import Todo_Page

driver = None


@pytest.fixture(autouse=True, scope="class")
def setup_module(request):
    global driver

    url = os.environ.get("TODO_URL")

    if url is None:
        url = "http://localhost:3000/"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get(url)

    todo_page = Todo_Page(driver)
    request.cls.todo_page = todo_page

    yield


def teardown_module(request):
    driver.quit()


@pytest.mark.run(order=1)
class Test_Todo_Page:

    @pytest.mark.run(order=1)
    def test_add_task(self):
        old_todos_count = self.todo_page.todo_count()
        self.todo_page.add_todo("test 1")
        updated_todos_count = self.todo_page.todo_count()

        assert updated_todos_count == old_todos_count + 1

    @pytest.mark.run(order=2)
    def test_update_task(self):
        todo_title = "test 2"
        self.todo_page.update_todo(0, todo_title)
        assert self.todo_page.get_todo(0).text == todo_title

    @pytest.mark.run(order=3)
    def test_check_task(self):
        self.toggle_todo(0, "completed")

    @pytest.mark.run(order=4)
    def test_uncheck_task(self):
        self.toggle_todo(0, "")

    @pytest.mark.run(order=5)
    def test_delete_task(self):
        old_todos_count = self.todo_page.todo_count()
        self.todo_page.delete_todo(0)
        updated_todos_count = self.todo_page.todo_count()
        assert updated_todos_count == old_todos_count - 1

    @pytest.mark.run(order=6)
    def test_not_adding_empty_task(self):
        old_todos_count = self.todo_page.todo_count()
        self.todo_page.add_todo("")
        updated_todos_count = self.todo_page.todo_count()

        assert updated_todos_count == old_todos_count

    def toggle_todo(self, todo_index, class_name):
        self.todo_page.toggle_todo_status(todo_index)
        assert self.todo_page.get_todo(todo_index).find_element(by=By.TAG_NAME, value='p') \
                   .get_attribute('class') == class_name
