# Selenium Testing Framework for E-Commerce Website

## Overview

This project is a comprehensive automated testing framework designed for an e-commerce website. The framework leverages Selenium WebDriver for browser automation and pytest for test management, focusing on critical functionalities such as user authentication, product interactions, and basket operations.

## Project Structure

### Configuration

- **`conftest.py`**: This file sets up the test environment, configuring the browser drivers and managing command-line options for selecting the browser and language.

### Test Files

- **`test_main_page.py`**: Contains tests that validate the main page functionalities, ensuring essential elements like login links are present and operational.
- **`test_product_page.py`**: Focuses on the product page functionalities, including adding products to the basket, checking success messages, and ensuring the basket's state is as expected.

### Page Object Model (POM)

- **`pages/`**: Directory that holds the Page Object Model classes for various pages on the website. These classes encapsulate the elements and actions of each page, promoting reusable and maintainable code.

## Key Features

### Flexible Browser and Language Options

The framework allows for flexible testing across different browsers (Chrome and Firefox) and languages. These options can be specified through command-line arguments, making it adaptable to various testing scenarios and locales.

### Comprehensive Test Coverage

#### Main Page Tests (`test_main_page.py`)

- **Navigation and Visibility**:
  - `test_guest_can_go_to_login_page`: Verifies that a guest user can navigate to the login page.
  - `test_guest_should_see_login_link`: Ensures the visibility of the login link on the main page.
- **Basket Verification**:
  - `test_guest_cant_see_product_in_basket_opened_from_main_page`: Checks that the basket is empty when accessed from the main page.

#### Product Page Tests (`test_product_page.py`)

- **User Interactions**:
  - `test_user_cant_see_success_message`: Ensures no success message is displayed to a logged-in user when viewing the product page.
  - `test_user_can_add_product_to_basket`: Tests that a user can add a product to the basket and verifies the operation.
- **Guest User Scenarios**:
  - `test_guest_can_add_product_to_basket`: Ensures that a guest user can add a product to the basket, including handling promo offers.
  - `test_guest_should_see_login_link_on_product_page`: Verifies the visibility of the login link on the product page.
  - `test_guest_can_go_to_login_page_from_product_page`: Checks that a guest user can navigate to the login page from the product page.
- **Negative Scenarios**:
  - `test_guest_cant_see_success_message_after_adding_product_to_basket`: Ensures no success message is shown after adding a product to the basket.
  - `test_message_disappeared_after_adding_product_to_basket`: Confirms that the success message disappears after a short duration.
  - `test_guest_cant_see_product_in_basket_opened_from_product_page`: Checks that the basket remains empty when accessed from the product page.

## Usage Scenarios

This framework is designed for:

- **Continuous Integration/Continuous Deployment (CI/CD)**: Integrate with CI/CD pipelines to automate the testing process, ensuring code changes do not break existing functionality.
- **Cross-Browser Testing**: Validate the website’s functionality across different browsers to ensure consistent user experience.
- **Internationalization Testing**: Verify that the website works seamlessly in multiple languages, ensuring global readiness.