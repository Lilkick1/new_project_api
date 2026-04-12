import time

from playwright.sync_api import expect


def test_add_item_and_check_in_cart_1(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """Добавление в корзину"""
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    """переход в корзину"""
    page.locator(".shopping_cart_link").click()

    """проверка, что товар есть"""
    item_name = page.locator('[data-test="inventory-item-name"]')
    assert item_name.inner_text() == "Sauce Labs Backpack"



def test_add_item_and_check_in_cart_2(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """Добавление в корзину"""
    page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    """переход в корзину"""
    page.locator(".shopping_cart_link").click()

    """проверка, что товар есть"""
    item_name_one = page.locator('[data-test="inventory-item-name"]').nth(0)
    assert item_name_one.inner_text() == "Sauce Labs Fleece Jacket"
    item_name_two = page.locator('[data-test="inventory-item-name"]').nth(1)
    assert item_name_two.inner_text() == "Sauce Labs Bolt T-Shirt"



def test_remove_item_from_cart(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """Добавление в корзину"""
    page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()

    """переход в корзину"""
    page.locator(".shopping_cart_link").click()

    """проверка наличия в корзине"""
    jacket = page.locator('.inventory_item_name', has_text='Sauce Labs Fleece Jacket')
    expect(jacket).to_be_visible()

    """Удаление товара"""
    page.locator('[data-test="remove-sauce-labs-fleece-jacket"]').click()

    """проверка, что товара больше нет в корзине"""
    expect(jacket).not_to_be_visible()



def test_remove_item_from_cart_2(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """Добавление в корзину"""
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()

    """переход в корзину"""
    page.locator(".shopping_cart_link").click()

    """проверка наличия в корзине"""
    item_1 = page.locator('.inventory_item_name', has_text='Test.allTheThings() T-Shirt (Red)')
    item_2 = page.locator('.inventory_item_name', has_text='Sauce Labs Backpack')
    expect(item_1).to_be_visible()
    expect(item_2).to_be_visible()

    """Удаление товара"""
    page.locator('[data-test="remove-test.allthethings()-t-shirt-(red)"]').click()
    page.locator('[data-test="remove-sauce-labs-backpack"]').click()

    """проверка, что товара больше нет в корзине"""
    expect(item_1).not_to_be_visible()
    expect(item_2).not_to_be_visible()

