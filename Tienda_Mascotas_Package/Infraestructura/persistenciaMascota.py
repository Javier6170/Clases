import pickle
import jsonpickle
import sqlite3

from Tienda_Mascotas_Package.Dominio.caballo import Caballo
from Tienda_Mascotas_Package.Dominio.gato import Gato
from Tienda_Mascotas_Package.Dominio.mascota import Mascota
from Tienda_Mascotas_Package.Dominio.perro import Perro
from Tienda_Mascotas_Package.Dominio.pez import Pez


class PersistenciaMascota():

    def connect(self):
        self.con = sqlite3.connect('la_tienda_del_yeye_mascota.sqlite')
        self.__crear_tabla()
        self.__crear_tabla_pez()
        self.__crear_tabla_caballo()
        self.__crear_tabla_perro()
        self.__crear_tabla_gato()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE MASCOTA(id text primary key, nombre text," \
                    "apellido text, documento text, raza text, color text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_mascota(self, mascota: Mascota):
        cursor = self.con.cursor()
        query = "insert into MASCOTA(id, nombre, apellido, documento, raza, " \
                "color) values(?,?,?,?,?,?)"
        cursor.execute(query, (
            str(mascota.id), mascota.nombre, mascota.apellido, mascota.documento, mascota.raza, mascota.color))
        self.con.commit()

    def __crear_tabla_pez(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PEZ(id text primary key, nombre text," \
                    "apellido text, documento text, raza text, color text, discapacidad text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_pez(self, pez: Pez):
        cursor = self.con.cursor()
        query = "insert into PEZ(id, nombre, apellido, documento, raza, " \
                "color, discapacidad) values(?,?,?,?,?,?,?)"
        cursor.execute(query,
                       (str(pez.id), pez.nombre, pez.apellido, pez.documento, pez.raza, pez.color, pez.discapacidad))
        self.con.commit()

    def __crear_tabla_perro(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PERRO(id text primary key, nombre text," \
                    "apellido text, documento text, raza text, color text, pesoActual text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_perro(self, perro: Perro):
        cursor = self.con.cursor()
        query = "insert into PERRO(id, nombre, apellido, documento, raza, " \
                "color, pesoActual) values(?,?,?,?,?,?,?)"
        cursor.execute(query,
                       (str(perro.id), perro.nombre, perro.apellido, perro.documento, perro.raza, perro.color,
                        perro.pesoActual))
        self.con.commit()

    def __crear_tabla_gato(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE GATO(id text primary key, nombre text," \
                    "apellido text, documento text, raza text, color text, numeroHermanos text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_gato(self, gato: Gato):
        cursor = self.con.cursor()
        query = "insert into GATO(id, nombre, apellido, documento, raza, " \
                "color, numeroHermanos) values(?,?,?,?,?,?,?)"
        cursor.execute(query,
                       (str(gato.id), gato.nombre, gato.apellido, gato.documento, gato.raza, gato.color,
                        gato.numeroHermanos))
        self.con.commit()

    def __crear_tabla_caballo(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CABALLO(id text primary key, nombre text," \
                    "apellido text, documento text, raza text, color text, comidaFavorita text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_caballo(self, caballo: Caballo):
        cursor = self.con.cursor()
        query = "insert into CABALLO(id, nombre, apellido, documento, raza, " \
                "color, comidaFavorita) values(?,?,?,?,?,?,?)"
        cursor.execute(query,
                       (str(caballo.id), caballo.nombre, caballo.apellido, caballo.documento, caballo.raza,
                        caballo.color,
                        caballo.comidaFavorita))
        self.con.commit()

    @classmethod
    def save(cls, mascota):
        binary_open = open("files/" + str(mascota.id) + '.gui', mode='wb')
        pickle.dump(mascota, binary_open)
        binary_open.close()

    @classmethod
    def load(cls, file_name):
        binary_open = open("files/" + file_name, mode='rb')
        mascota = pickle.load(binary_open)
        binary_open.close()
        return mascota

    @classmethod
    def save_json(cls, mascota):
        text_open = open("files/" + str(mascota.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(mascota)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        mascota = jsonpickle.decode(json_gui)
        text_open.close()
        return mascota
