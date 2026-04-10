import time

from playwright.sync_api import expect



def test_count_catalog(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """Проверка количества товаров"""
    product = page.locator(".inventory_item")

    assert product.count() == 6



def test_sorted_by_name(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    '''Ожидание видимости селектора'''
    sort_selector = page.locator(".product_sort_container")
    expect(sort_selector).to_be_visible()

    """сортируем от a - z"""
    sort_selector.select_option('az')

    """получаем список названий товаров"""
    names = page.locator(".inventory_item_name").all_text_contents()

    """проверка, что список отсортирован по алфавиту"""
    assert names == sorted(names)



def test_sorted_by_reverse_name(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    '''Ожидание видимости селектора'''
    sort_selector = page.locator(".product_sort_container")
    expect(sort_selector).to_be_visible()

    """сортируем от a - z"""
    sort_selector.select_option('za')

    """получаем список названий товаров"""
    names = page.locator(".inventory_item_name").all_text_contents()

    """проверка, что список отсортирован по алфавиту"""
    assert names == sorted(names, reverse=True)



def test_sort_by_price(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    '''Ожидание видимости селектора'''
    sort_selector = page.locator(".product_sort_container")
    expect(sort_selector).to_be_visible()

    """сортируем по возрастанию цены"""
    sort_selector.select_option('lohi')

    """получаем список цен"""
    prices_text = page.locator(".inventory_item_price").all_text_contents()

    """преобразование в числа"""
    price = [float(p.replace('$', '')) for p in prices_text]

    """проверка сортировки"""
    assert price == sorted(price)

    """сортируем по убыванию цены"""
    sort_selector.select_option('hilo')

    """получаем список цен"""
    prices_text = page.locator(".inventory_item_price").all_text_contents()

    """преобразование в числа"""
    price = [float(p.replace('$', '')) for p in prices_text]

    """проверка сортировки"""
    assert price == sorted(price, reverse=True)



def test_add_to_cart_1(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """добавление товара в корзину"""
    product_card = page.locator(".inventory_item", has_text="Sauce Labs Bike Light")
    add_button = product_card.locator('button')
    add_button.click()

    """кнопка изменила название"""
    expect(add_button).to_have_text("Remove")

    """счетчик корзины"""
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")



def test_add_to_cart_2(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """добавление товара в корзину"""
    product_card = page.locator(".inventory_item", has_text="Sauce Labs Onesie")
    add_button = product_card.locator('button')
    add_button.click()

    """кнопка изменила название"""
    expect(add_button).to_have_text("Remove")

    """счетчик корзины"""
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    """проверки после удаления товара"""
    add_button.click()

    expect(add_button).to_have_text("Add to cart")
    expect(page.locator(".shopping_cart_badge")).not_to_be_visible()



def test_product_details_onesie(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """находим карточку товара"""
    product_card = page.locator(".inventory_item", has_text="Sauce Labs Onesie")

    """Сохраняем название и цену"""
    product_name = product_card.locator("[data-test='inventory-item-name']").inner_text()
    product_price = product_card.locator("[data-test='inventory-item-price']").inner_text()

    """переходим на страницу товара"""
    product_card.locator("[data-test='inventory-item-name']").click()

    """Проверяем название и цену"""
    detail_name = page.locator("[data-test='inventory-item-name']").inner_text()
    detail_price = page.locator("[data-test='inventory-item-price']").inner_text()

    assert detail_name == product_name, "Название не совпадает"
    assert detail_price == product_price, "Цена не совпадает"



def test_product_details_Jacket(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """находим карточку товара"""
    product_card = page.locator(".inventory_item", has_text="Sauce Labs Fleece Jacket")

    """Сохраняем название и цену"""
    product_name = product_card.locator("[data-test='inventory-item-name']").inner_text()
    product_price = product_card.locator("[data-test='inventory-item-price']").inner_text()

    """переходим на страницу товара"""
    product_card.locator("[data-test='inventory-item-name']").click()

    """Проверяем название и цену"""
    detail_name = page.locator("[data-test='inventory-item-name']").inner_text()
    detail_price = page.locator("[data-test='inventory-item-price']").inner_text()

    assert detail_name == product_name, "Название не совпадает"
    assert detail_price == product_price, "Цена не совпадает"



def test_remove_item_from_catalog(page):
    page.goto("https://www.saucedemo.com/")

    """Логин"""
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator("#login-button").click()

    """находим карточку товара"""
    product_card = page.locator(".inventory_item", has_text="Test.allTheThings() T-Shirt (Red)")

    """Добавляем товар"""
    add_button = product_card.locator("button")
    add_button.click()

    """кнопка ремув появилась"""
    expect(add_button).to_have_text("Remove")

    """удаляем товар"""
    add_button.click()
    expect(add_button).to_have_text("Add to cart")






