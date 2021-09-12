class Persona(): 
    def __init__(self, nombre, edad, ocupacion): 
        self.nombre = nombre 
        self.edad = edad 
        self.ocupacion = ocupacion 
        
    def mostrarper(self):
        print("Hola soy {}, mi edad es {} y mi ocupación es {}".format(self.nombre, self.edad, self.ocupacion)) 

Pers1 = Persona("Anita",25, "Docente")
Pers1.mostrarper() 