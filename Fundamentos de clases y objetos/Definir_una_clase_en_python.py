# Se crea una clase llamada curso
class Usuario:
    nombre = "Fernando"

    #Se crea un método llamado saludar que recibe por parámetro a self, esto va a permitir que se pueda recibir
    #información de un objeto, por ejemplo, al método le está llegando una propiedad del objeto donde se está mandando a llamar
    #fernando.saludar()
    def saludar(self):
        print("Hola, mi nombre es " + self.nombre);


# Se crea un objeto de tipo usuario y se le cambia el nombre
fernando = Usuario()
fernando.nombre = "José"

fernando.saludar()
