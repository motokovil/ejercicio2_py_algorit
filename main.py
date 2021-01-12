from classroom import Alumno

class Classroom(Alumno):

    def info(self):
        super().info()

u = Classroom("Luis", 23, 5)
u.info()