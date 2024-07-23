from pages.base_page import BasePage
from pages.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def select_role_supplier(self):
        self.browser.find_element(*RegistrationPageLocators.SELECT_ROLE_SUPPLIER_BUTTON).click()

    def select_role_seller(self):
        self.browser.find_element(*RegistrationPageLocators.SELECT_ROLE_SELLER_BUTTON).click()

    def enter_email(self, email):
        reg_email = self.browser.find_element(*RegistrationPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)

    def enter_password(self, password):
        reg_pass = self.browser.find_element(*RegistrationPageLocators.REGISTER_PASS)
        reg_pass.send_keys(password)

    def submit_create_account_button(self):
        reg_button = self.browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        reg_button.submit()