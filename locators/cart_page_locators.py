from selenium.webdriver.common.by import By


class CartPageLocators:
    ITEM_IN_CART = (By.CLASS_NAME, 'cart_item_label')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    ZIP_CODE_FIELD = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    OVERVIEW_SCREEN = (By.XPATH, '//span[text()="Checkout: Overview"]')
    FINISH_BUTTON = (By.ID, 'finish')
    COMPLETE_SCREEN = (By.XPATH, '//h2[text()="Thank you for your order!"]')
