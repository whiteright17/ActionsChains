import pytest

from drag_and_drop import MyTest_drag
from mytest_selenium import MyTestSelenium


@pytest.fixture
def mytest_selenium():
    mytest_selenium_instance = MyTestSelenium()
    yield mytest_selenium_instance
    mytest_selenium_instance.close()


@pytest.fixture
def drag_and_drop():
    mytest_selenium_instance = MyTest_drag()
    yield mytest_selenium_instance
    mytest_selenium_instance.close()
