from pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize(
    'link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(5)
    page.should_be_message_about_item_added_to_basket()
    browser.implicitly_wait(5)
    page.should_be_cart_total_equals_product_total()
    
    #http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear - ссылка, которую использовали изначально для теста
    #http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019 - ссылка, которую использовали для проверки, что тест не упадет