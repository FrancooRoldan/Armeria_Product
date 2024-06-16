from flask import Blueprint, jsonify, request
from app.services.product_service import ProductService
from ..mapping.product_schema import ProductSchema

service = ProductService()
product_schema_many = ProductSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
product_schema = ProductSchema()
product = Blueprint('product', __name__)

@product.route('/product/', methods=['GET'])
def index():
    list = service.find_all()
    result = product_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@product.route('/product/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response = product_schema.dump(service.find_by_id(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/name/', methods=['GET'])
def find_by_name():
    name = request.args.get('name')

    response = product_schema_many.dump(service.find_by_name(name))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/caliber/<string:caliber>', methods=['GET'])
def find_by_caliber(caliber):
    response = product_schema.dump(service.find_by_caliber(caliber))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/brand/<string:brand>', methods=['GET'])
def find_by_brand(brand):
    response = product_schema.dump(service.find_by_brand(brand))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/type/<string:type>', methods=['GET'])
def find_by_type(type):
    response = product_schema.dump(service.find_by_type(type))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/serial_number/<string:serial_number>', methods=['GET'])
def find_by_serial_number(serial_number):
    response = product_schema.dump(service.find_by_serial_number(serial_number))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/create/', methods=['POST'])
def create_product():
    product = product_schema.load(request.json)
    response = product_schema.dump(service.create(product))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/update/<int:id>', methods=['PUT'])
def update_product(id):
    product = request.json
    response = product_schema.dump(service.update(product, id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

@product.route('/product/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    response = product_schema.dump(service.delete(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp