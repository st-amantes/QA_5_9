import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def driver_setting():
    browser.driver.set_window_size(1920, 1080)
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.fullscreen_window()
    browser.driver.set_script_timeout(2)
    yield

    browser.quit()
