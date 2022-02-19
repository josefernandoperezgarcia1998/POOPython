"""
El método constructor ya es un método prefedinido por el lenguaje que se esté utilizando

Este método se ejecuta de manera automática cuando se instancia un nuevo objeto de una clase

En Python el método constructur está definido de la siguiente forma => def __init__(self):

El método constructor puede recibir argumentos de un objeto (nombre)

"""


class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self, saludo):
        print(saludo + self.nombre)


fernando = Usuario("Fernando")
fernando.saludar("Aloha, mi nombre es ")
