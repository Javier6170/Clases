import uuid
import pickle
import jsonpickle

class Servicio:
    def __init__(self, nombre, calidad, productos_necesarios):
        self.nombre = nombre
        self.calidad = calidad
        self.productos_necesarios = productos_necesarios
        self.id = uuid.uuid4()

    def cumple(self, especificacion):
        dict_servicio = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_servicio or dict_servicio[k] != especificacion.get_value(k):
                return False
        return True

    def __repr__(self):
        return str(self.id)
