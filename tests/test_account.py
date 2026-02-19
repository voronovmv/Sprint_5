from locators import MainPageLocators, AccountPageLocators
from helpers import safe_click, is_url_contains, is_visible
from utils_auth import register_user, login_user
from conftest import BASE_URL


def test_go_to_account_from_main(driver):
    email, password = register_user(driver, BASE_URL)

    # Мы уже на /login
    login_user(driver, email, password)

    safe_click(driver, MainPageLocators.ACCOUNT_LINK)

    assert is_url_contains(driver, "/account/profile"), "Не перешли в профиль"
    assert is_visible(driver, AccountPageLocators.LOGOUT_BUTTON), "Не видно кнопку Выход в профиле"


def test_go_from_account_to_constructor_by_constructor_link(driver):
    email, password = register_user(driver, BASE_URL)
    login_user(driver, email, password)

    safe_click(driver, MainPageLocators.ACCOUNT_LINK)

    assert is_url_contains(driver, "/account/profile"), "Не перешли в профиль"
    assert is_visible(driver, AccountPageLocators.LOGOUT_BUTTON), "Не видно кнопку Выход в профиле"

    safe_click(driver, AccountPageLocators.CONSTRUCTOR_LINK)

    assert is_visible(driver, MainPageLocators.ORDER_BUTTON), "Не вернулись в конструктор, кнопка Оформить заказ не видна"


def test_go_from_account_to_constructor_by_logo(driver):
    email, password = register_user(driver, BASE_URL)
    login_user(driver, email, password)

    safe_click(driver, MainPageLocators.ACCOUNT_LINK)
    assert is_url_contains(driver, "/account/profile"), "Не перешли в профиль"

    safe_click(driver, MainPageLocators.LOGO)

    assert is_visible(driver, MainPageLocators.ORDER_BUTTON), "Не вернулись на главную по клику на логотип"


def test_logout_from_account(driver):
    email, password = register_user(driver, BASE_URL)
    login_user(driver, email, password)

    safe_click(driver, MainPageLocators.ACCOUNT_LINK)
    assert is_url_contains(driver, "/account/profile"), "Не перешли в профиль"

    safe_click(driver, AccountPageLocators.LOGOUT_BUTTON)

    assert is_url_contains(driver, "/login"), "После выхода не открылась страница логина"
