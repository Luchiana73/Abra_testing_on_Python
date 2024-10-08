from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    LOGIN_PASS = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


class RegistrationPageLocators:
    SELECT_ROLE_SUPPLIER_BUTTON = (By.XPATH, "//button[text()=\"I'm here to sell\"]")
    SELECT_ROLE_SELLER_BUTTON = (By.XPATH, "//button[text()=\"I'm here to buy\"]")
    REGISTER_EMAIL = LoginPageLocators.LOGIN_EMAIL
    REGISTER_PASS = LoginPageLocators.LOGIN_PASS
    REGISTER_BUTTON = LoginPageLocators.LOGIN_BUTTON
    LINK_SENT_MESSAGE = (By.XPATH, '//div[text()="A link for sign up has been sent to your email address."]')


class ConfirmEmailPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, 'a.ConfirmEmailPage_link__kO5Ku[href="/login"]')


class SetupAccountPageLocators:
    FIRST_NAME_FIELD = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'lastName')
    PHONE_COUNTRY_DROPDOWN = (By.CLASS_NAME, 'flag-dropdown.PhoneNumberInput_phone_flag__Npodl')
    COUNTRY_LOCATOR_TURKEY = (By.CSS_SELECTOR, 'li.country[data-country-code="tr"]')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'input.PhoneNumberInput_phone__M4NhG')
    SUBMIT_FIRST_STEP_BUTTON = (By.CSS_SELECTOR, 'button.SupplierPersonalInfoForm_submit_btn__8BNcQ')
    UPLOAD_LOGO_INPUT = (By.ID, 'profileLogo')
    SHOP_NAME_FIELD = (By.CSS_SELECTOR, 'input.Input_input__YeDuE[name="storeName"]')
    SELECT_BUSINESS_SECTOR_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[1]/div/label[2]/div/div')
    CLOTHES_BUSINESS_SECTOR = (By.XPATH, '//li[@class="SelectItem_item__kFdkV"]//p[text()="Clothes"]')
    MANUFACTURER_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    LICENCE_NUMBER_FIELD = (By.CSS_SELECTOR, 'input[name="license"]')
    ESTABLISHMENT_YEAR_FIELD = (By.CSS_SELECTOR, 'input[name="yearEstablished"]')
    NUMBER_OF_EMPLOYEES_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/div/label[2]/div/div')
    NUMBER_OF_EMPLOYEES = {
        '<10': (By.XPATH, '//*[@id="combobox-list"]/li[1]'),
        '11-50': (By.XPATH, '//*[@id="combobox-list"]/li[2]'),
        '50-100': (By.XPATH, '//*[@id="combobox-list"]/li[3]'),
        '>100': (By.XPATH, '//*[@id="combobox-list"]/li[4]'),
    }
    COUNTRY_OF_COMPANY_REGISTRATION_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/label[1]/div/div')
    COUNTRY_OF_COMPANY_REGISTRATION_TURKEY = (By.XPATH, '//li[@class="SelectItem_item__kFdkV"]//p[text()="Turkey"]')
    BUSINESS_DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'input[name="description"]')
    BUSINESS_PHONE_COUNTRY_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[3]/div[1]/label/div/div[2]')
    BUSINESS_COUNTRY_LOCATOR_TURKEY = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[3]/div[1]/label/div/div['
                                                 '2]/ul/li[7]')
    BUSINESS_EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    COMPANY_ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[name="address"]')
    PROFILE_SAVE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div/form/button')


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/a[2]')
    REGISTRATION_LINK = (By.CSS_SELECTOR, 'a.Button_light_red__G4Gow[href="/register"]')
    All_CATEGORIES_MENU_ITEM = (By.CSS_SELECTOR, 'button.HeaderCategories_button__Lv0HF')
    CATEGORIES_MENU_OPTION = (By.CSS_SELECTOR, 'button.FilterButton_button_categories__Ro3J4')
    CLOTHES_CATEGORY_MENU_OPTION = (By.XPATH, "//button[text()=\"Clothes\"]")
    SUBCATEGORY_ITEMS = (By.CSS_SELECTOR, 'a.MenuItems_link__VIVu7')
    PRODUCT_LIST_ITEM = (By.CLASS_NAME, 'MenuItems_items_links__tePb6')
    LAST_NEWS_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/news"]')
    TUTORIALS_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/tutorials"]')
    SELL_ON_ABRA_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/sell"]')
    CONTACT_SUPPORT_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/contact"]')
    FAQ_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/faq"]')
    ABOUT_US_MENU_ITEM = (By.CSS_SELECTOR, 'a.HeaderMenuItem_item__noyAd[href="/about"]')
    LANGUAGE_AND_CURRENCY_MENU_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/header/div[2]/div[3]/div/div[1]/div')
    SHIPMENT_COUNTRY_MENU_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div/header/div[2]/div[3]/div/div[2]/div/div')
    DROPDOWN_MENU_ITEM = (By.CSS_SELECTOR, 'li.SelectItem_item__kFdkV[role="option"]')


class SellOnAbraPageLocators:
    TITLE_SELL_ON_ABRA = (By.XPATH, '//*[@id="root"]/div/div/main/div/h2')


class ContactSupportPageLocators:
    WHATSAPP_PHONE_NUMBER = (By.CLASS_NAME, 'WhatsappPhoneNumber_phone_number__9IzKq')
    SOCIAL_MEDIA_ICON = (By.CLASS_NAME, 'SocialNetworks_network__d03A9')


class FaqPageLocators:
    TITLE_ON_THE_FAQ_PAGE = (By.XPATH, '//*[@id="root"]/div/div/main/div/h2')
    LINK_CONTACT_SUPPORT_FROM_FAQ_PAGE = (By.CSS_SELECTOR, 'a.FAQ_link_text__jvPZN[href="/contact"]')


class AboutUsPageLocators:
    TITLE_ABOUT_US = (By.XPATH, "//h2[text()=\"About Us\"]")


class ProductCategoryPageLocators:
    PRODUCT_FILTER = (By.CLASS_NAME, 'ProductFilter_product_filter__naSzd')
