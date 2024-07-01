import allure


class TestOrderFeed:

    @allure.title("Проверка открытия информации о заказе из ленты заказов")
    def test_open_order_info(self, get_order_feed_instance):
        assert get_order_feed_instance.open_order_info()

    @allure.title("Проверка отображения личных заказов в общей ленте заказов")
    def test_check_private_orders_in_feed(self, get_order_feed_instance, get_new_user):
        assert get_order_feed_instance.check_private_orders_in_feed(get_new_user)

    @allure.title("Проверка увеличения счетчика заказов за сегодня и за все время при создании заказа")
    def test_check_order_counter(self, get_order_feed_instance, get_new_user):
        assert get_order_feed_instance.check_order_counter(get_new_user)

    @allure.title("Проверка отображения созданного заказа в поле 'В работе'")
    def test_check_order_in_progress(self, get_order_feed_instance, get_new_user):
        assert get_order_feed_instance.check_order_in_progress(get_new_user)