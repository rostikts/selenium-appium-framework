import pytest
from driver_factory import driver_factory
import os

BROWSER = os.environ.get('BROWSER')
if BROWSER is None:
    BROWSER = 'chrome'


global_server_url = 'https://www.google.com'


@pytest.fixture(scope='function')
def init_driver(request):
    driver = driver_factory.DriverManager().return_driver(BROWSER)

    request.cls.driver = driver
    driver.implicitly_wait(10)

    yield driver
    driver.close()
    driver.quit()



