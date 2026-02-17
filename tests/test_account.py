from locators import MainPageLocators, AccountPageLocators
from tests.helpers import safe_click, wait_url_contains, wait_visible
from tests.test_utils_auth import register_user, login_user


def test_go_to_account_from_main(driver, base_url):
    email, password = register_user(driver, base_url)

    # Мы уже на /login
    login_user(driver, email, password)

    # Переход через кнопку в шапке
    safe_click(driver, MainPageLocators.ACCOUNT_LINK)

    wait_url_contains(driver, "/account/profile")
    wait_visible(driver, AccountPageLocators.LOGOUT_BUTTON, 10)

    assert "/account/profile" in driver.current_url


def test_go_from_account_to_constructor_by_constructor_link(driver, base_url):
    email, password = register_user(driver, base_url)
    login_user(driver, email, password)

    # Переход в ЛК через UI
    safe_click(driver, MainPageLocators.ACCOUNT_LINK)
    wait_url_contains(driver, "/account/profile")

    wait_visible(driver, AccountPageLocators.LOGOUT_BUTTON, 10)

    safe_click(driver, AccountPageLocators.CONSTRUCTOR_LINK)

    wait_visible(driver, MainPageLocators.ORDER_BUTTON, 10)


def test_go_from_account_to_constructor_by_logo(driver, base_url):
    email, password = register_user(driver, base_url)
    login_user(driver, email, password)

    # Переход в ЛК через UI
    safe_click(driver, MainPageLocators.ACCOUNT_LINK)
    wait_url_contains(driver, "/account/profile")

    safe_click(driver, MainPageLocators.LOGO)

    wait_visible(driver, MainPageLocators.ORDER_BUTTON, 10)


def test_logout_from_account(driver, base_url):
    email, password = register_user(driver, base_url)
    login_user(driver, email, password)

    # Переход в ЛК через UI
    safe_click(driver, MainPageLocators.ACCOUNT_LINK)
    wait_url_contains(driver, "/account/profile")

    safe_click(driver, AccountPageLocators.LOGOUT_BUTTON)

    wait_url_contains(driver, "/login")
