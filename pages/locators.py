from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators:
    THE_ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    NAME_BOOK = (By.XPATH, "//h1")
    NAME_BOOK_NOTIFICATION = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    PRICE_BOOK = (By.XPATH, "(//p[@class='price_color'])[1]")
    PRICE_BOOK_IN_NOTIFICATION = (By.XPATH, "(//p/strong)[2]")
