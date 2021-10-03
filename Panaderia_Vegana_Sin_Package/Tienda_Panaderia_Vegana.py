import os
import random
from Panaderia_Vegana_Sin_Package.Dominio.producto import Producto
from Panaderia_Vegana_Sin_Package.Dominio.controlador_panaderia_vegana import ControladorPanaderiaVegana
from Panaderia_Vegana_Sin_Package.Infraestructura.persistenciaProducto import PersistenciaProducto

if __name__ == '__main__':
    nombres = ['Pan de remolacha', 'Pan de garbanzo', 'Pan de calabaza', 'Pan violet', 'TORTA DE CHOCOLATE']
    ingredientes = {
        'Pan de remolacha': ['remolacha-arina-huevos', 'remolacha-arina-huevos-semillas-sesamo',
                             'remolacha-arina-huevos-semillas-sesamo-negro'],
        'Pan de garbanzo': ['arina de garbanzo,semilla de sesamo natural y espinacas',
                            'arina de garbanzo,semilla de sesamo natural, espinacas y huevos'],
        'Pan de calabaza': ['arina,semillas de calabaza, especies,toppings de colores',
                            'arina,semillas de calabaza, especies,zanahoria,rabano'],
        'Pan violet': ['zanahorias moradas, naranjas, arina, semillas de girasol',
                       'zanahorias normales, ralladura limon, arina, semillas de girasol'],
        'TORTA DE CHOCOLATE': ['arina de arroz integral, arveja amarilla',
                               'arina de arroz integral, arveja amarilla ademas un toque de soya']
    }
    precios = [100000, 120000, 130000, 140000, 150000]
    nombre = random.choice(nombres)
    ingrediente = random.choice(ingredientes[nombre])
    precio = random.choice(precios)
    p = Producto(nombre, precio, ingrediente)
    PersistenciaProducto.save(p)
    PersistenciaProducto.save_json(p)
    controlador = ControladorPanaderiaVegana()
    controlador_json = ControladorPanaderiaVegana()
    for file in os.listdir("files"):
        if '.gui' in file:
            controlador.agregar_producto(PersistenciaProducto.load(file))
        if '.json' in file:
            controlador_json.agregar_producto(PersistenciaProducto.load_json(file))
    for g in controlador.productos:
        PersistenciaProducto.save(g)
        PersistenciaProducto.save_json(g)
