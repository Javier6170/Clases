from Tienda_Mascotas_Package.Dominio.mascota import Mascota
import uuid


class Perro(Mascota):
    def __init__(self, nombre, apellido, documento, raza, color, pesoActual):
        self.nombre = nombre
        self.apellido = apellido
        self.id = str(uuid.uuid4())
        self.documento = documento
        self.raza = raza
        self.color = color
        self.pesoActual = pesoActual
        super().__init__(nombre, apellido, documento, raza, color)


