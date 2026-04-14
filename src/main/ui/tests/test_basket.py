import time
from src.main.ui.pages.cart_page import CartPage
from src.main.ui.pages.catalog_page import CatalogPage
from playwright.sync_api import expect


def test_add_item_and_check_in_cart_1(auth_page):
    cart_page = CartPage(auth_page)
    catalog_page = CatalogPage(auth_page)
    """Добавление в корзину"""
    catalog_page.add_to_cart('Sauce Labs Backpack')

    """переход в корзину"""
    cart_page.open_cart()

    """проверка, что товар есть"""
    cart_page.expect_item_in_cart('Sauce Labs Backpack')



def test_add_item_and_check_in_cart_2(auth_page):
    cart_page = CartPage(auth_page)
    catalog_page = CatalogPage(auth_page)
    """Добавление в корзину"""
    catalog_page.add_to_cart('Sauce Labs Fleece Jacket')
    catalog_page.add_to_cart('Sauce Labs Bolt T-Shirt')

    """переход в корзину"""
    cart_page.open_cart()

    """проверка, что товар есть"""
    cart_page.expect_item_in_cart('Sauce Labs Fleece Jacket')
    cart_page.expect_item_in_cart('Sauce Labs Bolt T-Shirt')



def test_remove_item_from_cart(auth_page):
    cart_page = CartPage(auth_page)
    catalog_page = CatalogPage(auth_page)
    """Добавление в корзину"""
    catalog_page.add_to_cart('Sauce Labs Fleece Jacket')

    """переход в корзину"""
    cart_page.open_cart()

    """проверка наличия в корзине"""
    cart_page.expect_item_in_cart('Sauce Labs Fleece Jacket')

    """Удаление товара"""
    cart_page.remove_item('Sauce Labs Fleece Jacket')

    """проверка, что товара больше нет в корзине"""
    cart_page.expect_item_not_in_card('Sauce Labs Fleece Jacket')



def test_remove_item_from_cart_2(auth_page):
    cart_page = CartPage(auth_page)
    catalog_page = CatalogPage(auth_page)
    """Добавление в корзину"""
    catalog_page.add_to_cart('Sauce Labs Fleece Jacket')
    catalog_page.add_to_cart('Sauce Labs Bolt T-Shirt')

    """переход в корзину"""
    cart_page.open_cart()

    """проверка, что товар есть"""
    cart_page.expect_item_in_cart('Sauce Labs Fleece Jacket')
    cart_page.expect_item_in_cart('Sauce Labs Bolt T-Shirt')

    """Удаление товара"""
    cart_page.remove_item('Sauce Labs Fleece Jacket')
    cart_page.remove_item('Sauce Labs Bolt T-Shirt')

    """проверка, что товара больше нет в корзине"""
    cart_page.expect_item_not_in_card('Sauce Labs Fleece Jacket')
    cart_page.expect_item_not_in_card('Sauce Labs Bolt T-Shirt')

