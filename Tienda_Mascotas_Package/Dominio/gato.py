import uuid
from Tienda_Mascotas_Package.Dominio.mascota import Mascota


class Gato(Mascota):
    def __init__(self, nombre, apellido, documento, raza, color, numeroHermanos):
        self.nombre = nombre
        self.apellido = apellido
        self.id = str(uuid.uuid4())
        self.documento = documento
        self.raza = raza
        self.color = color
        self.numeroHermanos = numeroHermanos
        super().__init__(nombre, apellido, documento, raza, color)

    def muestra_dato(self):
        super(Gato, self).muestra_dato()
        print("Es un gato")
        print(f'El gato tiene {str(self.numeroHermanos)} hermanos')
