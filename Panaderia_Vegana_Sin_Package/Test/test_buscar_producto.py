import random
from Panaderia_Vegana_Sin_Package.Dominio.controlador_panaderia_vegana import ControladorPanaderiaVegana
from Panaderia_Vegana_Sin_Package.Dominio.producto import Producto
from Panaderia_Vegana_Sin_Package.Dominio.especificacion_panaderia_vegana import Especificacion_Panaderia_Vegana


def test_buscar_producto():
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
    inv = ControladorPanaderiaVegana()
    for nombre in nombres:
        for ingrediente in ingredientes:
            nombre = nombre
            precio = 104512
            ingrediente = ingrediente
            inv.agregar_producto(Producto(nombre, precio, ingrediente))
        especificacion = Especificacion_Panaderia_Vegana()
        especificacion.agregar_parametros("nombre", nombre)
    for producto in inv.buscar(especificacion):
        assert producto is not None
    assert len(list(inv.buscar(especificacion))) > 0


def test_fuzzing_buscar():
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
    cantidad_servicio = random.randint(100, 1000)
    controlador = ControladorPanaderiaVegana()
    especificaciones = []
    for i in range(cantidad_servicio):
        nombre = random.choice(nombres)
        ingrediente = random.choice(ingredientes[nombre])
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = Especificacion_Panaderia_Vegana()
            especificacion.agregar_parametros('nombre', nombre)
            especificacion.agregar_parametros('ingredientes', ingrediente)
            especificaciones.append(especificacion)
        p = Producto(nombre, precio, ingrediente)
        controlador.agregar_producto(p)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(controlador.buscar(esp))) > 0
        print('productos veganos encontrados: ')
        print(list(controlador.buscar(esp)))
    esp_fake = Especificacion_Panaderia_Vegana()
    esp_fake.agregar_parametros('delineado', 'rojo')
    print(controlador.productos)
    assert len(list(controlador.buscar(esp_fake))) == 0
    p = Producto(nombre, precio, ingrediente)
    controlador.agregar_producto(p)
    try:
        controlador.agregar_producto(p)
        assert False
    except Exception as ex:
        assert ex
