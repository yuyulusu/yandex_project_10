from faker import Faker
fake = Faker()

user_data_min = {
    "firstName": "Анатолий",
    "phone": "+79998887766",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

user_data_full = {
    "firstName": fake.first_name(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "comment": fake.text(),
    "address": fake.address()
}

kit_body_data = {
    "name": "a"
}
