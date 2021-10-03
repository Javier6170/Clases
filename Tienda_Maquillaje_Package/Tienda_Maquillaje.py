import os
import random
from Tienda_Maquillaje_Package.Dominio.controlador_servicio import ControladorServicio
from Tienda_Maquillaje_Package.Dominio.servicio import Servicio
from Tienda_Maquillaje_Package.Infraestructura.persistenciaServicio import PersistenciaServicio


if __name__ == '__main__':
    nombres = ['depilacion de cejas', 'delineado de ojos', 'brillo', 'servicio premium']
    productos_necesarios = {
        'depilacion de cejas': ['depilador', 'cera', 'tela para depilar'],
        'delineado de ojos': ['lapiz', 'delineador'],
        'brillo': ['iluminador de ojos'],
        'servicio premium': ['depilacion de cejas', 'masaje', 'esfoliantes', 'polvos', 'rubor', 'delineador', 'sombra',
                             'base']
    }
    calidades = [1, 2, 3, 4, 5]
    nombre = random.choice(nombres)
    productoNecesario = random.choice(productos_necesarios[nombre])
    calidad = random.choice(calidades)
    s = Servicio(nombre, calidad, productoNecesario)
    PersistenciaServicio.save(s)
    PersistenciaServicio.save_json(s)
    controlador = ControladorServicio()
    controlador_json = ControladorServicio()
    for file in os.listdir("files"):
        if '.gui' in file:
            controlador.agregar_servicio(PersistenciaServicio.load(file))
        if '.json' in file:
            controlador_json.agregar_servicio(PersistenciaServicio.load_json(file))
    for g in controlador.serivicios:
        PersistenciaServicio.save(g)
        PersistenciaServicio.save_json(g)
