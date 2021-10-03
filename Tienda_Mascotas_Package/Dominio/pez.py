from Tienda_Mascotas_Package.Dominio.mascota import Mascota
import uuid


class Pez(Mascota):

    def __init__(self, nombre, apellido, documento, raza, color, discapacidad):
        self.nombre = nombre
        self.apellido = apellido
        self.id = uuid.uuid4()
        self.documento = documento
        self.raza = raza
        self.color = color
        self.discapacidad = discapacidad
        super().__init__(nombre, apellido, documento, raza, color)

    def muestra_dato(self):
        super(Pez, self).muestra_dato()
        print("Es un pez")
        print(f'El pez presenta la siguiente discapacidad:  {str(self.discapacidad)} ')
