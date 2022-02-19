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
        print("Mi nombre es: "+self.nombre+" y gano:" +str(self.salario))

# Creando objeto empleado que heredará el atributo de nombre y el saludo de la clase Padre Usuario
empleado = Empleado("Fernando") #Agregando nombre al objeto empleado que pasa por la clase hijo y clase Padre (Empleado está heredando de Usuario)
#empleado.saludar("Hola, soy ")  #Agregando mensaje de saludo (Empleado está heredando de Usuario)
empleado.modificar_salario(1000)    #Agregando un monto al salario del método de la clase hijo
empleado.ver_salario()  #Imprimiendo el salario del método de la clase hijo

empleado.saludar(" ")  #Agregando mensaje de saludo (Empleado está heredando de Usuario)