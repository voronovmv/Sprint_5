from locators import RegisterPageLocators, LoginPageLocators
from helpers import (
    generate_email,
    generate_password,
    generate_bad_password,
    safe_click,
    is_url_contains,
    is_visible
)
from conftest import BASE_URL


TEST_USER_NAME = "Тест"


def test_success_registration(driver):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(TEST_USER_NAME)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_password())

    safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

    assert is_url_contains(driver, "/login"), "После регистрации не открылась страница логина"
    assert is_visible(driver, LoginPageLocators.LOGIN_BUTTON), "На странице логина не видно кнопку Войти"


def test_registration_short_password_error(driver):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(TEST_USER_NAME)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(generate_bad_password())

    safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

    assert is_visible(driver, RegisterPageLocators.PASSWORD_ERROR), "Не появилась ошибка для короткого пароля"
