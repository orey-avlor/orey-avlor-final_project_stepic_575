from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def add_product_to_basket(self):
		link = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
		link.click()

	def should_be_message_about_item_added_to_basket(self): #Сообщение о том, что товар добавлен в корзину.
		name_of_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
		message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERT)
		assert name_of_product.text == message.text, "Product name not found in the successful addition to cart message"

	def should_be_cart_total_equals_product_total(self): #Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
	    price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
	    price_product_alert = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_ALERT)
	    assert price_product.text in price_product_alert.text, "The amount of the product and the amount in the cart do not match"