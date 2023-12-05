from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MyTestSelenium:
    def __init__(self):
        self.base_url = "https://magento.softwaretestingboard.com"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def click_top_menu_item(self, item_text):
        self.driver.get(self.base_url)
        top_menu = self.driver.find_element(By.CLASS_NAME, "navigation")
        menu_items = top_menu.find_elements(By.TAG_NAME, "li")

        for item in menu_items:
            if item.text == item_text:
                item.click()
                break

    def navigate_multilevel_menu(self, menu_text, submenu_text):
        self.driver.get(self.base_url)
        menu = self.driver.find_element(By.PARTIAL_LINK_TEXT, menu_text)
        menu.click()

        submenu = self.driver.find_element(By.PARTIAL_LINK_TEXT, submenu_text)
        actions = ActionChains(self.driver)
        actions.move_to_element(submenu).perform()

        submenu_item = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Jackets')
        actions.click(submenu_item).perform()

    def close(self):
        self.driver.quit()


