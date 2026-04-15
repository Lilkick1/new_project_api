from playwright.sync_api import expect
from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.pages.login_page import LoginPage
from src.main.ui.steps.login_steps import LoginSteps
from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.utils.constants import Urls


def test_auth(page):
    steps = LoginSteps(page)
    catalog_page = CatalogPage(page)

    steps.open_login_page().login("standard_user", "secret_sauce")

    assert catalog_page.get_product_count() > 0, "Ожидаем товары на странице каталога"

def test_invalid_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user", "secret_sauce")

    error_text = steps.login_page.get_error_text()

    assert 'locked out' in error_text, "Ожидаем сообщение о заблокированном пользователе"

def test_logout(auth_page):
    steps = CatalogSteps(auth_page)
    """разлогин"""
    assert steps.get_product_count() > 0
    steps.logout()
    expect(auth_page).to_have_url(Urls.BASE)



def test_logout_visual_user(auth_page):
    steps = CatalogSteps(auth_page)
    assert steps.get_product_count() > 0
    """разлогин"""
    steps.logout()

    """проверка страницы логина"""
    expect(auth_page).to_have_url(Urls.BASE)
    

