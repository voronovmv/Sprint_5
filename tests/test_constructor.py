from locators import MainPageLocators
from tests.helpers import safe_click, wait_visible


def test_constructor_tabs_sauces(driver, base_url):
    driver.get(base_url)

    safe_click(driver, MainPageLocators.TAB_SAUCES)
    # проверяем факт перехода: заголовок секции виден
    wait_visible(driver, MainPageLocators.SECTION_SAUCES, 10)

    assert driver.find_element(*MainPageLocators.SECTION_SAUCES).is_displayed()


def test_constructor_tabs_fillings(driver, base_url):
    driver.get(base_url)

    safe_click(driver, MainPageLocators.TAB_FILLINGS)
    wait_visible(driver, MainPageLocators.SECTION_FILLINGS, 10)

    assert driver.find_element(*MainPageLocators.SECTION_FILLINGS).is_displayed()


def test_constructor_tabs_buns(driver, base_url):
    driver.get(base_url)

    # Булки обычно активны по умолчанию, но чтобы избежать перехвата клика:
    # сначала уйдём на соусы, потом вернёмся на булки
    safe_click(driver, MainPageLocators.TAB_SAUCES)
    wait_visible(driver, MainPageLocators.SECTION_SAUCES, 10)

    safe_click(driver, MainPageLocators.TAB_BUNS)
    wait_visible(driver, MainPageLocators.SECTION_BUNS, 10)

    assert driver.find_element(*MainPageLocators.SECTION_BUNS).is_displayed()
