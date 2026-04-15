from src.main.ui.steps.cart_steps import CartSteps
from src.main.ui.steps.catalog_steps import CatalogSteps


def test_add_item_and_check_in_cart_1(auth_page):
    cart = CartSteps(auth_page)
    catalog= CatalogSteps(auth_page)
    """Добавление в корзину"""
    catalog.add_to_cart('Sauce Labs Backpack')

    """переход в корзину"""
    cart.open_cart()

    """проверка, что товар есть"""
    cart.expect_item_in_cart('Sauce Labs Backpack')



def test_add_item_and_check_in_cart_2(auth_page):
    cart = CartSteps(auth_page)
    catalog = CatalogSteps(auth_page)
    """Добавление в корзину"""
    catalog.add_to_cart('Sauce Labs Fleece Jacket')
    catalog.add_to_cart('Sauce Labs Bolt T-Shirt')

    """переход в корзину"""
    cart.open_cart()

    """проверка, что товар есть"""
    cart.expect_item_in_cart('Sauce Labs Fleece Jacket')
    cart.expect_item_in_cart('Sauce Labs Bolt T-Shirt')



def test_remove_item_from_cart(auth_page):
    cart = CartSteps(auth_page)
    catalog = CatalogSteps(auth_page)
    """Добавление в корзину"""
    catalog.add_to_cart('Sauce Labs Fleece Jacket')

    """переход в корзину"""
    cart.open_cart()

    """проверка наличия в корзине"""
    cart.expect_item_in_cart('Sauce Labs Fleece Jacket')

    """Удаление товара"""
    cart.remove_item('Sauce Labs Fleece Jacket')

    """проверка, что товара больше нет в корзине"""
    cart.expect_item_not_in_cart('Sauce Labs Fleece Jacket')



def test_remove_item_from_cart_2(auth_page):
    cart = CartSteps(auth_page)
    catalog = CatalogSteps(auth_page)
    """Добавление в корзину"""
    catalog.add_to_cart('Sauce Labs Fleece Jacket')
    catalog.add_to_cart('Sauce Labs Bolt T-Shirt')

    """переход в корзину"""
    cart.open_cart()

    """проверка, что товар есть"""
    cart.expect_item_in_cart('Sauce Labs Fleece Jacket')
    cart.expect_item_in_cart('Sauce Labs Bolt T-Shirt')

    """Удаление товара"""
    cart.remove_item('Sauce Labs Fleece Jacket')
    cart.remove_item('Sauce Labs Bolt T-Shirt')

    """проверка, что товара больше нет в корзине"""
    cart.expect_item_not_in_cart('Sauce Labs Fleece Jacket')
    cart.expect_item_not_in_cart('Sauce Labs Bolt T-Shirt')

