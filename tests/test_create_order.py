import pytest
import api
import helpers


class TestCreateOrder:
    """Проверяет, что можно создать заказ с разными вариантами цета"""
    @pytest.mark.parametrize('color', (['BLACK'], ['GREY'], ['BLACK', 'GREY'], ''))
    def test_create_order(self, color):
        order_info = helpers.order_data(color)
        response = api.create_order(order_info)

        assert response.status_code == 201
        assert "track" in response.json()