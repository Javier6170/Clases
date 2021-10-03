import uuid


class Alimento:
    def __init__(self, nombre, tipoAnimal):
        self.nombre = nombre
        self.referencia = uuid.uuid4()
        self.tipoAnimal = tipoAnimal

    def mostrar_datos(self):
        print("El nombre del alimento es: " + self.nombre)
        print("el alimento es para el tipo de animal " + self.tipoAnimal)

    def __repr__(self):
        return str(self.referencia)

    def cumple_alimento(self, especificacion):
        dict_alimento = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_alimento or dict_alimento[k] != especificacion.get_value(k):
                return False
        return True
