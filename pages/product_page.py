from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.driver.find_element(*ProductPageLocators.THE_ADD_TO_CART_BUTTON).click()

    def check_product_added(self):
        name_book = self.driver.find_element(*ProductPageLocators.NAME_BOOK).text
        name_book_notification = self.driver.find_element(*ProductPageLocators.NAME_BOOK_NOTIFICATION).text
        price_book = self.driver.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_book_in_notification = self.driver.find_element(*ProductPageLocators.PRICE_BOOK_IN_NOTIFICATION).text

        assert name_book == name_book_notification, f"The product name '{name_book}' does not" \
                                                    f"match the name in the alert ':{name_book_notification}'"
        assert price_book == price_book_in_notification, f"The price of the book:{price_book}' does not match the basket" \
                                                         f"total in the alert '{price_book_in_notification}'"
