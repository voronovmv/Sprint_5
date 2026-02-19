from locators import (
    MainPageLocators,
    RegisterPageLocators,
    ForgotPasswordLocators
)
from helpers import safe_click, is_url_contains, is_visible
from utils_auth import register_user, login_user
from conftest import BASE_URL


def test_login_from_main_page_button(driver):
    email, password = register_user(driver, BASE_URL)

    driver.get(BASE_URL)
    safe_click(driver, MainPageLocators.LOGIN_BUTTON_MAIN)

    assert is_url_contains(driver, "/login"), "Не открылась страница логина"

    login_user(driver, email, password)

    assert is_visible(driver, MainPageLocators.ORDER_BUTTON), "Нет кнопки Оформить заказ после логина"


def test_login_via_account_button(driver):
    email, password = register_user(driver, BASE_URL)

    driver.get(BASE_URL)
    safe_click(driver, MainPageLocators.ACCOUNT_LINK)

    assert is_url_contains(driver, "/login"), "Не открылась страница логина"

    login_user(driver, email, password)

    assert is_visible(driver, MainPageLocators.ORDER_BUTTON), "Нет кнопки Оформить заказ после логина"


def test_login_from_register_form_link(driver):
    email, password = register_user(driver, BASE_URL)

    driver.get(f"{BASE_URL}/register")
    safe_click(driver, RegisterPageLocators.LOGIN_LINK)

    assert is_url_contains(driver, "/login"), "Не открылась страница логина"

    login_user(driver, email, password)

    assert is_visible(driver, MainPageLocators.ORDER_BUTTON), "Нет кнопки Оформить заказ после логина"


def test_login_from_forgot_password_form_link(driver):
    email, password = register_user(driver, BASE_URL)

    driver.get(f"{BASE_URL}/forgot-password")
    safe_click(driver, ForgotPasswordLocators.LOGIN_LINK)

    assert is_url_contains(driver, "/login"), "Не открылась страница логина"

    login_user(driver, email, password)

    assert is_visible(driver, MainPageLocators.ORDER_BUTTON), "Нет кнопки Оформить заказ после логина"
