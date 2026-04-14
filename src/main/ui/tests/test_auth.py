from playwright.sync_api import expect
from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.pages.login_page import LoginPage


def test_auth(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html", 'Ожидаем редирект на страницу каталога'

def test_invalid_auth(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    error_text = login_page.get_error_text()

    assert page.url == "https://www.saucedemo.com/", 'Ожидаем редирект на страницу каталога'
    assert 'locked out' in error_text, "Ожидаем сообщение о заблокированном пользователе"

def test_logout(auth_page):
    """разлогин"""
    catalog = CatalogPage(auth_page)
    assert catalog.get_product_count() > 0
    catalog.logout()
    expect(auth_page).to_have_url(LoginPage.URL)



def test_logout_visual_user(auth_page):
    catalog = CatalogPage(auth_page)
    assert catalog.get_product_count() > 0
    """разлогин"""
    catalog.logout()

    """проверка страницы логина"""
    expect(auth_page).to_have_url(LoginPage.URL)
    

