# main.py
from data import user_data_min, user_data_full
from sender_stand_request import post_new_client_kit, get_new_user_token



def get_kit_body(name):
    return {
        "name": name
    }


def main():
    token = get_new_user_token(user_data_min)

    # Minimal user data
    minimal_kit_body = get_kit_body("Набор с минимальными данными пользователя")
    minimal_kit_response = post_new_client_kit(minimal_kit_body, token)
    print(minimal_kit_response.json())

    # Full user data
    full_kit_body = get_kit_body("Набор с полными данными пользователя")
    full_kit_response = post_new_client_kit(full_kit_body, token)
    print(full_kit_response.json())


if __name__ == "__main__":
    main()


import pytest
from sender_stand_request import post_new_client_kit

# Функция для позитивных проверок (код ответа 201)
def positive_assert(kit_body):
    token = get_new_user_token(user_data_min)
    response = post_new_client_kit(kit_body, token)
    assert response.status_code == 201, f"Ожидается код ответа 201, получен {response.status_code}"
    assert response.json()["name"] == kit_body["name"], "Поле name в ответе не совпадает с переданным значением"

# Функция для негативных проверок (код ответа 400)
def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body, "")
    assert response.status_code == 400, f"Ожидается код ответа 400, получен {response.status_code}"

# Тесты

# Позитивные тесты
@pytest.mark.parametrize("kit_body", [
    # Количество символов 1
    {"name": "a"},  # 1

    # Количество символов 511
    {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"},  # 2

    # Разрешены английские буквы
    {"name": "QWErty"},  # 5

    # Разрешены русские буквы
    {"name": "Мария"},   # 6

    # Разрешены спецсимволы
    {"name": "\"№%@\","},    # 7

    # Разрешены пробелы
    {"name": " Человек и КО "},  # 8

    # Разрешены цифры
    {"name": "123"}      # 9
])
def test_positive_assert(kit_body):
    positive_assert(kit_body)

# Негативные тесты
@pytest.mark.parametrize("kit_body", [
    # Количество символов 0
    {"name": ""},       # 3

    # Количество символов 512
    {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"},  # 4

    # Параметр не передан в запросе
    {},       # 10

    # Передан другой тип параметра (число)
    {"name": 123}       # 11
])
def test_negative_assert_code_400(kit_body):
    negative_assert_code_400(kit_body)


