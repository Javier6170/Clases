from Panaderia_Vegana_Sin_Package.Dominio.producto import Producto
from Panaderia_Vegana_Sin_Package.Dominio.especificacion_panaderia_vegana import Especificacion_Panaderia_Vegana


class ControladorPanaderiaVegana:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if type(producto) == Producto:
            espec = Especificacion_Panaderia_Vegana()
            espec.agregar_parametros('id', producto.id)
            if len(list(self.buscar(espec))) == 0:
                self.productos.append(producto)
            else:
                raise Exception('Producto Repetido')

    def buscar(self, especificacion):
        for p in self.productos:
            if p.cumple(especificacion):
                yield p
