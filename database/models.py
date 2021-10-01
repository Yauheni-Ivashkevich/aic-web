from .db import db


class Customer(db.Document):
    сustomer_type = db.ListField(
        db.StringField(), required=True)  # тип заказчика (ИП или Самозанятый)
    сustomer_name = db.StringField(
        required=True, unique=True)  # Ф.И.О. заказчика (ИП или Самозанятый)
    counterparties = db.ListField(
        db.StringField(), required=True)  # список контрагентов заказчика


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
