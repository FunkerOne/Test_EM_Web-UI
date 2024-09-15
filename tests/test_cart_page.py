import allure
from data import SignInData
from pages.home_page import HomePage
from pages.cart_page import CartPage


@allure.suite("Раздел «Корзина»")
class TestCartPage:

    @allure.title("Проверка успешного оформления заказа")
    def test_success_order(self, driver):
        home_page = HomePage(driver)
        home_page.sign_in(*SignInData.USER)
        home_page.should_be_home_page()
        home_page.click_on_random_item()
        home_page.click_on_cart()
        cart_page = CartPage(driver)
        cart_page.check_item_in_cart()
        cart_page.click_on_checkout_button()
        cart_page.fill_personal_information_form()
        cart_page.click_on_continue_button()
        cart_page.should_be_overview_form()
        cart_page.click_on_finish_button()
        result = cart_page.complete_order_screen()
        assert 'Thank you for your order!' in result
