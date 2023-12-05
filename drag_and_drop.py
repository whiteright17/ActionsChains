from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MyTest_drag:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_page(self, url):
        self.driver.get(url)

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def get_element_position(self, locator):
        element = self.driver.find_element(*locator)
        return element.location

    def close(self):
        self.driver.quit()
