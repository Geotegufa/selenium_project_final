from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")