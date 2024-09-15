from selenium.webdriver.common.by import By


class HomePageLocators:
    HEADER_LOGO = (By.CLASS_NAME, 'app_logo')
    LIST_OF_ITEMS = (By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
