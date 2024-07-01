class Urls:

    MAIN = 'https://stellarburgers.nomoreparties.site/'  # Главная страница

    REG         = MAIN + 'register'  # Регистрация
    LOGIN       = MAIN + 'login'  # Авторизация
    FORGOT_PASS = MAIN + 'forgot-password'  # Восстановление пароля
    RESET_PASS  = MAIN + 'reset-password'  # Восстановление пароля
    PERSONAL_AREA = MAIN + 'account/profile' # Профиль
    ORDER_HISTORY = MAIN + 'account/order-history' # История заказов
    ORDER_FEED  = MAIN + 'feed' # Лента заказов


class EndPoints:
    test_url = 'https://stellarburgers.nomoreparties.site'
    ingridients     = test_url + '/api/ingredients'  # get
    create_order    = test_url + '/api/orders'  # post {"ingredients": ["123123123","456456456"]}
    create_user     = test_url + '/api/auth/register'  # post {"email": "test-user@yandex.ru",
                                                   # "password": "password",
                                                   # "name": "Username"}
    login_user      = test_url + '/api/auth/login'  # post
    get_user_info   = test_url + '/api/auth/user'  # GET
    update_user     = test_url + '/api/auth/user'  # PATCH
    delete_user     = test_url + '/api/auth/user'  # DELETE
    get_all_orders  = test_url + '/api/orders/all'  # GET
    get_orders      = test_url + '/api/orders'  # GET