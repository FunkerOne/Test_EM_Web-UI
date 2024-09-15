import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    _USER_NAME_FIELD = (By.ID, 'user-name')
    _PASSWORD_FIELD = (By.ID, 'password')
    _SIGN_IN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть по элементу")
    def click_on_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, element):
        return self.driver.find_element(*element).text

    @allure.step("Элемент представлен")
    def element_is_visible(self, element):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(element))

    @allure.step("Вставить текст")
    def paste_text_into_element(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    @allure.step("Авторизация пользователя")
    def sign_in(self, user_name, password):
        self.driver.find_element(*self._USER_NAME_FIELD).send_keys(user_name)
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self._SIGN_IN_BUTTON).click()
