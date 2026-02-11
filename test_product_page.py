# test_product_page.py

from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    # Ссылка на новый товар
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Решаем математическую задачу в алерте
    page.solve_quiz_and_get_code()

    # Проверяем название товара
    page.should_be_correct_product_name_in_message()

    # Проверяем цену корзины
    page.should_be_correct_basket_total()