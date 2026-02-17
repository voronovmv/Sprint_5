import random
import string

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_email():
    # Генерим почту вида maksim_voronov_41_123abc@yandex.ru
    digits = "".join(random.choice(string.digits) for _ in range(3))
    letters = "".join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"maksim_voronov_41_{digits}{letters}@yandex.ru"


def generate_password(length=10):
    # Пароль минимум 6 символов, делаем 10 чтобы не попадать в граничные значения
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def generate_bad_password():
    # Короткий пароль для проверки ошибки
    return "12345"


def wait_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_url_contains(driver, part, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(part)
    )


def safe_click(driver, locator, timeout=10):
    # Клик с подстраховкой. Иногда Selenium ловит перехват клика или элемент вне видимой области.
    element = wait_clickable(driver, locator, timeout)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)
