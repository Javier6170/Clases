import os
import tkinter as tk
import tkinter as ttk
from tkinter import *

from Tienda_Mascotas_Package.Dominio.caballo import Caballo
from Tienda_Mascotas_Package.Dominio.comprador import Comprador
from Tienda_Mascotas_Package.Dominio.controladorMascotas import ControladorMascotas
from Tienda_Mascotas_Package.Dominio.gato import Gato
from Tienda_Mascotas_Package.Dominio.perro import Perro
from Tienda_Mascotas_Package.Dominio.pez import Pez
from Tienda_Mascotas_Package.Dominio.especificacion_tienda_mascotas import Especificacion_Tienda_Mascotas
from Tienda_Mascotas_Package.Dominio.venta import Venta
from Tienda_Mascotas_Package.Infraestructura.persistenciaComprador import PersistenciaComprador
from Tienda_Mascotas_Package.Infraestructura.persistenciaEstado import PersistenciaEstado
from Tienda_Mascotas_Package.Infraestructura.persistenciaMascota import PersistenciaMascota
from Tienda_Mascotas_Package.Infraestructura.persistenciaVenta import PersistenciaVenta

inv = ControladorMascotas()
raiz = Tk()

estado_persistencia = ''
for file in os.listdir("./files"):
    if '.json' in file:
        try:
            estado_persistencia = PersistenciaEstado.load_json(file)
        except Exception as ex:
            pass


def persistencia_por_BD():
    estado_persistencia = "BD"
    PersistenciaEstado.save_json(estado_persistencia)
    print("Se ha cambiado metodo de persistencia por BD")


def persistencia_por_json():
    estado_persistencia = "Json"
    PersistenciaEstado.save_json(estado_persistencia)
    print("Se ha cambiado metodo de persistencia por JSON")


def vender_mascota():
    m = ''
    for file in os.listdir("./files"):
        if '.json' in file:
            try:
                inv.agregar_mascota(PersistenciaMascota.load_json(file))
                inv.agregar_venta(PersistenciaVenta.load_json(file))
            except Exception as ex:
                pass

    print("VENTA DE MASCOTA")
    nombreComprador = input("Digita el nombre del comprador: ")
    apellidoComprador = input("Digita el apellido del comprador: ")
    documentoComprador = input("Digita el documento del comprador: ")
    comprador = Comprador(nombreComprador, apellidoComprador, documentoComprador)
    print("BUSCANDO LA MASCOTA POR ESPECIFICACION")
    especifiacion = Especificacion_Tienda_Mascotas()
    print("PRAMETROS DE BUSQUEDA MASCOA QUE SE DESEA COMPRAR: \n"
          "1. nombre \n"
          "2. apellido \n"
          "3. documento \n"
          "4. raza \n"
          "5. color \n"
          "6. id \n")
    eleccion = 0
    try:
        eleccion = int(input("digita tu eleccion: "))
    except ValueError:
        print('Error, introduce un numero entero')
    parametro = ''
    if eleccion == 1:
        parametro = "nombre"
    elif eleccion == 2:
        parametro = "apellido"
    elif eleccion == 3:
        parametro = "documento"
    elif eleccion == 4:
        parametro = "raza"
    elif eleccion == 5:
        parametro = "color"
    elif eleccion == 6:
        parametro = "id"
    if parametro != '':
        especifiacion.agregar_parametros(parametro, input(f"ingresa {parametro} del animal: "))
        if len(list(inv.buscar(especifiacion))) > 0:
            print("Esta mascota esta ingresada correctamente")
            print(list(inv.buscar(especifiacion)))
            m = inv.buscar(especifiacion)
            v = Venta(m, comprador)
            inv.agregar_venta(v)
            print("SE HA AGREGADO LA VENTA CORRECTAMENTE")
            PersistenciaVenta.save_json(v)
        else:
            print("No hemos podido encontrar tu mascota")
    if parametro == '':
        print("Debes escoger un numero entre 1 y 6")


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def buscar_comprador():
    if estado_persistencia == "Json":
        for file in os.listdir("./files"):
            if '.json' in file:
                try:
                    inv.agregar_comprador(PersistenciaComprador.load_json(file))
                except Exception as ex:
                    pass
    print("BUSCANDO POR ESPECIFICACION")
    especifiacion = Especificacion_Tienda_Mascotas()
    print("PRAMETROS DE BUSQUEDA: \n"
          "1. nombre \n"
          "2. apellido \n"
          "3. documento \n")
    eleccion = 0
    try:
        eleccion = int(input("digita tu eleccion: "))
    except ValueError:
        print('Error, introduce un numero entero')
    parametro = ''
    if eleccion == 1:
        parametro = "nombre"
    elif eleccion == 2:
        parametro = "apellido"
    elif eleccion == 3:
        parametro = "documento"
    if parametro != '':
        especifiacion.agregar_parametros(parametro, input(f"ingresa {parametro} del comprador: "))
        if len(list(inv.buscar_comprador(especifiacion))) > 0:
            print("Este comprador esta ingresada correctamente")
            print(list(inv.buscar_comprador(especifiacion)))
    if parametro == '':
        print("Debes escoger un numero entre 1 y 3")


