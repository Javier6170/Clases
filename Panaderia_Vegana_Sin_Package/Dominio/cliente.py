from Panaderia_Vegana_Sin_Gluten.producto import Producto


class Cliente(Producto):
    def __init__(self, nombre, precio, descripcion, tipoTorta, clienteRegular):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.tipoTorta = tipoTorta
        self.clienteRegular = clienteRegular
        super().__init__(nombre, precio, descripcion, tipoTorta)
