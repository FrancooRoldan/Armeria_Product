from app.models import Product
from app.repositories.product_repository import ProductRepository

class ProductService:

    def __init__(self):
        self.__repo = ProductRepository()

    def find_by_id(self, id) -> Product:
        return self.__repo.find_by_id(id)
    
    def find_all(self) -> Product:
        return self.__repo.find_all()

    def find_by_name(self, name) -> list:
        return self.__repo.find_by_name(name)

    def find_by_caliber(self, caliber) -> list:
        return self.__repo.find_by_caliber(caliber)
    
    def find_by_brand(self, brand) -> list:
        return self.__repo.find_by_brand(brand)
    
    def find_by_type(self, type) -> list:
        return self.__repo.find_by_type(type)
    
    def find_by_serial_number(self, serial_number) -> Product:
        return self.__repo.find_by_serial_number(serial_number)
    
    def create(self, entity: Product) -> Product:
        return self.__repo.create(entity)
    
    def update(self, entity: Product, id:int) -> Product:
        return self.__repo.update(entity, id)
    
    def delete(self, id:int) -> Product:
        return self.__repo.delete(id)
    