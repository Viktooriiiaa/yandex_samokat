import configuration
import data
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         )
def get_params(order_number):
    current_params = data.params.copy() # создаем копию словаря c блоком параметров
    current_params["t"] = order_number # присваиваем параметру t значение, равное параметру функции
    return current_params # в реузльтате функции возвращаем сохраненное ранее значение

def get_order_by_track (track_num):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_WITH_TRACK_PATH,  # подставляем полный url
                      params= get_params(track_num)   # тут параметры
                        )

