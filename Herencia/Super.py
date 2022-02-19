"""
Super:
Conservar la funcionalidad existente de un método Padre y solo extenderlo en la clase hijo
"""

class Usuario:  # Clase Padre
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self, saludo):
        print(saludo + self.nombre)


class Empleado(Usuario):  # Clase hijo
    salario = 0

    def modificar_salario(self, salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)

    def saludar(self, saludo): #Sobreescribiendo el método <saludar> de la clase Padre
        # Con la función super se puede obtener el método por default de la clase Padre y no afecta la funcionalidad
        # al sobre escribir el de la clase hijo
        super().saludar("Saludo con super para ")
        print("Mi nombre es: "+self.nombre+" y gano:" +str(self.salario))

empleado = Empleado("Fernando")
empleado.saludar(" ")





