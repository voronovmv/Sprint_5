from locators import MainPageLocators
from helpers import safe_click, wait_visible
from conftest import BASE_URL


def test_constructor_tabs_sauces(driver):
    driver.get(BASE_URL)

    safe_click(driver, MainPageLocators.TAB_SAUCES)

    # Проверяем, что вкладка стала активной
    active_tab = wait_visible(driver, MainPageLocators.TAB_SAUCES_ACTIVE, 10)
    assert active_tab.is_displayed()


def test_constructor_tabs_fillings(driver):
    driver.get(BASE_URL)

    safe_click(driver, MainPageLocators.TAB_FILLINGS)

    active_tab = wait_visible(driver, MainPageLocators.TAB_FILLINGS_ACTIVE, 10)
    assert active_tab.is_displayed()


def test_constructor_tabs_buns(driver):
    driver.get(BASE_URL)

    # Чтобы булки точно переключились, сначала уходим на соусы
    safe_click(driver, MainPageLocators.TAB_SAUCES)
    wait_visible(driver, MainPageLocators.TAB_SAUCES_ACTIVE, 10)

    safe_click(driver, MainPageLocators.TAB_BUNS)

    active_tab = wait_visible(driver, MainPageLocators.TAB_BUNS_ACTIVE, 10)
    assert active_tab.is_displayed()
