from locators import RegisterPageLocators, LoginPageLocators, MainPageLocators
from helpers import (
    generate_email,
    generate_password,
    safe_click,
    is_url_contains,
    is_visible
)


TEST_USER_NAME = "Тест"


def register_user(driver, base_url):
    driver.get(f"{base_url}/register")

    email = generate_email()
    password = generate_password()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(TEST_USER_NAME)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

    assert is_url_contains(driver, "/login"), "После регистрации не открылась страница логина"
    return email, password


def login_user(driver, email, password):
    assert is_visible(driver, LoginPageLocators.EMAIL_INPUT), "Не видно поле Email на странице логина"

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    safe_click(driver, LoginPageLocators.LOGIN_BUTTON)

    assert is_visible(driver, MainPageLocators.ORDER_BUTTON), "После логина не появилась кнопка Оформить заказ"
