"""
Tema de encapsulamiento...

Para los métodos que se crean en el código para modificar los valores de las propiedades de los objetos se llama "Metodos accesores"

Existen 2 tipos: Get y Set.

Normalmente un get y un set se define para una misma propiedad.

El método get se encarga se retornar el valor actual de la propiedad.
El método set se encarga de asignar un nuevo valor a esa propiedad.


"""

class Usuario:  # Clase Padre
    __edad = 0
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self, saludo):
        print(saludo + self.nombre)

    #Método getter
    @property
    def edad(self):
         return self.__edad

    #Método setter
    @edad.setter
    def edad(self,valor_edad):
        if(valor_edad < 0):
            raise ValueError('Edad no puede ser menor que 0')
        self.__edad = valor_edad

class Empleado(Usuario):  # Clase hijo
    salario = 0

    #Método Setter
    def modificar_salario(self, salario):
        self.salario = salario

    #Método getter
    def ver_salario(self):
        print(self.salario)

    def saludar(self, saludo):
        super().saludar("Saludo con super para ")
        print("Mi nombre es: "+self.nombre+" y gano:" +str(self.salario))

empleado = Empleado("José Fernando")
empleado.edad = 23 #La edad se manda a llamar con el método setter, ya no con la propiedad original de la clase Padre Usuario
#empleado.edad = -2 #La edad no puede ser < 0
print(empleado.edad) #La edad se manda a llamar como propiedad, ya no cómo el método


