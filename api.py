import requests
import urls


"""Отправляем запрос на создание курьера"""
def create_courier(data):
    return requests.post(urls.CREATE_COURIER, json=data)

"""Отправляем запрос на удаление курьера"""
def delete_courier(courier_id):
    return requests.delete(urls.DELETE_COURIER + str(courier_id))

"""Отправляем запрос логина курьера"""
def login_courier(data):
    return requests.post(urls.LOGIN_COURIER, json=data)

"""Отправляем запрос на создание заказа"""
def create_order(data):
    return requests.post(urls.CREATE_ORDER, json=data)

"""Отправляем запрос на получение списка заказов"""
def get_orders():
    return requests.get(urls.GET_ORDERS)