from playwright.sync_api import Page
from src.main.ui.utils.constants import Urls


class LoginPage:

    """Лакаторы"""
    def __init__(self, page: Page):
        self.page = page
        self.user_name_input = page.get_by_placeholder("Username")
        self.user_password_input = page.get_by_placeholder("Password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    """Методы"""
    def open(self):
        self.page.goto(Urls.BASE)

    def login(self, username: str, password: str):
        self.user_name_input.fill(username)
        self.user_password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        return self.error_message.inner_text()
