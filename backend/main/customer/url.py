from main.customer.views import *
from main import api

api.add_resource(
    CustomerApi,
    '/api/v1/customers',
    '/api/v1/customers/<int:id>'
)
