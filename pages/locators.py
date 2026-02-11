# pages/locators.py

from selenium.webdriver.common.by import By


class ProductPageLocators:
    # Кнопка "Добавить в корзину"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Название товара на странице
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")

    # Цена товара на странице
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")

    # Сообщение об успешном добавлении товара
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")

    # Название товара в сообщении
    SUCCESS_MESSAGE_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "#messages .alert-success strong"
    )

    # Сообщение со стоимостью корзины
    BASKET_TOTAL_MESSAGE = (
        By.CSS_SELECTOR,
        "#messages .alert-info strong"
    )