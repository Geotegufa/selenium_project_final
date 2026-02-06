from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    """
    Page Object для главной страницы сайта.
    Содержит методы для работы с элементами страницы.
    """

    # Метод-проверка наличия ссылки на логин
    def should_be_login_link(self):
        """
        Проверяет, что на странице есть ссылка на логин.
        """
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"

    # Метод перехода на страницу логина
    def go_to_login_page(self):
        """
        Находит ссылку на логин и кликает по ней.
        """
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()