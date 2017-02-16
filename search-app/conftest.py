import pytest
import os
from appium import webdriver


@pytest.yield_fixture(scope='function', autouse=True)
def session_driver(request):
    capabilities = {
        'platformName': 'iOS',
        'platformVersion': '10.2',
        'deviceName': 'iPhone 6',
        'app': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app/Search.swift.app'),
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    yield driver
    driver.quit()
