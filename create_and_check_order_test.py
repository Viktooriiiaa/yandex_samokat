# Барышникова Викторя, 6-ая когорта-финальный проект. Инженер по тестированию плюс.
import data
import sender_stand_request

def test_create_and_check_order():
    track_number = sender_stand_request.post_new_order(data.order_body).json()["track"] # сохранили номер заказа
    # В переменную order_response сохраняется результат запроса на получение заказа по его номеру
    order_response = sender_stand_request.get_order_by_track(track_number)
    assert order_response.status_code == 200  # Проверяется, что код ответа равен 200


