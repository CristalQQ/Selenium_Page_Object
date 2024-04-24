from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.driver.current_url, "The substring 'login' is missing in the current url"

    def should_be_login_form(self):
        assert self.driver.find_element(*LoginPageLocators.LOGIN_FORM), "The login form was not found"

    def should_be_register_form(self):
        assert self.driver.find_element(*LoginPageLocators.REGISTER_FORM), "The registration form was not found"