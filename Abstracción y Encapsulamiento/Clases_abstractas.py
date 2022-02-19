"""

Clases abstractas: Busca definir la estructura de un objeto de manera gerneral,
sin pensar ó sin definir los detalles de la implementación

Las clases abstractas se define el esqueleto de la clase para que sean las clases hijas puedan implementar el esqueleto

No se debe de introducir objetos dentro de las clases abstractas porque impide que el código sea mantanible

"""
from abc import ABC, abstractmethod

#Clase abstracta - Primer nivel
class EstructuraAbstracta(ABC):

    @abstractmethod
    def obtener():
        pass

    @abstractmethod
    def agregar():
        pass


#Segundo nivel
class Hash(EstructuraAbstracta):
    datos = {}

    def obtener(self,llave):
        datos[llave]

    def agregar(self, llave,valor):
        datos[llave] = valor


class Queue(EstructuraAbstracta):
    datos = []

    def obtener(self):
        datos[0]

    def agregar(self, llave, valor):
        datos[len(datos) - 1] = valor


#Tercer nivel
class FilaBanco:

    def __init__(self, almacen_usuarios):
        if not isinstance(almacen_usuarios, EstructuraAbstracta):
            raise ValueError('Store is not supported')
        self.usuarios = almacen_usuarios

    def siguiente_usuario(self, numero):
        # Implementación
        return self.usuarios.obtener(numero)

    def formar_usuario(self, numero, usuario):
        self.usuarios.agregar(numero, usuario)

FilaBanco(Queue())
#FilaBanco([])

