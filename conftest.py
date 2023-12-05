import pytest
from mytest_selenium import MyTestSelenium


@pytest.fixture
def mytest_selenium():
    mytest_selenium_instance = MyTestSelenium()
    yield mytest_selenium_instance
    mytest_selenium_instance.close()
