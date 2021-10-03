class Comprador:
    def __init__(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.id = documento

    def __repr__(self):
        return f'documento del comprador: {str(self.id)}-\n' \
               f'nombre del comprador: {self.nombre}-\n' \
               f'apellido del comprador: {self.apellido}-\n'

    def cumple_comprador(self, especificacion):
        dict_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascota or dict_mascota[k] != especificacion.get_value(k):
                return False
        return True