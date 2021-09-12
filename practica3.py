class Persona():

    def __init__(self, cedula, nombres, apellidos,correo):
        self.cedula= cedula
        self.nombres= nombres
        self.apellidos = apellidos
        self.correo= correo

    def mostrar(self):
        txt = "{0}, {1}"
        return txt.format(self.nombres, self.apellidos)

class Estudiante(Persona):

    def __init__(self, cedula, nombres, apellidos, correo, carrera):
        super().__init__(cedula, nombres, apellidos, correo)
        self.carrera= carrera

    ##Getters
    def get_Cedula(self):
        return self.cedula
    def get_NombresC(self):
        return self.nombres, self.apellidos
    def get_Correo(self):
        return self.correo
    def get_Carrera(self):
        return self.carrera

    ##Setters
    def set_Cedula(self, cedula):
        if isinstance(cedula, int):
            if cedula=="0123456789":
                self.cedula= cedula
        else:
            raise ValueError("Ha ingresado un valor no valido")

def run(Estudiante):
    print("Estudiante")
    cedula = int(input("Ingrese su número de cédula: "))
    nombres = input("Ingrese sus nombres: ")
    apellidos = input("Ingrese sus apellidos: ")
    correo = input("Ingrese su correo electronico: ")
    carrera = input("Ingrese la carrera que sigue: ")
    Dato= Estudiante(cedula, nombres, apellidos, correo, carrera)
    print("Identificación del estudiante: ", Dato.get_Cedula())
    print("Los nombres del estudiante: ", Dato.get_NombresC())
    print("El correo del estudiante: ", Dato.get_Correo())
    print("la carrera del estudiante: ", Dato.get_Carrera())

if __name__ == "__main__":
    run(Estudiante)