import uuid


class Mascota():
    def __init__(self, nombre, apellido, documento, raza, color):
        self.nombre = nombre
        self.apellido = apellido
        self.id = str(uuid.uuid4())
        self.documento = documento
        self.raza = raza
        self.color = color

    def muestra_dato(self):
        print("El nombre y apellido de la mascota es: " + self.nombre, self.apellido)
        print("El ID y el documento de la mascota es: " + str(self.id), str(self.documento))
        print("La raza y el color de la amscota es: " + self.raza, self.color)

    def __str__(self):
        return f'{self.color}---{self.id}---{self.nombre}---{self.apellido}'

    def __repr__(self):
        return f'id de la mascota: {str(self.id)}-\n' \
               f'color: {self.color}-\n' \
               f'nombre: {self.nombre}-\n' \
               f'nombre: {self.apellido}-\n' \
               f'documento: {self.documento}-\n' \
               f'raza: {self.raza}-\n'

    def cumple(self, especificacion):
        dict_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascota or dict_mascota[k] != especificacion.get_value(k):
                return False
        return True


if __name__ == '__main__':
    print(Mascota.__subclasses__())
