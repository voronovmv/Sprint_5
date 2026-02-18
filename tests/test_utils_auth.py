from locators import RegisterPageLocators, LoginPageLocators, MainPageLocators
from tests.helpers import (
    generate_email,
    generate_password,
    wait_visible,
    wait_url_contains,
    safe_click
)


def register_user(driver, base_url):
    driver.get(f"{base_url}/register")

    email = generate_email()
    password = generate_password()

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Тест")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    safe_click(driver, RegisterPageLocators.REGISTER_BUTTON)

    # После регистрации ожидаем страницу логина
    wait_url_contains(driver, "/login")

    return email, password


def login_user(driver, email, password):
    # Мы должны быть на странице логина
    wait_visible(driver, LoginPageLocators.EMAIL_INPUT, 10)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    safe_click(driver, LoginPageLocators.LOGIN_BUTTON)

    # После логина ждём кнопку "Оформить заказ" на главной
    wait_visible(driver, MainPageLocators.ORDER_BUTTON, 10)
