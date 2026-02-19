import random
import string

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def generate_email():
    # Почта вида maksim_voronov_41_123abc@yandex.ru
    digits = "".join(random.choice(string.digits) for _ in range(3))
    letters = "".join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"maksim_voronov_41_{digits}{letters}@yandex.ru"


def generate_password(length=10):
    # Пароль минимум 6 символов, делаем с запасом
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def generate_bad_password():
    # Короткий пароль для проверки ошибки
    return "12345"


def wait_clickable(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def safe_click(driver, locator, timeout=10):
    element = wait_clickable(driver, locator, timeout)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)


def is_url_contains(driver, part, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.url_contains(part))
        return True
    except TimeoutException:
        return False


def is_visible(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False


def is_tab_active(driver, tab_locator, timeout=10):
    try:
        def _active(_driver):
            el = _driver.find_element(*tab_locator)
            cls = el.get_attribute("class") or ""
            return "tab_tab_type_current" in cls

        WebDriverWait(driver, timeout).until(_active)
        return True
    except Exception:
        return False


def wait_visible(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
