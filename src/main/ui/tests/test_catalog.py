import time

from playwright.sync_api import expect
from src.main.ui.pages.catalog_page import CatalogPage


def test_count_catalog(auth_page):
    """Проверка количества товаров"""
    catalog = CatalogPage(auth_page)
    assert catalog.get_product_count() == 6



def test_sorted_by_name(auth_page):
    catalog = CatalogPage(auth_page)

    """сортируем от a - z"""
    catalog.sort_item('az')
    assert catalog.get_product_names() == sorted(catalog.get_product_names())

    """сортируем от z - a"""
    catalog.sort_item('za')
    assert catalog.get_product_names() == sorted(catalog.get_product_names(), reverse=True)



def test_sort_by_price(auth_page):
    catalog = CatalogPage(auth_page)
    """сортируем по возрастанию цены"""
    catalog.sort_item('lohi')
    assert catalog.get_product_names() == sorted(catalog.get_product_names())

    """сортируем по убыванию цены"""
    catalog.sort_item('hilo')
    assert catalog.get_product_names() == sorted(catalog.get_product_names(), reverse=True)




def test_add_to_cart_1(auth_page):
    catalog = CatalogPage(auth_page)
    """добавление товара в корзину"""
    button = catalog.add_to_cart('Sauce Labs Bike Light')
    expect(button).to_have_text("Remove")
    assert catalog.get_cart_count() == 1



def test_add_to_cart_2(auth_page):
    catalog = CatalogPage(auth_page)
    """добавление товара в корзину"""
    button = catalog.add_to_cart('Sauce Labs Onesie')
    expect(button).to_have_text("Remove")
    assert catalog.get_cart_count() == 1



def test_add_and_remove_onesie(auth_page):
    catalog = CatalogPage(auth_page)
    catalog.add_to_cart('Sauce Labs Bike Light')
    assert catalog.get_cart_count() == 1

    catalog.remove_from_cart('Sauce Labs Bike Light')
    assert catalog.get_cart_count() == 0



def test_product_details_onesie(auth_page):
    catalog = CatalogPage(auth_page)
    name, price, details_name, details_price = catalog.open_product_details('Sauce Labs Onesie')
    assert name == details_name
    assert price == details_price



def test_product_details_Jacket(auth_page):
    catalog = CatalogPage(auth_page)
    name, price, details_name, details_price = catalog.open_product_details('Sauce Labs Fleece Jacket')
    assert name == details_name
    assert price == details_price



def test_remove_item_from_catalog(auth_page):
    catalog = CatalogPage(auth_page)
    remove_button = catalog.remove_from_cart('Test.allTheThings() T-shirt (Red)')

    expect(remove_button).to_have_text("Add to cart")






