from app.models.product import Product
from marshmallow import validate, fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True) #dump_only es para que la info que envío al cliente se muestre
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    caliber = fields.String(required=True, validate=validate.Length(min=1, max=15)) #required=True es porque se requiere que el cliente complete ese campo si o si
    brand = fields.String(required=True, validate=validate.Length(min=1, max=50))
    description = fields.String(required=True, validate=validate.Length(min=1, max=256))
    type = fields.String(required=True, validate=validate.Length(min=1, max=50))
    serial_number = fields.String(required=True, validate=validate.Length(min=1, max=25))

    '''
    Esta clase adapta los modelos a json
    '''
    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)
