import unittest
from app import create_app, db
from app.models import Product

class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_product_create(self):
        product = Product(
            name='test', 
            caliber='test', 
            brand='test', 
            description='test', 
            type='test',
            serial_number='test')
        db.session.add(product)
        db.session.commit()
        self.assertTrue(product.id)
        self.assertTrue(product.name)
        self.assertTrue(product.caliber)
        self.assertTrue(product.brand)
        self.assertTrue(product.description)
        self.assertTrue(product.type)
        self.assertTrue(product.serial_number)

    
    def test_product_read(self):
        product = Product(name='test', caliber='test', brand='test', description='test', type='test', serial_number='test')
        db.session.add(product)
        db.session.commit()
        self.assertTrue(product.id)
        self.assertTrue(product.name)
        self.assertTrue(product.caliber)
        self.assertTrue(product.brand)
        self.assertTrue(product.description)
        self.assertTrue(product.type)
        self.assertTrue(product.serial_number)

    
    def test_product_find_by_id(self):
        product = Product(name='test', caliber='test', brand='test', description='test', type='test', serial_number='test')
        db.session.add(product)
        db.session.commit()
        self.assertTrue(product.id)
        self.assertTrue(product.name)
        product = Product.query.get(1)
        self.assertTrue(product)


    def test_product_find_all(self):
        product = Product(name='test', caliber='test', brand='test', description='test', type='test', serial_number='test')
        db.session.add(product)
        db.session.commit()
        self.assertTrue(product.id)
        self.assertTrue(product.name)
        products = Product.query.all()
        self.assertTrue(products)

    def test_product_update(self):
        product = Product(name='test', caliber='test', brand='test', description='test', type='test', serial_number='test')
        db.session.add(product)
        db.session.commit()
        product.name = 'test2'
        db.session.commit()
        self.assertEqual(product.name, 'test2')


    def test_product_delete(self):
        product = Product(
            name='test', 
            caliber='tet',
            brand='test', 
            description='test', 
            type='test',
            serial_number='test')
        db.session.add(product)
        db.session.commit()
        db.session.delete(product)
        db.session.commit()
        product = Product.query.get(1)
        self.assertFalse(product)