import random

from Tienda_Mascotas_Package.Dominio.alimento import Alimento
from Tienda_Mascotas_Package.Dominio.controladorMascotas import ControladorMascotas
from Tienda_Mascotas_Package.Dominio.especificacion_tienda_mascotas import Especificacion_Tienda_Mascotas


def test_buscar_alimento():
    tipoAnimales = ['Pez', 'Caballo', 'Gato']
    nombres = {
        'Pez': ['hierbas', 'legumbres', 'árboles leguminosos', 'lechuga'],
        'Caballo': ['MAÍZ', 'SALVADO', 'MELAZA', 'ZANAHORIAS'],
        'Gato': ['Royal Canin', 'Purina ', 'Feliz ', 'Royal Canin']
    }
    inv = ControladorMascotas()
    for tipoAnimal in tipoAnimales:
        for nombre in nombres[tipoAnimal]:
            nombre = nombre
            tipoAnimal = tipoAnimal
            inv.agregar_alimento(Alimento(nombre, tipoAnimal))
        especificacion = Especificacion_Tienda_Mascotas()
        especificacion.agregar_parametros("tipoAnimal", tipoAnimal)
    for mascota in inv.buscar_alimento(especificacion):
        assert mascota is not None
    assert len(list(inv.buscar_alimento(especificacion))) > 0


def test_fuzzing_buscar_alimento():
    tipoAnimales = ['Pez', 'Caballo', 'Gato']
    nombres = {
        'Pez': ['hierbas', 'legumbres', 'árboles leguminosos', 'lechuga'],
        'Caballo': ['MAÍZ', 'SALVADO', 'MELAZA', 'ZANAHORIAS'],
        'Gato': ['Royal Canin', 'Purina ', 'Feliz ', 'Royal Canin']
    }

    cantidad_mascotas = random.randint(100, 1000)
    controlador = ControladorMascotas()
    especificaciones = []
    for i in range(cantidad_mascotas):
        tipoAnimal = random.choice(tipoAnimales)
        nombre = random.choice(nombres[tipoAnimal])
        if i % 10 == 0:
            especificacion = Especificacion_Tienda_Mascotas()
            especificacion.agregar_parametros("tipoAnimal", tipoAnimal)
            especificaciones.append(especificacion)
        a = Alimento(nombre, tipoAnimal)
        controlador.agregar_alimento(a)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(controlador.buscar_alimento(esp))) > 0
        print('Alimentos encontrados: ')
        print(list(controlador.buscar_alimento(esp)))
    esp_fake = Especificacion_Tienda_Mascotas()
    esp_fake.agregar_parametros('sentimiento', 'feicidad')
    print(controlador.alimentos)
    assert len(list(controlador.buscar_alimento(esp_fake))) == 0
    a = Alimento(nombre, tipoAnimal)
    controlador.agregar_alimento(a)
    try:
        controlador.agregar_alimento(a)
        assert False
    except Exception as ex:
        assert ex
