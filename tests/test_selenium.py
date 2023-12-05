import pytest
import time


@pytest.mark.usefixtures("mytest_selenium")
def test_click_top_menu_item(mytest_selenium):
    menu_item_text = "Men"
    mytest_selenium.click_top_menu_item(menu_item_text)
    time.sleep(2)
    assert mytest_selenium.driver.title == "Men"


@pytest.mark.usefixtures("mytest_selenium")
def test_navigate_multilevel_menu(mytest_selenium):
    menu_text = "Men"
    submenu_text = "Tops"
    mytest_selenium.navigate_multilevel_menu(menu_text, submenu_text)
    time.sleep(2)
    assert mytest_selenium.driver.title == "Jackets - Tops - Men"
