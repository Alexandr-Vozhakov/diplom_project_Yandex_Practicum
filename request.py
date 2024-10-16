import requests
import config
import data

def post_new_order():
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER,
           json=data.order_body)

def get_order_track(number):
    return requests.get(config.URL_SERVICE + config.ORDER_TRACK,
           params={"t": number})