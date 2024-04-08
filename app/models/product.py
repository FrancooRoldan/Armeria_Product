from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property

class Product(db.Model):
    __tablename__ = 'products'
    __id = db.Column('id' , db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name' , db.String(250), unique=True, index=True)
    __caliber = db.Column('caliber', db.String(250))
    __brand = db.Column('brand', db.String(250), index=True)
    __description = db.Column('description', db.String(250))
    __type = db.Column('type', db.String(250))
    __serial_number = db.Column('serial_number', db.String(250), unique=True, index=True)

    '''
    name: str, name of the product, max char 50
    caliber: str, caliber of the product, max char 50
    brand: str, brand of the product, max char 30
    description: str, description of the product, max char 250
    type: str, type of the product, max char 20
    serial_number: str, serial number of the product, max char 100
    '''
    def __init__(self, name:str, caliber:str, brand:str, description:str, type:str, serial_number:str): # Constructor
        self.__name = name
        self.__caliber = caliber
        self.__brand = brand
        self.__description = description
        self.__type = type
        self.__serial_number = serial_number

    @hybrid_property
    def id(self)->int:
        return self.__id

    @id.setter
    def id(self, id:int):
        self.__id = id

    @hybrid_property # Es un decorador, hace un patron de diseño, le agrega funcionalidad al método en este caso, lo encapsula en un atributo, puede estar arriba de una clase
    def name(self)->str: # Sería el get name
        return self.__name

    @name.setter  # Sería el set name
    def name(self, value:str):
        self.__name = value

    @hybrid_property
    def caliber(self)->str: # Sería el get caliber
        return self.__caliber

    @caliber.setter  # Sería el set caliber
    def caliber(self, value:str):
        self.__caliber = value

    @hybrid_property
    def brand(self)->str: # Sería el get brand
        return self.__brand

    @brand.setter  # Sería el set brand
    def brand(self, value:str):
        self.__brand = value

    @hybrid_property
    def description(self)->str: # Sería el get description
        return self.__description

    @description.setter  # Sería el set description
    def description(self, value:str):
        self.__description = value

    @hybrid_property
    def type(self)->str: # Sería el get type
        return self.__type

    @type.setter  # Sería el set type
    def type(self, value:str):
        self.__type = value

    @hybrid_property
    def serial_number(self)->str: # Sería el get serial number
        return self.__serial_number

    @serial_number.setter  # Sería el set serial number
    def serial_number(self, value:str):
        self.__serial_number = value

    def __repr__(self) -> str:  # Da la info de cada objeto
        return f'Product: \n Nombre: {self.name} \n Calibre: {self.caliber} \n Marca: {self.brand} \n Descripción: {self.description} \n Tipo: {self.type} \n Número de Serie: {self.serial_number}'

    def __eq__(self, value: object) -> bool: # Es para comparar si dos objetos están en la BD
        return self.serial_number == value.serial_number
