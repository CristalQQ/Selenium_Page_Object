from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        self.driver.find_element(*MainPageLocators.LOGIN_LINK).click()
        return LoginPage(driver=self.driver, url=self.driver.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
