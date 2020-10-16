from py.xml import html
import pytest
from pages.login_page import LoginPage
from stored_values.common_values import base_url

'''
To run tests on Chrome or Firefox:

        pytest tests/test_login_page.py --driver {Browser} --html=output/report.html -v

NOTE: If the driver path isn't set as a system variable, add it to the command line " --driver-path <path to driver> "
'''

@pytest.fixture()
def selenium(selenium):
    selenium.set_window_size(1280, 1000)
    return selenium

@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = False
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("window-size=1920,1080")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--remote-debugin-port=9222")
    return firefox_options

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.headless = False
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugin-port=9222")
    return chrome_options

# Add fixtures for pages
@pytest.fixture()
def LoginPageObject(selenium):
    page = LoginPage(selenium, root_uri=base_url)
    return page