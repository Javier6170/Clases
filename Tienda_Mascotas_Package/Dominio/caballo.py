from Tienda_Mascotas_Package.Dominio.mascota import Mascota
import uuid


class Caballo(Mascota):
    def __init__(self, nombre, apellido, documento, raza, color, comidaFavorita):
        self.nombre = nombre
        self.apellido = apellido
        self.id = uuid.uuid4()
        self.documento = documento
        self.raza = raza
        self.color = color
        self.comidaFavorita = comidaFavorita
        super().__init__(nombre, apellido, documento, raza, color)

    def muestra_dato(self):
        super(Caballo, self).muestra_dato()
        print("Es un caballo")
        print(f'Su comida favorita es:  {str(self.comidaFavorita)} ')
