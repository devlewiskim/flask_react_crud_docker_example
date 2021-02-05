from main import db
from sqlalchemy_serializer import SerializerMixin


class Customer(db.Model, SerializerMixin):
    serialize_only = ('id', 'name', 'birthdate', 'phone_no', 'address')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    birthdate = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(255))

    def __init__(self, name, birthdate, phone_no=None, address=None):
        self.name = name
        self.birthdate = birthdate
        self.phone_no = phone_no
        self.address = address
