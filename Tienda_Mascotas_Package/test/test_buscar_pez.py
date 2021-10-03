import random

from Tienda_Mascotas_Package.Dominio.pez import Pez
from Tienda_Mascotas_Package.Dominio.controladorMascotas import ControladorMascotas
from Tienda_Mascotas_Package.Dominio.especificacion_tienda_mascotas import Especificacion_Tienda_Mascotas


def test_buscar_pez():
    nombres = ['Lucky', 'Julio César', 'Lola', 'Chupita', 'Lili Bet']
    documentos = {
        'Lucky': ['648654', '31534512', '454554', '5646544'],
        'Julio César': ['559684', '6546768', '545457', '654687687'],
        'Lola': ['665261', '63265146', '56465', '5564685'],
        'Chupita': ['544564', '46546540', '164050468', '46546134'],
        'Lili Bet': ['4654164', '6465465', '65464684', '654869465']
    }

    inv = ControladorMascotas()
    for nombre in nombres:
        for documento in documentos[nombre]:
            nombre = nombre
            apellido = "perez"
            documento = documento
            raza = "mixta"
            color = "cafe"
            discapacidad = "le falta una aleta"
            inv.agregar_mascota(Pez(nombre, apellido, documento, raza, color, discapacidad))
        especificacion = Especificacion_Tienda_Mascotas()
        especificacion.agregar_parametros("nombre", nombre)
    for mascota in inv.buscar(especificacion):
        assert mascota is not None
    assert len(list(inv.buscar(especificacion))) > 0


def test_fuzzing_buscar_pez():
    nombres = ['Lucky', 'Julio César', 'Lola', 'Chupita', 'Lili Bet']
    documentos = {
        'Lucky': ['648654', '31534512', '454554', '5646544'],
        'Julio César': ['559684', '6546768', '545457', '654687687'],
        'Lola': ['665261', '63265146', '56465', '5564685'],
        'Chupita': ['544564', '46546540', '164050468', '46546134'],
        'Lili Bet': ['4654164', '6465465', '65464684', '654869465']
    }
    apellidos = ['perez', 'martinez', 'quintero', 'muñoz', 'garcia', 'tabares']
    razas = ['mixta', 'labrador', 'pastor aleman', 'landseer']
    colores = ['Azul', 'Rojo', 'Verde', 'Naranja', 'Amarillo', 'Cafe', 'Blanco', 'Negro']
    discapacidades = ['le falta una aleta', 'le falta un ojo', 'falta de alimentacion']
    cantidad_mascotas = random.randint(100, 1000)
    controlador = ControladorMascotas()
    especificaciones = []
    for i in range(cantidad_mascotas):
        nombre = random.choice(nombres)
        documento = random.choice(documentos[nombre])
        apellido = random.choice(apellidos)
        raza = random.choice(razas)
        color = random.choice(colores)
        discapacidad = random.choice(discapacidades)
        if i % 10 == 0:
            especificacion = Especificacion_Tienda_Mascotas()
            especificacion.agregar_parametros('nombre', nombre)
            especificacion.agregar_parametros('documento', documento)
            especificaciones.append(especificacion)
        p = Pez(nombre, apellido, documento, raza, color, discapacidad)
        controlador.agregar_mascota(p)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(controlador.buscar(esp))) > 0
        print('Peces encontrados: ')
        print(list(controlador.buscar(esp)))
    esp_fake = Especificacion_Tienda_Mascotas()
    esp_fake.agregar_parametros('sentimiento', 'feicidad')
    print(controlador.mascotas)
    assert len(list(controlador.buscar(esp_fake))) == 0
    p = Pez(nombre, apellido, documento, raza, color, discapacidad)
    controlador.agregar_mascota(p)
    try:
        controlador.agregar_mascota(p)
        assert False
    except Exception as ex:
        assert ex
