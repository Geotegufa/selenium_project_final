from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    """
    Page Object для главной страницы сайта.
    Содержит методы для работы с элементами страницы.
    """

    # Метод-проверка наличия ссылки на логин
    def should_be_login_link(self, red_test=False):
        """
        Проверяет, что на странице есть ссылка на логин.
        red_test=True -> использовать намеренно неправильный селектор
        """
        if red_test:
            # Красный тест: неправильный селектор
            assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), \
                "Login link is not presented"
        else:
            # Зеленый тест: правильный селектор
            assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), \
                "Login link is not presented"

    # Метод перехода на страницу логина
    def go_to_login_page(self):
        """
        Находит ссылку на логин и кликает по ней.
        """
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()