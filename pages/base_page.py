from selenium.common.exceptions import NoSuchElementException  # импорт исключения

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # Неявное ожидание элементов
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открывает страницу по URL
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Проверяет, что элемент присутствует на странице.
        Возвращает True, если элемент найден, иначе False.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True