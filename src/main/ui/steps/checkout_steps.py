import allure
from playwright.sync_api import Page, expect
from src.main.ui.pages.checkout_page import CheckoutPage



class CheckoutSteps:
    def __init__(self, page: Page):
        self.page = page
        self.checkout = CheckoutPage(self.page)

    @allure.step("Начинаем Checkout: {first_name}, {last_name}, {zip}")
    def checkout(self, first_name: str, last_name: str, zip: int):
        self.checkout.start_checkout(first_name, last_name, zip)
        return self

    @allure.step("Завершаем Checkout")
    def finish_checkout(self):
        self.checkout.finish_checkout()
        return self

    @allure.step("Получаем текст ошибки Checkout")
    def get_error_text(self) -> str:
        return self.checkout.get_error_text()

    @allure.step("Получаем сумму товаров после continue")
    def get_item_total_after_continue(self) -> float:
        return self.checkout.get_item_total_after_continue()

