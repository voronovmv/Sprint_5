from locators import (
    MainPageLocators,
    LoginPageLocators,
    RegisterPageLocators,
    ForgotPasswordLocators
)
from tests.helpers import wait_visible, safe_click, wait_url_contains
from tests.test_utils_auth import register_user, login_user


def test_login_from_main_page_button(driver, base_url):
    email, password = register_user(driver, base_url)

    driver.get(base_url)
    safe_click(driver, MainPageLocators.LOGIN_BUTTON_MAIN)

    wait_url_contains(driver, "/login")

    login_user(driver, email, password)

    wait_visible(driver, MainPageLocators.ORDER_BUTTON, 10)
    assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()


def test_login_via_account_button(driver, base_url):
    email, password = register_user(driver, base_url)

    driver.get(base_url)
    safe_click(driver, MainPageLocators.ACCOUNT_LINK)

    wait_url_contains(driver, "/login")

    login_user(driver, email, password)

    wait_visible(driver, MainPageLocators.ORDER_BUTTON, 10)
    assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()


def test_login_from_register_form_link(driver, base_url):
    email, password = register_user(driver, base_url)

    driver.get(f"{base_url}/register")
    safe_click(driver, RegisterPageLocators.LOGIN_LINK)

    wait_url_contains(driver, "/login")

    login_user(driver, email, password)

    wait_visible(driver, MainPageLocators.ORDER_BUTTON, 10)
    assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()


def test_login_from_forgot_password_form_link(driver, base_url):
    email, password = register_user(driver, base_url)

    driver.get(f"{base_url}/forgot-password")
    safe_click(driver, ForgotPasswordLocators.LOGIN_LINK)

    wait_url_contains(driver, "/login")

    login_user(driver, email, password)

    wait_visible(driver, MainPageLocators.ORDER_BUTTON, 10)
    assert driver.find_element(*MainPageLocators.ORDER_BUTTON).is_displayed()
