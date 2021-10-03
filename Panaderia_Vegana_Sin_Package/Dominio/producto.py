import uuid
import pickle
import jsonpickle


class Producto:
    def __init__(self, nombre, precio, ingredientes):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes
        self.id = uuid.uuid4()

    def __repr__(self):
        return str(self.id)

    def cumple(self, especificacion):
        dict_producto = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_producto or dict_producto[k] != especificacion.get_value(k):
                return False
        return True
