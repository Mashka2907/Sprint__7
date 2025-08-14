import api


class TestOrderList:
    """Проверяет, что в тело ответа возвращается список заказов."""
    def test_list_orders_success(self):
        response = api.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()