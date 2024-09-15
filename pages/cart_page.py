import allure
from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators
from helpers import PersonalInformationData


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Товар в корзине")
    def check_item_in_cart(self):
        self.element_is_visible(CartPageLocators.ITEM_IN_CART)

    @allure.step("Клик на кнопку Checkout")
    def click_on_checkout_button(self):
        self.click_on_element(CartPageLocators.CHECKOUT_BUTTON)

    @allure.step("Заполнить персональные данные")
    def fill_personal_information_form(self):
        self.paste_text_into_element(CartPageLocators.FIRST_NAME_FIELD, PersonalInformationData.first_name_gen())
        self.paste_text_into_element(CartPageLocators.LAST_NAME_FIELD, PersonalInformationData.last_name_gen())
        self.paste_text_into_element(CartPageLocators.ZIP_CODE_FIELD, PersonalInformationData.zip_code_gen())

    @allure.step("Клик на кнопку Continue")
    def click_on_continue_button(self):
        self.click_on_element(CartPageLocators.CONTINUE_BUTTON)

    @allure.step("На странице Overview")
    def should_be_overview_form(self):
        self.element_is_visible(CartPageLocators.OVERVIEW_SCREEN)

    @allure.step("Клик на кнопку Finish")
    def click_on_finish_button(self):
        self.click_on_element(CartPageLocators.FINISH_BUTTON)

    @allure.step("На странице успешного оформления заказа")
    def complete_order_screen(self):
        return self.get_text_from_element(CartPageLocators.COMPLETE_SCREEN)
