import pytest
from selenium.webdriver.common.by import By

from drag_and_drop import MyTest_drag
import time


@pytest.fixture
def my_selenium_fixture(request):
    my_selenium = MyTest_drag()
    yield my_selenium
    my_selenium.close()


def test_drag_and_drop(my_selenium_fixture):

    my_selenium_fixture.open_page("https://the-internet.herokuapp.com/drag_and_drop")

    column_a_locator = (By.ID, "column-a")
    column_b_locator = (By.ID, "column-b")

    initial_position_a = my_selenium_fixture.get_element_position(column_a_locator)
    initial_position_b = my_selenium_fixture.get_element_position(column_b_locator)

    my_selenium_fixture.drag_and_drop(column_a_locator, column_b_locator)

    time.sleep(2)

    final_position_a = my_selenium_fixture.get_element_position(column_a_locator)
    final_position_b = my_selenium_fixture.get_element_position(column_b_locator)

    assert initial_position_a == final_position_a
    assert initial_position_b == final_position_b
