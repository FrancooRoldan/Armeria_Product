from app.models import Product
from app.repositories.product_repository import ProductRepository
from app import cache
from tenacity import retry, stop_after_attempt, stop_after_delay

class ProductService:

    def __init__(self):
        self.__repo = ProductRepository()

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_all(self) -> Product:
        return self.__repo.find_all()

    def find_by_id(self, id) -> Product:
        product = cache.get(str(id)) # primero creamos/obtenemos el cache
        if product == None:
            product = self.__repo.find_by_id(id)
            cache.set(str(product.id), product, timeout=50)
        return product
    
    def find_all(self) -> Product:
        return self.__repo.find_all()

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_name(self, name) -> list:
        product = cache.get(str(name))
        if product == None:
            product = self.__repo.find_by_name(name)
            print(product)
            product = product[0]
            cache.set(str(product.name), product, timeout=50)
        return product
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_caliber(self, caliber) -> list:
        product = cache.get(str(caliber))
        if product == None:
            product = self.__repo.find_by_caliber(caliber)
            print(product)
            product = product[0]
            cache.set(str(product.caliber), product, timeout=50)
        return product
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_brand(self, brand) -> list:
        product = cache.get(str(brand))
        if product == None:
            product = self.__repo.find_by_brand(brand)
            print(product)
            product = product[0]
            cache.set(str(product.brand), product, timeout=50)
        return product
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_type(self, type) -> list:
        product = cache.get(str(type))
        if product == None:
            product = self.__repo.find_by_type(type)
            print(product)
            product = product[0]
            cache.set(str(product.type), product, timeout=50)
        return product
    
    def find_by_serial_number(self, serial_number: int) -> Product:
        product = cache.get(str(serial_number))
        if product == None:
            product = self.__repo.find_by_serial_number(serial_number)
            cache.set(str(product.id), product, timeout=50)
        return product
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def create(self, entity: Product) -> Product:
        product = self.__repo.create(entity)
        cache.set(str(product.id), product, timeout=50)
        return product
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def update(self, dto: Product, id: int) -> Product:
        product = self.__repo.update(dto, id)
        cache.set(str(product.id), product, timeout=50)   
        return product
    
    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def delete(self, id: int) -> Product:
        product = self.__repo.delete(id)
        cache.set(str(id), product, timeout=0) 
        