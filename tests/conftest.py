import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


BASE_URL = "https://stellarburgers.education-services.ru"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def driver():
    options = ChromeOptions()
    options.add_argument("--window-size=1280,900")

    drv = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    yield drv
    drv.quit()
