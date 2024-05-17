import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('offer_number', ['0', '1', '2', '3', '4', '5', '6',
                                          pytest.param(
                                              '7', marks=pytest.mark.xfail),
                                          '8', '9'])
def test_guest_can_add_product_to_basket(driver, offer_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{
        offer_number}'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_product_added()


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()


# Negative checks
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link, timeout=0)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link, timeout=0)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link, timeout=0)
    page.open()
    page.add_to_cart()
    page.success_message_should_disappear()


def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(driver, driver.current_url, timeout=0)
    basket_page.basket_should_be_empty()
    basket_page.should_be_message_about_empty_basket()
