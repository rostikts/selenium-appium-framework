import pytest


@pytest.mark.usefixtures('init_driver')
class TestBase:

    def visit_page(self, url):
        self.driver.get(url)