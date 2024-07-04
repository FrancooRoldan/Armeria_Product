from flask import Blueprint, jsonify, request
from app.services.product_service import ProductService
from ..mapping.product_schema import ProductSchema

service = ProductService()
product_schema_many = ProductSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
product_schema = ProductSchema()
product = Blueprint('product', __name__)

@product.route('/all/', methods=['GET'])
def index():
    list = service.find_all()
    result = product_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@product.route('/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response = product_schema.dump(service.find_by_id(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/name/', methods=['GET'])
def find_by_name():
    name = request.args.get('name')

    response = product_schema_many.dump(service.find_by_name(name))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/caliber/<string:caliber>', methods=['GET'])
def find_by_caliber(caliber):
    list = service.find_by_caliber(caliber)
    response = product_schema_many.dump(list)
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/brand/<string:brand>', methods=['GET'])
def find_by_brand(brand):
    list = service.find_by_brand(brand)
    response = product_schema_many.dump(list)
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/type/<string:type>', methods=['GET'])
def find_by_type(type):
    list = service.find_by_type(type)
    response = product_schema_many.dump(list)
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/serial_number/<string:serial_number>', methods=['GET'])
def find_by_serial_number(serial_number):
    response = product_schema.dump(service.find_by_serial_number(serial_number))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/create/', methods=['POST'])
def create_product():
    product = product_schema.load(request.json)
    response = product_schema.dump(service.create(product))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    product = request.json
    response = product_schema.dump(service.update(product, id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    response = product_schema.dump(service.delete(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp