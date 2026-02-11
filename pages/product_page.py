from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def add_product_to_basket(self):
        """Нажимаем кнопку 'Добавить в корзину'"""
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        """Получаем название товара на странице"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_basket_total(self):
        """Получаем стоимость корзины"""
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text

    def should_be_correct_product_name_in_message(self):
        """Проверяем, что название товара совпадает с сообщением после добавления в корзину"""
        expected_name = self.get_product_name()
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert expected_name == message_name, \
            f"Название товара в сообщении ({message_name}) не совпадает с названием на странице ({expected_name})"

    def should_be_correct_basket_total(self):
        """Проверяем, что цена корзины совпадает с ценой товара"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.get_basket_total()
        assert product_price in basket_total, \
            f"Цена корзины ({basket_total}) не совпадает с ценой товара ({product_price})"