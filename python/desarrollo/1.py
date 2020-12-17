"""
class Persona():
    edad = 18
    def __init__ (self, nombre, nacionalidad):
        self.nombre=nombre
        self.nacionalidad=nacionalidad
    def nadar(selft):
        print ("estoy nadando")

persona1 = Persona("harold", "Camargo")

print (persona1.nombre)

print (Persona.edad)

persona1.nadar()
"""
class Persona():

    def __init__ (self):
        pass
    def despedir(selft):
        print ("adios")
    @classmethod
    def saludar (cls, nombre):   # utiliza la variable que esta dentro de la funcion, sin instanciarlo en la clase
        print ("estoy saludando a "+ nombre)

    @staticmethod
    def correr ():   # metodo statico, no llama ni una variable de clase ni de la funcion
        print ("estoy corriendo a ")

Persona.saludar("Alveiro")
