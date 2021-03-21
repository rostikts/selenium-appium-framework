import pytest
from conftest import global_server_url
from tests.test_base import TestBase
from page_objects.base_page import BasePage


@pytest.mark.usefixtures('init_driver')
class TestFirst(TestBase):

    def test_one(self):
        self.google = BasePage(self.driver)
        self.visit_page(global_server_url)
        self.google.enter_query()
        assert True is True