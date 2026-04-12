from playwright.sync_api import expect


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

    """проверка цены товаров"""
    item_1_price = page.locator('[data-test="inventory-item-price"]').nth(0).inner_text()
    item_2_price = page.locator('[data-test="inventory-item-price"]').nth(1).inner_text()
    full_price = float(item_2_price.replace("$", "")) + float(item_1_price.replace("$", ""))

    """переходим к оплате"""
    page.locator("#checkout").click()
    page.locator("#first-name").fill('lol')
    page.locator("#last-name").fill('kek')
    page.locator("#postal-code").fill('1337')
    page.locator("#continue").click()

    """проверка цены"""
    item_total_price = page.locator('[data-test="subtotal-label"]').inner_text().replace('Item total: $', '')
    tax = page.locator('[data-test="tax-label"]').inner_text().replace('Tax: $', '')
    total = page.locator('[data-test="total-label"]').inner_text().replace('Total: $', '')
    assert float(item_total_price) == full_price
    assert float(total) == float(tax) + full_price

    """окончание заказа"""
    page.locator('#finish').click()
    expect(page.locator('[data-test="complete-header"]')).to_have_text('Thank you for your order!')



