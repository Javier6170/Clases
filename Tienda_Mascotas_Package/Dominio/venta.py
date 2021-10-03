import uuid
from Tienda_Mascotas_Package.Dominio.especificacion_tienda_mascotas import Especificacion_Tienda_Mascotas


class Venta:
    def __init__(self, mascota, comprador):
        self.ventas = []
        self.mascota = mascota
        self.comprador = comprador
        self.id = uuid.uuid4()

    def cumple_venta(self, especificacion):
        dict_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascota or dict_mascota[k] != especificacion.get_value(k):
                return False
        return True
