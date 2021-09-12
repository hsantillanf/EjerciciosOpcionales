class Persona:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
    def mostrarPersona(self):
        print("Nombre: {},Edad: {}".format(self.nombre,self.edad))
         
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
    def mostrarEmpleado(self):
        super().mostrarPersona()
        print("Sueldo: ".format(self.sueldo))
 
    def pagImpuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no paga impuestos.")
 

pers1=Persona()
pers1.mostrarPersona()
empleado1=Empleado()
empleado1.mostrarEmpleado()
empleado1.pagImpuestos()
 