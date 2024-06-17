from app.models import Product
from app import db
from .CRUD import Create, Read, Update, Delete

class ProductRepository(Create, Read, Update, Delete):
    def __init__(self):
        self.__model = Product

    '''
    Recibe el objeto product y lo guarda en la base de datos
    '''
    def create(self, dto: Product):
        #entity = Product(name = product['name'], caliber = product['caliber'], brand = product['brand'], description = ['description'], type = ['type'], serial_number = ['serial_number'])
        db.session.add(dto)
        db.session.commit()
        return dto

    '''
    Cambia uno o mas de los valores de un objeto que esta identificado con el id
    '''
    def update(self, dto, id: int) -> Product:
        entity = self.find_by_id(id)
        for key, value in dto.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity
    
    '''
    Borra el objeto identificado con ese id
    '''
    def delete(self, id: int) -> Product:
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    '''
    Devuelve todos los objetos de la Base de Datos
    '''
    def find_all(self) -> Product:
        return db.session.query(self.__model).all()

    '''
    Devuelve el objeto con el id específico
    '''
    def find_by_id(self, id: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    '''
    Devuelve los objetos con el nombre solictado
    '''
    def find_by_name(self, name: str) -> list:
        return db.session.query(self.__model).filter(self.__model.name.like(name)).all()
    
    '''
    Devuelve los objetos con el calibre solicitado
    '''
    def find_by_caliber(self, caliber: str) -> list:
        return db.session.query(self.__model).filter(self.__model.caliber == caliber).all()
    
    '''
    Devuelve los objetos con la marca solicitada
    '''
    def find_by_brand(self, brand: str) -> list:
        return db.session.query(self.__model).filter(self.__model.brand == brand).all()
    
    '''
    Devuelve los objetos con el tipo solicitado
    '''
    def find_by_type(self, type: str) -> list:
        return db.session.query(self.__model).filter(self.__model.type == type).all()
    
    '''
    Devuelve el objeto con el número de serie específico
    '''
    def find_by_serial_number(self, serial_numb: str) -> Product:
        return db.session.query(self.__model).filter(self.__model.serial_number == serial_numb).first()
  