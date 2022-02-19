"""
Alcance de las propiedades
Caracteristica que describe "quien" ó "que" puede acceder a una propiedad de un objeto






Propiedades...
publico | protegido | privado
public | protected | private





1.-Se puede acceder a las propiedades de un objeto desde la misma clase en la que se instancia un objeto
class Usuario:
    nombre = "fernando"
    def mi_nombre(self):
        return self.nombre

2.-Se puede acceder a la propiedad de un objeto desde una clase que haya heredado de la clase en la que se declaró en la propiedad
 (Si se declaró la propiedad en la clase padre se puede acceder a la propiedad en la clase hija)

class Empleado(Usuario):
    def nombre(self):
        return self.nombre

3.-Se puede acceder a uns propiedad de un objeto desde una instancia
empleado = Empleado()
empleado.nombre







Propiedad public...
    -Se puede acceder a la propiedad desde la clase que se declaró la propiedad
    -Desde clases que heredan de la clase Padre
    -Desde una instancia

Propiedad protected
    -Se puede acceder a la propiedad desde la clase que se declaró la propiedad
    -Desde clases que heredan de la clase Padre
    -NO SE PUEDE ACCEDER DESDE UNA INSTANCIA

Propiedad private
    -Se puede acceder a la propiedad desde la clase que se declaró la propiedad
    -NO desde clases que heredan de la clase Padre
    -NO SE PUEDE ACCEDER DESDE UNA INSTANCIA

"""