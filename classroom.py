class Alumno:

    def __init__(self, nombre, edad, calificacion):
        self.edad = edad
        self.nombre = nombre
        self.calificaion = calificacion

    def info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Calificacion:", self.calificaion)

class Empleado:
    
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Calificacion:", self.calificaion)

# alumno = Alumno(nombre="Luis",calificacion=5,edad=24)
# print(alumno.nombre)