from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), "basket is empty"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_MESSAGE), "message 'trash is empty' is missing"
