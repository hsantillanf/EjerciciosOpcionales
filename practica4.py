#HERENCIA
class Vehiculo:
 
    def __init__(self, nomb, color):
        self.__nombre = nomb      # __name es un atributo privado
        self.__color = color
 
    def getColor(self):         # getColor() funcion accesible a la clase Auto
        return self.__color
 
    def setColor(self, color):  # setColor es accesible fuera de la clase
        self.__color = color
 
    def getNombre(self):          # getNombre() es accesible fuera de la clase
        return self.__nombre

 
class Moto(Vehiculo):
 
    def __init__(self, nombre, color, modelo):
        # Llamada al constructor para la herencia de nombre y color  
        super().__init__(nombre, color)       
        self.__modelo = modelo
 
    def getDescripcion(self):
        return self.getNombre() + self.__modelo + " de color " + self.getColor() 


# En el método getDescripcion podemos llamar a getNombre() y getColor porque
# son accesibles al pasar la herencia a la clase Derivada (Auto)

c = Moto("Suzuki", "azul", "GT350")
print(c.getDescripcion())
print(c.getNombre()) # La clase moto no tiene un método getNombre() pero es accesible de la clase heredada Vehiculo