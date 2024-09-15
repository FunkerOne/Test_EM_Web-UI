import allure
import random
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Отображается главная страница")
    def should_be_home_page(self):
        self.element_is_visible(HomePageLocators.HEADER_LOGO)

    @allure.step("Клик на произвольный товар")
    def click_on_random_item(self):
        random.choice(self.driver.find_elements(*HomePageLocators.LIST_OF_ITEMS)).click()

    @allure.step("Клик на корзину")
    def click_on_cart(self):
        self.click_on_element(HomePageLocators.CART_BUTTON)
