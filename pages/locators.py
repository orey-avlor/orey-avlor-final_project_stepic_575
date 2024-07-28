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

    