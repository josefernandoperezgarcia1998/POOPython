"""
Polimorfismo

Poli: Muchos
Morf: Formas

En POO, a la habilidad de un objeto de tomar muchas formas se le denomina Polimorfismo


"""

#Ejercicio, hacer que un objeto pasé por muchas formas

#Retorne el #mayor
class Numero:
    valor = 0

    def __init__(self, valor):
        self.valor = valor

    def comparar(self, numero):
        if numero.valor > self.valor:
            return numero.valor
        return self.valor


#Retorne la cadena quie se acerca más a la A del abecedario
class Cadena:
    valor = ""

    def __init__(self, valor):
        self.valor = valor

    def comparar(self, cadena):
        palabras = [self.valor, cadena.valor]
        palabras.sort()
        return palabras[0]


#Retorna la lista más grande
class Lista:
    valor = []

    def __init__(self, valor):
        self.valor = valor

    def comparar(self, lista):
        if len(self.valor) > len(lista.valor):
            return self.valor
        return lista.valor


def retornaElMayor(a, b):
    return a.comparar(b)


numero_uno = Numero(10)
numero_dos = Numero(2)

cadena_uno = Cadena("José")
cadena_dos = Cadena("Alejandro")

lista_uno = Lista([1, 2])
lista_dos = Lista([1, 2, 23, 4])

print(retornaElMayor(numero_uno, numero_dos))
print(retornaElMayor(cadena_uno, cadena_dos))
print(retornaElMayor(lista_uno, lista_dos))

"""

Sin polimorfismo

def retornaElMayor(a,b):
    #isinstance()
    if isinstance(a,int) and isinstance(b,int):
        if a > b:
            return a
    return b
    if isinstance(a,str) and isinstance(b,str):
        palabras = [a,b]
        palabras.sort()
        return palabras[0]
    if isinstance(a,list) and isinstance(b,list):
        if len(a) < len(b):
            return a
    return b
#print(retornaElMayor(100,20))
#print(retornaElMayor("Fernando","Totoro"))
#print(retornaElMayor([1,2,3], [1,2,8,8]))

"""
