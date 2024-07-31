from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REG1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REG2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    ALERT = (By.ID, "messages")
    NAME_PRODUCT = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1 ')
    NAME_PRODUCT_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_PRODUCT = (By.CLASS_NAME, "price_color")
    PRICE_PRODUCT_IN_ALERT = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')




    

