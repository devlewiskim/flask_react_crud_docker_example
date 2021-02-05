from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

from main import db
from .models import Customer

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('phone_no', type=str)
parser.add_argument('address', type=str)
parser.add_argument('birthdate', type=str)


class CustomerApi(Resource):
    def get(self, id=None):
        if not id:  # /api/v1/customers
            customers = Customer.query.all()
            if customers:
                status = 200
                result = {'result': [customer.to_dict() for customer in customers]}
            else:
                status = 204
                result = {'result': 'No Customer Data'}
        else:  # /api/v1/customers/<id>
            customer = Customer.query.filter_by(id=id).first()
            if not customer:
                status = 400
                result = {
                    'result': 'Failed'
                }
            else:
                status = 200
                result = {'result': customer.to_dict()}

        resp = make_response((jsonify(result), status))
        return resp

    def post(self):
        # Get the request data
        args = parser.parse_args()
        name = args['name']
        birthdate = args['birthdate']
        phone_no = args['phone_no']
        address = args['address']

        try:
            new_customer = Customer(name, birthdate, phone_no, address)
            db.session.add(new_customer)
            db.session.commit()
            status = 200
            result = {'result': new_customer.to_dict()}
        except IntegrityError:
            result = {'result': 'Same name exists!'}
            status = 400

        return make_response((jsonify(result), status))

    def put(self, id):
        args = parser.parse_args()
        name = args['name']
        birthdate = args['birthdate']
        phone_no = args['phone_no']
        address = args['address']

        try:
            customer = Customer.query.filter_by(id=id).first()
            customer.name = name
            customer.birthdate = birthdate
            customer.phone_no = phone_no
            customer.address = address
            db.session.commit()
            return make_response((jsonify({'result': customer.to_dict()}), 200))
        except Exception:
            return make_response((jsonify({'result': 'Failed'}), 400))

    def delete(self, id):
        customer = Customer.query.filter_by(id=id)
        if customer:
            customer.delete()
            db.session.commit()
            status = 200
            result = {'result': 'Success'}
        else:
            status = 400
            result = {'result': 'Not found the customer'}

        return make_response((jsonify(result), status))

