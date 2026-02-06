import pytest
from pages.login_page import LoginPage

# Ссылка на страницу логина
LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"

@pytest.mark.login
def test_guest_should_see_login_page(browser):
    """Тест проверяет, что гость на странице логина видит URL и обе формы"""
    # Открываем страницу логина
    login_page = LoginPage(browser, LOGIN_PAGE_LINK)
    login_page.open()
    
    # Проверяем URL
    login_page.should_be_login_url()
    
    # Проверяем форму логина
    login_page.should_be_login_form()
    
    # Проверяем форму регистрации
    login_page.should_be_register_form() 
