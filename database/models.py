from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Customer(db.Document):
    сustomer_type = db.ListField(
        db.StringField(), required=True)  # тип заказчика (ИП или Самозанятый)
    сustomer_name = db.StringField(
        required=True, unique=True)  # Ф.И.О. заказчика (ИП или Самозанятый)
    counterparties = db.ListField(
        db.StringField(), required=True)  # список контрагентов заказчика
    added_by = db.ReferenceField('User') 


class User(db.Document):
    # name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    сustomers = db.ListField(db.ReferenceField('Customer', reverse_delete_rule=db.PULL)) 


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')


    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Customer, 'added_by', db.CASCADE)
