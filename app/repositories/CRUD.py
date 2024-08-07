from abc import ABC, abstractmethod
from app import db


class Create(ABC):

    @abstractmethod
    def create(self, entity):
        pass


class Read(ABC):

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id:int):
        pass


class Update(ABC):

    @abstractmethod
    def update(self, entity, id:int):
        pass


class Delete(ABC):
    
    @abstractmethod
    def delete(self, entity):
        pass

# Es para realizar las consultas en la base de datos
# Este archivo se encarga de obligar al programador a programar (sobrescribir) estos metodos existentes)
