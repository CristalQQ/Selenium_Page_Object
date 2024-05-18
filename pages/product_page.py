from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.driver.find_element(
            *ProductPageLocators.THE_ADD_TO_CART_BUTTON).click()

    def check_product_name(self):
        assert self.is_element_present(
            *ProductPageLocators.NAME_BOOK), "product name was not found"
        assert self.is_element_present(
            *ProductPageLocators.NAME_BOOK_NOTIFICATION), "notification with title of book was not found"
        name_book = self.driver.find_element(
            *ProductPageLocators.NAME_BOOK).text
        name_book_notification = self.driver.find_element(
            *ProductPageLocators.NAME_BOOK_NOTIFICATION).text
        assert name_book == name_book_notification, f"The product name '{name_book}' does not" \
            f"match the name in the alert ':{name_book_notification}'"

    def check_product_price(self):
        assert self.is_element_present(
            *ProductPageLocators.PRICE_BOOK), "product price was not found"
        assert self.is_element_present(
            *ProductPageLocators.PRICE_BOOK_IN_NOTIFICATION), "notification with product price was not found"
        price_book = self.driver.find_element(
            *ProductPageLocators.PRICE_BOOK).text
        price_book_in_notification = self.driver.find_element(
            *ProductPageLocators.PRICE_BOOK_IN_NOTIFICATION).text
        assert price_book == price_book_in_notification, f"The price of the book:{price_book}' does not match the basket" \
            f"total in the alert '{price_book_in_notification}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_BOOK_NOTIFICATION), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_BOOK_NOTIFICATION), \
            "Success message does not disappear after a while"
