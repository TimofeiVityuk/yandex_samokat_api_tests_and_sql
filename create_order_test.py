# Тимофей Витюк, 12-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data
# Функция тестирования создания и получения номера заказа

def test_get_order_by_track_success():
    new_order = sender_stand_request.post_new_order(data.order_body)
    track_number = str(new_order.json()["track"])
    response_order_track_status = sender_stand_request.get_track_order(track_number).status_code
    assert response_order_track_status == 200
