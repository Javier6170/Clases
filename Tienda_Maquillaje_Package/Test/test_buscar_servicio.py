import random

from Tienda_Maquillaje_Package.Dominio.controlador_servicio import ControladorServicio
from Tienda_Maquillaje_Package.Dominio.servicio import Servicio
from Tienda_Maquillaje_Package.Dominio.especificacion_tienda_maquillaje import Especificacion_Tienda_Maquillaje


def test_buscar_servicio():
    nombres = ['depilacion de cejas', 'delineado de ojos', 'brillo', 'servicio premium']
    productos_necesarios = {
        'depilacion de cejas': ['depilador', 'cera', 'tela para depilar'],
        'delineado de ojos': ['lapiz', 'delineador'],
        'brillo': ['iluminador de ojos'],
        'servicio premium': ['depilacion de cejas', 'masaje', 'esfoliantes', 'polvos', 'rubor', 'delineador', 'sombra',
                             'base']
    }

    inv = ControladorServicio()

    for nombre in nombres:
        for productoNecesario in productos_necesarios[nombre]:
            nombre = nombre
            calidad = 10
            productoNecesario = productoNecesario
            inv.agregar_servicio(Servicio(nombre, calidad, productoNecesario))
        especificacion = Especificacion_Tienda_Maquillaje()
        especificacion.agregar_parametros("nombre", nombre)
    for servicio in inv.buscar(especificacion):
        assert servicio is not None
    assert len(list(inv.buscar(especificacion))) > 0

def test_fuzzing_buscar():
    nombres = ['depilacion de cejas', 'delineado de ojos', 'brillo', 'servicio premium']
    productos_necesarios = {
        'depilacion de cejas': ['depilador', 'cera', 'tela para depilar'],
        'delineado de ojos': ['lapiz', 'delineador'],
        'brillo': ['iluminador de ojos'],
        'servicio premium': ['depilacion de cejas', 'masaje', 'esfoliantes', 'polvos', 'rubor', 'delineador', 'sombra',
                             'base']
    }
    calidades = [1, 2, 3, 4, 5]
    cantidad_servicio = random.randint(100, 1000)
    controlador = ControladorServicio()
    especificaciones = []
    for i in range(cantidad_servicio):
        nombre = random.choice(nombres)
        productoNecesario = random.choice(productos_necesarios[nombre])
        calidad = random.choice(calidades)
        if i % 10 == 0:
            especificacion = Especificacion_Tienda_Maquillaje()
            especificacion.agregar_parametros('nombre', nombre)
            especificacion.agregar_parametros('productos_necesarios', productoNecesario)
            especificaciones.append(especificacion)
        s = Servicio(nombre, calidad, productoNecesario)
        controlador.agregar_servicio(s)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(controlador.buscar(esp))) > 0
        print('productos de maquillaje encontrados: ')
        print(list(controlador.buscar(esp)))
    esp_fake = Especificacion_Tienda_Maquillaje()
    esp_fake.agregar_parametros('cuido', 'mirringo')
    print(controlador.serivicios)
    assert len(list(controlador.buscar(esp_fake))) == 0
    s = Servicio(nombre, calidad, productoNecesario)
    controlador.agregar_servicio(s)
    try:
        controlador.agregar_servicio(s)
        assert False
    except Exception as ex:
        assert ex
