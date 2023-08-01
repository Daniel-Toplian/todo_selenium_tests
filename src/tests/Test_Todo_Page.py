import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from src.pages.Todo_Page import Todo_Page

driver = None


@pytest.fixture(autouse=True, scope="class")
def setup_module(request):
    global driver

    url = os.environ.get("TODO_URL")

    if url is None:
        url = "http://localhost:3000/"

    chrome_options = Options()

    options = [
        "--headless",
        "--disable-gpu",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]

    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get(url)

    todo_page = Todo_Page(driver)
    request.cls.todo_page = todo_page

    yield todo_page


def teardown_module():
    driver.quit()


class Test_Todo_Page:

    def test_add_task(self):
        old_todos_count = self.todo_page.todo_count()
        self.todo_page.add_todo("test 1")
        updated_todos_count = self.todo_page.todo_count()
        assert updated_todos_count == old_todos_count + 1, "Couldn't add new todo - test failed"

    def test_update_task(self):
        todo_title = "test 2"
        self.todo_page.update_todo(0, todo_title)
        assert self.todo_page.get_todo(0).text == todo_title, "Couldn't update todo - test failed"

    def test_check_task(self):
        self.toggle_todo(0, "completed", "Couldn't check todo - test failed")

    def test_uncheck_task(self):
        self.toggle_todo(0, "", "Couldn't uncheck todo - test failed")

    def test_delete_task(self):
        old_todos_count = self.todo_page.todo_count()
        self.todo_page.delete_todo(0)
        updated_todos_count = self.todo_page.todo_count()
        assert updated_todos_count == old_todos_count - 1, "Couldn't Delete todo - test failed"

    def test_not_adding_empty_task(self):
        old_todos_count = self.todo_page.todo_count()
        self.todo_page.add_todo("")
        updated_todos_count = self.todo_page.todo_count()

        assert updated_todos_count == old_todos_count, "An empty todo was created - test failed"

    def toggle_todo(self, todo_index, class_name, fail_message):
        self.todo_page.toggle_todo_status(todo_index)
        assert self.todo_page.get_todo(todo_index).find_element(by=By.TAG_NAME, value='p') \
                   .get_attribute('class') == class_name, fail_message
