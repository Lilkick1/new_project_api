import allure
from playwright.sync_api import Page, expect
from src.main.ui.pages.checkout_page import CheckoutPage
from src.main.ui.pages.cart_page import CartPage


class CartSteps:
    def __init__(self, page: Page):
        self.page = page
        self.cart = CartPage(self.page)

    @allure.step('Открываем корзину')
    def open_cart(self):
        self.cart.open_cart()
        return self

    @allure.step("Проверяем, что товар {product_name} есть в корзине")
    def expect_item_in_cart(self, product_name: str):
        self.cart.expect_item_in_cart(product_name)
        return self

    @allure.step("Проверяем, что товара {product_name} нет в корзине")
    def expect_item_not_in_cart(self, product_name: str):
        self.cart.expect_item_not_in_cart(product_name)
        return self

    @allure.step("Удаляем товар {product_name} из корзины")
    def remove_item(self, product_name: str):
        self.cart.remove_item(product_name)
        return self

    @allure.step("Переходим к Checkout")
    def checkout(self):
        self.cart.checkout()
        return self

    @allure.step("Получаем список названий товаров в корзине")
    def get_item_names(self) -> list[str]:
        return self.cart.get_item_names()

    @allure.step("Получаем общую сумму товаров в корзине")
    def get_item_price(self) -> float:
        return self.cart.get_item_total_price()



