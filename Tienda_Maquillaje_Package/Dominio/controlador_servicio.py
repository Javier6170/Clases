from Tienda_Maquillaje_Package.Dominio.servicio import Servicio
from Tienda_Maquillaje_Package.Dominio.especificacion_tienda_maquillaje import Especificacion_Tienda_Maquillaje


class ControladorServicio:
    def __init__(self):
        self.serivicios = []

    def agregar_servicio(self, servicio):
        if type(servicio) == Servicio:
            espec = Especificacion_Tienda_Maquillaje()
            espec.agregar_parametros('id', servicio.id)
            if len(list(self.buscar(espec))) == 0:
                self.serivicios.append(servicio)
            else:
                raise Exception('servicio repetido')

    def buscar(self, especificacion):
        for s in self.serivicios:
            if s.cumple(especificacion):
                yield s
