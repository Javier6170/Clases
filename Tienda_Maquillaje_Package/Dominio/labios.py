from Tienda_Maquillaje_Package.Dominio.servicio import Servicio


class Labio(Servicio):
    def __init__(self, nombre, calidad, productos_necesarios, tipo_maquillaje):
        self.nombre = nombre
        self.calidad = calidad
        self.productos_necesarios = productos_necesarios
        self.tipo_maquillaje = tipo_maquillaje
        super().__init__(nombre, calidad, productos_necesarios, tipo_maquillaje)
