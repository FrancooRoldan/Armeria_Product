import unittest
from flask import current_app
from app.models import Product
from app.services import ProductService

from app import create_app, db

service = ProductService()

class ProductTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_create_product(self):
        product = self.__create_product()
        self.assertGreaterEqual(product.id, 1)

    def __create_product(self):
        product = Product('Pistola', '9mm', 'Beretta', 'Nueva', 'Arma', '12-B123-A')
        service.create(product)
        return product

    def test_find_by_id(self):
        product = self.__create_product()
        service.find_by_id(1)
        # self.assertIsNone(product)
        self.assertEqual(product.name, 'Pistola')
        self.assertEqual(product.caliber, '9mm')
        self.assertEqual(product.brand, 'Beretta')
        self.assertEqual(product.description, 'Nueva')
        self.assertEqual(product.type, 'Arma')
        self.assertEqual(product.serial_number, '12-B123-A')

    def test_find_all(self):
        _ = self.__create_product()
        products = service.find_all()
        self.assertGreaterEqual(len(products), 1)
    
    def test_update(self):
        product = self.__create_product()
        product.name = 'Municion'
        product.caliber = '50mm'
        product.brand = 'Argentum'
        product.description = '100 municiones'
        product.type = 'Bala'
        product.serial_number = '123-B1234567-B'
        result = service.find_by_id(1)
        self.assertEqual(result.name, 'Municion')
        self.assertEqual(result.caliber, '50mm')
        self.assertEqual(result.brand, 'Argentum')
        self.assertEqual(result.description, '100 municiones')
        self.assertEqual(result.type, 'Bala')
        self.assertEqual(result.serial_number, '123-B1234567-B')

    def test_delete(self):
        _ = self.__create_product()
        service.delete(1)
        products = service.find_all()
        self.assertEqual(len(products), 0)

if __name__ == '__main__':
  unittest.main()