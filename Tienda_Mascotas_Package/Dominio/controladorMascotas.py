from Tienda_Mascotas_Package.Dominio.alimento import Alimento
from Tienda_Mascotas_Package.Dominio.caballo import Caballo
from Tienda_Mascotas_Package.Dominio.comprador import Comprador
from Tienda_Mascotas_Package.Dominio.gato import Gato
from Tienda_Mascotas_Package.Dominio.perro import Perro
from Tienda_Mascotas_Package.Dominio.pez import Pez
from Tienda_Mascotas_Package.Dominio.mascota import Mascota
from Tienda_Mascotas_Package.Dominio.especificacion_tienda_mascotas import Especificacion_Tienda_Mascotas
from Tienda_Mascotas_Package.Dominio.venta import Venta


class ControladorMascotas:
    def __init__(self):
        self.mascotas = []
        self.alimentos = []
        self.ventas = []
        self.compradores = []

    def agregar_mascota(self, mascota):
        if type(mascota) == Pez:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('id', mascota.id)
            if len(list(self.buscar(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('Pez repetida')
        if type(mascota) == Gato:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('id', mascota.id)
            if len(list(self.buscar(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('Gato repetida')
        if type(mascota) == Caballo:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('id', mascota.id)
            if len(list(self.buscar(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('Caballo repetida')
        if type(mascota) == Perro:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('id', mascota.id)
            if len(list(self.buscar(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('Perro repetido')
        if type(mascota) == Mascota:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('id', mascota.id)
            if len(list(self.buscar(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('Mascota repetida')

    def agregar_alimento(self, alimento):
        if type(alimento) == Alimento:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('referencia', alimento.referencia)
            self.alimentos.append(alimento)
        else:
            raise Exception("No es un alimento")

    def agregar_venta(self, venta):
        if type(venta) == Venta:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('id', venta.id)
            self.ventas.append(venta)
        else:
            raise Exception("No es una venta")

    def agregar_comprador(self, comprador):
        if type(comprador) == Comprador:
            espec = Especificacion_Tienda_Mascotas()
            espec.agregar_parametros('id', comprador.id)
            if len(list(self.buscar(espec))) == 0:
                self.compradores.append(comprador)
            else:
                raise Exception('Comprador repetido')

    def buscar_comprador(self, especificacion):
        for c in self.compradores:
            if c.cumple_comprador(especificacion):
                yield c

    def buscar_venta(self, especificacion):
        for v in self.ventas:
            if v.cumple_venta(especificacion):
                yield v

    def buscar_alimento(self, especificacion):
        for a in self.alimentos:
            if a.cumple_alimento(especificacion):
                yield a

    def buscar(self, especificacion):
        for m in self.mascotas:
            if m.cumple(especificacion):
                yield m
