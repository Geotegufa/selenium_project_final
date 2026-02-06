from selenium.webdriver.common.by import By

# Локаторы для главной страницы
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# Локаторы для страницы логина
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")