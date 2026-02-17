from locators import RegisterPageLocators, LoginPageLocators
from tests.helpers import (
    generate_email,
    generate_password,
    generate_bad_password,
    wait_visible,
    wait_url_contains,
    safe_click
)


def test_success_registration(driver, base_url):
    driver.get(f"{base_url}/register")

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Тест")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password())

    safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

    wait_url_contains(driver, "/login")
    wait_visible(driver, LoginPageLocators.LOGIN_BUTTON, 10)


def test_registration_short_password_error(driver, base_url):
    driver.get(f"{base_url}/register")

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Тест")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_bad_password())

    safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

    err = wait_visible(driver, RegisterPageLocators.PASSWORD_ERROR, 10)
    assert err.is_displayed()
