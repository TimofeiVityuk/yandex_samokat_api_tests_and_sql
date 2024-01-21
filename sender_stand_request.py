import requests
import data
import configuration


# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body)  # тут тело

# Функция получения заказа по его трек-номеру
def get_track_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK_PATH + "?t=" + track_number) # подставляем полный url) #тут тело

