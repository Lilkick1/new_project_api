from playwright.sync_api import expect
from src.main.ui.pages.cart_page import CartPage
from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.pages.checkout_page import CheckoutPage


def test_remove_item_from_cart_2(auth_page):
    catalog_page = CatalogPage(auth_page)
    checkout_page = CheckoutPage(auth_page)
    cart_page = CartPage(auth_page)
    """Добавление в корзину"""
    catalog_page.add_to_cart('Sauce Labs Bike Light')
    catalog_page.add_to_cart('Test.allTheThings() T-Shirt (Red)')

    """переход в корзину"""
    cart_page.open_cart()

    """проверка наличия в корзине"""
    cart_page.expect_item_in_cart('Sauce Labs Bike Light')
    cart_page.expect_item_in_cart('Test.allTheThings() T-Shirt (Red)')
    total_price = cart_page.get_item_total_price()

    """переходим к оплате"""
    cart_page.checkout()
    checkout_page.start_checkout('Ivan', 'Ivanov', '1234')

    """проверка цены"""
    assert total_price == checkout_page.get_item_total()

    """окончание заказа"""
    checkout_page.finish_checkout()
    assert checkout_page.get_success_message() == 'Thank you for your order!'