def buscar_mascota():
    if estado_persistencia == "Json":
        for file in os.listdir("./files"):
            if '.json' in file:
                try:
                    inv.agregar_mascota(PersistenciaMascota.load_json(file))
                except Exception as ex:
                    pass
    print("BUSCANDO POR ESPECIFICACION")
    especifiacion = Especificacion_Tienda_Mascotas()
    print("PRAMETROS DE BUSQUEDA: \n"
          "1. nombre \n"
          "2. apellido \n"
          "3. documento \n"
          "4. raza \n"
          "5. color \n"
          "6. id \n")
    eleccion = 0
    try:
        eleccion = int(input("digita tu eleccion: "))
    except ValueError:
        print('Error, introduce un numero entero')
    parametro = ''
    if eleccion == 1:
        parametro = "nombre"
    elif eleccion == 2:
        parametro = "apellido"
    elif eleccion == 3:
        parametro = "documento"
    elif eleccion == 4:
        parametro = "raza"
    elif eleccion == 5:
        parametro = "color"
    elif eleccion == 6:
        parametro = "id"
    if parametro != '':
        especifiacion.agregar_parametros(parametro, input(f"ingresa {parametro} del animal: "))
        if len(list(inv.buscar(especifiacion))) > 0:
            print("Esta mascota esta ingresada correctamente")
            print(list(inv.buscar(especifiacion)))
        else:
            print("No hemos podido encontrar tu mascota")
    if parametro == '':
        print("Debes escoger un numero entre 1 y 6")


