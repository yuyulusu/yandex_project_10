from faker import Faker
fake = Faker()

user_data_min = {
    "firstName": fake.first_name(),
    "phone": fake.phone_number(),
    "address": fake.address()
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
kit_data = {
    "name": fake.name(),
    "cardId": 7
}