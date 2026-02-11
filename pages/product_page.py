# pages/product_page.py

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_button.click()

    # Метод возвращает название товара на странице
    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    # Метод возвращает цену товара на странице
    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    # Проверка, что название товара в сообщении совпадает с заголовком товара
    def should_be_correct_product_name_in_message(self):
        expected_name = self.get_product_name()
        message_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        assert expected_name == message_name, \
            f"Название товара в сообщении ({message_name}) не совпадает с названием на странице ({expected_name})"

    # Проверка, что цена корзины совпадает с ценой товара
    def should_be_correct_basket_total(self):
        expected_price = self.get_product_price()
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_MESSAGE
        ).text
        assert expected_price == basket_total, \
            f"Цена корзины ({basket_total}) не совпадает с ценой товара ({expected_price})"