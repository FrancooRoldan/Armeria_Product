import unittest
from sqlalchemy import text
import requests
from app.services.product_service import Product, ProductService
from app import create_app, db, cache

service = ProductService()

class TestRequests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        cache.clear()
        self.app_context.pop()
    
    def create_product(self):
        product = Product()
        product.name = 'Mira'
        product.caliber = '0'
        product.brand = 'brandd'
        product.description = 'descripcion'
        product.type = 'Accesorio'
        product.serial_number = '1D2'
        product_db = service.create(product)
        return product_db

    def test_create(self): 
        body = {"name":"Mira", "caliber":"0", "brand":"brandd", "description":"descripcion", "type":"Accesorio", "serial_number":"1D2"}
        
        response = requests.post('http://127.0.0.1:5000/api/v1/product/create', json=body)
        response = response.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["name"], 'Mira')
        self.assertEqual(response["caliber"], '0')
        self.assertEqual(response["brand"], 'brandd')
        self.assertEqual(response["description"], 'descripcion')
        self.assertEqual(response["type"], 'Accesorio')
        self.assertEqual(response["serial_number"], '1D2')
        
    def test_find_by_id(self):
        product_db = self.create_product()
        product = self.app.test_product(use_cookies=True)
        response = product.get('http://localhost:5000/api/v1/product/id/1')
        response = response.get_json()
        # self.assertGreaterEqual(response["id"], 1) Cual va?
        self.assertEqual(response["id"], 1)
    
    def test_find_all(self): # Preguntar como se testearia un find_all en la vida real
        product = self.app.test_product(use_cookies=True)
        response = product.get('http://localhost:5000/api/v1/product/')
        self.assertEqual(response.status_code, 200)
    
    def test_find_by_name(self):             # Preguntar porque no anda, anda perfecto el metodo
        product_db = self.create_product()
        response = requests.get('http://localhost:5000/api/v1/product/name/', params={"name":"Mira"})
        response = response.json()
        self.assertEqual(response["id"], 1)

    def test_find_by_caliber(self):
        product_db = self.create_product()
        product = self.app.test_product(use_cookies=True)
        response = product.get('http://localhost:5000/api/v1/product/caliber/0')
        response = response.get_json()
        self.assertEqual(response["id"], 1)
    
    def test_find_by_brand(self):
        product_db = self.create_product()
        product = self.app.test_product(use_cookies=True)
        response = product.get('http://localhost:5000/api/v1/product/brand/brandd')
        response = response.get_json()
        self.assertEqual(response["id"], 1)

    def test_find_by_type(self):
        product_db = self.create_product()
        product = self.app.test_product(use_cookies=True)
        response = product.get('http://localhost:5000/api/v1/product/type/Accesorio')
        response = response.get_json()
        self.assertEqual(response["id"], 1)

    def test_find_by_serial_number(self):
        product_db = self.create_product()
        product = self.app.test_product(use_cookies=True)
        response = product.get('http://localhost:5000/api/v1/product/serial_number/1D2')
        response = response.get_json()
        self.assertEqual(response["id"], 1)

    def test_update(self):
        product_db = self.create_product()
        product = self.app.test_product(use_cookies=True)
        body = {"name": "Silenciador", "caliber":"0,9", "brand":"marca", "description":"descripcton", "type":"Accesorio", "serial_number":"1A3"}
        response = product.put('http://localhost:5000/api/v1/product/update/1', json=body)
        response = response.get_json()

        self.assertEqual(response["id"], 1)
        self.assertEqual(response["name"], 'Silenciador')
        self.assertEqual(response["caliber"], '0,9')
        self.assertEqual(response["brand"], 'marca')
        self.assertEqual(response["description"], 'description')
        self.assertEqual(response["type"], 'Accesorio')
        self.assertEqual(response["serial_number"], '1A3')

    def test_delete(self):
        product_db = self.create_product()
        product = self.app.test_product(use_cookies=True)
        response = product.delete('http://localhost:5000/api/v1/product/delete/1')
        products = service.find_all()
        self.assertEqual(len(products), 0)

if __name__ == '__main__':
    unittest.main()