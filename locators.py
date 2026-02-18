from selenium.webdriver.common.by import By


class RegisterPageLocators:
    # Поле "Имя" на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[normalize-space()='Имя']/following-sibling::input")

    # Поле "Email" на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")

    # Поле "Пароль" на странице регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")

    # Ссылка "Войти" под формой регистрации
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")

    # Текст ошибки под полем пароля (например, при коротком пароле)
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]")


class LoginPageLocators:
    # Поле "Email" на странице входа
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")

    # Поле "Пароль" на странице входа
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")

    # Ссылка "Зарегистрироваться" на странице входа
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")

    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")

    # Ссылка "Личный кабинет" в шапке (ведет на /account)
    ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")

    # Вкладка "Булки" в конструкторе
    TAB_BUNS = (By.XPATH, "//span[normalize-space()='Булки']/parent::*")

    # Вкладка "Соусы" в конструкторе
    TAB_SAUCES = (By.XPATH, "//span[normalize-space()='Соусы']/parent::*")

    # Вкладка "Начинки" в конструкторе
    TAB_FILLINGS = (By.XPATH, "//span[normalize-space()='Начинки']/parent::*")

    # Заголовок секции "Булки"
    SECTION_BUNS = (By.XPATH, "//h2[normalize-space()='Булки']")

    # Заголовок секции "Соусы"
    SECTION_SAUCES = (By.XPATH, "//h2[normalize-space()='Соусы']")

    # Заголовок секции "Начинки"
    SECTION_FILLINGS = (By.XPATH, "//h2[normalize-space()='Начинки']")

    # Логотип Stellar Burgers (кликабельный, ведет на главную)
    # Иногда это div с классом logo, иногда просто ссылка с svg внутри
    LOGO = (
        By.XPATH,
        "(//div[contains(@class,'AppHeader_header__logo')]/a)[1] | //a[@href='/' and .//svg]"
    )

    # Кнопка "Оформить заказ" на главной
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")


class AccountPageLocators:
    # Ссылка "Конструктор" в шапке (ведет на главную)
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/' and .//p[normalize-space()='Конструктор']]")

    # Кнопка "Выход" в меню личного кабинета
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")


class ForgotPasswordLocators:
    # Ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