def agregarMascota():
    def pedirNumeroEntero():

        correcto = False
        num = 0
        while not correcto:
            try:
                num = int(input("Introduce un numero entero: "))
                correcto = True
            except ValueError:
                print('Error, introduce un numero entero')

        return num

    salir = False
    opcion = 0

    while not salir:

        print("1. Agregar pez")
        print("2. Agregar caballo")
        print("3. Agregar gato")
        print("4. Agregar perro")
        print("5. Agregar Comprador")
        print("6. Salir")

        print("Elige una opcion")

        opcion = pedirNumeroEntero()

        if opcion == 1:
            nombre = input("ingresa el nombre del pez: ")
            apellido = input("ingresa el apellido del pez: ")
            documento = input("ingresa el documento del pez: ")
            raza = input("ingresa la raza del pez: ")
            color = input("ingresa el color del pez: ")
            discapacidad = input("ingresa si tiene alguna discapacidad: ")
            p = Pez(nombre, apellido, documento, raza, color, discapacidad)
            inv.agregar_mascota(p)
            if estado_persistencia == "Json":
                PersistenciaMascota.save_json(p)
            elif estado_persistencia == "BD":
                saver.guardar_pez(p)
            print("SE HA REGISTRADO CORRECTAMENTE EL PEZ")
        elif opcion == 2:
            nombre = input("ingresa el nombre del caballo: ")
            apellido = input("ingresa el apellido del caballo: ")
            documento = input("ingresa el documento del caballo: ")
            raza = input("ingresa la raza del caballo: ")
            color = input("ingresa el color del caballo: ")
            comidaFavorita = input("ingresa la comida favorita del caballo: ")
            c = Caballo(nombre, apellido, documento, raza, color, comidaFavorita)
            inv.agregar_mascota(c)
            if estado_persistencia == "Json":
                PersistenciaMascota.save_json(c)
            elif estado_persistencia == "BD":
                saver.guardar_caballo(c)
            print("SE HA REGISTRADO CORRECTAMENTE EL CABALLO")
        elif opcion == 3:
            nombre = input("ingresa el nombre del gato: ")
            apellido = input("ingresa el apellido del gato: ")
            documento = input("ingresa el documento del gato: ")
            raza = input("ingresa la raza del gato: ")
            color = input("ingresa el color del gato: ")
            numeroHermanos = input("ingresa el numero de hermanos del gato: ")
            g = Gato(nombre, apellido, documento, raza, color, numeroHermanos)
            inv.agregar_mascota(g)
            if estado_persistencia == "Json":
                PersistenciaMascota.save_json(g)
            elif estado_persistencia == "BD":
                saver.guardar_gato(g)
            print("SE HA REGISTRADO CORRECTAMENTE EL GATO")
        elif opcion == 4:
            nombre = input("ingresa el nombre del perro: ")
            apellido = input("ingresa el apellido del perro: ")
            documento = input("ingresa el documento del perro: ")
            raza = input("ingresa la raza del perro: ")
            color = input("ingresa el color del perro: ")
            pesoActual = input("peso actual del perro: ")
            p = Perro(nombre, apellido, documento, raza, color, pesoActual)
            inv.agregar_mascota(p)
            if estado_persistencia == "Json":
                PersistenciaMascota.save_json(p)
            elif estado_persistencia == "BD":
                saver.guardar_perro(p)
            print("SE HA REGISTRADO CORRECTAMENTE EL PERRO")
        elif opcion == 5:
            nombre = input("ingresa el nombre del comprador: ")
            apellido = input("ingresa el apellido del comprador: ")
            documento = input("ingresa el documento del comprador: ")
            comprador = Comprador(nombre, apellido, documento)
            inv.agregar_comprador(comprador)
            if estado_persistencia == "Json":
                PersistenciaComprador.save_json(comprador)
            elif estado_persistencia == "BD":
                saver_comprador.guardar_comprador(comprador)
            print("SE HA REGISTRADO CORRECTAMENTE EL COMPRADOR")
        elif opcion == 6:
            salir = True
        else:
            print("Introduce un numero entre 1 y 3")

    print("Fin")


if __name__ == '__main__':
    saver = PersistenciaMascota()
    saver.connect()
    saver_comprador = PersistenciaComprador()
    saver_comprador.connect()
    raiz.title("TIENDA DE MASCOTAS")
    raiz.geometry("425x200")
    raiz.resizable(0, 0)
    center(raiz)
    raiz.iconbitmap("./imgs/icon.ico")
    label = ttk.Label(text="Metodo de persistencia: ")
    label.place(x=15, y=55)
    botonBD = tk.Button(text="Persistencia por BD", bg="blue", command=persistencia_por_BD)
    botonJson = ttk.Button(text="Persistencia por Json", bg="blue", command=persistencia_por_json)
    botonBD.place(x=160, y=55)
    botonJson.place(x=290, y=55)
    botonBuscarMascota = ttk.Button(text="Buscar mascota ", bg="blue", command=buscar_mascota)
    botonBuscarMascota.place(x=160, y=25)
    label = ttk.Label(text="Buscar mascota: ")
    label.place(x=15, y=25)
    botonAgregar = ttk.Button(text="Agregar", bg="blue", command=agregarMascota)
    botonAgregar.place(x=160, y=90)
    label2 = ttk.Label(text="Agregar: ")
    label2.place(x=15, y=90)
    label3 = Label(text="MIRA LA CONSOLA CUANDO OPRIMAS UN BOTON")
    label3.place(x=15, y=2)
    label4 = Label(text="Vender mascota: ")
    label4.place(x=15, y=120)
    botonVender = tk.Button(text="Vender mascota", bg="blue", command=vender_mascota)
    botonVender.place(x=160, y=120)
    botonBuscarComprador = ttk.Button(text="Buscar Comprador ", bg="blue", command=buscar_comprador)
    botonBuscarComprador.place(x=160, y=150)
    label6 = ttk.Label(text="Buscar Comprador: ")
    label6.place(x=15, y=150)
    print(f"la persistencia actual {estado_persistencia}")
    raiz.mainloop()
