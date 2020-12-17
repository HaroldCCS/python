class Persona:
    nbrazos=0
    npiernas=0
    cabello=True
    ccabello="Defecto"
    hambre=0

    #un constructor es para definir una variable
    def __init__(self):
        self.nbrazos=2
        self.npiernas=2
    
    def dormir ():
        pass
    def comer (self):
        self.hambre = 5
        
# self es para referirse a que va a utilizar una variable de la misma clase

class Hombre (Persona):
    nombre="Defecto"
    sexo="M"

    def cambiarNombre (self, nombre):
        self.nombre = nombre

class Mujer (Persona):
    nombre="Defecto"
    sexo="F"

    def cambiarNombre(seft, nombre):
        self.nombre = nombre


jose = Hombre()
jose.comer()
print (jose.hambre)
