import time

from playwright.sync_api import expect
from src.main.ui.pages.catalog_page import CatalogPage


def test_count_catalog(auth_page):
    """Проверка количества товаров"""
    steps = CatalogPage(auth_page)
    assert steps.get_product_count() == 6



def test_sorted_by_name(auth_page):
    steps = CatalogPage(auth_page)

    """сортируем от a - z"""
    steps.sort_item('az')
    assert steps.get_product_names() == sorted(steps.get_product_names())

    """сортируем от z - a"""
    steps.sort_item('za')
    assert steps.get_product_names() == sorted(steps.get_product_names(), reverse=True)



def test_sort_by_price(auth_page):
    steps = CatalogPage(auth_page)
    """сортируем по возрастанию цены"""
    steps.sort_item('lohi')
    assert steps.get_product_names() == sorted(steps.get_product_names())

    """сортируем по убыванию цены"""
    steps.sort_item('hilo')
    assert steps.get_product_names() == sorted(steps.get_product_names(), reverse=True)



def test_add_to_cart_1(auth_page):
    steps = CatalogPage(auth_page)
    """добавление товара в корзину"""
    steps.add_to_cart('Sauce Labs Bike Light')
    assert steps.get_cart_count() == 1



def test_add_to_cart_2(auth_page):
    steps = CatalogPage(auth_page)
    """добавление товара в корзину"""
    steps.add_to_cart('Sauce Labs Onesie')
    assert steps.get_cart_count() == 1




def test_add_and_remove_onesie(auth_page):
    steps = CatalogPage(auth_page)
    steps.add_to_cart('Sauce Labs Bike Light')
    assert steps.get_cart_count() == 1

    steps.remove_from_cart('Sauce Labs Bike Light')
    assert steps.get_cart_count() == 0



def test_product_details_onesie(auth_page):
    steps = CatalogPage(auth_page)
    name, price, details_name, details_price = steps.open_product_details('Sauce Labs Onesie')
    assert name == details_name
    assert price == details_price



def test_product_details_Jacket(auth_page):
    steps = CatalogPage(auth_page)
    name, price, details_name, details_price = steps.open_product_details('Sauce Labs Fleece Jacket')
    assert name == details_name
    assert price == details_price



def test_remove_item_from_catalog(auth_page):
    steps = CatalogPage(auth_page)
    steps.add_to_cart('Test.allTheThings() T-shirt (Red)')
    remove_button = steps.remove_from_cart('Test.allTheThings() T-shirt (Red)')
    expect(remove_button).to_have_text("Add to cart")






