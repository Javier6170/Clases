from Panaderia_Vegana_Sin_Gluten.persona import Persona


class Panadero(Persona):
    def __init__(self, nombre, precio, descripcion, tipoTorta, jornada, sector):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.tipoTorta = tipoTorta
        self.jornada = jornada
        self.sector = sector
        super().__init__(nombre, precio, descripcion, tipoTorta)
