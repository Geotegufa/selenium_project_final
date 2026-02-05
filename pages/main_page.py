# Импортируем базовый класс BasePage, от которого будем наследоваться
from .base_page import BasePage

# Импортируем By, чтобы искать элементы на странице через CSS, ID и т.д.
from selenium.webdriver.common.by import By

# Создаём класс MainPage, который наследует BasePage
# Наследование означает, что MainPage получает все методы и атрибуты BasePage
class MainPage(BasePage):

    # Метод для перехода на страницу логина
    # self — это ссылка на текущий объект MainPage, через неё обращаемся к браузеру и другим методам
    def go_to_login_page(self):
        # Находим ссылку на логин по CSS-селектору
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # Кликаем по найденной ссылке, чтобы перейти на страницу логина
        login_link.click()