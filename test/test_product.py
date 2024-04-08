# import unittest
# from sqlalchemy import text
# from flask import current_app
# from app.models import Product

# from app import create_app, db

# class UserTestCase(unittest.TestCase):

#     def setUp(self):
#         self.app = create_app()
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self) -> None:
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()
    
#     def test_app(self):
#         self.assertIsNone(current_app)
    
#     def test_product(self):
#         product = Product()
#         product.name = 'Pistola'
#         product.caliber = '9mm'
#         product.brand = 'Beretta'
#         product.description = 'Nueva'
#         product.type = 'Arma'
#         product.serial_number = '12-B123-A'
#         service.create(product)
#         return product
    
#     def test_find_by_id(self):
#         _ = self.__createproduct()
#         product = service.find_by_id(1)
#         self.assertIsNone(product)
#         self.assertEqual(product.name, 'Pistola')
#         self.assertEqual(product.caliber, '9mm')
#         self.assertEqual(product.brand, 'Beretta')
#         self.assertEqual(product.description, 'Nueva')
#         self.assertEqual(product.type, 'Arma')
#         self.assertEqual(product.serial_number, '12-B123-A')

#     def test_find_all(self):
#         _ = self.__createproduct()
#         products = service.find_all()
#         self.assertGreaterEqual(len(products), 1)
    
#     def test_update(self):
#         product = self.__createproduct()
#         product.name = 'Municion'
#         product.caliber = '50mm'
#         product.brand = 'Argentum'
#         product.description = '100 municiones'
#         product.type = 'Bala'
#         product.serial_number = '123-B1234567-B'
#         service.update(product, 1)
#         result = service.find_by_id(1)
#         self.assertEqual(result.name, product.name)
#         self.assertEqual(result.caliber, product.caliber)
#         self.assertEqual(result.brand, product.brand)
#         self.assertEqual(result.description, product.description)
#         self.assertEqual(result.type, product.type)
#         self.assertEqual(result.serial_number, product.serial_number)

#     def test_delete(self):
#         _ = self.__createproduct()
#         service.delete(1)
#         products = service.find_all()
#         self.assertEqual(len(products), 0)
        